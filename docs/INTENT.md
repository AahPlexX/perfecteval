# Product intent

Perfect Eval makes AI-assisted work demonstrate completion with evidence rather than relying on a completion claim.

## Core requirements

- Provider and model agnostic.
- Repository and project agnostic.
- Works in standard ChatGPT conversations without subagents.
- Subagents are optional and may improve independence or parallelism, but must not change required coverage.
- Supports human-in-the-loop and autonomous session modes.
- Every new chat begins in human-in-the-loop mode.
- The user can change modes at any time; the latest explicit mode applies until changed or the chat ends.
- Every evaluation and review stage derived from the source workflow is accounted for on every substantive run, either by execution or an explicit not-applicable result.
- GitHub can provide repository evidence and authorized file changes, but GitHub Actions are not required.
- Claims that require execution need execution evidence.
- Confirmed failures become regression candidates.
- Repeated review misses or false positives can become concise learned rules.
- Evaluation depth increases with risk.
- Review loops have convergence limits and explicit stop conditions.

## Default exclusions

- No required dependency on any named model provider.
- No required dependency on Claude Code, Codex, Work mode, multi-agent support, CI/CD, or a local shell.
- No bundled MCP server or external API credential is required for core operation.
- No automatic creation of GitHub Actions.
- No repository mutation outside the user's authorized scope.
- No assumption that a model judge is ground truth when human judgment is the intended reference.

## Success definition

A run succeeds when it gives the user a defensible decision backed by explicit tasks, graders, available execution evidence, independent review, failure classification, and regression protection where appropriate.
