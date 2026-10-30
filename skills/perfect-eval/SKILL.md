---
name: perfect-eval
description: Use when a user wants to design, run, compare, diagnose, validate, benchmark, or maintain evaluations for an AI model, agent, prompt, workflow, application, or repository-backed system; especially for regression prevention, model/provider comparison, quality gates, grader design, or converting failures into repeatable tests.
---

# Perfect Eval

Build trustworthy evaluations that measure the user's actual task rather than a provider, model family, benchmark fashion, or implementation detail.

## Core contract

Operate provider-agnostically and project-agnostically.

Do not require a specific model vendor, API, SDK, repository layout, CI system, programming language, benchmark framework, or agent harness. Use the capabilities available in the current host. If a connected repository source such as GitHub is available and relevant, use it to inspect evidence or make authorized repository changes. If local files, shell, Python, tracing, browser, or other tools are available, use only the capabilities needed for the task.

Never claim an eval was executed, a test passed, a repository was inspected, or a metric was measured without tool-produced evidence. Distinguish clearly between:

- designed: the evaluation specification exists but has not been executed;
- executed: trials or deterministic checks actually ran;
- calibrated: automated grading was compared with trusted human labels or another accepted reference;
- regression-protected: previously demonstrated failures are represented in a maintained regression suite.

Prefer evidence over confidence language. Mark unsupported claims as unverified.

## What counts as success

An evaluation is useful only when it answers a concrete decision question, such as:

- Did this change improve the target behavior without breaking previously working behavior?
- Which candidate performs better on the user's real task distribution?
- Is this system reliable enough for repeated use?
- Where does the system fail, and are those failures caused by the system, the grader, or the environment?
- Can a new model, provider, prompt, tool, or workflow replace the current one without unacceptable regression?

Do not optimize for a single aggregate score when the user needs a decision across multiple dimensions.

## Autonomous workflow

### 1. Establish the evaluation target

Identify, from the current conversation and available evidence:

- subject under test;
- user-visible job to be done;
- unit of evaluation: response, turn, conversation, trace, artifact, repository change, end state, or other outcome;
- baseline and candidate, when comparison is requested;
- hard constraints that must never regress;
- quality dimensions that may trade off;
- relevant cost, latency, reliability, safety, or resource constraints;
- available evidence sources and execution capabilities.

Do not ask for information already present. If some details are missing but the task can proceed, record them as explicit assumptions or open questions and continue with the strongest defensible evaluation design.

### 2. Inspect real evidence before inventing tests

Use the most direct evidence available, in this order when applicable:

1. explicit user requirements and acceptance criteria;
2. authoritative domain or technical documentation for time-sensitive facts;
3. repository rules, implementation, tests, issues, pull requests, traces, logs, or product artifacts;
4. representative production or historical examples;
5. trusted human labels, reference answers, or known-good outcomes;
6. synthetic examples added to improve coverage, never as the sole evidence when real examples are available.

When repository access is available, inspect before editing. Identify existing test conventions, evaluation assets, requirements, changed surfaces, and affected contracts. Respect repository instructions and default branch rules. Do not add GitHub Actions, branches, or unrelated automation unless the user asks for them.

### 3. Write the eval contract before scoring

Define the decision contract in plain language before generating metrics.

For each evaluation suite, capture:

- objective;
- target behavior;
- out-of-scope behavior;
- task population or intended traffic distribution;
- capability suite criteria;
- regression suite criteria;
- hard gates;
- graded dimensions;
- pass threshold or decision rule;
- expected sources of nondeterminism;
- minimum evidence needed to make a decision;
- conditions that invalidate the run.

Hard gates should represent conditions that cannot be traded away. Soft dimensions may receive partial credit or weighted scoring.

### 4. Build a balanced task bank

Source tasks from requirements, manual checks, bugs, support incidents, production examples, known failure modes, and realistic usage.

When starting from zero, a small high-signal set is better than a large low-quality synthetic set. Aim for roughly 20-50 tasks when that scale is practical, then grow from observed failures and coverage gaps.

Cover, when relevant:

