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
- no GitHub Actions runtime requirement;
- convergence limits for review loops;
- risk-scaled evaluation depth;
- first-time-user testing;
- root-cause bug diagnosis and regression creation;
- learned rules from repeated misses or false positives;
- evidence-backed execution claims only.

Maintainer packaging automation is now complete and verified. The repository includes a deterministic Python packager, unit tests, and a read-only GitHub Actions workflow that produces the exact portable plugin ZIP. None of that maintainer infrastructure is packaged into or required by Perfect Eval at runtime.

The exact CI-produced portable ZIP has also been installed successfully as a private ChatGPT plugin through Plugin Creator, and the stored release inventory has been inspected. Do **not** create another private `perfecteval` instance by default; resolve the existing owned private plugin through Plugin Creator before updating it.

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

Each specialized skill declares that it is a stage of Perfect Eval. Unless the user explicitly asks for that stage only, it routes into the complete workflow or continues the remaining ledger sequentially if sibling-skill invocation is unavailable.

## Architecture and acceptance

- Portable architecture: `docs/ADR-0001-portable-skills-only-architecture.md`
- Deterministic maintainer packaging: `docs/ADR-0002-deterministic-maintainer-packaging.md`
- Observable behavior scenarios: `docs/ACCEPTANCE.md`
- Product intent: `docs/INTENT.md`
- Validation evidence and limits: `docs/VALIDATION.md`
- User-facing overview: `README.md`

The plugin uses root `plugin.json` with the Agent Plugins v1 schema. Portable packages discover the root `skills/` directory automatically. No MCP server is required.

The source manifest includes non-identity OpenAI presentation metadata under `extensions.com.openai.interface` so ChatGPT/Codex can present the product as **Perfect Eval** with accurate descriptions, capabilities, starter prompts, brand color, composer icon, and logo.

A private Plugin Creator install was observed to normalize the stored release by adding account-derived author/developer metadata, a host-selected default category, and a compatibility `.codex-plugin/plugin.json`. Those generated values are deployment state and are intentionally not copied into the public repository. Do not expose account email or backend plugin/release identifiers in public repo docs.

## Research basis

Primary/authoritative references used in the implementation include:

- User-provided video: https://youtu.be/S49gppZl8H0
- Anthropic code review article: https://claude.dev/blog/solving-code-review-at-anthropic/
- Anthropic verification-loop guidance: https://claude.com/resources/articles/building-verification-loops-in-claude-code-with-skills
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

The 2026-10-30 research session retrieved a machine-readable transcript for the user-provided video. That transcript explicitly identified write-evals, review-loop, first-time-user, fix-a-bug, classifier, builder, verifier, reviewer, orchestrator, and a separate code-review step. The implementation preserves these as skills or explicit roles and corroborates operational behavior against first-party sources.

## Packaging and validation evidence

See `docs/VALIDATION.md` for exact evidence.

Important verified state:

- TDD RED was observed before packager implementation.
- `scripts/package_plugin.py` is implemented.
- `tests/test_package_plugin.py` passes in GitHub Actions.
- `.github/workflows/package-plugin.yml` completed successfully for implementation commit `8a3d0b918d3bead8fc6779aacb8ec5a790a5ea84`.
- workflow run ID: `41149191002`;
- workflow job ID: `124381364234`;
- GitHub artifact ID: `13022281982`;
- outer artifact SHA-256: `623c4fabde6802360af5b36e34c986e88a10b4b649646bfedfd0b29a07a5dbc6`;
- inner portable ZIP SHA-256: `78dd7b5201a2dd3bc5abe67fa7da8955b4da9e6113c015869a46886cb3b5c57d`;
- private Plugin Creator installation: verified;
- stored private release inventory: verified.

The public repository intentionally omits account-specific Plugin Creator backend IDs. Future authorized work should discover the existing private `perfecteval` through Plugin Creator and preserve its current release/audience rather than creating a duplicate.

## Remaining behavioral validation

The current conversation could not invoke the newly created private plugin through the general Plugin Management search surface; the search returned no `Perfect Eval` result after creation. Therefore the following remain unverified in the installed host and must not be claimed as complete:

1. Fresh-chat implicit or explicit activation of Perfect Eval.
2. New-chat default to `human` mode.
3. `/perfecteval mode autonomous` persistence within one chat.
4. Immediate switch back with `/perfecteval mode human`.
5. Full 13-stage ledger execution without subagents.
6. Equivalent stage coverage when fresh-context workers/subagents are available.

These are behavioral smoke tests, not packaging defects.

## Public-submission boundary

Private installation is **not** public submission.

Do not infer public-directory readiness from the private release's account-derived developer metadata or generated category. Public submission still requires the actual intended verified publisher identity, selected supported category/listing values, required public URLs, supported countries, commerce declarations if applicable, legal/policy attestations, scans, and the current OpenAI review/submission workflow.

Package validity, private installation, draft upload, submission, approval, and publication remain separate states.

## Next logical work

1. Open a fresh ChatGPT conversation with the existing private `perfecteval` plugin selected/available and exercise the session-mode acceptance scenarios A1-A4.
2. Run one complete Perfect Eval evaluation in ordinary chat without subagents and verify all 13 ledger stages are accounted for.
3. When a host exposes fresh-context workers, run the same acceptance target with them and compare stage-ledger equivalence against the single-agent result.
4. Promote any discovered behavioral failure into `docs/ACCEPTANCE.md`, a regression test/eval, or a concise learned rule as appropriate.
5. After behavioral smoke tests pass, prepare the public Plugin Directory submission package/listing using the actual verified publisher and required dashboard facts; do not invent missing publication metadata.
