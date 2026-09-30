---
name: omarchy-package-submit
description: Prepare and submit an Omarchy package contribution from a tested recipe. Use for fork branches, PR descriptions, CI verification, draft readiness, tester instructions and publication handoff to omarchy-pkgs maintainers.
---

# Submit an Omarchy Package

Make the contribution reviewable and verify its external state.

1. Read current AGENTS.md, contribution guidance, templates, trusted-author/build approval rules and existing package conventions. Review the exact final diff and base freshness. Stage only the package contribution; preserve other work.
2. Read [submission.md](references/submission.md). Collect upstream provenance, redistribution evidence, packaging choices, data/update behavior, actual tests and missing desktop/lifecycle acceptance. Do not copy another PR's passing results.
3. Commit to a focused branch in the user's fork and open a PR to the observed target branch within authorization. Use a draft when material acceptance remains unresolved. Do not request secrets access or change build policy to make CI run.
4. Lead the PR with the application's resulting install behavior. Explain source/binary route, architecture support, dependency choices, licensing notices, update tracking, wrapper/migration behavior and tests. Separate validation actually run from outstanding checks.
5. Verify the PR URL, head SHA, changed files and draft status. Follow the latest head's build and test jobs; fix package-caused failures. If maintainer build approval is required, identify that precise gate rather than repeatedly rerunning.
6. Deliver copyable tester commands from the exact artifact observed in CI. Record test results in the PR when authorized. Move out of draft when required acceptance is established and the user's scope permits it.
7. Treat merge, signed publication and channel promotion as separate actions requiring their own authorization and evidence. After an authorized merge, verify the actual repository database before saying omarchy pkg add works. Do not infer stable availability from an edge build or merged PR.

Hand off maintainable upstream watch details to `omarchy-package-maintain`.

## Establish the current contract

Read the target checkout's AGENTS.md, contribution guidance, README, `docs/upstream-sources.md`, package metadata implementation and relevant CI before editing. Fetch upstream and record the base commit and date. Treat the September 2026 example as historical evidence; verify current commands and schemas against the checkout. Never execute a downloaded PKGBUILD merely to inspect it: it is shell code. Keep work scoped to the named package and preserve unrelated changes.

Use the user's existing authorization for routine implementation and PR work. Do not infer authorization to merge, publish, promote channels, or change repository policy. Track those actions separately. Distinguish recipe completion, Arch build success, live desktop acceptance, PR acceptance, and repository publication.

Read the bundled reference before implementing this stage. End with the concrete result, evidence, unresolved checks, and the next stage. When a sibling skill is unavailable, follow its described stage from current repository documentation rather than stopping merely because the bundle is partially installed.
