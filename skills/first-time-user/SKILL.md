---
name: first-time-user
description: Use when Perfect Eval must test a user-facing experience from the perspective of someone who did not see it being built and should not rely on implementation knowledge.
---

# First-Time User

Evaluate the experience without privileged implementation context.

## Purpose

Catch failures that builders and reviewers miss because they already understand the system, terminology, hidden assumptions, or intended path.

## Isolation

Prefer a fresh-context subagent when the host supports one. If no subagent exists, the same agent must simulate a fresh-user pass by:

1. freezing all implementation-specific notes;
2. using only the information a real first-time user would have;
3. avoiding source code, hidden architecture notes, internal test names, and implementation details unless the product itself exposes them;
4. documenting any unavoidable contamination of the perspective.

When the evaluated product is not user-facing, mark this stage `not-applicable` with a reason rather than omitting it.

## Procedure

1. Identify the legitimate first-use entry point and the user's intended goal.
2. Use the product, artifact, or interaction path as a new user would.
3. Check discoverability, terminology, affordances, errors, recovery, navigation, defaults, and completion feedback.
4. For visual interfaces, cover relevant responsive states, zoom/text resizing, keyboard/input modes, and error/empty/loading states when those are part of the product contract.
5. Do not repair issues during the observation pass; preserve them first.
6. Convert material friction or confusion into concrete eval/regression candidates.

## Data safety

Use test/sandbox data when available. Never modify real user data merely to perform a first-time-user test unless the user has explicitly authorized that exact action.

## Output

Report:

- attempted goal;
- observation path;
- blockers/friction ordered by impact;
- evidence;
- regression candidates;
- stage status `passed`, `failed`, or `not-applicable`.
