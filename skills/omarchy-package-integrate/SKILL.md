---
name: omarchy-package-integrate
description: Implement desktop and user-data integration for an Arch or Omarchy package. Use for launch wrappers, desktop entries, protocol handlers, XDG directories, portable-mode migration, permissions and application self-update behavior.
---

# Integrate an Omarchy Package

Make an installed upstream application behave correctly as an ordinary desktop user.

1. Inspect upstream entry-point, data selection, portable mode, home overrides, self-updater and desktop creation code. Record the actual precedence before designing a wrapper.
2. Install application files as package-owned read-only content. Store mutable models, settings, databases and environments in user-owned locations. Honour supported explicit directory arguments and saved selections; use XDG locations only where compatible with upstream. Do not force a new library on every launch.
3. Resolve relative explicit paths before changing directory. Forward arguments using arrays and "$@". Reject malformed/missing arguments rather than treating another option as a directory. Handle spaces and literal shell-looking arguments without evaluation.
4. Fail clearly for a missing saved drive or invalid saved configuration; never silently create a replacement library. Do not adopt /opt portable data or change ownership recursively without a reviewed migration plan. Preserve originals and backups.
5. Provide a validated desktop file, icon, correct Exec/TryExec and supported protocol handlers. Inspect duplicate per-user entries. Set StartupWMClass only from observed application identity. Document whether the app uses XWayland.
6. Disable application self-updates through supported controls when available. Otherwise preserve package ownership, document prompts and verify that ordinary-user updates cannot overwrite packaged application files. Keep separately managed tools' updates working. Never recommend launching the app with sudo to bypass permissions.
7. For services, use the target repository's established system/user unit and lifecycle conventions. Start/enable only within the requested scope; preserve uninstall semantics and user data.
8. Test path precedence, fresh installs, saved libraries, missing mounts, explicit overrides and arguments. Hand off to `omarchy-package-test` with the ownership map and migration/removal behavior.

Read [desktop-and-data.md](references/desktop-and-data.md).

## Establish the current contract

Read the target checkout's AGENTS.md, contribution guidance, README, `docs/upstream-sources.md`, package metadata implementation and relevant CI before editing. Fetch upstream and record the base commit and date. Treat the September 2026 example as historical evidence; verify current commands and schemas against the checkout. Never execute a downloaded PKGBUILD merely to inspect it: it is shell code. Keep work scoped to the named package and preserve unrelated changes.

Use the user's existing authorization for routine implementation and PR work. Do not infer authorization to merge, publish, promote channels, or change repository policy. Track those actions separately. Distinguish recipe completion, Arch build success, live desktop acceptance, PR acceptance, and repository publication.

Read the bundled reference before implementing this stage. End with the concrete result, evidence, unresolved checks, and the next stage. When a sibling skill is unavailable, follow its described stage from current repository documentation rather than stopping merely because the bundle is partially installed.
