from __future__ import annotations

import importlib.util
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "package_plugin.py"


def load_packager():
    if not SCRIPT.is_file():
        return None
    spec = importlib.util.spec_from_file_location("perfecteval_packager", SCRIPT)
    if spec is None or spec.loader is None:
        return None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


PACKAGER = load_packager()


def copy_package_source(destination: Path) -> None:
    shutil.copy2(ROOT / "plugin.json", destination / "plugin.json")
    shutil.copytree(ROOT / "assets", destination / "assets")
    shutil.copytree(ROOT / "skills", destination / "skills")


class PackagePluginTests(unittest.TestCase):
    def require_packager(self):
        if PACKAGER is None:
            self.skipTest("packager implementation is not present yet")
        return PACKAGER

    def test_packager_exists(self) -> None:
        self.assertTrue(
            SCRIPT.is_file(),
            "scripts/package_plugin.py must exist before packaging can pass",
        )

    def test_repository_validates(self) -> None:
        packager = self.require_packager()
        self.assertEqual([], packager.validate_plugin(ROOT))

    def test_archive_is_deterministic_and_portable(self) -> None:
        packager = self.require_packager()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            archive_a = temp / "a.zip"
            archive_b = temp / "b.zip"
            packager.build_package(ROOT, archive_a)
            packager.build_package(ROOT, archive_b)

            self.assertEqual(archive_a.read_bytes(), archive_b.read_bytes())

            with zipfile.ZipFile(archive_a) as archive:
                names = archive.namelist()

            self.assertEqual(names, sorted(names))
            self.assertIn("plugin.json", names)
            self.assertIn("skills/perfect-eval/SKILL.md", names)
            self.assertIn("assets/icon.svg", names)
            self.assertFalse(any(name.startswith("docs/") for name in names))
            self.assertFalse(any(name.startswith("scripts/") for name in names))
            self.assertFalse(any(name.startswith("tests/") for name in names))
            self.assertFalse(any(name.startswith(".github/") for name in names))
            self.assertFalse(any(name.startswith("perfecteval/") for name in names))

    def test_manifest_traversal_is_rejected(self) -> None:
        packager = self.require_packager()
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            copy_package_source(temp)
            manifest_path = temp / "plugin.json"
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            manifest["extensions"]["com.openai"]["interface"]["composerIcon"] = (
                "./assets/../assets/icon.svg"
            )
            manifest_path.write_text(
                json.dumps(manifest, indent=2) + "\n", encoding="utf-8"
            )

            errors = packager.validate_plugin(temp)

            self.assertTrue(
                any("composerIcon" in error and "unsafe" in error for error in errors),
                errors,
            )


if __name__ == "__main__":
    unittest.main()
