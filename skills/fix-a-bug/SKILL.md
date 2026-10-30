---
name: fix-a-bug
description: Use when Perfect Eval has a reproducible failure, regression, incident, or review finding and must identify root cause, prove the diagnosis, apply an authorized fix, and prevent recurrence.
---

# Fix a Bug

Fix causes, not symptoms.

## Procedure

1. Reproduce the failure using the smallest reliable steps available.
2. Capture the failing evidence before editing.
3. Form a root-cause hypothesis grounded in the implementation, configuration, prompt, data, tool contract, environment, or grader as applicable.
4. Test the hypothesis against evidence. If it fails, revise it rather than patching blindly.
5. Identify the smallest safe correction.
6. When repository history is available, inspect relevant prior versions or changes when they can help isolate the regression; do not require branching or rollback if the repository/user policy does not call for it.
7. Apply the fix only when mutation is authorized by the user and current execution mode.
8. Re-run the exact reproduction plus affected regression/capability evals.
9. Add or propose a regression case that would have caught the failure before release.
10. Feed repeated or systemic mistakes into the learned-rules stage.

## Recovery and rollback

For medium/high-risk changes, identify how to undo the change before treating the repair as complete when rollback is relevant to the system. Prefer reversible fixes. Do not perform destructive rollback merely because version control exists.

## When nothing is failing

Perfect Eval still invokes this stage by default. If all prior stages pass and no reproducible defect exists, return `not-applicable: no defect to diagnose` rather than manufacturing a bug.

## Output

Return:

- reproduction;
- root cause;
- evidence that supports the diagnosis;
- fix applied or proposed;
- verification results;
- regression coverage added/proposed;
- rollback/recovery note when relevant;
- stage status `passed`, `failed`, or `not-applicable`.
