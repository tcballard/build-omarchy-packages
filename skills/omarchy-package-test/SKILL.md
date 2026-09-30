---
name: omarchy-package-test
description: Validate Arch and Omarchy application packages with meaningful evidence. Use for clean package builds, launcher tests, CI artifacts, package contents, live desktop acceptance, upgrades, removal and rollback checks.
---

# Test an Omarchy Package

Establish which claims the evidence supports.

1. Record target commit/tree, environment, architecture, channel, available tools and application version. Read [validation.md](references/validation.md) and [Stability Matrix example](references/stabilitymatrix.md).
2. Run shell syntax, local-source checksum, desktop-entry and target repository checks after reviewing the recipe. Test custom wrappers' actual behavior with a mocked executable and isolated user paths; do not execute application downloads during wrapper unit tests.
3. Inspect the scoped build plan. Run a clean Arch/container package build for each claimed supported architecture. A dry-run, host-side package() staging, --help or mocked test does not establish a package build. If tools are absent, use PR CI within existing authorization and record the limitation.
4. Inspect the actual .pkg.tar artifact's .PKGINFO, file paths, modes, licenses, executable architecture and dependencies. Verify the preserved upstream executable bytes when required. Check no user library, unexpected download, world-writable directory or live-host file leaked into the package.
5. Match CI runs and artifacts to the exact latest head and package tree. Distinguish queued, skipped, awaiting approval, failed and successfully built. Obtain the real job result, not only an overall green status. Read logs for failures; fix the recipe and rerun affected checks.
6. On a live Omarchy test machine, install the built package, launch as an ordinary user from terminal and desktop, perform its core operation, relaunch with persisted settings, upgrade, remove and verify user-data retention. For GPU tools, generate an output using the intended backend. A GUI opening alone does not establish GPU success.
7. Give artifact-specific tester commands using observed run/artifact/file names and a fresh destination. Note artifact expiry and unsigned PR-build status. Do not change global pacman signature policy to install a test artifact. Pause dependent acceptance when user-machine access is unavailable and give a small concrete test checklist.
8. Report each layer as passed, failed, blocked or not run, with evidence. Hand off to `omarchy-package-submit`; keep missing acceptance visible.

## Establish the current contract

Read the target checkout's AGENTS.md, contribution guidance, README, `docs/upstream-sources.md`, package metadata implementation and relevant CI before editing. Fetch upstream and record the base commit and date. Treat the September 2026 example as historical evidence; verify current commands and schemas against the checkout. Never execute a downloaded PKGBUILD merely to inspect it: it is shell code. Keep work scoped to the named package and preserve unrelated changes.

Use the user's existing authorization for routine implementation and PR work. Do not infer authorization to merge, publish, promote channels, or change repository policy. Track those actions separately. Distinguish recipe completion, Arch build success, live desktop acceptance, PR acceptance, and repository publication.

Read the bundled reference before implementing this stage. End with the concrete result, evidence, unresolved checks, and the next stage. When a sibling skill is unavailable, follow its described stage from current repository documentation rather than stopping merely because the bundle is partially installed.
