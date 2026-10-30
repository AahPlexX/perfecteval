# Perfect Eval handoff

Updated: 2026-10-30

## Current state

Perfect Eval is implemented as a portable, skills-only Agent Plugin at version `0.1.0`.

The repository currently satisfies the core product requirements:

- provider/model agnostic;
- repository/project agnostic;
- ordinary ChatGPT chat support without subagents;
- optional fresh-context/subagent use when available;
- default human-in-the-loop mode;
- session command to switch to autonomous mode and back;
- full default stage ledger with explicit `not-applicable` handling;
- all video-derived skills/roles represented and routed through the full workflow by default;
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

Each specialized skill now declares that it is a stage of Perfect Eval. Unless the user explicitly asks for that stage only, it routes into the complete workflow or continues the remaining ledger sequentially if sibling-skill invocation is unavailable.

## Architecture and acceptance

- Architecture: `docs/ADR-0001-portable-skills-only-architecture.md`
- Observable behavior scenarios: `docs/ACCEPTANCE.md`
- Product intent: `docs/INTENT.md`
- Validation evidence and limits: `docs/VALIDATION.md`
- User-facing overview: `README.md`

The plugin uses root `plugin.json` with the Agent Plugins v1 schema. Portable packages discover the root `skills/` directory automatically. No MCP server is required.

The root manifest now includes non-identity OpenAI presentation metadata under `extensions.com.openai.interface` so ChatGPT/Codex can present the product as **Perfect Eval** with accurate descriptions, capabilities, starter prompts, brand color, composer icon, and logo. Verified publisher-dependent fields remain intentionally unset.

## Research basis

Primary/authoritative references used in the implementation include:

- User-provided video: https://youtu.be/S49gppZl8H0
- Anthropic code review article: https://claude.dev/blog/solving-code-review-at-anthropic/
- Anthropic eval guidance: https://www.anthropic.com/research/demystifying-evals-for-ai-agents
- OpenAI eval best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- OpenAI plugin docs: https://developers.openai.com/plugins
- OpenAI plugin packaging: https://developers.openai.com/plugins/build/plugins
- OpenAI skill docs: https://developers.openai.com/plugins/build/skills
- OpenAI submission metadata: https://developers.openai.com/plugins/deploy/submission
- Agent Plugins v1 spec/schema: https://agent-plugins.org/specification and https://agent-plugins.org/schemas/1.0.0/plugin.schema.json
- Agent Skills spec: https://agentskills.io/specification
- Google Cloud generative AI evaluation overview: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview
- Microsoft Foundry generative AI evaluation guidance: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app

The video transcript explicitly identified write-evals, review-loop, first-time-user, fix-a-bug, classifier, builder, verifier, reviewer, orchestrator, and a separate code-review step. The implementation preserves these as skills or explicit roles.

## Validation status

See `docs/VALIDATION.md` for exact evidence.

Current deterministic checks cover:

- Agent Plugins v1 root-manifest schema constraints;
- current OpenAI presentation-field limits and asset-path rules;
- all eight skill identities/frontmatter requirements;
- orchestrator OpenAI skill metadata;
- square SVG icon/logo requirements;
- mandatory no-subagent fallback;
- session-mode semantics;
- full-stage routing from specialized skills.

Environment limitation remains: the available local container cannot resolve `github.com`, so a clean archive clone and fresh ChatGPT/plugin-install discovery smoke test has not yet been executed. Do not convert static/package evidence into a claim that installation behavior was observed.

## Public-submission boundary

Do not invent the verified publisher identity. Final public Plugin Directory submission still needs the actual verified `developerName`, dashboard category, and any other publisher-facing facts required by the submission surface. Package validity, local installation, submission, approval, and publication are separate states.

## Next logical work

1. Build the exact repository archive in an environment with repository/network access and perform a clean plugin install/discovery smoke test.
2. Exercise both session-mode commands in a new ChatGPT conversation and confirm that mode persists only within that conversation.
3. Exercise one full workflow in an environment without subagents and, separately, with fresh-context workers when available; compare stage-ledger equivalence.
4. Only after verified publisher identity/category are available, complete public-directory metadata and submission-readiness material.
