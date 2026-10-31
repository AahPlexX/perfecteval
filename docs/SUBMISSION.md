# Public Plugin Directory preparation

Updated: 2026-10-30
Status: GREEN implementation committed candidate; CI verification pending.

## Purpose

This document tracks public Plugin Directory readiness separately from private installation, package validity, review approval, and publication. It is the canonical handoff for submission-specific work.

## Current verified baseline

- Portable source package `0.1.0`: validated.
- Deterministic GitHub Actions packaging for `0.1.0`: validated.
- Exact CI-produced `0.1.0` ZIP: privately installed through Plugin Creator.
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
- natural reviewer prompts may be supplied at `extensions.com.openai.review.prompts`;
- reviewer prompts are optional, with at most 20 nonblank strings and at most 4,000 characters each;
- release notes may be supplied under `extensions.com.openai.publication.release_notes`;
- skills-only plugins do not require MCP-specific five-positive/three-negative cases, a demo recording, or reviewer credentials solely because they contain skills;
- the selected verified developer identity is a submission/dashboard fact and must not be inferred from GitHub ownership or private-install normalization;
- skills-only metadata validation does not require the four MCP review URLs, while attached MCP apps do;
- legal/policy attestations are completed by the authorized developer in the submission flow, not fabricated in source control.

## RED evidence

Commit: `00d32bb61ab7b07a4f4477fb0d8b7e71af32c30f`
Workflow run: `41150238351`
Job: `124384783098`

Seven tests ran. Four existing tests passed and the three newly introduced public-metadata checks failed exactly as intended:

1. `test_public_candidate_metadata_is_present` errored because `extensions.com.openai.review` was absent.
2. `test_invalid_public_category_is_rejected` failed because the validator did not yet reject an unsupported category value.
3. `test_overlong_review_prompt_is_rejected` failed because the validator did not yet enforce the 4,000-character prompt limit.

No unrelated regression appeared. Packaging/artifact steps were skipped because the unit-test step failed.

## GREEN candidate implemented

Source version target: `0.1.1`.

Repository-controlled metadata now included in the GREEN candidate:

- Category: `Developer Tools`.
- Dark listing logo: `./assets/logo-dark.svg`.
- Eight natural reviewer prompts covering full evaluation, eval authoring, candidate comparison, independent review, no-subagent execution, bug diagnosis, first-time-user evaluation, and autonomous-mode behavior.
- Release notes describing the initial public-directory candidate.

The packager/validator now additionally checks:

- exact supported category titles;
- reviewer prompts are a list of at most 20 entries;
- each reviewer prompt is nonblank and at most 4,000 characters;
- optional public listing URLs, when present, are HTTPS, at most 1,024 characters, and contain no embedded credentials;
- optional publication release notes are nonblank when supplied;
- optional country allowlists, when supplied, contain uppercase two-letter codes.

The existing package-boundary, asset, skill, traversal, symlink, secret-shaped-file, and deterministic ZIP checks remain in place.

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

## Current gate

The GREEN source change is not considered validated until GitHub Actions passes the complete test/package workflow and the resulting `0.1.1` artifact is inspected.

Until that evidence exists:

- the existing private plugin remains on the previously verified `0.1.0` release;
- do not upload/update the private plugin from an unverified local reconstruction;
- do not call the `0.1.1` package submission-ready.

## Next steps

1. Require the GREEN CI run to pass all seven tests plus deterministic double-build, archive inspection, and artifact upload.
2. Download and inspect the exact `0.1.1` artifact; record its hashes and inventory.
3. Update the existing private `perfecteval` plugin in place from that exact artifact; do not create a duplicate plugin.
4. Verify Plugin Creator stored the new version and inventory.
5. Keep fresh-chat behavioral smoke testing separate from package acceptance.
6. Prepare publisher URLs/policies only from confirmed publisher identity and legal/data-practice decisions.
7. Upload a public submission draft only when the verified identity/listing facts are available and the user has authorized that online action.
