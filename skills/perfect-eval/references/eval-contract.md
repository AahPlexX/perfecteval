# Durable eval contract

Use this structure when Perfect Eval needs to create or maintain a reusable evaluation specification. Adapt field names to existing project conventions rather than forcing a new format.

## Identity

- evaluation name
- version or revision
- owner or responsible team when known
- created date
- last updated date
- authoritative requirement sources

## Decision question

State the exact decision the evaluation must support. Examples:

- whether a candidate can replace a baseline;
- whether a release preserves required behavior;
- whether an agent is reliable enough for a defined workflow;
- whether a prompt change improves quality without increasing unacceptable errors.

## Subject under test

Record independently:

- system or artifact under test;
- model/provider, if relevant;
- prompt/instruction revision, if relevant;
- tool set and permissions;
- environment or harness;
- baseline;
- candidate;
- judge model/provider, if a model judge is used.

Never collapse the subject and judge into one unlabeled model field.

## Population and task bank

Describe the intended use distribution and task sources.

For each task, record:

- stable task ID;
- source category: requirement, production, bug, support, synthetic, adversarial, expert-authored, or other;
- input/context;
- success criteria visible to the system under test;
- reference outcome or oracle when feasible;
- applicable graders;
- weight or priority;
- tags such as happy-path, edge, adversarial, should-do, should-not-do, regression;
- invalidation conditions.

## Graders

For every grader, record:

- grader ID;
- type: deterministic, model, human, hybrid;
- dimension measured;
- inputs available to the grader;
- rubric/assertions;
- scoring range;
- hard gate or soft score;
- pass threshold;
- expected failure modes;
- calibration evidence for subjective automated graders.

## Trials

Record:

- number of trials per task;
- isolation strategy;
- temperature/sampling settings when exposed by the system;
- seed when supported and meaningful;
- retry policy;
- timeout/resource constraints;
- invalid-trial rules.

## Metrics

Choose only metrics that answer the decision question.

Examples:

- hard-gate pass rate;
- per-task success rate;
- pass@1;
- pass@k;
- pass^k;
- pairwise win/tie/loss rate;
- groundedness or coverage score;
- tool-call correctness;
- executable test pass rate;
- latency;
- token usage;
- cost;
- human/model agreement.

Always retain per-task results behind aggregates.

## Comparison controls

For baseline-vs-candidate comparisons, record:

- task set equality;
- environment equality;
- tool equality;
- randomized/blinded response order when possible;
- any intentional differences;
- confound controls;
- tie handling.

## Failure taxonomy

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

## Decision rule

State the rule before interpreting results.

A robust rule may combine:

- all hard gates must pass;
- no critical regression is allowed;
- minimum improvement on a capability metric;
- maximum tolerated degradation on latency/cost;
- minimum human/model agreement for judge-backed scores.

## Run record

For each executed run, preserve:

- timestamp;
- exact subject revisions;
- exact eval revision;
- execution evidence;
- per-task results;
- aggregates;
- invalid trials;
- sampled traces/transcripts reviewed;
- discovered grader or harness defects;
- decision and rationale.

## Regression maintenance

Every understood real-world failure should be considered for a regression task. Record why the case was added and what behavior it protects. Retire or rewrite tasks only with an explicit reason so the suite does not silently lose coverage.
