# Validation layers

| Layer | Required evidence |
|---|---|
| Static recipe | reviewed code, syntax, checksums and repository policy checks |
| Launcher | actual argument/path/failure behavior in isolated tests |
| Arch build | clean makepkg/container build exit status and artifact |
| Contents | actual package metadata, file ownership/modes and required notices |
| Desktop | terminal and desktop launch on named Omarchy/display stack |
| Core operation | output from representative app action, including GPU if claimed |
| Lifecycle | upgrade/relaunch/removal with original user data retained |
| Published | named version/architecture/channel in repository database |

Historical scoped commands (re-verify against current bin/repo help):
```bash
bin/build-matrix <package>
bin/repo build --local --mirror edge --arch x86_64 --package <package> --dry-run
bin/repo build --local --mirror edge --arch x86_64 --package <package>
```
Only the build command makes a package; none of these publish it. Always name the package so a local checkout does not rebuild the entire repository.

Read the current PR build workflow before downloading artifacts. In September 2026 it uploaded an unsigned package inside packages.tar, wrapped in a GitHub Actions ZIP. Verify archive member paths before extraction; use a fresh dedicated directory. gh run download expects a run ID and artifact label, then tar extracts packages.tar, then pacman -U installs the exact observed package filename. Reused download directories can make stale bytes appear current.

Do not hide skip flags, unavailable tools, unrelated failing checks or failed GUI attempts. Record hardware/runtime constraints; do not repeatedly force a display backend when the environment cannot support it.
