# Validation report

Date: 2026-10-30
Core manifest revision validated after publisher-neutral correction: `a633bd4407047d7f03ba1c6df83f1cb2739b3512`

## Authoritative contracts checked

- OpenAI plugin packaging: https://developers.openai.com/plugins/build/plugins
- OpenAI skill packaging: https://developers.openai.com/plugins/build/skills
- OpenAI submission errors/limits: https://developers.openai.com/plugins/deploy/submission-errors
- OpenAI submission metadata: https://developers.openai.com/plugins/deploy/submission
- Agent Plugins v1 specification: https://agent-plugins.org/specification
- Agent Plugins v1 manifest schema: https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- Agent Skills specification: https://agentskills.io/specification

## Checks executed

### Portable manifest

Result: PASS

- `plugin.json` exists at plugin root.
- `$schema` matches the canonical Agent Plugins v1 identifier.
- The current publisher-neutral manifest validates against the published Agent Plugins v1 JSON schema constraints used in the check.
- Plugin name `perfecteval` matches the v1 name pattern and length constraints.
- No MCP server or hook dependency is declared.
- Public-directory `interface` metadata is intentionally omitted until a verified publisher identity is supplied; OpenAI documents `interface` as optional for Agent Plugins packages and can derive basic package text from root metadata.

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

For all eight skills, validation checked:

- directory name matches frontmatter `name`;
- name uses lowercase letters/numbers/hyphens only;
- no leading/trailing/consecutive hyphen;
- name length <= 64;
- non-empty description <= 1024 characters;
- unique skill identity;
- combined `perfecteval:<skill-name>` identity <= 64 characters.

### OpenAI skill metadata

Result: PASS

`skills/perfect-eval/agents/openai.yaml` parses as a mapping and contains:

- non-empty `interface.display_name`;
- non-empty `interface.short_description`;
- non-empty `interface.default_prompt`;
- valid `policy.products` values (`CHAT`, `CODEX`);
- boolean `policy.allow_implicit_invocation`;
- no unsupported policy keys.

This supplies ChatGPT/Codex presentation for the orchestrator without inventing plugin-level publisher identity.

### Prepared brand assets

Result: PASS

- `assets/icon.svg`: 128 x 128 with square viewBox.
- `assets/logo-light.svg`: 256 x 256 with square viewBox.
- `assets/logo-dark.svg`: 256 x 256 with square viewBox.
- SVG XML parses and dimensions are positive.
- Light/dark logos share the same geometry.

The assets are intentionally not declared in plugin-level public listing metadata yet.

### Architecture requirements

Result: PASS by inspection.

- Provider/model neutrality is explicit.
- Repository/project neutrality is explicit.
- No-subagent fallback is explicit and mandatory.
- Default mode is human-in-the-loop.
- `/perfecteval mode autonomous` persists for the current conversation until changed.
- `/perfecteval mode human` switches back immediately.
- New chats reset to human mode unless the host supplies durable state.
- Every source-workflow stage is accounted for in the mandatory stage ledger.
- GitHub Actions are not required or added.
- Repository browsing is not treated as runtime test execution.
- Review loops have convergence rules and hard stop behavior.

## Environment limitation

The local container available during this build could not resolve `github.com`, so a direct local clone/archive round-trip was not available. Repository contents were instead inspected through the connected GitHub plugin, and deterministic schema/length/YAML/SVG checks were executed against committed content retrieved from GitHub.

No claim is made that a fresh local/plugin-directory installation was smoke-tested in this session.

## Public directory readiness boundary

The portable functional package is implemented and the checks above pass. Public Plugin Directory submission is intentionally not marked ready because `developerName`, category/listing copy, and any other publisher-facing fields that depend on the verified submitting identity must be supplied from that verified identity rather than inferred from the GitHub owner name.
