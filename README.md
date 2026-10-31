# Perfect Eval

Perfect Eval is a skills-only, provider-agnostic evaluation plugin for ChatGPT and other Agent Plugins-compatible clients. It turns requirements, product behavior, repository evidence, incidents, and bugs into a repeatable prove-review-fix-regress workflow.

The plugin is intentionally independent of any specific model provider, repository layout, CI system, programming language, or subagent feature.

## Session modes

Perfect Eval starts every new chat in **human-in-the-loop** mode.

```text
/perfecteval mode human
/perfecteval mode autonomous
```

The latest explicit command in the current conversation wins and stays active until changed. A new conversation resets to `human` unless the host explicitly supplies persistent state.

`autonomous` removes routine approval pauses but does not expand permissions, publication authority, destructive-action authority, spending authority, repository access, or safety boundaries.

## Default workflow

Every substantive run accounts for all 13 stages; a stage may be `not-applicable` with a concrete reason but is never silently dropped:

1. Resolve session mode.
2. Inspect target, requirements, evidence, tools, and execution limits.
3. Classify risk.
4. Write capability + regression evals.
5. Build or repair when requested and authorized.
6. Verify applicable evals.
7. Run an independent review.
8. Iterate builder -> verifier -> reviewer with convergence limits.
9. Learn durable rules from repeated misses/noise.
10. Run a first-time-user test for user-facing work.
11. Diagnose and fix any reproducible remaining bug.
12. Re-run affected regression/capability checks.
13. Report evidence, uncertainty, regressions, and next action.

## Packaged skills

- `perfect-eval` — orchestrator and full fallback workflow
- `risk-classifier`
- `write-evals`
- `code-review`
- `review-loop`
- `learned-rules`
- `first-time-user`
- `fix-a-bug`

Specialized skills are stages of the full workflow rather than competing default entry points. Unless the user explicitly requests only one stage, they route back into the complete Perfect Eval ledger or continue it sequentially when sibling-skill invocation is unavailable.

## Works without subagents

Subagents are optional. When fresh-context workers exist, Perfect Eval may use them for independence or safe parallelism. Without them, the primary agent executes the same roles sequentially with explicit role isolation and the same stage ledger.

## Repository behavior

Perfect Eval can use connected GitHub or another repository capability when available, but repository connectivity is evidence/action infrastructure rather than a methodology dependency.

The plugin does **not** require GitHub Actions. This repository contains explicitly authorized maintainer-only validation/package automation that is excluded from the distributed plugin ZIP.

Repository browsing is not test execution. If the host cannot execute tests, Perfect Eval reports runtime results as unverified rather than simulating them.

## Maintainer validation and packaging

```text
scripts/package_plugin.py
tests/test_package_plugin.py
.github/workflows/package-plugin.yml
```

Validate locally:

```bash
python scripts/package_plugin.py --check
```

Build deterministically:

```bash
mkdir -p dist
python scripts/package_plugin.py --output dist/perfecteval.zip
```

The validator covers the portable manifest, OpenAI presentation/submission metadata constraints implemented by this project, safe referenced assets, skill frontmatter, traversal/symlink/secret-shaped-file rejection, and deterministic packaging. The ZIP contains only `plugin.json`, `assets/`, and `skills/`.

## Public-directory preparation

Current version: `0.1.1`.

Repository-controlled public metadata now includes:

- category `Developer Tools`;
- light/dark listing logos;
- eight natural reviewer prompts covering Perfect Eval's actual workflows;
- release notes for the candidate package.

Current OpenAI guidance allows skills-only plugins to provide reviewer prompts and release notes without MCP-specific review cases, a demo recording, or reviewer credentials solely because the plugin is skills-only.

The repository intentionally does **not** invent verified publisher identity, final publisher URLs, country targeting, commerce declarations, or legal/policy attestations. Private Plugin Creator normalization is deployment state, not proof of public-directory verification or approval.

Canonical submission status lives in `docs/SUBMISSION.md`.

## Current verification status

- `0.1.0` deterministic packaging and private install: verified historically.
- Public-metadata RED contract: observed failing for exactly the intended three missing behaviors.
- `0.1.1` GREEN CI: verified; all seven tests, double-build comparison, archive inspection, and artifact upload passed.
- Exact CI-produced `0.1.1` ZIP: independently inspected and installed into the existing private Perfect Eval plugin in place.
- Stored private `0.1.1` manifest/inventory: verified through Plugin Creator.
- Fresh-chat installed-plugin behavior: not yet smoke-tested from this conversation.
- Public draft upload/review/approval/publication: not started.

See `docs/VALIDATION.md` for hashes/run evidence, `docs/SUBMISSION.md` for marketplace readiness, and `docs/HANDOFF.md` for the exact continuation point.
