# Validation report

Date: 2026-10-30
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

## Checks executed

### Portable manifest

Result: PASS

- `plugin.json` exists at plugin root.
- `$schema` matches the canonical Agent Plugins v1 identifier.
- The manifest validates against the published Agent Plugins v1 JSON schema constraints used in the check.
- Plugin name `perfecteval` satisfies the published name pattern and length constraints.
- No MCP server or lifecycle-hook dependency is declared.
- Portable skill discovery relies on the root `skills/` directory, which OpenAI documents as automatically discovered for Agent Plugins packages.

### OpenAI presentation metadata

Result: PASS for package-level structure/limits checked here; public submission remains a separate gate.

`extensions.com.openai.interface` now supplies non-identity presentation metadata:

- `displayName`: `Perfect Eval` — 12/30 characters.
- `shortDescription`: `Evidence-first eval workflows` — 29/30 characters.
- `longDescription`: 628/4000 characters.
- `capabilities`: 10 entries; longest is 90/120 characters.
- `defaultPrompt`: 3 prompts; lengths are 102, 99, and 108 characters, each within the 128-character limit.
- `brandColor`: `#111111`; valid `#RRGGBB` and approximately 18.88:1 contrast against white.
- `composerIcon`: `./assets/icon.svg`.
- `logo`: `./assets/logo-light.svg`.
- Declared asset paths are package-relative, `./`-prefixed, and contain no traversal segment.

OpenAI documents `interface` as optional for portable Agent Plugins package upload, while public listing fields such as `developerName` and `category` are required at submission. Those publisher-dependent fields remain intentionally unset rather than inferred.

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

For all eight skills, prior deterministic validation checked:

- directory name matches frontmatter `name`;
- name uses lowercase letters/numbers/hyphens only;
- no leading/trailing/consecutive hyphen;
- name length <= 64;
- non-empty description <= 1024 characters;
- unique skill identity;
- combined `perfecteval:<skill-name>` identity <= 64 characters.

Every specialized skill now states that it is a stage of Perfect Eval, not a competing default entry point, and routes back into the complete stage ledger unless the user explicitly requests stage-only work.

### OpenAI skill metadata

Result: PASS

`skills/perfect-eval/agents/openai.yaml` parses as a mapping and contains:

- non-empty `interface.display_name`;
- non-empty `interface.short_description`;
- non-empty `interface.default_prompt`;
- valid `policy.products` values (`CHAT`, `CODEX`);
- boolean `policy.allow_implicit_invocation`;
- no unsupported policy keys identified by the prior validation pass.

### Prepared brand assets

Result: PASS

- `assets/icon.svg`: 128 x 128 with square viewBox.
- `assets/logo-light.svg`: 256 x 256 with square viewBox.
- `assets/logo-dark.svg`: 256 x 256 with square viewBox.
- SVG XML parses and dimensions are positive.
- Light/dark logos share the same geometry.
- Current manifest declares the composer icon and light logo; the dark logo remains packaged and available for a future `logoDark` declaration if desired.

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
- GitHub Actions are not required or added.
- Repository browsing is not treated as runtime test execution.
- Review loops have convergence rules and hard-stop behavior.

## Environment limitation

The local container available during this work cannot resolve `github.com`, so a direct local clone/archive round-trip and fresh ChatGPT install/discovery smoke test were not executed from that container. Repository contents were inspected and mutated through the connected GitHub plugin, and deterministic schema/length/metadata checks were executed against the committed manifest content.

No claim is made that a fresh plugin installation has been smoke-tested yet.

## Public directory readiness boundary

The portable functional package is implemented and the deterministic checks above pass. Public Plugin Directory submission is intentionally not marked ready because verified `developerName`, dashboard category, and any other publisher/listing facts must come from the actual submitting identity rather than being inferred from the GitHub owner name. Public submission and approval are separate states from package validity.