- common happy paths;
- legitimate alternative formulations;
- edge cases;
- adversarial cases;
- ambiguous or underspecified inputs;
- long-context or multi-turn cases;
- tool failures and partial failures;
- should-do cases;
- should-not-do cases;
- misuse or over-triggering cases;
- previously observed regressions.

Avoid class imbalance that can reward a trivial strategy.

### 5. Prove tasks are fair

Every task must state enough information for a capable system to succeed without guessing hidden grader expectations.

For each important task, create a reference solution, reference outcome, executable oracle, or expert-accepted example when feasible. Use it to verify that the task and grader are solvable.

If a strong system repeatedly scores zero, audit the task, grader, harness, and environment before concluding the system lacks capability.

### 6. Select graders by evidence strength

Prefer the least subjective grader that correctly measures the requirement.

Use deterministic or code-based graders for objectively verifiable conditions such as:

- exact or structured output constraints;
- schema validity;
- executable correctness;
- unit, integration, or regression tests;
- static analysis;
- state changes;
- factual field checks against authoritative data;
- tool-call validity when the path itself is part of the contract;
- latency, token, cost, or count thresholds when measurement is available.

Use model-based graders when the property is genuinely semantic, open-ended, or difficult to encode deterministically. Prefer:

- pass/fail against explicit assertions;
- pointwise scoring with anchored rubric examples;
- reference-guided grading;
- blinded pairwise comparison for candidate-vs-baseline decisions;
- separate judges for materially different dimensions rather than one vague overall-quality judge.

Use human evaluation for:

- creating trusted labels;
- calibrating model judges;
- high-stakes or expert-only judgments;
- ambiguous cases;
- periodic spot checks of automated grading.

Do not use a model judge as unquestioned ground truth. Give a judge an explicit `unknown` or `insufficient evidence` outcome when appropriate.

### 7. Grade outcomes before paths

Prefer evaluating the final outcome or artifact over forcing a specific sequence of internal steps.

Only grade a tool choice, call sequence, reasoning step, or implementation path when that path is itself a requirement, such as safety, authorization, compliance, or a necessary interaction contract.

Do not penalize a valid solution merely because it differs from an anticipated approach.

### 8. Handle partial success deliberately

For multi-part tasks, separate hard gates from scored dimensions.

Use binary scoring when every condition is mandatory. Use weighted or partial-credit scoring when intermediate success is meaningful. Use a hybrid when some requirements are mandatory while others represent quality gradients.

Do not hide a hard failure inside a high average score.

### 9. Measure nondeterminism

When the evaluated system can vary across runs, run multiple independent trials when execution resources allow.

Use:

- pass@1 for first-attempt success;
- pass@k when at least one successful solution across k attempts is the relevant product behavior;
- pass^k when consistent success across all k attempts is the relevant product behavior;
- per-task success rates and confidence intervals when sample size supports them.

Keep trials isolated. Shared files, caches, history, leaked answers, resource exhaustion, or other correlated state can invalidate the result.

### 10. Compare candidates fairly

When comparing prompts, models, providers, agents, or workflows:

- use the same task bank and decision rules;
- keep environment and tool access equivalent unless the difference is intentionally under test;
- blind candidate identity from human or model judges when practical;
- randomize response order in pairwise judging when practical;
- control obvious confounds such as response length when the rubric does not reward verbosity;
- report ties and uncertainty;
- preserve per-task results instead of reporting only an aggregate winner.

A judge may be from the same or a different provider as the subject under test. Record that fact. Do not claim evaluator independence when it does not exist.

### 11. Read traces and transcripts

Aggregate scores are not sufficient evidence.

Inspect a meaningful sample of:

- failed trials;
- surprising passes;
- borderline scores;
- disagreements between graders;
- disagreements between automated and human grading;
- regressions introduced by a candidate;
- cases where the agent found an unanticipated valid solution.

Classify each important failure as one of:

- system/model failure;
- prompt/instruction failure;
- retrieval/context failure;
- tool or integration failure;
- harness/environment failure;
- task-specification failure;
- grader failure;
- data-distribution or coverage gap;
- inconclusive.

