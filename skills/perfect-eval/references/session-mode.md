# Session execution mode

Perfect Eval has exactly two user-selectable execution modes.

## Commands

- `/perfecteval mode human`
- `/perfecteval mode autonomous`

Equivalent explicit natural-language requests such as “switch Perfect Eval to full autonomy” or “switch back to human in the loop” are valid, but the slash commands are the canonical unambiguous form.

## State semantics

- A new conversation starts in `human` mode.
- The most recent explicit mode command in the current conversation is authoritative.
- The selected mode remains active for the rest of the current conversation until the user changes it.
- A mode change takes effect immediately and does not restart already completed stages.
- Do not claim cross-chat persistence. A new chat resets to `human` unless the host explicitly supplies a durable mode state.
- If the current conversation contains conflicting mode statements, the latest explicit user instruction wins.

## Human-in-the-loop mode

This is the default.

Pause for the user's decision at the smallest meaningful approval gates, normally:

1. after the risk classification and eval contract are drafted, before material mutation/build/fix work begins;
2. when an ambiguous product, architectural, policy, or high-risk tradeoff cannot be resolved from authoritative requirements;
3. before persisting a newly learned review rule that changes future behavior;
4. before irreversible or materially destructive actions when a human approval is not already clearly provided;
5. before final acceptance when the decision inherently depends on human taste, business judgment, or a mandatory human reviewer.

Do not ask for approval for routine read-only inspection, deterministic verification, or changes the user has already explicitly authorized.

## Autonomous mode

Proceed without routine approval pauses for the rest of the conversation.

The agent may make reversible, evidence-backed decisions within the user's already-authorized scope. It must:

- record material assumptions and decisions;
- prefer reversible changes when alternatives are otherwise equivalent;
- keep the stage ledger current;
- preserve repository and project rules;
- perform the same eval, verification, review, first-time-user, and bug-diagnosis stages used in human mode;
- stop only when a required permission, credential, safety boundary, legal requirement, mandatory external human approval, or irreversible action cannot legitimately be delegated.

Autonomous mode is not permission escalation. It never expands repository access, tool permissions, spending authority, publication authority, or destructive-action authority beyond what the user and host already granted.

## Subagent independence

Execution mode and subagent availability are separate concerns.

When subagents are available, Perfect Eval may use fresh-context workers for independence and parallelism. When they are unavailable, the same primary agent must execute each role sequentially using role isolation:

1. finish one role's evidence record;
2. clear role-specific assumptions from the active checklist;
3. reread only the evidence that the next role is permitted to see;
4. execute the next role against its own rubric;
5. do not reuse an earlier role's unverified conclusions as facts.

The absence of subagents may reduce independence and parallelism, but it must never cause a required stage to be omitted.
