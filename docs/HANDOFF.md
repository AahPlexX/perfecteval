# Perfect Eval handoff

Updated: 2026-10-30

## Current state

Perfect Eval source and the existing private ChatGPT plugin are both at version `0.1.1`.

Core product requirements remain satisfied:

- provider/model agnostic;
- repository/project agnostic;
- ordinary ChatGPT fallback without subagents;
- optional fresh-context workers when available;
- default human-in-the-loop mode;
- `/perfecteval mode autonomous` and `/perfecteval mode human` session controls;
- complete 13-stage default workflow with explicit `not-applicable` handling;
- all video-derived skills/roles represented and routed through the full workflow by default;
- connected GitHub optional, not required;
- no GitHub Actions runtime requirement;
- bounded review-loop convergence;
- risk-scaled evaluation depth;
- first-time-user testing;
- root-cause bug diagnosis and regression protection;
- learned rules from repeated misses/false positives;
- evidence-backed execution claims only.

Maintainer packaging automation is repository infrastructure only and is excluded from the distributed plugin ZIP.

## Canonical commands

```text
/perfecteval mode human
/perfecteval mode autonomous
```

A new conversation starts in `human`; the latest explicit command controls only the current conversation unless the host explicitly supplies durable state.

## Skill inventory

- `skills/perfect-eval/` — orchestrator and single-agent fallback
- `skills/risk-classifier/`
- `skills/write-evals/`
- `skills/code-review/`
- `skills/review-loop/`
- `skills/learned-rules/`
- `skills/first-time-user/`
- `skills/fix-a-bug/`

Specialized skills are stages of Perfect Eval rather than competing default entry points.

## Canonical documentation

- `README.md` — user/maintainer overview
- `docs/INTENT.md` — product intent
- `docs/ADR-0001-portable-skills-only-architecture.md` — runtime architecture
- `docs/ADR-0002-deterministic-maintainer-packaging.md` — package/CI architecture
- `docs/ACCEPTANCE.md` — observable scenarios
- `docs/VALIDATION.md` — executed evidence and limitations
- `docs/SUBMISSION.md` — public-directory readiness state
- this file — continuation handoff

## Public-metadata TDD evidence

RED:

- commit `00d32bb61ab7b07a4f4477fb0d8b7e71af32c30f`;
- workflow run `41150238351`;
- job `124384783098`;
- seven tests ran; four existing tests passed; the three new metadata tests failed exactly for missing review metadata/category validation/reviewer-prompt length validation.

GREEN:

- implementation commit `fe3e75c85af28459e8c8a1f0a384c7bd67569211`;
- workflow run `41150753395`;
- job `124386429246`;
- artifact `13022558764`;
- all seven tests passed;
- deterministic double-build, archive inspection, and artifact upload passed;
- outer artifact SHA-256 `c3b5482b9bf4d4e9a62e3c49c3ac1a9d123c68f46f29b3d10c6f11a5c5866ff9` matched independent inspection;
- inner portable ZIP SHA-256 `18cee08420a972f7d97ce4a12107f09ce51dd81e98fde1abfaed1a6ca710720d`.

The exact inner GREEN ZIP updated the existing private `perfecteval` plugin in place. Plugin Creator then confirmed stored version `0.1.1`, `Developer Tools`, dark logo, eight review prompts, release notes, and the expected file inventory.

Do not publish account-specific Plugin Creator IDs, release IDs, or account email in this public repository. Resolve the existing owned private plugin before any future update; do not create a duplicate.

## Current OpenAI submission facts

Checked against current OpenAI submission docs on 2026-10-30:

- Agent Plugins public metadata belongs under `extensions.com.openai`.
- Skills-only plugins may provide `review.prompts` and release notes.
- Review prompts are optional, max 20, max 4,000 characters each.
- Skills-only plugins do not need MCP-specific five-positive/three-negative cases, demo recording, or reviewer credentials solely for being skills-only.
- Exact supported category is required for submission.
- Verified publisher identity is selected during submission and must not be inferred from GitHub ownership or private-install normalization.
- Four listing URLs are required for attached MCP review; skills-only metadata validation does not require all four.

## Remaining behavioral validation

The installed private plugin has not yet been exercised from a fresh ChatGPT conversation in this session. Do not claim these as tested:

1. fresh-chat activation;
2. new-chat default to human mode;
3. autonomous-mode persistence within one chat;
4. immediate switch back to human;
5. full 13-stage ledger execution without subagents;
6. equivalent stage coverage with fresh-context workers.

## Public-submission boundary

The plugin is privately installed and technically packaged for a public-directory candidate, but no public draft has been uploaded in this sequence.

Do not invent:

- verified public `developerName`;
- publisher-matching website/support/privacy/terms URLs if required by the live submission surface;
- country targeting;
- commerce declarations;
- legal/policy attestations;
- review approval/publication state.

Private installation, draft upload, submission, approval, and publication are separate states.

## Next logical work

1. Check whether the currently exposed Plugin Creator/Plugin Management tools support creating or managing a public submission draft; if not, preserve the dashboard boundary explicitly.
2. Exercise the installed private plugin from a fresh ChatGPT conversation and verify acceptance scenarios A1-A4 plus one complete 13-stage run without subagents.
3. When fresh-context workers are available, compare stage-ledger equivalence against the single-agent run.
4. Resolve actual publisher identity and any live-dashboard publisher/legal/listing facts before public submission.
5. Upload a public draft only through the supported submission surface, resolve automated findings, complete required attestations, submit for review, and publish only after approval.
