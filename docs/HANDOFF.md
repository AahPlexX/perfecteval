# Perfect Eval handoff

Updated: 2026-10-30

## Current state

Perfect Eval is a portable, skills-only Agent Plugin. Source is now a `0.1.1` GREEN candidate for public-directory metadata; the currently verified private ChatGPT release remains `0.1.0` until the new CI artifact passes and is installed in place.

Core requirements remain unchanged and satisfied by source design:

- provider/model agnostic;
- repository/project agnostic;
- complete ordinary-ChatGPT fallback without subagents;
- optional fresh-context workers when available;
- default human-in-the-loop mode;
- `/perfecteval mode autonomous` and `/perfecteval mode human` session controls;
- full 13-stage workflow with explicit `not-applicable` handling;
- video-derived skills/roles represented and routed through the full workflow by default;
- connected GitHub optional, not required;
- no GitHub Actions runtime requirement;
- bounded review-loop convergence;
- risk-scaled evaluation depth;
- first-time-user testing;
- root-cause bug diagnosis and regression protection;
- learned rules from repeated misses/false positives;
- evidence-backed execution claims only.

Maintainer packaging automation is repository infrastructure only. It is excluded from the plugin ZIP and remains optional to runtime behavior.

## Current TDD stage

Public-directory metadata RED was observed on commit `00d32bb61ab7b07a4f4477fb0d8b7e71af32c30f`:

- workflow run `41150238351`;
- job `124384783098`;
- 7 tests executed;
- 4 existing tests passed;
- 3 new submission-metadata tests failed exactly for missing review metadata, missing category validation, and missing review-prompt length validation.

GREEN source candidate now targets `0.1.1` and adds:

- `Developer Tools` category;
- `logoDark` using `assets/logo-dark.svg`;
- eight natural `review.prompts`;
- `publication.release_notes`;
- validator support for exact category titles, review-prompt count/length, optional HTTPS listing URLs, release notes, and optional country codes.

The private plugin must remain on `0.1.0` until GREEN CI succeeds and the exact CI artifact is inspected.

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

Specialized skills are stages of the full workflow, not competing default entry points.

## Canonical documentation

- `README.md` — user/maintainer overview
- `docs/INTENT.md` — product intent
- `docs/ADR-0001-portable-skills-only-architecture.md` — runtime architecture
- `docs/ADR-0002-deterministic-maintainer-packaging.md` — package/CI architecture
- `docs/ACCEPTANCE.md` — observable scenarios
- `docs/VALIDATION.md` — executed evidence and limitations
- `docs/SUBMISSION.md` — public-directory readiness state
- this file — continuation handoff

## Stable verified packaging/private-install evidence

Previously verified `0.1.0` state:

- packaging implementation commit: `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`;
- successful packaging workflow run: `41149191002`;
- job: `124381364234`;
- artifact: `13022281982`;
- portable ZIP SHA-256: `78dd7b5201a2dd3bc5abe67fa7da8955b4da9e6113c015869a46886cb3b5c57d`;
- private Plugin Creator installation: verified;
- stored private release inventory: verified;
- post-documentation workflow run `41149780988`: success and reproduced the same inner ZIP hash.

Do not publish account-specific Plugin Creator backend IDs or account email in the public repository. Resolve the existing owned private `perfecteval` plugin through Plugin Creator before updating it; do not create a duplicate.

## Current OpenAI submission facts

Checked against current OpenAI submission docs on 2026-10-30:

- Agent Plugins public metadata belongs under `extensions.com.openai`.
- Skills-only plugins may provide `review.prompts` and release notes.
- Review prompts are optional, max 20, max 4,000 characters each.
- Skills-only plugins do not need MCP-specific five-positive/three-negative cases, demo recording, or reviewer credentials solely for being skills-only.
- Exact supported category is required for submission.
- Verified publisher identity is selected in the submission flow and must not be inferred from GitHub ownership or private-install normalization.
- Four listing URLs are required for attached MCP review; skills-only metadata validation does not require all four.

## Remaining behavioral validation

The private plugin still has not been exercised from a fresh ChatGPT conversation in this session. Do not claim these as tested:

1. fresh-chat activation;
2. new-chat default to human mode;
3. autonomous-mode persistence in one chat;
4. immediate switch back to human;
5. all 13 stages without subagents;
6. stage equivalence with fresh-context workers.

## Public-submission boundary

Do not invent:

- verified `developerName`;
- publisher-matching website/support/privacy/terms URLs;
- country targeting;
- commerce declarations;
- legal/policy attestations;
- approval/publication state.

Private installation, draft upload, submission, approval, and publication are separate states.

## Next logical work

1. Observe GREEN CI for the `0.1.1` candidate and require all tests/package steps to pass.
2. Download and inspect the exact CI artifact; record inner and outer hashes.
3. Update the existing private `perfecteval` plugin in place from that exact artifact.
4. Verify stored `0.1.1` metadata/inventory through Plugin Creator.
5. Synchronize `README.md`, `docs/VALIDATION.md`, `docs/SUBMISSION.md`, and this handoff with the final GREEN/install evidence.
6. Perform fresh-chat behavioral smoke tests when the installed private plugin can be invoked in a new chat.
7. Only then proceed toward a public draft once verified publisher/legal/listing facts are available.
