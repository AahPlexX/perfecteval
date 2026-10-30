# ADR-0001: Portable skills-only architecture

- Status: Accepted
- Date: 2026-10-30

## Context

Perfect Eval must work across model providers and project types, in ordinary ChatGPT chat as well as environments that expose subagents, local workspaces, browsers, shells, or other advanced tools. The user also expects the connected GitHub plugin to be usable when repository evidence is relevant, without requiring GitHub Actions.

Current OpenAI plugin documentation recommends the portable Agent Plugins root `plugin.json` format and allows skills to work without an MCP server. Agent Plugins v1 discovers skills from immediate child directories under `skills/`.

OpenAI public-directory listing metadata requires a developer name associated with the verified publishing identity. That identity must not be inferred from a repository owner name.

## Decision

Perfect Eval will be a skills-only portable Agent Plugin.

- Root manifest: `plugin.json` using Agent Plugins v1.
- The root portable manifest remains publisher-neutral until verified listing identity is supplied.
- ChatGPT-specific presentation for the orchestrator uses `skills/perfect-eval/agents/openai.yaml`.
- Brand assets are prepared under `assets/` for a future directory listing but are not currently declared as public listing metadata.
- No bundled MCP server for the core workflow.
- No provider API dependency.
- No GitHub Actions dependency.
- Connected GitHub or other host tools are optional capabilities used when available.
- `perfect-eval` is the orchestrator and contains a complete single-agent fallback contract.
- Specialized sibling skills implement the video-derived stages.
- Human/autonomous mode is session-scoped conversation state established by explicit user input, not hidden persistent storage.

## Consequences

### Positive

- Works in ChatGPT chat without subagents.
- Portable workflow logic is not tied to a vendor API.
- Advanced hosts can still use fresh-context workers or execution tools.
- Repository connectivity can be added by the host without changing the plugin architecture.
- The core plugin has no external credential or service dependency.
- No unverified publisher identity is embedded in the package.

### Tradeoffs

- In a single-agent chat, reviewer independence is weaker than a true fresh-context reviewer, so Perfect Eval must disclose that limitation when material.
- Session mode cannot truthfully persist across new chats without host-provided durable state; new conversations therefore reset to human-in-the-loop.
- Runtime verification depends on tools exposed by the current host. When execution is unavailable, Perfect Eval must report runtime results as unverified.
- Public-directory listing metadata must be completed later using the actual verified publisher identity.

## Rejected alternatives

- Anthropic/Claude-specific skill or hook implementation: rejected because it violates provider neutrality.
- Mandatory MCP service: rejected because the core workflow needs procedures, not a dedicated external data/action service.
- Mandatory subagents: rejected because ordinary ChatGPT chat must remain fully functional.
- Mandatory GitHub Actions/CI: rejected because repository automation is not required to perform or specify the evaluation workflow.
- Guessing `developerName` from the GitHub owner: rejected because repository ownership does not prove the verified OpenAI publisher identity.
