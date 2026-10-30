---
name: risk-classifier
description: Use when Perfect Eval must classify the consequence of failure before choosing evaluation depth, review effort, or human approval requirements.
---

# Risk Classifier

## Orchestration rule

This is a stage of Perfect Eval, not the default standalone entry point. Unless the user explicitly asks to run only risk classification, continue under the `perfect-eval` workflow and account for the complete stage ledger: mode resolution, intake, risk classification, write-evals, authorized build/repair, verification, independent review, review loop, learned rules, first-time-user, fix-a-bug, final regression sweep, and evidence report. If the host cannot invoke the sibling orchestrator, continue those stages sequentially in the current agent rather than stopping after this skill.

Classify the target change or evaluated behavior by consequence, not by author, model, provider, or implementation effort.

## Default tiers

- **Low:** failure is readily reversible and primarily cosmetic, informational, or internal; no meaningful loss, lockout, security exposure, or durable user harm is expected.
- **Medium:** failure can break ordinary product behavior or materially inconvenience users, but is normally recoverable without irreversible loss.
- **High:** failure can cause financial loss, data exposure, authorization failure, lockout, destructive data change, safety harm, legal/compliance harm, release/CI compromise, or another difficult-to-reverse outcome.

Project-specific rules may raise a tier. Never lower an explicit project or regulatory requirement.

## Procedure

1. Ask: what happens to a real user, system, or organization if this fails?
2. Identify blast radius, reversibility, data sensitivity, authorization effects, financial effects, security effects, safety effects, and release/operational effects.
3. Cite concrete evidence when repository or product evidence is available.
4. Choose the highest tier supported by any material consequence.
5. Record why lower tiers were rejected when the classification is high.
6. Translate the tier into evaluation depth rather than a vendor-specific feature:
   - low: focused deterministic checks plus targeted review;
   - medium: broader regression coverage, fresh-context review when available, and explicit failure analysis;
   - high: deepest relevant checks, independent review where possible, stronger human gate in human mode, rollback/recovery evidence, and stricter treatment of uncertainty.

## Human/autonomous control

In `human` mode, surface medium/high classifications and any ambiguous tier decision at the pre-mutation approval gate. In `autonomous` mode, choose the defensible higher tier when material uncertainty remains and proceed within authorized scope.

## Output

Return `low`, `medium`, or `high`, the consequence rationale, required evaluation depth, and stage status `passed`, `failed`, or `not-applicable`.
