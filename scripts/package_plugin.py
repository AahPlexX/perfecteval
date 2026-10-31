#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path, PurePosixPath
from typing import Iterable
from urllib.parse import urlparse
from xml.etree import ElementTree

PLUGIN_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SEMVER_RE = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
    r"(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?"
    r"(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?$"
)
HEX_COLOR_RE = re.compile(r"^#[0-9A-Fa-f]{6}$")
SUPPORTED_CATEGORIES = frozenset(
    {
        "Business & Operations",
        "Communication",
        "Creativity",
        "Data & Analytics",
        "Developer Tools",
        "Education & Research",
        "Entertainment",
        "Finance",
        "Healthcare",
        "Other",
        "Productivity",
        "Scientific Research",
        "Security",
        "Travel",
    }
)
PACKAGE_DIRS = ("assets", "skills")
FIXED_ZIP_TIME = (1980, 1, 1, 0, 0, 0)
MAX_ASSET_BYTES = 5 * 1024 * 1024
ALLOWED_ASSET_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".svg"}
DISALLOWED_PARTS = {".git", "node_modules", "__pycache__", ".pytest_cache", ".mypy_cache"}
SECRET_NAME_RE = re.compile(
    r"(^\.env(?:\..*)?$|(?:^|[-_.])(secret|token|password)(?:[-_.]|$)|\.(?:pem|key)$|^id_rsa$)",
    re.IGNORECASE,
)


def _scalar(frontmatter: str, key: str) -> str | None:
    match = re.search(rf"(?m)^{re.escape(key)}:\s*(.+?)\s*$", frontmatter)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value.strip()


