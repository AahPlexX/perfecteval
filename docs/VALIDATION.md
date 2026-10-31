# Validation report

Updated: 2026-10-30
Current source candidate: `0.1.1` (GREEN implementation; CI pending at this revision)

## Authoritative contracts checked

- OpenAI plugin packaging: https://developers.openai.com/plugins/build/plugins
- OpenAI skill packaging: https://developers.openai.com/plugins/build/skills
- OpenAI submission metadata/lifecycle: https://developers.openai.com/plugins/deploy/submission
- OpenAI submission errors: https://developers.openai.com/plugins/deploy/submission-errors
- Agent Plugins v1 schema/specification: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json and https://agent-plugins.org/specification
- Agent Skills specification: https://agentskills.io/specification
- GitHub Actions guidance: https://docs.github.com/actions

## Stable verified `0.1.0` evidence

Portable packaging and private installation were verified before the public-metadata increment:

- implementation commit: `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`;
- successful workflow run: `41149191002`;
- successful job: `124381364234`;
- artifact ID: `13022281982`;
- outer artifact SHA-256: `623c4fabde6802360af5b36e34c986e88a10b4b649646bfedfd0b29a07a5dbc6`;
- inner portable ZIP SHA-256: `78dd7b5201a2dd3bc5abe67fa7da8955b4da9e6113c015869a46886cb3b5c57d`;
- private Plugin Creator upload/install: PASS;
- stored private release inventory inspection: PASS.

A later documentation-only run `41149780988` also passed and reproduced the same inner portable ZIP hash, demonstrating that repository-only documentation did not change the runtime package.

## Portable package contract

Previously verified and still enforced by the packager:

- root `plugin.json` uses the Agent Plugins v1 schema;
- plugin name is lowercase kebab-case and bounded;
- version uses strict semantic versioning;
- `extensions.com.openai.interface` presentation limits are checked;
- default prompts are bounded and unique after normalization;
- brand colors use `#RRGGBB` syntax;
- referenced assets use safe `./` relative paths and supported image types;
- SVG icons/logos are square and at least 48x48;
- every direct child under `skills/` contains valid `SKILL.md` frontmatter;
- package rejects traversal paths, symlinks, transient/dependency paths, and secret-shaped files;
- archive contains only `plugin.json`, `assets/**`, and `skills/**`;
- ZIP entry ordering, timestamps, permissions, compression mode, and compression level are deterministic.

## Public-directory metadata TDD

### RED

Commit: `00d32bb61ab7b07a4f4477fb0d8b7e71af32c30f`
Workflow run: `41150238351`
Job: `124384783098`

Result: expected failure.

Seven unit tests ran. Existing package behavior remained green, while the three new public-metadata checks failed exactly for the missing functionality:

- `test_public_candidate_metadata_is_present`: ERROR because `extensions.com.openai.review` was absent;
- `test_invalid_public_category_is_rejected`: FAIL because an unsupported category produced no validator error;
- `test_overlong_review_prompt_is_rejected`: FAIL because a 4,001-character review prompt produced no validator error.

The workflow stopped before package creation/artifact upload, as intended.

### GREEN source candidate

The `0.1.1` candidate adds:

- exact category `Developer Tools`;
- `logoDark: ./assets/logo-dark.svg`;
- eight natural reviewer prompts;
- `publication.release_notes`;
- validator enforcement for the documented category set;
- review prompt list max 20 and per-prompt max 4,000 characters;
- optional HTTPS listing-URL validation when those fields are present;
- nonblank optional release notes;
- uppercase two-letter optional country codes.

At this documentation revision, the GREEN CI run has not yet been observed. Therefore:

- source-level implementation status: GREEN candidate;
- CI/package status for `0.1.1`: UNVERIFIED;
- private installed version: still verified `0.1.0`;
- public submission draft: NOT UPLOADED;
- public review/approval/publication: NOT STARTED.

## Current public-submission interpretation

Current OpenAI documentation states:

- `extensions.com.openai.review.prompts` may contain up to 20 nonblank strings, each at most 4,000 characters;
- skills-only plugins do not need MCP-specific five-positive/three-negative review cases or a demo recording solely for being skills-only;
- exact category is required for public submission;
- `publication.release_notes` is supported;
- a verified Developer identity is selected during submission and must not be inferred from repository ownership;
- the four product/support/privacy/terms URLs are required for attached MCP review, while skills-only metadata validation does not require all four.

## Private-host normalization boundary

The `0.1.0` private Plugin Creator install generated deployment-specific compatibility metadata, including account-derived author/developer values and a `.codex-plugin/plugin.json`. These host-generated values are not copied back into source control and are not evidence of public-directory publisher verification, final category selection, review approval, or publication.

## Remaining behavior gap

The installed private plugin has not yet been invoked from a fresh ChatGPT conversation in this session. Session-mode persistence, implicit/explicit activation, and complete stage-ledger execution in the installed host remain behavioral smoke-test items rather than package-validation claims.
