# Acceptance scenarios

These scenarios define observable behavior for Perfect Eval independent of model/provider implementation.

## A1 — New chat defaults to human mode

**Given** a new conversation with no prior Perfect Eval mode command  
**When** the user asks Perfect Eval to evaluate work that may require mutation  
**Then** the reported mode is `human` and the workflow reaches the pre-mutation approval gate after risk classification + eval contract unless the user already explicitly authorized that scope.

## A2 — Autonomous mode persists within the chat

**Given** the user enters:

```text
/perfecteval mode autonomous
```

**When** subsequent Perfect Eval tasks occur in the same conversation  
**Then** routine approval pauses are omitted, the mode is reported as `autonomous`, all mandatory stages still run, and the mode stays autonomous until explicitly changed.

## A3 — User can switch back immediately

**Given** autonomous mode is active  
**When** the user enters:

```text
/perfecteval mode human
```

**Then** the current and subsequent Perfect Eval work in that conversation uses human-in-the-loop gates without restarting already completed stages.

## A4 — New chat does not inherit autonomous mode

**Given** autonomous mode was active in a prior conversation  
**When** a new conversation starts without host-provided durable state  
**Then** Perfect Eval reports `human` mode by default.

## A5 — No subagent support

**Given** the host cannot spawn subagents  
**When** Perfect Eval runs  
**Then** one agent executes classifier, builder (when applicable), verifier, independent reviewer, first-time-user, and bug-diagnosis roles sequentially with role isolation, and no required stage is omitted solely because subagents are unavailable.

## A6 — Subagents available

**Given** the host can spawn fresh-context workers  
**When** independence or safe parallelism materially improves the run  
**Then** Perfect Eval may use them, but stage requirements and final result shape remain equivalent to the single-agent path.

## A7 — Specialized skill is activated directly

**Given** the host activates `write-evals`, `risk-classifier`, `code-review`, `review-loop`, `learned-rules`, `first-time-user`, or `fix-a-bug` directly  
**When** the user did not explicitly ask for only that stage  
**Then** that skill routes back into the complete Perfect Eval stage ledger or continues the full ledger itself if sibling-skill invocation is unavailable.

## A8 — Stage legitimately not applicable

**Given** a target is not user-facing  
**When** Perfect Eval reaches the first-time-user stage  
**Then** the stage is recorded as `not-applicable` with a reason rather than being silently omitted.

**And given** no reproducible defect remains  
**When** Perfect Eval reaches fix-a-bug  
**Then** it records `not-applicable: no defect to diagnose` rather than inventing a problem.

## A9 — GitHub connected, no execution environment

**Given** GitHub is connected but the host cannot run tests/builds  
**When** repository evaluation is requested  
**Then** Perfect Eval can inspect repository evidence and make authorized file changes, but it does not claim tests/builds passed and does not add GitHub Actions unless explicitly requested.

## A10 — Evidence gates completion

**Given** a required check has no execution evidence  
**When** Perfect Eval prepares the final report  
**Then** execution-dependent status is `not executable`, `unverified`, or `inconclusive` rather than `passed`.

## A11 — Review loop convergence

**Given** repeated review/repair rounds do not resolve a material failure  
**When** the same failure survives two materially distinct fix attempts, or three unsuccessful rounds show the current approach is ineffective  
**Then** Perfect Eval reconsiders the approach and stops no later than the configured hard cap (five rounds by default) unless a stricter project limit applies.

## A12 — Public listing identity is not inferred

**Given** the repository owner is visible but the verified OpenAI publisher identity has not been deliberately established for public submission  
**When** packaging Perfect Eval  
**Then** the portable source plugin remains functional without invented public-listing identity metadata, and public-directory listing completion remains a separate step.

## A13 — Maintainer package is deterministic and minimal

**Given** the same repository revision is packaged twice with `scripts/package_plugin.py`  
**When** both package builds complete successfully  
**Then** the ZIP bytes are identical, the archive entries are deterministically ordered, and the package contains only `plugin.json`, `assets/**`, and `skills/**` without `.github/**`, `docs/**`, `scripts/**`, `tests/**`, or a wrapper directory.

## A14 — Private install does not redefine portable source

**Given** the validated portable ZIP is uploaded through Plugin Creator  
**When** ChatGPT stores the private plugin release  
**Then** installation may add account-derived metadata or compatibility files, but the portable repository source remains authoritative and those host-generated fields are not treated as proof of public-directory verification, approval, or publication.

## A15 — Installation evidence is distinct from behavioral evidence

**Given** Plugin Creator accepted the ZIP and the stored release inventory can be inspected  
**When** the installed plugin has not yet been exercised in a fresh ChatGPT conversation  
**Then** the project may report `private installation verified` but must not report session-mode behavior, implicit invocation, or full stage-ledger execution as smoke-tested in the installed host.
