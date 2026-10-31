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

## Repository behavior

Perfect Eval can use a connected GitHub plugin or another repository capability when available. Repository access is evidence/action infrastructure, not part of the eval methodology itself.

The plugin does **not** require GitHub Actions. This repository includes an explicitly authorized, maintainer-only validation/package workflow, but that workflow is excluded from the plugin ZIP and is not a runtime dependency.

Repository browsing is not test execution. If the host cannot execute tests, Perfect Eval reports runtime results as unverified rather than simulating them.

## Maintainer validation and packaging

Repository tooling:

```text
scripts/package_plugin.py
tests/test_package_plugin.py
.github/workflows/package-plugin.yml
```

Local validation:

```bash
python scripts/package_plugin.py --check
```

Deterministic package build:

```bash
mkdir -p dist
python scripts/package_plugin.py --output dist/perfecteval.zip
```

The validator covers portable manifest structure, OpenAI presentation limits, supported public category titles, review-prompt limits, safe referenced assets, optional HTTPS listing URLs, skill frontmatter, unsafe paths, symlinks, secret-shaped files, and the deterministic portable package boundary. The ZIP contains only `plugin.json`, `assets/`, and `skills/`.

See `docs/VALIDATION.md` and `docs/ADR-0002-deterministic-maintainer-packaging.md` for execution evidence and rationale.

## Public-directory preparation

Source version: `0.1.1`.

The `0.1.1` candidate adds repository-controlled public-directory metadata that can be established without guessing publisher identity:

- category: `Developer Tools`;
- light/dark listing logos;
- natural reviewer prompts covering Perfect Eval's real workflows;
- release notes for the candidate package.

Current OpenAI guidance allows skills-only plugins to provide reviewer prompts and release notes without MCP-specific review cases, a demo recording, or reviewer credentials solely because the plugin is skills-only.

The repository intentionally does **not** invent the verified public publisher identity, final publisher URLs, country targeting, commerce declarations, or legal/policy attestations. Private Plugin Creator normalization is deployment state, not proof of public-directory verification or approval.

Canonical submission status lives in `docs/SUBMISSION.md`.

## Research basis

The workflow was researched on 2026-10-30 from the user-provided video plus first-party Anthropic, OpenAI, Google Cloud, Microsoft, Agent Plugins, and Agent Skills documentation. See `skills/perfect-eval/references/methodology.md` for the evidence-backed synthesis and source rationale.

## Plugin shape

Perfect Eval uses the portable Agent Plugins v1 root `plugin.json` format and is skills-only: no MCP server, external runtime service, provider API key, or CI integration is required for the core workflow. Portable packages discover the root `skills/` directory automatically.

OpenAI-specific presentation/review/publication metadata lives under `extensions.com.openai`. ChatGPT-specific presentation for the orchestrator also lives in `skills/perfect-eval/agents/openai.yaml`.

## Current verification status

- `0.1.0` deterministic CI packaging: verified.
- `0.1.0` exact CI ZIP private Plugin Creator installation: verified.
- `0.1.1` public-metadata RED tests: observed failing for the intended missing behavior.
- `0.1.1` GREEN source implementation: committed candidate; CI verification pending at this revision.
- Fresh-chat behavior of the installed private plugin: not yet smoke-tested from this session.
- Public draft upload/review/approval/publication: not started.

See `docs/HANDOFF.md` for the exact continuation point and `docs/VALIDATION.md` for evidence IDs/hashes.
