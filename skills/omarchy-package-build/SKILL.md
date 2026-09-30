---
name: omarchy-package-build
description: Create or repair an Arch PKGBUILD and Omarchy package metadata for an existing application. Use for source builds, pinned binary archives, AppImage extraction, upstream release tracking and dependency or architecture fixes.
---

# Build an Omarchy Package Recipe

Turn the inspection record into a reproducible package contribution.

1. Read `omarchy-package-inspect`'s decision record or establish the same evidence. Create `pkgbuilds/<name>/PKGBUILD` and `.omarchy/package.json` under the target repository's current contract.
2. Pin every source to immutable release bytes or an exact commit; verify complete downloads against trusted upstream digests where available. Use version-qualified cached filenames for reused upstream asset names. Do not replace failures with SKIP or unpinned branch sources.
3. Set accurate architecture lists. Package architecture-specific ELF binaries as that architecture; do not use `any` or invent ARM support. Separate depends, makedepends, checkdepends and optdepends based on actual build/runtime behavior.
4. Use prepare/build/check/package phases appropriately. Install only to pkgdir during package(). Preserve binary bytes when upstream terms require unchanged redistribution; disable stripping/debug transformations when required and record the reason. Avoid downloading user models or starting services during install.
5. Use local recipe ownership and upstream watches supported by the current schema. Default to normal edge → rc → stable policy. Explicitly justify any channels, fast-ring, auto-merge or branch-watch exception; never add one solely to speed this contribution.
6. Add desktop/data integration through `omarchy-package-integrate`. Add package-specific checks for fragile behavior through `omarchy-package-test`.
7. Review the final diff and refresh local-source checksums after every edit. Record input revision and produced package identity; hand off to testing.

Read [recipe.md](references/recipe.md) before writing sources or metadata.

## Establish the current contract

Read the target checkout's AGENTS.md, contribution guidance, README, `docs/upstream-sources.md`, package metadata implementation and relevant CI before editing. Fetch upstream and record the base commit and date. Treat the September 2026 example as historical evidence; verify current commands and schemas against the checkout. Never execute a downloaded PKGBUILD merely to inspect it: it is shell code. Keep work scoped to the named package and preserve unrelated changes.

Use the user's existing authorization for routine implementation and PR work. Do not infer authorization to merge, publish, promote channels, or change repository policy. Track those actions separately. Distinguish recipe completion, Arch build success, live desktop acceptance, PR acceptance, and repository publication.

Read the bundled reference before implementing this stage. End with the concrete result, evidence, unresolved checks, and the next stage. When a sibling skill is unavailable, follow its described stage from current repository documentation rather than stopping merely because the bundle is partially installed.
