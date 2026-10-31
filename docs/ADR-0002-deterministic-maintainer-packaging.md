# ADR-0002: Deterministic maintainer packaging

- Status: Accepted
- Date: 2026-10-30

## Context

Perfect Eval's portable runtime must remain independent of GitHub Actions, but maintainers still need a reproducible way to validate the source package, produce the exact ZIP that is uploaded to ChatGPT, and retain execution evidence without hand-assembling release archives.

Earlier validation was constrained because the local container could not resolve `github.com`. The user explicitly authorized adding repository Actions when useful. That created an opportunity to move packaging verification into a clean GitHub runner while preserving the runtime architecture from ADR-0001.

The package boundary is intentionally narrower than the repository boundary: the distributed plugin should contain only the portable runtime surface, not repository docs, tests, scripts, or CI configuration.

## Decision

Use a deterministic, standard-library Python packager plus a maintainer-only GitHub Actions workflow.

### Source-of-truth files

- `scripts/package_plugin.py` — validates and builds the portable ZIP.
- `tests/test_package_plugin.py` — defines the packager contract and security/regression checks.
- `.github/workflows/package-plugin.yml` — executes the contract in GitHub and uploads the resulting ZIP artifact.

### Package boundary

The generated plugin archive contains only:

- `plugin.json`
- `assets/**`
- `skills/**`

The archive must not contain repository-only surfaces such as:

- `.github/**`
- `docs/**`
- `scripts/**`
- `tests/**`
- an extra wrapper directory

### Determinism and validation

The packager:

- validates the portable manifest, semantic version, plugin name, OpenAI presentation-field limits, referenced asset paths, SVG shape/size metadata, and skill frontmatter;
- rejects unsafe traversal-style asset paths, symlinks, dependency/transient directories, and secret-shaped package files;
- sorts archive entries;
- uses a fixed ZIP timestamp and fixed regular-file permissions;
- uses a fixed compression mode/level;
- reports SHA-256 of the generated archive.

The workflow builds the archive twice from the same checkout and requires byte equality before upload.

### CI security posture

The workflow:

- has `contents: read` permissions only;
- disables persisted checkout credentials;
- pins `actions/checkout`, `actions/setup-python`, and `actions/upload-artifact` to immutable full commit SHAs with the human-readable release version in comments;
- pins the Python runtime to an exact version;
- does not use repository secrets or publication credentials;
- uploads the validated ZIP as a short-retention workflow artifact.

### Runtime separation

The workflow and packager are repository-maintainer infrastructure only. They are excluded from the plugin ZIP and are not required for Perfect Eval to function in ChatGPT, Codex, another Agent Plugins-compatible host, or an offline/local environment.

Host-generated deployment files are also not canonical source. A private Plugin Creator install may add account-derived metadata or generate a compatibility `.codex-plugin/plugin.json`; those generated files remain deployment state and are not copied into the portable repository package automatically.

## Verification evidence

The TDD sequence was observed on 2026-10-30:

1. RED: the committed unit-test contract failed because `scripts/package_plugin.py` did not exist.
2. GREEN: the packager implementation was committed.
3. GitHub Actions run `41149191002` completed successfully for commit `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`.
4. Unit tests, double-build comparison, archive inspection, and artifact upload all passed.
5. GitHub artifact `13022281982` was downloaded and its reported SHA-256 matched independent inspection.
6. The inner plugin ZIP was installed successfully as a private ChatGPT plugin with Plugin Creator, and the stored release inventory was inspected.

Exact hashes and package inventory are recorded in `docs/VALIDATION.md`.

## Consequences

### Positive

- Maintainers can reproduce the same portable archive from the same source state.
- Package drift is caught before upload.
- Repository-only files cannot accidentally become runtime payload.
- CI evidence can be inspected independently of the development chat.
- The exact CI-produced bytes can be used for private installation and later submission preparation.
- Runtime portability remains unchanged.

### Tradeoffs

- GitHub Actions now exists in this repository even though it remains optional to the plugin itself; documentation must preserve that distinction.
- The custom validator mirrors selected published contract constraints and therefore must be updated when official package rules change.
- GitHub-hosted artifact wrapping is not the plugin payload itself; the inner `perfecteval.zip` remains the portable artifact whose digest matters for package identity.
- Private host normalization can make the stored ChatGPT release differ from the uploaded portable ZIP without implying a source mismatch.

## Rejected alternatives

- Manual ZIP assembly: rejected because it is easy to omit files, include repository-only files, or produce nondeterministic artifacts.
- Adding a runtime MCP service solely for validation/packaging: rejected because packaging is a maintainer concern, not a user workflow requirement.
- Depending on third-party packaging libraries: rejected because Python's standard library is sufficient for the current contract and avoids unnecessary dependency/version surface.
- Treating GitHub's outer workflow-artifact ZIP as the plugin artifact: rejected because it is a transport wrapper around `perfecteval.zip`.
