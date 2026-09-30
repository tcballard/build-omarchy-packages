---
name: omarchy-package-inspect
description: Inspect an upstream application for Arch and Omarchy packaging. Use for adding an existing app, reviewing an AUR recipe, choosing source versus binary packaging, or auditing licensing and architecture support before writing a PKGBUILD.
---

# Inspect an Omarchy Package

Produce a packaging decision that another agent can implement.

1. Resolve the canonical upstream, release/tag/commit, asset names, supported CPU architectures, existing official Arch/AUR/Omarchy packages, and current package version. Record primary-source URLs and immutable revisions. Inspect rather than assume that an AUR package is suitable.
2. Compare source build, upstream binary archive, and AppImage extraction. Prefer the route consistent with upstream distribution, maintainability, licensing and repository policy. Describe why; do not silently switch upstream artifacts.
3. Verify source license and binary redistribution terms separately. Retain required notices and attribution. If redistribution rights are unresolved, report the exact unresolved term and continue unaffected preparation; do not present permission as established.
4. Inspect runtime/build/check dependencies, embedded runtimes, ABI needs, X11/XWayland/Wayland support, GPU backends, services, desktop protocols, auto-updates and first-run downloads. Separate app dependencies from optional models, tools and GPU drivers.
5. Identify existing user data and migration risk. Locate real upstream path selection code when documentation is insufficient. Record writable directories and ownership boundaries.
6. Hand off to `omarchy-package-build` with package name, route, version, architectures, pinned sources/checksums, dependencies, update watch and acceptance criteria.

Read [inspection.md](references/inspection.md) for the decision record and primary sources.

## Establish the current contract

Read the target checkout's AGENTS.md, contribution guidance, README, `docs/upstream-sources.md`, package metadata implementation and relevant CI before editing. Fetch upstream and record the base commit and date. Treat the September 2026 example as historical evidence; verify current commands and schemas against the checkout. Never execute a downloaded PKGBUILD merely to inspect it: it is shell code. Keep work scoped to the named package and preserve unrelated changes.

Use the user's existing authorization for routine implementation and PR work. Do not infer authorization to merge, publish, promote channels, or change repository policy. Track those actions separately. Distinguish recipe completion, Arch build success, live desktop acceptance, PR acceptance, and repository publication.

Read the bundled reference before implementing this stage. End with the concrete result, evidence, unresolved checks, and the next stage. When a sibling skill is unavailable, follow its described stage from current repository documentation rather than stopping merely because the bundle is partially installed.
