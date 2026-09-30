# Recipe contract

Inspect the current checkout's metadata parser, `docs/upstream-sources.md`, nearby examples, `bin/build-matrix` and pinned-source tests. Do not assume fields from another package apply.

Historical binary-watch example, Stability Matrix 2.16.4 (2026-09-30):
```json
{"source":"local","upstream":{"github":"LykosAI/StabilityMatrix","digests":true,"assets":{"x86_64":"StabilityMatrix-linux-x64.zip"}}}
```
The recipe owns packaging; the watch updates upstream release metadata. This is not an instruction to copy version 2.16.4 or reuse its checksum for a newer release.

Use shell arrays and quote paths. Avoid `eval`, `curl | sh`, chmod 777, writing live /usr or /opt, and build-time HOME assumptions. A wrapper dependency such as jq must be a runtime dependency. A desktop validator used in check() belongs in checkdepends. Derive dependencies from code and actual linkage, then verify in a clean Arch build; the developer machine's installed packages can conceal missing dependencies.

For a vendor AppImage: verify the outer archive, extract without running its payload, locate the application executable and bundled resources, inspect their references, and install the required resources together. Removing the runtime may change APPIMAGE/AppDir-dependent behavior, update paths and desktop creation: inspect those before setting environment variables. An APPIMAGE override must never let a self-updater replace package-owned files under ordinary user permissions.

Use `makepkg --printsrcinfo` only after reviewing the recipe: sourcing PKGBUILD executes code. Generate .SRCINFO only when the target repository requires it. Packaging changes without a new upstream release normally increment pkgrel; an upstream version change resets pkgrel under repository convention. Compare versions using pacman's vercmp, not lexicographic strings.

Primary sources:
- https://man.archlinux.org/man/PKGBUILD.5.en
- https://man.archlinux.org/man/makepkg.8.en
- https://github.com/omacom/omarchy-pkgs/blob/master/docs/upstream-sources.md
