---
name: perfect-eval
description: Use when a user wants to design, run, compare, diagnose, validate, benchmark, review, or maintain evaluations for an AI model, agent, prompt, workflow, application, feature, bug fix, or repository-backed system; especially for proving work is done, preventing regressions, comparing providers/models, or autonomously iterating until evidence supports completion.
---

# Perfect Eval

Run an evidence-first evaluation and review system that is provider-agnostic, model-agnostic, repository-agnostic, and usable in ordinary ChatGPT chat as well as environments with subagents, shells, browsers, local workspaces, or other advanced execution tools.

Perfect Eval must never require a particular model vendor, API, SDK, agent framework, repository layout, CI provider, programming language, or subagent feature.

## Session control

Perfect Eval has two execution modes. Read `references/session-mode.md` whenever mode is relevant.

Canonical commands:

- `/perfecteval mode human`
- `/perfecteval mode autonomous`

Rules:

1. Every new conversation defaults to `human` mode.
2. The latest explicit mode command in the current conversation wins immediately.
3. The chosen mode remains active for the rest of that conversation until the user changes it.
4. Do not claim cross-chat persistence; a new chat resets to `human` unless the host explicitly provides durable state.
5. `autonomous` mode removes routine approval pauses but never expands permissions, publication authority, spending authority, destructive-action authority, safety boundaries, repository rules, or mandatory human approvals.

## Mandatory default stage ledger

For every substantive Perfect Eval run, execute every stage below in order. A stage may return `not-applicable` with a concrete reason, but it must not silently disappear.

1. **Mode resolution** — determine current `human` or `autonomous` mode from the conversation.
2. **Target/evidence intake** — identify the subject, intended outcome, baseline/candidate if relevant, available tools, governing requirements, and execution limits.
3. **Risk classifier** — run the `risk-classifier` workflow before choosing evaluation depth.
4. **Write evals** — run the `write-evals` workflow to produce capability/regression tasks, graders, hard gates, and decision rules before judging success.
5. **Build or repair target** — only when the user's task includes implementation/repair and mutation is authorized. Otherwise mark this stage not-applicable.
6. **Verifier** — execute every applicable eval and preserve evidence. This role is part of `review-loop` and must not self-certify work it created.
7. **Independent code/review pass** — run `code-review` to search for failures the explicit evals missed.
8. **Review loop** — run `review-loop` until all hard evals pass and blocking findings are cleared, or a convergence/stop rule fires.
9. **Learned rules** — run `learned-rules` to decide whether repeated misses/noise warrant a durable rule or grader change.
10. **First-time-user test** — run `first-time-user` for user-facing experiences; otherwise mark not-applicable with reason.
11. **Fix-a-bug** — run `fix-a-bug` when any reproducible defect remains; if nothing is failing, explicitly mark `not-applicable: no defect to diagnose`.
12. **Final regression sweep** — re-run affected capability and regression checks after the last change.
13. **Evidence report** — report stage statuses, verified results, regressions, uncertainty, artifacts, and next highest-value action.

The dedicated sibling skills provide detailed procedures. If the host can invoke sibling skills directly, use them. If it cannot, execute the contracts above and the rules below in the current agent; sibling-skill invocation is an optimization, not a correctness dependency.

## No-subagent guarantee

Perfect Eval must work fully in ordinary ChatGPT chat where no subagents can be spawned.

When subagents are available, they may be used for fresh-context independence or parallel read-only analysis. When they are unavailable, the same agent executes builder, verifier, reviewer, classifier, first-time-user, and bug-diagnosis roles sequentially.

For single-agent role isolation:

1. finish and freeze the current role's evidence record;
2. switch to the next role's rubric explicitly;
3. reread the governing requirements/evidence appropriate to that role;
4. do not treat the previous role's unverified conclusion as fact;
5. actively search for disconfirming evidence;
6. record the independence limitation when it materially affects confidence.

Never skip a required stage merely because fresh context windows, parallel workers, Work mode, or Codex are unavailable.

## Evidence contract

Never claim an eval was executed, a test passed, a repository was inspected, a screenshot was checked, or a metric was measured without tool-produced or directly observable evidence.

Use these status terms precisely:

- `designed`: an evaluation specification exists but was not executed;
- `executed`: the relevant checks/trials actually ran;
- `calibrated`: an automated grader was compared with trusted human labels or another accepted reference;
- `regression-protected`: a demonstrated failure is represented by maintained regression coverage.

If execution is unavailable, produce the strongest executable design/static analysis possible and mark runtime claims unverified.

## Evaluation target

Identify:

- subject under test;
- user-visible job to be done;
- unit of evaluation: response, turn, conversation, trace, artifact, feature, repository change, final state, or other outcome;
- baseline and candidate, when comparison is requested;
- non-negotiable constraints;
- quality dimensions that may trade off;
- risk/cost/latency/reliability/safety constraints;
- available evidence and execution capabilities.

Do not ask for information already present. If something is missing but work can proceed, record the assumption/open question and continue unless human mode reaches a defined approval gate.

## Evidence sourcing

Prefer, in order when applicable:

1. explicit user requirements and acceptance criteria;
2. authoritative current documentation for time-sensitive facts;
3. repository instructions, implementation, tests, issues, pull requests, traces, logs, or product artifacts;
4. representative production/historical examples;
5. trusted human labels or known-good outcomes;
6. synthetic examples used to fill coverage gaps, never as the only evidence when real examples exist.

When repository access is available, inspect before editing. Reuse existing test/eval conventions. Do not add GitHub Actions, branches, CI systems, or unrelated automation unless the user explicitly asks for them.

## Eval design

Read `references/eval-contract.md` for durable specifications and `references/methodology.md` for source-backed rationale.

