# Validation report

Date: 2026-10-30
Current package implementation commit: `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`
Validated manifest presentation revision: `774b5da3ee9efb8e71313ad7d90af349677a7f92`
Validated manifest blob: `ffcf1f6300e67bab34d2b701b074daccb769d58b`

## Authoritative contracts checked

- OpenAI plugin packaging: https://developers.openai.com/plugins/build/plugins
- OpenAI skill packaging: https://developers.openai.com/plugins/build/skills
- OpenAI submission metadata: https://developers.openai.com/plugins/deploy/submission
- OpenAI submission errors/limits: https://developers.openai.com/plugins/deploy/submission-errors
- Agent Plugins v1 manifest schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- Agent Plugins v1 specification: https://agent-plugins.org/specification
- Agent Skills specification: https://agentskills.io/specification
- GitHub Actions workflow syntax/security guidance: https://docs.github.com/actions
- Python release index: https://www.python.org/downloads/

## Checks executed

### Portable manifest

Result: PASS

- `plugin.json` exists at plugin root.
- `$schema` matches the canonical Agent Plugins v1 identifier.
- The manifest validates against the published Agent Plugins v1 constraints covered by the repository validator.
- Plugin name `perfecteval` satisfies the published name pattern and length constraints.
- No MCP server or lifecycle-hook dependency is declared.
- Portable skill discovery relies on the root `skills/` directory, which OpenAI documents as automatically discovered for Agent Plugins packages.

### OpenAI presentation metadata

Result: PASS for package-level structure/limits checked here; public submission remains a separate gate.

`extensions.com.openai.interface` supplies non-identity presentation metadata:

- `displayName`: `Perfect Eval` — 12/30 characters.
- `shortDescription`: `Evidence-first eval workflows` — 29/30 characters.
- `longDescription`: 628/4000 characters.
- `capabilities`: 10 entries; longest is 90/120 characters.
- `defaultPrompt`: 3 prompts; lengths are 102, 99, and 108 characters, each within the 128-character limit.
- `brandColor`: `#111111`; valid `#RRGGBB` and approximately 18.88:1 contrast against white.
- `composerIcon`: `./assets/icon.svg`.
- `logo`: `./assets/logo-light.svg`.
- Declared asset paths are package-relative, `./`-prefixed, and contain no traversal segment.

The portable repository manifest intentionally does not hard-code account-derived publisher identity from a private install. Public publisher/listing fields remain a submission-lifecycle concern.

### Skill inventory

Result: PASS

Eight immediate child skill directories are present and each has a `SKILL.md`:

1. `perfect-eval`
2. `risk-classifier`
3. `write-evals`
4. `code-review`
5. `review-loop`
6. `learned-rules`
7. `first-time-user`
8. `fix-a-bug`

For all eight skills, deterministic validation covers:

- directory name matches frontmatter `name`;
- name uses lowercase letters/numbers/hyphens only;
- no leading/trailing/consecutive hyphen;
- name length <= 64;
- non-empty description <= 1024 characters;
- unique skill identity.

Every specialized skill states that it is a stage of Perfect Eval, not a competing default entry point, and routes back into the complete stage ledger unless the user explicitly requests stage-only work.

### OpenAI skill metadata

Result: PASS

`skills/perfect-eval/agents/openai.yaml` contains:

- non-empty `interface.display_name`;
- non-empty `interface.short_description`;
- non-empty `interface.default_prompt`;
- valid `policy.products` values (`CHAT`, `CODEX`);
- boolean `policy.allow_implicit_invocation`.

### Prepared brand assets

Result: PASS

- `assets/icon.svg`: 128 x 128 with square viewBox.
- `assets/logo-light.svg`: 256 x 256 with square viewBox.
- `assets/logo-dark.svg`: 256 x 256 with square viewBox.
- SVG XML parses and dimensions are positive.
- Light/dark logos share the same geometry.

### Architecture requirements

Result: PASS by implementation inspection.

- Provider/model neutrality is explicit.
- Repository/project neutrality is explicit.
- No-subagent fallback is explicit and mandatory.
- Default mode is human-in-the-loop.
- `/perfecteval mode autonomous` persists for the current conversation until changed.
- `/perfecteval mode human` switches back immediately.
- New chats reset to human mode unless the host supplies durable state.
- Every source-workflow stage is accounted for in the mandatory stage ledger.
- Specialized skill activation routes into the full ledger unless explicitly stage-only.
- GitHub Actions are not a plugin runtime requirement.
- Repository browsing is not treated as runtime test execution.
- Review loops have convergence rules and hard-stop behavior.

## Maintainer packaging automation

Result: PASS

### RED evidence

The committed unit-test contract was executed before `scripts/package_plugin.py` existed.

Observed result:

- 4 tests discovered;
- `test_packager_exists` failed with the expected missing-packager assertion;
- 3 behavior tests skipped because the implementation was absent;
- process exit status was non-zero.

This demonstrated that the test contract could detect the missing behavior before GREEN implementation.

### GREEN implementation

Commit: `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`

`scripts/package_plugin.py` now:

- validates the portable manifest and skill structure;
- validates declared OpenAI presentation-field limits covered by the script;
- validates referenced asset safety and SVG dimensions;
- rejects traversal-style paths, symlinks, dependency/transient package paths, and secret-shaped files;
- packages only `plugin.json`, `assets/**`, and `skills/**`;
- writes sorted ZIP entries with fixed timestamp, fixed regular-file permissions, and fixed compression settings;
- reports the generated ZIP SHA-256.

