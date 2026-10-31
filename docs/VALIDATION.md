# Validation report

Updated: 2026-10-30
Current source/private version: `0.1.1`

## Authoritative contracts checked

- OpenAI plugin packaging: https://developers.openai.com/plugins/build/plugins
- OpenAI skill packaging: https://developers.openai.com/plugins/build/skills
- OpenAI submission metadata/lifecycle: https://developers.openai.com/plugins/deploy/submission
- OpenAI submission errors: https://developers.openai.com/plugins/deploy/submission-errors
- Agent Plugins v1 schema/specification: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json and https://agent-plugins.org/specification
- Agent Skills specification: https://agentskills.io/specification
- GitHub Actions guidance: https://docs.github.com/actions

## Stable historical `0.1.0` evidence

- packaging implementation commit: `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`;
- successful workflow run: `41149191002`;
- job: `124381364234`;
- artifact ID: `13022281982`;
- outer artifact SHA-256: `623c4fabde6802360af5b36e34c986e88a10b4b649646bfedfd0b29a07a5dbc6`;
- inner ZIP SHA-256: `78dd7b5201a2dd3bc5abe67fa7da8955b4da9e6113c015869a46886cb3b5c57d`;
- private Plugin Creator installation: PASS;
- stored release inventory inspection: PASS.

Documentation-only workflow run `41149780988` later reproduced the same inner `0.1.0` ZIP hash.

## Portable package contract

The current validator enforces:

- Agent Plugins v1 root schema identity;
- lowercase kebab-case plugin name and semantic versioning;
- OpenAI presentation field limits used by this package;
- exact supported public category titles when category is present;
- capabilities count/length;
- default prompt count/length/normalized uniqueness;
- reviewer prompt list max 20 and each prompt nonblank/max 4,000 characters;
- optional public listing URLs are HTTPS, max 1,024 characters, with no embedded credentials;
- optional release notes are nonblank;
- optional country allowlists contain uppercase two-letter codes;
- brand color syntax;
- safe `./` asset paths and supported image types;
- SVG icons/logos square and at least 48x48;
- skill frontmatter identity/description rules;
- traversal, symlink, transient/dependency, and secret-shaped-file rejection;
- package boundary limited to `plugin.json`, `assets/**`, and `skills/**`;
- deterministic ZIP ordering, timestamp, permissions, and compression settings.

## Public-directory metadata TDD

### RED

Commit: `00d32bb61ab7b07a4f4477fb0d8b7e71af32c30f`
Workflow run: `41150238351`
Job: `124384783098`

Result: expected failure.

Seven tests ran. The four existing tests passed. Three new checks failed exactly for the intended missing behavior:

- missing `review` metadata;
- unsupported category not rejected;
- 4,001-character reviewer prompt not rejected.

No unrelated regression appeared.

### GREEN

Implementation commit: `fe3e75c85af28459e8c8a1f0a384c7bd67569211`
Workflow run: `41150753395`
Job: `124386429246`
Artifact ID: `13022558764`

Result: PASS.

All seven tests passed. The deterministic double-build comparison, archive inspection, and artifact upload also passed.

GitHub reported outer artifact SHA-256:

`c3b5482b9bf4d4e9a62e3c49c3ac1a9d123c68f46f29b3d10c6f11a5c5866ff9`

Independent inspection produced the same outer hash.

Inner portable plugin ZIP SHA-256:

`18cee08420a972f7d97ce4a12107f09ce51dd81e98fde1abfaed1a6ca710720d`

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

Confirmed absent: `.github/**`, `docs/**`, `scripts/**`, `tests/**`, and any wrapper directory.

The inspected inner manifest reports version `0.1.1`, category `Developer Tools`, eight reviewer prompts, dark logo metadata, and release notes.

## Private ChatGPT update verification

Result: PASS for package acceptance/storage.

The exact GREEN CI-produced `0.1.1` inner ZIP updated the existing owned private `perfecteval` plugin in place. Plugin Creator reported:

- version `0.1.1`;
- scope `USER`;
- discoverability `PRIVATE`;
- successful update status.

A subsequent stored-release read confirmed:

- stored version `0.1.1`;
- category `Developer Tools`;
- `logoDark: ./assets/logo-dark.svg`;
- all eight reviewer prompts;
- release notes;
- expected skill/asset inventory.

Account-specific backend IDs, release IDs, and account email are intentionally omitted from this public repository.

## Final no-runtime-drift verification

The documentation synchronization commit triggered workflow run `41151144978`, job `124387694657`.

Result: PASS.

All workflow steps succeeded: checkout, exact Python setup, seven unit tests, deterministic double-build comparison, archive inspection, and artifact upload.

Artifact ID: `13022559484`.

GitHub-reported outer artifact SHA-256:

`3b7315328f45e01da047c8972aeeaa50c2f62811b58b3fd345dee75d3e14493d`

Independent inspection produced the same outer hash.

Inner portable ZIP SHA-256:

`18cee08420a972f7d97ce4a12107f09ce51dd81e98fde1abfaed1a6ca710720d`

This exactly matches the installed `0.1.1` GREEN package, so the later documentation-only edits produced no runtime-package drift.

## Current OpenAI submission interpretation

Current OpenAI documentation states:

- `extensions.com.openai.review.prompts` accepts up to 20 nonblank strings, each at most 4,000 characters;
- skills-only plugins do not need MCP-specific five-positive/three-negative review cases, demo recording, or reviewer credentials solely for being skills-only;
- exact category is required for public submission;
- `publication.release_notes` is supported;
- verified Developer identity is selected in the submission flow and must not be inferred from repository ownership;
- four product/support/privacy/terms URLs are required for attached MCP review, while skills-only metadata validation does not require all four;
- package upload creates a draft, submission for review is separate, and publication is a later separate action after approval.

## Submission-tool availability check

The currently exposed Plugin Creator actions were inspected after the private `0.1.1` update. Available operations cover private plugin creation, update, file/archive inspection, metadata inspection, and release listing. No public-draft upload, submit-for-review, or publish action is exposed.

The currently exposed Plugin Management actions cover discovery, dependencies, permissions, suggestions, and uninstall. No public submission/publication action is exposed there either.

Therefore this conversation cannot honestly claim that a public directory draft was created. The verified ZIP is ready to be taken into the OpenAI Plugins dashboard, where the user must select the verified Developer identity, upload the ZIP, resolve automated findings, complete required attestations, submit for review, and publish only after approval.

## Remaining behavior/submission gaps

Fresh-chat behavior of the installed private plugin remains unverified from this conversation: activation, session-mode persistence/reset, and complete 13-stage execution still need a fresh-host smoke test.

Public submission remains separate from private installation. No public draft has been uploaded in this validation sequence; review, approval, and publication have not started.
