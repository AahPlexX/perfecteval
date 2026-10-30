# Perfect Eval methodology

Research snapshot: 2026-10-30T13:08:00-05:00.

This reference captures the primary-source reasoning behind the Perfect Eval workflow. It intentionally describes provider-neutral evaluation concepts rather than vendor-specific APIs.

## Source handling

The user-provided video was verified as the YouTube video **“Anthropic Just Released A New System For Using Claude Code”** at:

- https://youtu.be/S49gppZl8H0

The available retrieval surface exposed the video identity but not a machine-readable transcript. Perfect Eval therefore does not invent or attribute unseen statements to the video. Its operational rules are corroborated against Anthropic's first-party evaluation guidance and independent first-party guidance from OpenAI and Google Cloud.

## Primary sources

### Anthropic — Demystifying evals for AI agents

https://www.anthropic.com/research/demystifying-evals-for-ai-agents

Key points used by Perfect Eval:

- A task is one test with inputs and success criteria; a trial is one attempt; a grader scores an aspect of performance; a trace/transcript records the run.
- Agent evals commonly combine deterministic/code-based, model-based, and human graders.
- Capability/quality evals should expose room for improvement; regression evals protect behavior that should already work reliably.
- Agent behavior is nondeterministic, so repeated trials matter.
- `pass@k` measures the chance of at least one success across k attempts; `pass^k` measures consistent success across all k attempts.
- Start early; 20-50 high-signal tasks can be a useful initial suite.
- Start from manual checks, product requirements, bugs, support cases, and real failures.
- Tasks must be unambiguous and should have a reference solution or known-good outcome where feasible.
- Balanced suites should test both when a behavior should happen and when it should not.
- Trials should start from isolated, stable environments.
- Prefer deterministic graders where possible and model graders where necessary.
- Outcome grading is usually more robust than forcing one exact internal trajectory.
- Model judges should be calibrated against human experts.
- Read traces/transcripts to distinguish true model failures from bad graders, ambiguous tasks, or harness problems.
- Promote reliably solved capability cases into the regression suite and keep adding harder cases as suites saturate.

### OpenAI — Evaluation best practices

https://developers.openai.com/api/docs/guides/evaluation-best-practices

Key points used by Perfect Eval:

- Adopt eval-driven development: evaluate early and often with scoped tests.
- Make evals task-specific and representative of real distributions.
- Log behavior so real failures can become future eval cases.
- Automate scoring when practical, while maintaining human agreement.
- Avoid vibe-based evaluation and overly generic metrics.
- A complete workflow defines the objective, collects the dataset, defines metrics, runs comparisons, and continuously evaluates.
- Include typical, edge, and adversarial cases.
- Pairwise comparison, classification, and scoring against explicit criteria are often more reliable for model judges than unconstrained open-ended judging.
- Human evaluation remains the highest-quality reference for subjective judgment, though it is slower and more expensive.
- Model judges should use explicit rubrics, account for known biases such as response-order and verbosity bias, and be validated against human labels before scaling.

### Google Cloud — Gen AI evaluation service overview

https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/evaluation-overview

Key points used by Perfect Eval:

- Evaluate on the user's specific tasks and criteria rather than relying only on public leaderboards.
- The same evaluation workflow can compare model versions, first-party models, and third-party models.
- A standard workflow is: assemble an evaluation dataset, define metrics, generate responses, run evaluation, and interpret aggregate plus individual results.
- Rubric-based metrics complement deterministic/computation-based metrics.
- Pointwise and pairwise evaluation are distinct tools; pairwise evaluation is useful when direct preference is easier to define than an absolute score.
- Production logs, uploaded datasets, and synthetic generation can all contribute evaluation data.

### Microsoft Foundry — Generative AI evaluation

https://learn.microsoft.com/en-us/azure/foundry/how-to/evaluate-generative-ai-app

Key points used as corroboration:

- Evaluation can target full agent conversations, individual turns, models, datasets, and traces.
- Evaluation data may be simulated, historical, or directly supplied.
- Agent evaluation can assess task completion, instruction adherence, tool behavior, groundedness, completeness, and other quality dimensions.
- Multiple simulated conversations per scenario help expose variance.

## Derived provider-neutral rules

The following rules are synthesis, not vendor quotations:

1. **Separate the subject from the judge.** A model under test, the model used as judge, and any human reference labels are distinct roles. Record them separately.
2. **Do not make a vendor API the eval contract.** Store task definitions, criteria, expected outcomes, and results in forms that can be mapped onto different providers.
3. **Prefer observable outcomes.** Internal tool sequences matter only when they are part of the requirement, safety boundary, authorization boundary, or protocol contract.
4. **Treat judges as fallible instruments.** A high judge score is not ground truth until it agrees sufficiently with the target human or deterministic standard.
5. **Preserve uncertainty.** Ties, unknowns, invalid trials, grader disagreement, and missing execution evidence must remain visible.
6. **Turn real failures into regression assets.** The evaluation suite is a living product artifact, not a one-time benchmark.
7. **Compare under equivalent conditions.** Candidate and baseline should receive the same tasks, tools, environment, and decision rules unless the difference is intentionally part of the experiment.
8. **Use multiple layers.** Deterministic checks, model rubrics, human review, production evidence, and trace inspection catch different failure classes.

## What Perfect Eval deliberately does not require

- Claude, GPT, Gemini, or any other named model;
- Anthropic, OpenAI, Google, Microsoft, or any other provider API;
- a particular eval framework;
- GitHub Actions or any CI provider;
- one repository layout;
- one programming language;
- a separate MCP server;
- a permanent external credential.

When a host exposes useful tools, Perfect Eval uses them. When it does not, Perfect Eval must degrade honestly to design, static analysis, or report generation rather than pretending execution occurred.
