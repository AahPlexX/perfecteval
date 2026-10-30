# Validation report

Date: 2026-10-30
Validated implementation commit: `9b8e1d16b44c2b7842baaaa840575fb71c1ba06d`

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
- Manifest validates against the published Agent Plugins v1 JSON schema constraints used in the check.
- Plugin name `perfecteval` matches the v1 name pattern and length constraints.
- OpenAI-specific metadata is isolated under `extensions.com.openai`.
- No MCP server or hook dependency is declared.

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

### OpenAI listing metadata

Result: PASS for package-backed fields currently present.

Measured values:

- display name: 12 characters (limit 30);
- short description: 23 characters (limit 30);
- long description: 552 characters (limit 4000);
- capabilities: 10 entries (limit 20), longest 65 characters (limit 120);
- starter prompts: 3 entries, lengths 94 / 89 / 105 characters (limit 128 each);
- brand color: valid six-digit hex;
- declared asset paths are relative, under `./assets/`, and contain no traversal.

### Brand assets

Result: PASS

- `assets/icon.svg`: 128 x 128 with square viewBox.
- `assets/logo-light.svg`: 256 x 256 with square viewBox.
- `assets/logo-dark.svg`: 256 x 256 with square viewBox.
- SVG XML parses and dimensions are positive.
- Light/dark logos share the same geometry.

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

The local container available during this build could not resolve `github.com`, so a direct local clone/archive round-trip was not available. Repository contents were instead inspected through the connected GitHub plugin, and deterministic schema/length/YAML/SVG checks were executed against the committed package content retrieved from GitHub.

This limitation does not change the validation results above, but it means no claim is made that a fresh local/plugin-directory installation was smoke-tested in this session.

## Public directory readiness boundary

Technical package fields checked above are valid, but public submission is not marked ready because verified publisher identity and any publisher/legal fields required by the final submission flow must come from the actual verified submitting identity. They are intentionally not inferred from the GitHub owner name.
