---
name: write-evals
description: Use when Perfect Eval needs to turn requirements, bugs, product behavior, or repository evidence into concrete capability and regression evals before implementation or comparison work proceeds.
---

# Write Evals

Convert the target behavior into explicit checks that can prove whether the work is done.

## Required behavior

1. Read the governing requirements and evidence before inventing cases.
2. Define the decision question and the unit under test.
3. Separate hard gates from scored quality dimensions.
4. Build both capability and regression coverage.
5. Include positive, negative, edge, adversarial, and previously observed failure cases when applicable.
6. Prefer deterministic graders when the requirement is objectively checkable; use model or human grading only where judgment is genuinely required.
7. Make every task fair: no hidden grader-only requirement.
8. Provide a reference outcome, oracle, executable check, or expert-accepted example when feasible.
9. If the target has a visual design, create or identify a concrete visual reference before implementation when the host can do so; test responsive states relevant to the product rather than one viewport only.
10. Record invalidation conditions and the evidence needed to claim a pass.

## Human/autonomous control

Read the current Perfect Eval session mode from the conversation. In `human` mode, present the eval contract for approval before material implementation or repair work unless the user already explicitly approved that scope. In `autonomous` mode, proceed after recording assumptions and decisions.

## Output

Return or persist:

- eval objective;
- risk tier input;
- task bank;
- graders;
- thresholds/decision rule;
- capability vs. regression labels;
- unresolved uncertainties;
- status: `passed`, `failed`, or `not-applicable` for the write-evals stage itself.
