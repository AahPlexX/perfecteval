---
name: learned-rules
description: Use when Perfect Eval identifies repeated false negatives, false positives, review misses, or recurring defect classes and should convert them into concise durable review guidance without overfitting.
---

# Learned Rules

Turn repeated review failures into small, evidence-backed improvements to future evaluation and review behavior.

## Trigger

Run this stage on every Perfect Eval cycle. It may conclude `not-applicable` when there is not enough repeated evidence to justify a new durable rule.

## Eligible signals

A learned rule may be proposed when:

- the same defect class appears repeatedly across rounds or tasks;
- a real incident escaped the current eval/review process;
- the reviewer repeatedly flags something that is confirmed to be intentional or harmless;
- a project instruction is repeatedly violated because the governing guidance is ambiguous or missing;
- a grader repeatedly rewards or rejects the wrong behavior.

One isolated event is usually evidence for a regression test, not automatically a global rule.

## Rule quality

A durable rule should be:

- short;
- specific enough to change behavior;
- general enough to cover the defect class rather than one line or one example;
- tied to evidence;
- compatible with higher-priority project requirements;
- removable if later evidence disproves it.

Prefer updating an existing project review/instruction file over creating a new competing rulebook. Do not require names such as `REVIEW.md` or `CLAUDE.md`; use the repository's established conventions.

## Human/autonomous control

In `human` mode, propose the learned rule and obtain approval before persisting it unless the user already explicitly authorized autonomous rule maintenance.

In `autonomous` mode, persist a rule when evidence is strong, the mutation is within scope, and the target instruction location is clear. Record what evidence caused the rule to be added.

## Output

Return:

- evidence pattern;
- proposed or persisted rule;
- target instruction/eval location;
- reason it is not overfit;
- stage status `passed`, `failed`, or `not-applicable`.