Do not fix the system when the eval is the broken component.

### 12. Turn failures into durable regressions

When a real failure is understood, add or propose a minimal regression case that captures the behavior without overfitting to irrelevant details.

Run both:

- capability evals that expose room for improvement; and
- regression evals that protect behaviors already expected to work.

As capability tasks become reliably solved, promote them into the regression suite. When an eval saturates, add harder or more representative tasks instead of treating a ceiling score as proof that the system cannot improve.

### 13. Iterate one causal change at a time when possible

Use eval results to change the smallest relevant component: prompt, context, retrieval, tool contract, implementation, model, routing, or grader.

Re-run the affected capability suite and the regression suite after each meaningful change. Avoid making many unrelated changes before measurement unless the user explicitly wants a broad redesign.

### 14. Keep the eval suite alive

Treat evaluation assets as maintained product artifacts.

Continuously add cases from:

- production failures;
- user feedback;
- bug reports;
- new requirements;
- model/provider migrations;
- tool changes;
- newly discovered adversarial strategies;
- grader disagreements.

When repository mutation is authorized and no project convention already exists, prefer a small, readable evaluation area such as `evals/perfecteval/` rather than scattering files throughout the repository. Adapt to existing project conventions when they exist.

## Repository mode

When a repository is part of the task and a connected GitHub capability is available:

1. identify the exact repository and default branch;
2. read repository instructions and relevant documentation first;
3. inspect the implementation, existing tests, changed files, issues, and pull requests needed to understand the target behavior;
4. derive eval tasks from repository evidence rather than generic coding benchmarks;
5. keep repository reads separate from mutations;
6. make changes only when the user has authorized repository mutation;
7. never create workflow automation solely because an eval exists;
8. after mutation, update project documentation that must remain accurate for future handoff;
9. report exact files changed and evidence obtained.

If execution of repository tests is unavailable, do not convert inspection into a false pass/fail claim. Produce the executable evaluation plan, static evidence, and any repository artifacts that can be created honestly, and mark runtime results unverified.

## Research mode

When evaluation criteria depend on current specifications, APIs, standards, laws, pricing, model behavior, or other time-sensitive facts, verify them against current authoritative sources before encoding them into an eval.

Prefer first-party documentation, standards bodies, primary research, or official repositories. Record retrieval date and source URLs in durable eval documentation when repository artifacts are being created.

Do not turn a third-party summary into a grader requirement without primary-source corroboration.

## Required result shape

Return a concise result that still preserves decision-critical evidence:

- **Status:** designed / executed / calibrated / regression-protected;
- **Target:** what was evaluated;
- **Decision:** pass, fail, candidate preference, inconclusive, or not yet executable;
- **Hard gates:** pass/fail with evidence;
- **Key metrics:** per-dimension and aggregate only when meaningful;
- **Regressions:** any behavior that got worse;
- **Failure analysis:** system vs. eval vs. environment;
- **Uncertainty:** missing evidence, judge calibration gaps, or execution limits;
- **Artifacts:** tasks, rubrics, reports, or repository files created/updated;
- **Next highest-value action:** the single most useful follow-up based on the evidence.

For comparisons, include per-task or per-category differences sufficient to explain the decision.

## Stop and invalidate conditions

Do not present a result as trustworthy when any of these materially affect the decision:

- the task is ambiguous or hides grader-only requirements;
- the reference solution cannot satisfy the grader;
- the harness leaks answers or shared state across trials;
- the grader rewards a loophole instead of the intended behavior;
- the test distribution is materially unlike the intended use;
- required authoritative facts are unverified;
- the candidate and baseline did not receive comparable conditions;
- the automated judge has not been calibrated where human judgment is the true target;
- execution evidence is missing for claims that require execution.

In these cases, repair the evaluation first or report the result as inconclusive.

## Reference material

Read `references/methodology.md` for the evidence-backed methodology and source rationale. Read `references/eval-contract.md` when creating a durable evaluation specification. Read `references/repository-mode.md` when the task uses a source repository.