Every eval suite should define:

- objective and decision question;
- target behavior and out-of-scope behavior;
- intended task distribution;
- capability suite and regression suite;
- hard gates and soft dimensions;
- pass threshold/decision rule;
- expected nondeterminism;
- minimum evidence needed to decide;
- invalidation conditions.

Build balanced coverage from requirements, manual checks, bugs, incidents, support cases, production examples, known failures, and realistic use. When starting from zero, roughly 20-50 high-signal cases can be a useful initial target when practical, then grow from observed failures and coverage gaps.

Include relevant happy paths, edge cases, adversarial cases, ambiguous inputs, long-context/multi-turn behavior, tool failures, should-do cases, should-not-do cases, misuse/over-triggering cases, and known regressions.

Every important task must be solvable without hidden grader expectations. Create a reference outcome, executable oracle, known-good artifact, or expert-accepted example when feasible.

## Graders

Prefer the least subjective grader that correctly measures the requirement.

Use deterministic/code-based graders for objectively verifiable properties such as schema validity, executable correctness, tests, static analysis, state changes, exact factual fields, tool-call validity when the path is part of the contract, and measurable latency/token/cost thresholds.

Use model-based graders for genuinely semantic or open-ended properties. Prefer explicit assertions, anchored pointwise rubrics, reference-guided scoring, blinded pairwise comparison, and separate judges for materially distinct dimensions.

Use humans for trusted labels, judge calibration, high-stakes/expert-only judgment, ambiguous cases, and periodic spot checks.

A model judge is a measurement instrument, not unquestioned truth. Allow `unknown` or `insufficient evidence` when warranted.

## Outcome-first review

Grade the final outcome or artifact before forcing a specific internal trajectory. Only require a particular tool/path/sequence when the path itself is part of safety, authorization, compliance, or interaction correctness.

Do not penalize a valid solution merely for using an unanticipated implementation approach.

## Nondeterminism and comparisons

When behavior varies across runs and resources allow, use multiple isolated trials.

Use:

- `pass@1` for first-attempt success;
- `pass@k` when at least one success across k attempts matches the product behavior;
- `pass^k` when consistent success across all k attempts is required;
- per-task success rates/confidence intervals when sample sizes support them.

For candidate comparisons, keep task bank, decision rules, environment, and tool access equivalent unless a difference is intentionally under test. Blind candidate identity from judges when practical, randomize pairwise ordering when practical, report ties/uncertainty, and preserve per-task results behind aggregates.

## Failure analysis

Inspect failed trials, surprising passes, borderline scores, grader disagreement, human/automated disagreement, regressions, and unexpected valid solutions.

Classify important failures as:

- system/model;
- prompt/instruction;
- retrieval/context;
- tool/integration;
- harness/environment;
- task specification;
- grader;
- data/coverage;
- inconclusive.

Do not modify the target when the eval itself is the broken component.

Every understood real failure should become a candidate regression case. Promote reliably solved capability tasks into regression protection. When a suite saturates, add harder/more representative cases rather than treating a ceiling score as proof that no improvement is possible.

## Repository mode

Read `references/repository-mode.md` when source control is part of the task.

If a connected GitHub capability is available, use it only for repository operations it actually supports. Repository browsing is not test execution. Keep reads separate from mutations, honor repository rules, preserve concurrent work, and update project documentation when mutations would otherwise make it stale.

Perfect Eval does not require GitHub Actions and must not add them unless the user explicitly requests them.

## Human-in-the-loop behavior

In `human` mode, pause only at meaningful gates, normally:

- after risk classification + eval contract, before material mutation/build/fix work;
- when an unresolved product/architecture/policy/high-risk tradeoff requires judgment not supplied by authoritative requirements;
- before persisting a newly learned rule that changes future behavior;
- before an irreversible/materially destructive action not already authorized;
- before final acceptance when business/taste/expert judgment is inherently human or a mandatory human reviewer is required.

Routine read-only research, inspection, deterministic verification, and already-authorized changes do not require redundant approval.

## Autonomous behavior

In `autonomous` mode, proceed through all routine stages without approval pauses for the rest of the current conversation. Make evidence-backed, preferably reversible decisions within existing authorization. Record assumptions and material choices.

Stop only when a required permission, credential, safety/legal boundary, mandatory external human approval, or irreversible action cannot legitimately be delegated.

## Required final result

Report:

- **Mode:** human or autonomous;
- **Overall status:** designed / executed / calibrated / regression-protected;
- **Target:** what was evaluated;
- **Decision:** pass, fail, candidate preference, inconclusive, or not executable;
- **Risk tier:** low / medium / high with rationale;
- **Stage ledger:** every mandatory stage with `passed`, `failed`, or `not-applicable` and evidence/reason;
- **Hard gates:** pass/fail with evidence;
- **Key metrics:** only those that answer the decision question;
- **Regressions:** behavior that got worse;
- **Failure analysis:** system vs. eval vs. environment;
- **Uncertainty:** missing evidence, calibration gaps, or execution limits;
- **Artifacts:** tasks, rubrics, reports, code/repository files created or updated;
- **Next highest-value action:** one evidence-based follow-up.

## Invalidation conditions

Do not present a result as trustworthy when any materially decision-relevant condition holds:

- hidden or ambiguous task requirements;
- reference outcome cannot satisfy the grader;
- answer leakage/shared state invalidates trials;
- grader rewards a loophole instead of intended behavior;
- test distribution is materially unlike intended use;
- required authoritative facts are unverified;
- baseline and candidate did not receive comparable conditions;
- subjective automated judging lacks necessary calibration;
- execution evidence is missing for execution-dependent claims.

Repair the evaluation first or report the result as inconclusive.
