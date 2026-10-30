# Repository mode

Perfect Eval is repository-agnostic. This reference defines how it should behave when source control evidence is available through GitHub or another repository connector.

## Read before mutation

Before changing a repository:

1. identify the exact repository and default branch;
2. read repository-level instructions and contributor guidance;
3. inspect relevant requirements, architecture documentation, tests, fixtures, configuration, and exports;
4. trace the behavior under evaluation from entry point to observable outcome;
5. inspect related issues, pull requests, and recent changes when they materially affect the target;
6. identify existing eval/test conventions and reuse them where appropriate.

Do not create a parallel test framework merely because Perfect Eval is installed.

## Derive evals from repository evidence

Prefer cases from:

- explicit requirements;
- existing tests and acceptance criteria;
- real bugs and regressions;
- issue reports;
- support incidents represented in the repository;
- changed contracts or interfaces;
- security or accessibility requirements;
- production traces or fixtures when available.

Generic benchmark tasks are supplemental, not substitutes for project-specific cases.

## Mutation boundary

Repository reads do not imply permission to write.

When mutation is authorized:

- follow the repository's branch policy;
- avoid unrelated refactors;
- preserve concurrent work;
- update documentation that would otherwise become stale;
- add eval artifacts in the project's existing convention when one exists;
- otherwise prefer a contained area such as `evals/perfecteval/`;
- do not add GitHub Actions, CI providers, release automation, or background jobs unless explicitly requested.

## Execution evidence

Repository browsing is not test execution.

If the current host cannot run the repository's tests or eval harness:

- inspect and reason about the executable checks;
- create or update the eval specification if authorized;
- report which checks still require execution;
- mark pass/fail results as unverified rather than simulating them.

If shell, CI, a sandbox, or another execution capability is available, run the narrowest relevant commands and preserve the resulting evidence.

## GitHub-connected workflow

When a GitHub connector is available, use it for the repository-native operations it actually exposes, such as reading files, searching source, inspecting issues or pull requests, and performing authorized file mutations.

Do not assume the connector can execute tests, build artifacts, access secrets, or perform unsupported administrative operations.

## Handoff discipline

After repository mutation, make the stopping point recoverable by another capable agent or model. Keep durable documentation current with:

- what changed;
- why it changed;
- evaluation status;
- commands or checks actually executed;
- checks still unverified;
- known limitations;
- next highest-value action.
