# Perfect Eval

Perfect Eval is a skills-only, provider-agnostic evaluation plugin for ChatGPT and other Agent Plugins-compatible clients. It turns requirements, product behavior, repository evidence, incidents, and bugs into a repeatable prove-review-fix-regress workflow.

The plugin is intentionally independent of any specific model provider, repository layout, CI system, programming language, or subagent feature.

## Session modes

Perfect Eval starts every new chat in **human-in-the-loop** mode.

Use one of these commands at any time:

```text
/perfecteval mode human
/perfecteval mode autonomous
```

The latest explicit command in the current conversation wins and stays active until changed. A new conversation resets to `human` unless the host explicitly supplies persistent state.

`autonomous` mode removes routine approval pauses but does not expand permissions, publication authority, destructive-action authority, spending authority, repository access, or safety boundaries.

## Default workflow

Every substantive Perfect Eval run accounts for every stage below. A stage can be `not-applicable` with a reason, but it is never silently dropped.

1. Resolve current session mode.
2. Inspect target, requirements, evidence, tools, and execution limits.
3. Classify risk.
4. Write capability + regression evals.
5. Build or repair when the user requested and authorized mutation.
6. Verify every applicable eval.
7. Run an independent review for failures the evals missed.
8. Iterate builder -> verifier -> reviewer with convergence limits.
9. Learn durable review rules from repeated misses/noise.
10. Run a first-time-user test for user-facing work.
11. Diagnose and fix any reproducible remaining bug.
12. Re-run affected regression/capability checks.
13. Report evidence, uncertainty, regressions, and the next highest-value action.

## Packaged skills

- `perfect-eval` — orchestrator and full fallback workflow
- `risk-classifier` — consequence-based risk tiering
- `write-evals` — creates task banks, graders, hard gates, and decision rules
- `code-review` — independent review with evidence-backed findings
- `review-loop` — convergent builder/verifier/reviewer orchestration
- `learned-rules` — turns repeated misses/false positives into durable guidance
- `first-time-user` — fresh-user evaluation without implementation knowledge
- `fix-a-bug` — reproduce, diagnose root cause, repair, and regression-protect failures

The specialized skills are stages of the full workflow rather than competing default entry points. Unless the user explicitly requests only one stage, each specialized skill routes back into the complete Perfect Eval ledger or continues it sequentially when sibling-skill invocation is unavailable.

## Works without subagents

Subagents are optional. If the host can spawn fresh-context workers, Perfect Eval may use them for independence or safe parallelism. If not, the primary agent executes the same roles sequentially and preserves role isolation by freezing evidence before switching roles and refusing to treat earlier unverified conclusions as facts.

This means the plugin is intended to work in ordinary ChatGPT conversations as well as Work/Codex-style environments.

## Repository behavior

Perfect Eval can use a connected GitHub plugin or another repository capability when available. Repository access is evidence/action infrastructure, not part of the eval methodology itself.

The plugin does **not** require GitHub Actions and does not add CI automation unless the user explicitly requests it.

Repository browsing is not test execution. If the host cannot execute tests, Perfect Eval reports runtime results as unverified rather than simulating them.

## Research basis

The initial workflow synthesis was researched on 2026-10-30 from:

- User-provided video: https://youtu.be/S49gppZl8H0
- Anthropic first-party article: https://claude.dev/blog/solving-code-review-at-anthropic/
- Anthropic first-party eval guidance: https://www.anthropic.com/research/demystifying-evals-for-ai-agents
- OpenAI evaluation best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- OpenAI plugin and skills documentation: https://developers.openai.com/plugins
- Agent Plugins v1 specification: https://agent-plugins.org/specification
- Agent Skills specification: https://agentskills.io/specification
- Google Cloud generative AI evaluation overview: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview
- Microsoft Foundry generative AI evaluation guidance: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app

See `skills/perfect-eval/references/methodology.md` for the evidence-backed synthesis and source rationale.

## Plugin shape

Perfect Eval uses the portable Agent Plugins v1 root `plugin.json` format and is skills-only: no MCP server, external runtime service, provider API key, or CI integration is required for the core workflow. Portable packages discover the root `skills/` directory automatically.

The root manifest includes non-identity OpenAI presentation metadata under `extensions.com.openai.interface`: the user-facing `Perfect Eval` name, descriptions, capabilities, starter prompts, brand color, composer icon, and logo. These fields improve ChatGPT/Codex presentation without inventing publisher identity.

ChatGPT-specific presentation for the orchestrator also lives in `skills/perfect-eval/agents/openai.yaml`. Verified publisher-dependent fields such as `developerName`, category, and any future legal/support listing facts remain intentionally unset until they are supplied from the actual verified submitting identity.

## Current status

Version: `0.1.0`

The repository contains the implementation, brand assets, research references, deterministic validation evidence, acceptance scenarios, and current handoff documentation. The functional package is implemented; public Plugin Directory submission remains a separate state because verified publisher/listing facts and a clean install/discovery smoke test must not be inferred or fabricated.
