# Public Plugin Directory preparation

Updated: 2026-10-30
Status: `0.1.1` package verified and privately installed; public draft not uploaded.

## Current verified state

- Portable source `0.1.1`: implemented.
- Public-metadata TDD RED: observed.
- GREEN GitHub Actions run: passed.
- Exact CI-produced `0.1.1` ZIP: independently inspected.
- Existing private Perfect Eval plugin: updated in place to `0.1.1` from that exact ZIP.
- Stored private release manifest/inventory: verified.
- Fresh-chat behavioral smoke test: not yet executed from this conversation.
- Public submission draft: not uploaded.
- Public review: not started.
- Public publication: not started.

## Current OpenAI submission contract checked 2026-10-30

Authoritative source: https://developers.openai.com/plugins/deploy/submission

For this skills-only plugin:

- public directory metadata is supplied under `extensions.com.openai.interface`;
- exact supported category is required for submission;
- natural reviewer prompts may be supplied at `extensions.com.openai.review.prompts`;
- reviewer prompts are optional, at most 20 nonblank strings, each at most 4,000 characters;
- release notes may be supplied under `extensions.com.openai.publication.release_notes`;
- skills-only plugins do not require MCP-specific five-positive/three-negative cases, a demo recording, or reviewer credentials solely because they contain skills;
- the selected verified Developer identity is a submission/dashboard fact and must not be inferred from GitHub ownership or private-install normalization;
- the four listing URLs are required for attached MCP review, while skills-only metadata validation does not require all four;
- legal/policy attestations are completed by the authorized developer in the submission flow.

## TDD evidence

### RED

Commit: `00d32bb61ab7b07a4f4477fb0d8b7e71af32c30f`
Workflow run: `41150238351`
Job: `124384783098`

Seven tests ran. Four existing tests passed and the three new public-metadata tests failed exactly for missing review metadata, missing category validation, and missing reviewer-prompt length validation.

### GREEN

Implementation commit: `fe3e75c85af28459e8c8a1f0a384c7bd67569211`
Workflow run: `41150753395`
Job: `124386429246`
Artifact ID: `13022558764`

All seven tests passed, followed by successful deterministic double-build comparison, archive inspection, and artifact upload.

Artifact hashes:

- GitHub outer artifact SHA-256: `c3b5482b9bf4d4e9a62e3c49c3ac1a9d123c68f46f29b3d10c6f11a5c5866ff9`.
- Independently computed outer artifact SHA-256: same value.
- Inner portable `perfecteval.zip` SHA-256: `18cee08420a972f7d97ce4a12107f09ce51dd81e98fde1abfaed1a6ca710720d`.

The inner package contains only `plugin.json`, `assets/**`, and `skills/**` and reports version `0.1.1`, category `Developer Tools`, eight reviewer prompts, and release notes.

## Repository-controlled public metadata now verified

- Version: `0.1.1`.
- Category: `Developer Tools`.
- Dark listing logo: `./assets/logo-dark.svg`.
- Eight natural reviewer prompts covering full evaluation, eval authoring, candidate comparison, independent review, no-subagent execution, bug diagnosis, first-time-user evaluation, and autonomous-mode behavior.
- Release notes describing the initial public-directory candidate.

The validator enforces exact supported category titles, reviewer-prompt count/length, optional HTTPS listing URLs when present, nonblank optional release notes, optional uppercase two-letter country codes, plus the existing package/asset/skill safety rules.

## Private install/update evidence

The existing owned private `perfecteval` plugin was updated in place from the exact GREEN CI ZIP. Plugin Creator reports version `0.1.1`, scope `USER`, and `PRIVATE` discoverability. A subsequent stored-manifest read confirmed the expected category, dark logo, eight reviewer prompts, and release notes.

Account email and backend plugin/release identifiers are deliberately not stored in this public repository.

Private installation is not public submission, review approval, or publication.

## Deliberately unresolved publisher/dashboard facts

Do not invent or infer:

- verified public `developerName`;
- publisher-matching `websiteURL`, `supportURL`, `privacyPolicyURL`, or `termsOfServiceURL` if the selected submission flow requires them;
- country availability;
- commerce declarations if applicable;
- legal/policy attestations;
- final dashboard-selected identity state.

The private Plugin Creator release may contain account-derived compatibility metadata. Treat it as deployment state, not as evidence for the public publisher identity.

## Remaining gates

1. Exercise the installed private plugin from a fresh ChatGPT conversation and verify session-mode/13-stage behavior.
2. Resolve the intended verified publisher identity and any publisher-facing URLs or policy facts required by the live submission dashboard.
3. Upload a public submission draft when those facts are available and the user has authorized that online action.
4. Resolve automated findings, complete required attestations, submit for review, and only after approval perform the separate publish action.
