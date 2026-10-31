# Perfect Eval handoff

Updated: 2026-10-30

## Current state

Perfect Eval is implemented as a portable, skills-only Agent Plugin. The currently installed private release is version `0.1.0`.

Core product requirements remain satisfied:

- provider/model agnostic;
- repository/project agnostic;
- ordinary ChatGPT chat support without subagents;
- optional fresh-context/subagent use when available;
- default human-in-the-loop mode;
- `/perfecteval mode autonomous` and `/perfecteval mode human` session controls;
- full 13-stage default workflow with explicit `not-applicable` handling;
- all video-derived skills/roles represented and routed through the full workflow by default;
- connected GitHub usable as an optional repository capability;
- no GitHub Actions runtime requirement;
- convergence limits for review loops;
- risk-scaled evaluation depth;
- first-time-user testing;
- root-cause bug diagnosis and regression creation;
- learned rules from repeated misses or false positives;
- evidence-backed execution claims only.

Maintainer packaging automation is complete and verified. The repository contains a deterministic Python packager, unit tests, and a read-only GitHub Actions workflow. The exact CI-produced `0.1.0` ZIP was installed successfully through Plugin Creator as the existing private `perfecteval` plugin. Do **not** create a duplicate private plugin; update the existing owned plugin in place after a new validated artifact is produced.

## Current work in progress — public-directory metadata TDD

Public-directory preparation has now started. The canonical submission-specific status is `docs/SUBMISSION.md`.

A RED test contract is being introduced for repository-controlled public metadata. Until the GREEN implementation lands:

- source `plugin.json` remains `0.1.0`;
- `category`, `review.prompts`, `publication.release_notes`, and `logoDark` are not yet committed to the source manifest;
- `scripts/package_plugin.py` does not yet validate the supported category list or reviewer-prompt 4,000-character limit;
- the new tests are expected to fail;
- do not update the private plugin from this RED state.

Planned GREEN target:

- source version `0.1.1`;
- category `Developer Tools`;
- dark listing logo `./assets/logo-dark.svg`;
- natural reviewer prompts covering the actual Perfect Eval workflows;
- initial public-candidate release notes;
- validator coverage for supported categories and reviewer-prompt limits;
- successful GitHub Actions packaging;
- update of the existing private plugin from the exact CI artifact.

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

Each specialized skill is a stage of Perfect Eval. Unless the user explicitly asks for that stage only, it routes into the complete workflow or continues the remaining ledger sequentially if sibling-skill invocation is unavailable.

## Architecture and documentation

- Portable architecture: `docs/ADR-0001-portable-skills-only-architecture.md`
- Deterministic maintainer packaging: `docs/ADR-0002-deterministic-maintainer-packaging.md`
- Public-directory preparation: `docs/SUBMISSION.md`
- Observable behavior scenarios: `docs/ACCEPTANCE.md`
- Product intent: `docs/INTENT.md`
- Validation evidence and limits: `docs/VALIDATION.md`
- User-facing overview: `README.md`

The plugin uses root `plugin.json` with the Agent Plugins v1 schema. Portable packages discover root `skills/` automatically. No MCP server is required.

A private Plugin Creator install was observed to normalize the stored release by adding account-derived author/developer metadata, a host-selected default category, and a compatibility `.codex-plugin/plugin.json`. Those generated values are deployment state and are intentionally not copied into public source control. Do not expose account email or backend plugin/release identifiers in public repository docs.

## Research basis

Primary/authoritative sources include:

- User-provided video: https://youtu.be/S49gppZl8H0
- Anthropic code review: https://claude.dev/blog/solving-code-review-at-anthropic/
- Anthropic verification loops: https://claude.com/resources/articles/building-verification-loops-in-claude-code-with-skills
- Anthropic evals: https://www.anthropic.com/research/demystifying-evals-for-ai-agents
- OpenAI eval best practices: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- OpenAI plugin docs: https://developers.openai.com/plugins
- OpenAI submission lifecycle: https://developers.openai.com/plugins/deploy/submission
- Agent Plugins v1: https://agent-plugins.org/specification
- Agent Skills: https://agentskills.io/specification
- Google Cloud generative AI evaluation: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview
- Microsoft Foundry generative AI evaluation: https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app

The 2026-10-30 research session retrieved a machine-readable transcript for the user-provided video and corroborated operational rules against first-party sources.

## Verified packaging/private-install evidence

See `docs/VALIDATION.md` for exact details. Stable evidence before the current RED submission-metadata step:

- packaging implementation commit: `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`;
- successful workflow run: `41149191002`;
- successful job: `124381364234`;
- artifact: `13022281982`;
- portable ZIP SHA-256: `78dd7b5201a2dd3bc5abe67fa7da8955b4da9e6113c015869a46886cb3b5c57d`;
- private Plugin Creator installation: verified;
- stored private release inventory: verified;
- post-documentation workflow run `41149780988`: success;
- post-documentation artifact preserved the same inner portable ZIP SHA-256.

## Remaining behavioral validation

This conversation still cannot invoke the newly created private plugin through the general Plugin Management search surface. Do not claim the following as tested yet:

1. Fresh-chat implicit or explicit activation.
2. New-chat default to `human`.
3. Autonomous-mode persistence within one chat.
4. Immediate switch back to human mode.
5. Full 13-stage ledger execution without subagents.
6. Equivalent stage coverage with fresh-context workers.

These are behavioral smoke-test gaps, not packaging defects.

## Public-submission boundary

Current OpenAI guidance confirms a skills-only plugin does not require the MCP-specific five-positive/three-negative review cases, demo recording, or reviewer credentials solely for being skills-only. Repository-controlled category, reviewer prompts, release notes, and presentation metadata can be prepared now.

Do **not** infer or invent:

- verified public `developerName`;
- final publisher-matching website/support/privacy/terms URLs;
- country targeting;
- commerce declarations when not established;
- legal/policy attestations;
- review approval or publication state.

Private install, draft upload, submission, approval, and publication are separate states.

## Next logical work

1. Observe the intentional RED CI run from the submission-metadata test contract.
2. Implement the `0.1.1` metadata + validator GREEN change.
3. Require CI success and inspect the exact `0.1.1` artifact.
4. Update the existing private `perfecteval` plugin from that exact artifact.
5. Continue fresh-chat behavioral smoke testing when the host exposes the private plugin in a new conversation.
6. Resolve verified publisher identity and public legal/support URLs before any public submission action.