`tests/test_package_plugin.py` verifies repository validation, deterministic output/package boundary, and rejection of a traversal-style manifest path.

### GitHub Actions execution

Result: PASS

Workflow: `.github/workflows/package-plugin.yml`

Run evidence:

- workflow run ID: `41149191002`;
- job ID: `124381364234`;
- head commit: `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`;
- unit-test step: success;
- double-build deterministic comparison: success;
- archive inspection: success;
- artifact upload: success;
- overall job: success.

The workflow uses:

- `permissions: contents: read`;
- `actions/checkout` v7.0.1 pinned to commit `3d3c42e5aac5ba805825da76410c181273ba90b1` with persisted credentials disabled;
- `actions/setup-python` v7.1.0 pinned to commit `6d4fd22b20465ccc0f7354476588e8df7c9ca0e0`;
- Python `3.15.2`;
- `actions/upload-artifact` v7.0.2 pinned to commit `cf430e030ddbb5b0abf93d22962f4752f3646cd9`.

### CI artifact inspection

Result: PASS

GitHub artifact:

- artifact ID: `13022281982`;
- artifact name: `perfecteval-plugin-8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`;
- reported outer-artifact SHA-256: `623c4fabde6802360af5b36e34c986e88a10b4b649646bfedfd0b29a07a5dbc6`;
- independently inspected outer-artifact SHA-256: same value.

The outer GitHub workflow artifact contains exactly one payload file: `perfecteval.zip`.

Inner portable plugin ZIP SHA-256:

`78dd7b5201a2dd3bc5abe67fa7da8955b4da9e6113c015869a46886cb3b5c57d`

Inner ZIP inventory:

- `assets/icon.svg`
- `assets/logo-dark.svg`
- `assets/logo-light.svg`
- `plugin.json`
- `skills/code-review/SKILL.md`
- `skills/first-time-user/SKILL.md`
- `skills/fix-a-bug/SKILL.md`
- `skills/learned-rules/SKILL.md`
- `skills/perfect-eval/SKILL.md`
- `skills/perfect-eval/agents/openai.yaml`
- `skills/perfect-eval/references/eval-contract.md`
- `skills/perfect-eval/references/methodology.md`
- `skills/perfect-eval/references/repository-mode.md`
- `skills/perfect-eval/references/session-mode.md`
- `skills/review-loop/SKILL.md`
- `skills/risk-classifier/SKILL.md`
- `skills/write-evals/SKILL.md`

Confirmed absent from the portable ZIP:

- `.github/**`
- `docs/**`
- `scripts/**`
- `tests/**`
- any extra wrapper directory.

## Private ChatGPT install smoke test

Result: PASS for package acceptance/storage; behavioral invocation remains a separate unverified check.

The exact CI-produced inner `perfecteval.zip` was supplied to Plugin Creator.

Observed result:

- creation status: success;
- plugin name: `perfecteval`;
- plugin version: `0.1.0`;
- scope: `USER`;
- discoverability: `PRIVATE`;
- a concrete current release was created;
- the stored release file inventory was readable through Plugin Creator.

For privacy and because the repository is public, account-specific backend plugin/release identifiers are not recorded here. A future authorized agent should resolve the existing private `perfecteval` through Plugin Creator rather than creating a duplicate.

### Host normalization observed

Plugin Creator stored the uploaded portable package with host-generated normalization:

- the stored root `plugin.json` contains account-derived author/developer metadata not present in source;
- a generated `.codex-plugin/plugin.json` compatibility manifest is present in the private stored release;
- the compatibility manifest contains a host-selected default category.

No account email or private backend identifier is copied into this public repository.

These generated fields are deployment state. They do not redefine the portable source package and are not treated as proof of public Plugin Directory identity verification, category selection, review approval, or publication.

### Same-chat invocation limitation

After private creation, the general Plugin Management search surface did not return `Perfect Eval` in the current conversation. Therefore this session does **not** claim that the installed plugin's invocation routing, session-mode persistence, or full stage ledger has been exercised from a fresh ChatGPT conversation.

Status distinction:

- portable source validation: PASS;
- deterministic CI packaging: PASS;
- private Plugin Creator upload/install: PASS;
- stored-release inventory inspection: PASS;
- fresh-chat behavioral invocation: UNVERIFIED;
- public submission: NOT STARTED in this validation sequence;
- public approval/publication: NOT STARTED.

## Environment notes

The earlier local container could not directly resolve `github.com`, so it could not clone the repository itself. This is no longer a packaging blocker because GitHub Actions performed the clean repository checkout and packaging, and the resulting artifact was downloaded and independently inspected in the container.

The remaining environment gap is behavioral: a fresh ChatGPT conversation needs to invoke the installed private plugin and exercise session-mode and workflow behavior.

## Public directory readiness boundary

A successful private install does not equal public-directory readiness.

Before submission, use the current OpenAI submission lifecycle to establish the intended verified publisher identity, supported category/listing values, required public URLs, country targeting, commerce declarations if applicable, attestations, scans, and any other dashboard requirements. Do not infer public readiness from the private release's account-derived metadata or generated category.
