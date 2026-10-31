# Public Plugin Directory preparation

Updated: 2026-10-30
Status: TDD RED — repository-controlled submission metadata contract is committed, implementation pending.

## Purpose

This document tracks public Plugin Directory readiness separately from private installation, package validity, review approval, and publication. It is the canonical handoff for submission-specific work.

## Current verified baseline

- Portable source package: validated.
- Deterministic GitHub Actions packaging: validated.
- Exact CI-produced ZIP: privately installed through Plugin Creator.
- Stored private release inventory: inspected.
- Fresh-chat behavioral smoke test: not yet executed from this conversation.
- Public submission draft: not uploaded.
- Public review: not started.
- Public publication: not started.

## Current OpenAI submission contract checked 2026-10-30

Authoritative source: https://developers.openai.com/plugins/deploy/submission

For this skills-only plugin:

- public directory metadata is supplied under `extensions.com.openai.interface`;
- an exact supported category is required for public submission;
- reviewer prompts may be supplied under `extensions.com.openai.review.prompts`;
- release notes may be supplied under `extensions.com.openai.publication.release_notes`;
- skills-only plugins do not require MCP-specific five-positive/three-negative test cases, a demo recording, or reviewer credentials solely because they contain skills;
- the selected verified developer identity is a submission/dashboard fact and must not be inferred from GitHub ownership or private-install normalization;
- public URL requirements must be satisfied with accessible HTTPS pages whose publisher identity matches the selected verified publisher when they apply to the submission;
- legal/policy attestations are completed by the authorized developer in the submission flow, not fabricated in source control.

## Repository-controlled metadata selected

These values are based on the actual product behavior and do not depend on publisher identity:

- Category: `Developer Tools`.
- Dark listing logo: `./assets/logo-dark.svg`.
- Reviewer prompts: natural prompts covering full evaluation, eval authoring, candidate comparison, independent review, no-subagent execution, bug diagnosis, first-time-user evaluation, and autonomous-mode behavior.
- Release notes: concise description of the initial public-directory candidate.
- Semantic version target for this metadata release: `0.1.1`.

## TDD RED contract

`tests/test_package_plugin.py` now requires the public-candidate metadata above and requires the repository validator to reject:

- unsupported category values;
- review prompts longer than the documented 4,000-character maximum.

At this RED stage, `plugin.json` is intentionally still `0.1.0` and does not yet contain the selected category/review/publication metadata, and `scripts/package_plugin.py` does not yet enforce those submission-specific constraints. CI is therefore expected to fail until the GREEN implementation lands.

## Deliberately unresolved publisher/dashboard facts

Do not invent or infer any of the following:

- verified `developerName`;
- final publisher-matching `websiteURL`;
- final `supportURL`;
- final `privacyPolicyURL`;
- final `termsOfServiceURL`;
- country availability;
- commerce declarations if the submission surface asks for them;
- legal/policy attestations;
- final dashboard-selected/verified identity state.

The private Plugin Creator release contains account-derived author/developer metadata and a host-selected compatibility category. Those values are deployment state for the private release and are not evidence of the public-directory identity or final listing choices.

## Next steps

1. Observe the intentional RED CI run for the submission-metadata tests.
2. Add the selected metadata to `plugin.json`, bump to `0.1.1`, and extend `scripts/package_plugin.py` to validate the supported category list plus reviewer-prompt constraints.
3. Require CI GREEN and inspect the exact `0.1.1` artifact.
4. Update the existing private `perfecteval` plugin in place from that exact artifact; do not create a duplicate plugin.
5. Keep fresh-chat behavioral smoke testing separate from package acceptance.
6. Prepare publisher URLs/policies only from confirmed publisher identity and legal/data-practice decisions.
7. Upload a public submission draft only when the verified identity/listing facts are available and the user has authorized that online action.
