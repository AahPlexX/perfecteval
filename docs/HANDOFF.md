# Perfect Eval handoff

Updated: 2026-10-30

## Current state

Perfect Eval is implemented as a portable, skills-only Agent Plugin at version `0.1.0`.

Core requirements currently represented in the repository:

- provider/model agnostic;
- repository/project agnostic;
- ordinary ChatGPT chat support without subagents;
- optional use of subagents when available;
- default human-in-the-loop mode;
- session command to switch to autonomous mode and back;
- full default stage ledger with explicit not-applicable handling;
- all video-derived skills/roles represented;
- connected GitHub usable as an optional repository capability;
- no GitHub Actions requirement;
- convergence limits for review loops;
- risk-scaled evaluation depth;
- first-time-user testing;
- root-cause bug diagnosis and regression creation;
- learned rules from repeated misses or false positives;
- evidence-backed execution claims only.

## Canonical user commands

```text
/perfecteval mode human
/perfecteval mode autonomous
```

A new conversation starts in `human`. The latest explicit command controls the current conversation until changed. Do not claim persistence into a different chat.

## Skill inventory

- `skills/perfect-eval/` — orchestrator and single-agent fallback
- `skills/risk-classifier/`
- `skills/write-evals/`
- `skills/code-review/`
- `skills/review-loop/`
- `skills/learned-rules/`
- `skills/first-time-user/`
- `skills/fix-a-bug/`

## Architecture

See `docs/ADR-0001-portable-skills-only-architecture.md`.

The plugin uses root `plugin.json` with Agent Plugins v1 schema and OpenAI-specific presentation metadata under `extensions.com.openai`. No MCP server is required.

## Research basis

Primary/authoritative references used in the implementation:

- User-provided video: https://youtu.be/S49gppZl8H0
- Anthropic code review article: https://claude.dev/blog/solving-code-review-at-anthropic/
- Anthropic eval guidance: https://www.anthropic.com/research/demystifying-evals-for-ai-agents
- OpenAI eval best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- OpenAI plugin docs: https://developers.openai.com/plugins
- OpenAI plugin packaging: https://developers.openai.com/plugins/build/plugins
- OpenAI skill docs: https://developers.openai.com/plugins/build/skills
- Agent Plugins v1 spec: https://agent-plugins.org/specification
- Google Cloud generative AI evaluation overview: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview
- Microsoft Foundry generative AI evaluation guidance: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app

The video transcript explicitly identified write-evals, review-loop, first-time-user, fix-a-bug, classifier, builder, verifier, reviewer, orchestrator, and a separate code-review step. The implementation preserves these as skills or explicit roles.

## Validation status

Repository/package validation should verify:

- `plugin.json` against Agent Plugins v1 schema;
- every immediate child of `skills/` contains exactly one valid `SKILL.md`;
- YAML frontmatter parses with non-empty `name` and `description`;
- skill names are unique;
- referenced assets exist and are square SVGs;
- OpenAI listing strings stay within current limits;
- no secret-shaped files or symlinks enter the package;
- no runtime claim is made unless actually executed.

## Known submission blocker

Do not invent public publisher identity. Final public Plugin Directory submission requires verified publisher/listing details from the actual submitting identity. The repository owner name alone is not proof of the verified OpenAI developer identity.

## Next logical work

1. Run package/schema validation against the exact current commit.
2. Correct any validation issue without changing the product boundary.
3. Test plugin discovery in a clean ChatGPT/plugin environment if that surface is available.
4. Only when the verified publisher identity is supplied, complete public listing metadata and submission-readiness material.
