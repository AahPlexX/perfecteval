---
name: review-loop
description: Use when Perfect Eval must iteratively build or repair a target, verify every eval, independently review for missed failures, and converge without infinite agent-review loops.
---

# Review Loop

Run the builder -> verifier -> reviewer cycle until the target is acceptable, a stopping rule fires, or evidence shows the approach must be reconsidered.

## Roles

### Builder

Implement or repair the smallest change that satisfies the approved eval contract and current findings. Do not self-certify completion.

### Verifier

Evaluate the result against every applicable eval. Mark each case passed, failed, invalid, or not executable, and preserve execution evidence. The verifier does not invent a pass when the host cannot execute the required check.

### Reviewer

Run the independent `code-review` behavior after verification to find failures outside the explicit eval set.

### Orchestrator

Maintain round state, deduplicate findings, decide which role runs next, enforce mode/approval gates, and stop the loop correctly.

## Subagents are optional

When the host supports subagents, prefer fresh contexts for verifier and reviewer independence, and use parallelism only when it does not create conflicting mutations.

When subagents are unavailable, one agent MUST execute all roles sequentially. Preserve role isolation by freezing each role's evidence before switching roles and by re-reading the next role's rubric rather than carrying forward unverified conclusions.

The single-agent path is first-class and must produce the same stage ledger and stopping decisions.

## Loop state

Maintain, in conversation or durable project state when appropriate:

- current round;
- unresolved eval failures;
- unresolved review findings;
- defect classes already seen;
- fixes attempted;
- repeated failures;
- decisions/assumptions;
- current execution mode;
- evidence still unavailable.

Do not require a particular filename such as `state.md`; use existing project conventions when repository persistence is appropriate.

## Convergence rules

1. Round 1 performs full verification and full independent review.
2. Later rounds focus on the new diff and directly affected contracts; never drip-feed already-known findings.
3. Findings must identify their defect class so the builder can fix all equivalent instances.
4. After 3 unsuccessful rounds, explicitly reconsider the approach rather than applying more of the same fix pattern.
5. Hard stop after 5 rounds by default unless the user/project has supplied a stricter bound.
6. Stop earlier when the same material failure persists after 2 materially distinct fix attempts, because another identical round is not evidence-producing progress.
7. A round does not count as successful merely because a reviewer found fewer issues; all hard eval gates must pass and no blocking review finding may remain.
8. If the eval, grader, harness, or environment is proven defective, repair that component before continuing to modify the target.

## Human/autonomous control

In `human` mode, honor the Perfect Eval approval gates and surface unresolved product/architecture/high-risk decisions to the user. In `autonomous` mode, continue through routine rounds without approval pauses while staying within authorized scope.

## Completion

The loop passes only when:

- all applicable hard evals pass;
- soft-score decision rules are satisfied;
- independent review has no unresolved blocking finding;
- required recovery/rollback evidence exists for the risk tier when applicable;
- no invalidation condition makes the result untrustworthy.

Otherwise return `failed` or `inconclusive` with the exact blocker and next highest-value action.
