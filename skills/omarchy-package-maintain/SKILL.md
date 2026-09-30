---
name: omarchy-package-maintain
description: Maintain existing Omarchy package recipes as upstream changes. Use for release/version/checksum updates, upstream watch repair, dependency rebuilds, architecture changes, update failures and packaging regressions.
---

# Maintain an Omarchy Package

Update the maintained recipe while preserving user data and release policy.

1. Read current upstream release notes, immutable sources/digests and the target repository's upstream-watch and rebuild implementations. Compare published versions per architecture/channel using pacman's version ordering.
2. Inspect the new artifact's architecture, layout, runtime requirements, license/notice changes, updater behavior and setting/library schema. Revalidate wrappers when upstream changes these interfaces; a changed checksum alone is insufficient.
3. Run only the named package's upstream sync using the documented command after inspecting its mutation behavior. Review the resulting diff; preserve custom integration and supported architectures. Do not import an AUR recipe wholesale over the locally maintained one.
4. Distinguish upstream pkgver changes from packaging/ABI pkgrel changes and epoch changes. Use epochs only to repair version ordering with evidence. Keep default channels and reviewed update policy unless the user authorized a deliberate change.
5. Rebuild affected architectures and check runtime compatibility against the intended channel mirror. Do not copy edge-linked artifacts into stable merely because their filenames match.
6. Run `omarchy-package-test` and submit a focused PR with `omarchy-package-submit`. For regressions, identify the last good artifact and test rollback; preserve user-library backups and explain that binary rollback does not reverse data migrations.
7. Verify signed publication and actual package database availability only after authorized publication. Report version, architecture, channel and evidence separately.

Read [maintenance.md](references/maintenance.md).

## Establish the current contract

Read the target checkout's AGENTS.md, contribution guidance, README, `docs/upstream-sources.md`, package metadata implementation and relevant CI before editing. Fetch upstream and record the base commit and date. Treat the September 2026 example as historical evidence; verify current commands and schemas against the checkout. Never execute a downloaded PKGBUILD merely to inspect it: it is shell code. Keep work scoped to the named package and preserve unrelated changes.

Use the user's existing authorization for routine implementation and PR work. Do not infer authorization to merge, publish, promote channels, or change repository policy. Track those actions separately. Distinguish recipe completion, Arch build success, live desktop acceptance, PR acceptance, and repository publication.

Read the bundled reference before implementing this stage. End with the concrete result, evidence, unresolved checks, and the next stage. When a sibling skill is unavailable, follow its described stage from current repository documentation rather than stopping merely because the bundle is partially installed.
