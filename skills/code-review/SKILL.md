---
name: code-review
description: Use when Perfect Eval must independently review a change, artifact, prompt, workflow, or repository result for real failures that the planned evals may have missed.
---

# Code Review

Perform an independent review against intent, system context, and evidence. This is the portable equivalent of the separate-review step described in the source workflow; it does not depend on a particular vendor's review command.

## Independence

Prefer a fresh-context reviewer or subagent when the host supports one. If no subagent is available, the same agent must switch roles explicitly:

1. freeze the builder/verifier findings;
2. reread the governing requirements and the changed artifact from scratch;
3. do not treat earlier conclusions as evidence;
4. search for counterexamples and breakage rather than confirming the prior work;
5. report only findings supported by concrete evidence.

## Review scope

Check, when applicable:

- whether the result actually solves the stated problem;
- regressions outside the direct feature path;
- incorrect assumptions about existing contracts;
- security, privacy, authorization, data-loss, and release risks;
- error handling and recovery;
- accessibility and responsive behavior for user-facing work;
- stale documentation or instructions caused by the change;
- root cause for bug fixes rather than symptom-only changes;
- pre-existing issues separately from newly introduced issues.

Project-specific review rules override generic preferences when they are stricter.

## Finding quality

Every finding must include:

- severity/risk;
- concrete evidence such as file/line, trace, failing check, reproducible behavior, or exact artifact location when available;
- why it violates the requirement;
- whether it is new, pre-existing, or uncertain;
- the class of defect so repeated instances can be fixed together.

Drop unsupported style-only nits unless the project explicitly requires them.

## Convergence

After the initial broad pass, re-review only changed surfaces plus directly affected contracts unless new evidence justifies reopening broader scope. Do not repeat a finding already resolved or explicitly dispositioned.

## Output

Return findings ordered by severity, a clean result when nothing actionable remains, and stage status `passed`, `failed`, or `not-applicable`.
