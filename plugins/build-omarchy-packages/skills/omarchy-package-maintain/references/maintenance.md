# Maintenance checks

Review: asset renames; archive layout; ELF architecture; embedded runtime changes; dynamic dependency changes; upstream data/settings schema; desktop identity; self-updater targets; binary redistribution terms; checksum/signature trust; rebuilt dependent packages.

Historical scoped sync command: `bin/sync-upstream <package>`. It needs tools such as pacman's vercmp; missing tools mean a blocked sync, not a passed update check. Read current --help and implementation before running; watch schemas and provider names may change.

The normal Omarchy pipeline was edge → rc → stable at this bundle's creation. Fast-ring packages had distinct per-channel native builds. Preserve current repository policy; do not automatically fast-track third-party applications or enable unattended merge.

Keep release age, prerelease policy, asset digest lookup and git-commit pins aligned with repository conventions. If upstream replaces release bytes under the same name/tag, investigate the provenance and reason before accepting a new checksum.

Use the package cache or saved prior artifact for rollback, after backing up data. Do not delete models/settings to make old binaries launch. Report data-format incompatibility as an unresolved rollback constraint.
