# Desktop and data acceptance

Use upstream-supported flags and documented persistence. XDG environment paths must be absolute; relative XDG values are ignored according to the specification. A default user path is not permission to delete that directory on uninstall.

Test a fresh user, a saved library with spaces, an unmounted saved drive, corrupt JSON, explicit --data-dir and --data-dir= forms when supported, --home-dir, relative arguments, missing/empty argument values, and argument strings containing shell metacharacters. Verify package-owned paths are not world writable. Reject root application launches where app behavior could otherwise put user data into package directories; do not apply that rule blindly to intended administrative tools.

Launchers must choose one authoritative library selection rather than overwrite it. If upstream changes its setting keys or precedence, revisit the wrapper. A launch test using a mocked executable proves wrapper argument behavior, not GUI or application compatibility.

Document old portable installations, migration steps, backup locations, updates, removal and any upstream-generated per-user desktop file. Do not remove unrelated user's launchers automatically.

Primary sources:
- https://specifications.freedesktop.org/basedir/latest/
- https://specifications.freedesktop.org/desktop-entry-spec/latest/
- https://specifications.freedesktop.org/icon-theme-spec/latest/

For app UX, theming or native development beyond packaging, use Build Omarchy Apps. Shell plugins and theme registry submissions belong to their respective bundles.