def _frontmatter(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def _safe_manifest_path(value: object) -> tuple[str | None, str | None]:
    if not isinstance(value, str) or not value.startswith("./"):
        return None, "must be a ./-prefixed relative path"
    if "\\" in value:
        return None, "must use forward slashes"
    raw = value[2:]
    path = PurePosixPath(raw)
    if not raw or path.is_absolute() or any(part in {"", ".", ".."} for part in path.parts):
        return None, "is unsafe or contains traversal"
    return path.as_posix(), None


def _numeric_dimension(value: str | None) -> float | None:
    if value is None:
        return None
    match = re.fullmatch(r"\s*([0-9]+(?:\.[0-9]+)?)\s*(?:px)?\s*", value)
    if not match:
        return None
    return float(match.group(1))


def _svg_dimensions(path: Path) -> tuple[float | None, float | None, str | None]:
    try:
        root = ElementTree.parse(path).getroot()
    except (ElementTree.ParseError, OSError) as exc:
        return None, None, f"invalid SVG XML: {exc}"

    width = _numeric_dimension(root.attrib.get("width"))
    height = _numeric_dimension(root.attrib.get("height"))
    if width is not None and height is not None:
        return width, height, None

    view_box = root.attrib.get("viewBox")
    if view_box:
        parts = re.split(r"[\s,]+", view_box.strip())
        if len(parts) == 4:
            try:
                return float(parts[2]), float(parts[3]), None
            except ValueError:
                pass
    return None, None, "SVG needs numeric width/height or a numeric viewBox"


def _validate_asset(root: Path, field: str, manifest_value: object, errors: list[str]) -> None:
    relative, path_error = _safe_manifest_path(manifest_value)
    if path_error:
        errors.append(f"interface.{field} is unsafe: {path_error}")
        return

    assert relative is not None
    asset = root / relative
    if not asset.is_file() or asset.is_symlink():
        errors.append(f"interface.{field} does not reference a regular packaged file: {manifest_value}")
        return
    if asset.stat().st_size > MAX_ASSET_BYTES:
        errors.append(f"interface.{field} exceeds the 5 MiB asset limit: {manifest_value}")
        return
    if asset.suffix.lower() not in ALLOWED_ASSET_SUFFIXES:
        errors.append(f"interface.{field} has unsupported asset type: {manifest_value}")
        return

    if asset.suffix.lower() == ".svg":
        width, height, dimension_error = _svg_dimensions(asset)
        if dimension_error:
            errors.append(f"interface.{field} {dimension_error}: {manifest_value}")
            return
        assert width is not None and height is not None
        if width < 48 or height < 48:
            errors.append(f"interface.{field} must be at least 48x48: {manifest_value}")
        if abs(width - height) > 1e-9:
            errors.append(f"interface.{field} must be square: {manifest_value}")


def _validate_https_url(field: str, value: object, errors: list[str]) -> None:
    if not isinstance(value, str) or not value.strip() or len(value) > 1024:
        errors.append(f"interface.{field} must be a non-empty HTTPS URL up to 1024 characters")
        return
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc or parsed.username or parsed.password:
        errors.append(f"interface.{field} must be an HTTPS URL without embedded credentials")


def _validate_interface(root: Path, interface: object, errors: list[str]) -> None:
    if interface is None:
        return
    if not isinstance(interface, dict):
        errors.append("extensions.com.openai.interface must be an object")
        return

    string_limits = {
        "displayName": 30,
        "shortDescription": 30,
        "longDescription": 4000,
        "developerName": 80,
    }
    for field, limit in string_limits.items():
        value = interface.get(field)
        if value is None:
            continue
        if not isinstance(value, str) or not value.strip():
            errors.append(f"interface.{field} must be a non-empty string")
        elif len(value) > limit:
            errors.append(f"interface.{field} exceeds {limit} characters")

    category = interface.get("category")
    if category is not None and category not in SUPPORTED_CATEGORIES:
        errors.append(
            "interface.category must be an exact supported category title: "
            + ", ".join(sorted(SUPPORTED_CATEGORIES))
        )

    capabilities = interface.get("capabilities")
    if capabilities is not None:
        if not isinstance(capabilities, list) or len(capabilities) > 20:
            errors.append("interface.capabilities must be a list with at most 20 entries")
        else:
            for index, capability in enumerate(capabilities):
                if not isinstance(capability, str) or not capability.strip() or len(capability) > 120:
                    errors.append(
                        f"interface.capabilities[{index}] must be a non-empty string up to 120 characters"
                    )

    prompts = interface.get("defaultPrompt")
    prompt_values: list[str] = []
    if prompts is not None:
        if isinstance(prompts, str):
            prompt_values = [prompts]
        elif isinstance(prompts, list) and 1 <= len(prompts) <= 3:
            prompt_values = prompts
        else:
            errors.append("interface.defaultPrompt must be a string or a list of 1-3 strings")

    normalized_prompts: set[str] = set()
    for index, prompt in enumerate(prompt_values):
        if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 128:
            errors.append(
                f"interface.defaultPrompt[{index}] must be a non-empty string up to 128 characters"
            )
            continue
        normalized = " ".join(prompt.split()).casefold()
        if normalized in normalized_prompts:
            errors.append("interface.defaultPrompt entries must be unique after normalization")
        normalized_prompts.add(normalized)

    for field in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        value = interface.get(field)
        if value is not None:
            _validate_https_url(field, value, errors)

    for field in ("brandColor", "brandColorDark"):
        value = interface.get(field)
        if value is not None and (not isinstance(value, str) or not HEX_COLOR_RE.fullmatch(value)):
            errors.append(f"interface.{field} must be a #RRGGBB color")

    for field in ("composerIcon", "composerIconDark", "logo", "logoDark"):
        value = interface.get(field)
        if value is not None:
            _validate_asset(root, field, value, errors)


def _validate_review(review: object, errors: list[str]) -> None:
    if review is None:
        return
    if not isinstance(review, dict):
        errors.append("extensions.com.openai.review must be an object")
        return

    prompts = review.get("prompts")
    if prompts is None:
        return
    if not isinstance(prompts, list) or len(prompts) > 20:
        errors.append("review.prompts must be a list with at most 20 entries")
        return
    for index, prompt in enumerate(prompts):
        if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 4000:
            errors.append(
                f"review.prompts[{index}] must be a non-empty string up to 4000 characters"
            )


def _validate_publication(publication: object, errors: list[str]) -> None:
    if publication is None:
        return
    if not isinstance(publication, dict):
        errors.append("extensions.com.openai.publication must be an object")
        return

    release_notes = publication.get("release_notes")
    if release_notes is not None and (
        not isinstance(release_notes, str) or not release_notes.strip()
    ):
        errors.append("publication.release_notes must be a non-empty string when provided")

    countries = publication.get("countries")
    if countries is not None:
        if not isinstance(countries, list) or any(
            not isinstance(country, str)
            or len(country) != 2
            or country.upper() != country
            or not country.isalpha()
            for country in countries
        ):
            errors.append("publication.countries must contain uppercase two-letter country codes")


def _validate_manifest(root: Path, errors: list[str]) -> dict[str, object] | None:
    manifest_path = root / "plugin.json"
    if not manifest_path.is_file() or manifest_path.is_symlink():
        errors.append("plugin.json must exist at the plugin root as a regular file")
        return None

    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        errors.append(f"plugin.json is not valid UTF-8 JSON: {exc}")
        return None

    if not isinstance(manifest, dict):
        errors.append("plugin.json must contain a JSON object")
        return None

    if manifest.get("$schema") != PLUGIN_SCHEMA:
        errors.append(f"plugin.json $schema must be {PLUGIN_SCHEMA}")

    name = manifest.get("name")
    if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
        errors.append("plugin.json name must be lowercase kebab-case and at most 64 characters")

    version = manifest.get("version")
    if not isinstance(version, str) or not SEMVER_RE.fullmatch(version):
        errors.append("plugin.json version must be strict semantic versioning")

    description = manifest.get("description")
    if not isinstance(description, str) or not description.strip():
        errors.append("plugin.json description must be a non-empty string")

    extensions = manifest.get("extensions")
    if extensions is not None:
        if not isinstance(extensions, dict):
            errors.append("plugin.json extensions must be an object")
        else:
            openai_extension = extensions.get("com.openai")
            if openai_extension is not None:
                if not isinstance(openai_extension, dict):
                    errors.append("extensions.com.openai must be an object")
                else:
                    _validate_interface(root, openai_extension.get("interface"), errors)
                    _validate_review(openai_extension.get("review"), errors)
                    _validate_publication(openai_extension.get("publication"), errors)

    return manifest


def _validate_skills(root: Path, errors: list[str]) -> None:
    skills_root = root / "skills"
    if not skills_root.is_dir() or skills_root.is_symlink():
        errors.append("skills/ must exist as a regular directory")
        return

    skill_dirs = sorted(
        path for path in skills_root.iterdir() if path.is_dir() and not path.is_symlink()
    )
    if not skill_dirs:
        errors.append("skills/ must contain at least one skill directory")
        return

    seen_names: set[str] = set()
    for skill_dir in skill_dirs:
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.is_file() or skill_file.is_symlink():
            errors.append(f"{skill_dir.relative_to(root).as_posix()} must contain SKILL.md")
            continue
        try:
            text = skill_file.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"{skill_file.relative_to(root).as_posix()} is not readable UTF-8: {exc}")
            continue

        frontmatter = _frontmatter(text)
        if frontmatter is None:
            errors.append(f"{skill_file.relative_to(root).as_posix()} must start with YAML frontmatter")
            continue

        name = _scalar(frontmatter, "name")
        description = _scalar(frontmatter, "description")
        if name != skill_dir.name:
            errors.append(
                f"{skill_file.relative_to(root).as_posix()} name must match directory {skill_dir.name}"
            )
        if name is None or not NAME_RE.fullmatch(name) or len(name) > 64:
            errors.append(f"{skill_file.relative_to(root).as_posix()} has an invalid skill name")
        elif name in seen_names:
            errors.append(f"duplicate skill name: {name}")
        else:
            seen_names.add(name)

        if description is None or not description.strip() or len(description) > 1024:
            errors.append(
                f"{skill_file.relative_to(root).as_posix()} description must be 1-1024 characters"
            )


