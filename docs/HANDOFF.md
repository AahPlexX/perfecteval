# Perfect Eval handoff

Updated: 2026-10-30

## Current state

Perfect Eval is implemented and deterministically checked as a portable, skills-only Agent Plugin at version `0.1.0`.

Core requirements represented in the repository:

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
- Agent Skills spec: https://agentskills.io/specification
- Google Cloud generative AI evaluation overview: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview
- Microsoft Foundry generative AI evaluation guidance: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app

The video transcript explicitly identified write-evals, review-loop, first-time-user, fix-a-bug, classifier, builder, verifier, reviewer, orchestrator, and a separate code-review step. The implementation preserves these as skills or explicit roles.

## Validation status

Deterministic package checks completed successfully. See `docs/VALIDATION.md` for the exact evidence and limits.

Validated:

- root `plugin.json` against the Agent Plugins v1 schema constraints;
- all eight skill names, descriptions, directory identities, and combined plugin/skill identity lengths;
- `skills/perfect-eval/agents/openai.yaml` structure and policy fields;
- OpenAI listing text/prompt/capability limits for the fields currently present;
- brand color and relative asset paths;
- square, positive SVG dimensions/viewBoxes for icon and light/dark logos;
- mandatory no-subagent fallback and session-mode behavior by implementation inspection.

Environment limitation: the local container could not resolve `github.com`, so a fresh local clone/plugin-install smoke test was not possible in this session. Repository contents were inspected through the connected GitHub plugin and deterministic checks were run against the committed content retrieved from GitHub. Do not claim clean-install smoke-test evidence until that test is actually run.

## Known public-submission blocker

Do not invent public publisher identity. Final public Plugin Directory submission requires verified publisher/listing details from the actual submitting identity. The repository owner name alone is not proof of the verified OpenAI developer identity.

## Next logical work

1. Smoke-test plugin discovery and behavior in a clean ChatGPT/plugin environment when that surface is available.
2. Exercise both session-mode commands in a clean chat and confirm stage-ledger behavior with and without subagents.
3. Only when the verified publisher identity is supplied, complete public listing metadata and submission-readiness material.