def _package_files(root: Path) -> list[Path]:
    files = [root / "plugin.json"]
    for directory_name in PACKAGE_DIRS:
        directory = root / directory_name
        if not directory.exists():
            continue
        for path in directory.rglob("*"):
            if path.is_dir():
                continue
            relative = path.relative_to(root)
            if path.is_symlink():
                raise ValueError(
                    f"symlinks are not allowed in plugin packages: {relative.as_posix()}"
                )
            if any(part in DISALLOWED_PARTS for part in relative.parts):
                raise ValueError(
                    f"transient/dependency path is not allowed: {relative.as_posix()}"
                )
            if SECRET_NAME_RE.search(path.name):
                raise ValueError(
                    f"secret-shaped file is not allowed in the package: {relative.as_posix()}"
                )
            files.append(path)
    return sorted(set(files), key=lambda path: path.relative_to(root).as_posix())


def validate_plugin(root: Path | str) -> list[str]:
    root = Path(root).resolve()
    errors: list[str] = []
    _validate_manifest(root, errors)
    _validate_skills(root, errors)

    try:
        package_files = _package_files(root)
    except ValueError as exc:
        errors.append(str(exc))
        package_files = []

    for path in package_files:
        if not path.is_file() or path.is_symlink():
            errors.append(
                f"packaged path is not a regular file: {path.relative_to(root).as_posix()}"
            )

    return errors


def build_package(root: Path | str, output: Path | str) -> dict[str, object]:
    root = Path(root).resolve()
    output = Path(output).resolve()
    errors = validate_plugin(root)
    if errors:
        raise ValueError("plugin validation failed:\n- " + "\n- ".join(errors))

    files = _package_files(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    if output.exists():
        output.unlink()

    with zipfile.ZipFile(output, "w") as archive:
        for path in files:
            relative = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(relative, date_time=FIXED_ZIP_TIME)
            info.create_system = 3
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o100644 & 0xFFFF) << 16
            info.flag_bits |= 0x800
            archive.writestr(
                info,
                path.read_bytes(),
                compress_type=zipfile.ZIP_DEFLATED,
                compresslevel=9,
            )

    digest = hashlib.sha256(output.read_bytes()).hexdigest()
    return {
        "output": str(output),
        "sha256": digest,
        "files": [path.relative_to(root).as_posix() for path in files],
        "size": output.stat().st_size,
    }


def _print_errors(errors: Iterable[str]) -> None:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate and deterministically package Perfect Eval."
    )
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="Plugin repository root")
    parser.add_argument("--output", type=Path, help="ZIP path to create")
    parser.add_argument("--check", action="store_true", help="Validate without creating an archive")
    args = parser.parse_args(argv)

    if not args.check and args.output is None:
        parser.error("provide --check, --output, or both")

    errors = validate_plugin(args.root)
    if errors:
        _print_errors(errors)
        return 1

    print("PASS: plugin source validation")
    if args.output is not None:
        result = build_package(args.root, args.output)
        print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
