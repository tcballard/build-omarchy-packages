# Stability Matrix: historical worked example

Date: 2026-09-30. Contribution: https://github.com/omacom/omarchy-pkgs/pull/736
Upstream: https://github.com/LykosAI/StabilityMatrix, release v2.16.4.
Recipe commit: 83799c612640186af4cbed502b3353a5aa918091.
Package: stabilitymatrix 2.16.4-1, x86_64 only.

Choice: extract the official Linux archive's AppImage using 7zip without executing it. Install the unchanged executable, upstream icon, bundled AGPL text and separate binary EULA. The release archive SHA-256 was 379381025ded32a9875b6195130b4442cd85f19dbb7bdbca6120043362d3055c. This checksum applies only to that historical asset; re-fetch current releases and terms.

An AUR recipe was inspected at 742c9d08c918b8ca275aa8f178857ed7407674fb, but it used a different build route and writable portable data. The Omarchy recipe used its own pinned binary recipe and GitHub digest watch. It did not import those ownership assumptions.

Integration: preserve saved LibraryPath from library.json; honour explicit data/home overrides; adopt the supported existing home library; use user storage on fresh installs; stop on missing saved drives or corrupt config; refuse root GUI launch. Inspect upstream APPIMAGE-dependent behavior before using any equivalent workaround in another app. Old /opt portable data was not automatically migrated.

Validation: 13 isolated launcher tests, desktop validation, source checksums, staged file/mode inspection, unchanged executable comparison and --help passed locally. Local host staging was explicitly not called an Arch build. Initial GUI attempt failed because display sockets were unavailable. GitHub subsequently completed the actual x86_64 Arch build and test jobs successfully and uploaded an unsigned package artifact.

At the time this example was written, live Omarchy launch, real GPU generation, upgrade/removal acceptance and publication remained unverified; the PR stayed draft. Do not turn these historical facts into current CI or installability claims. Re-query the PR and current head when using it.

Transferable lesson: build success, user-data safety, application operation and repository availability need separate evidence. Do not bake Stability Matrix's argument names or paths into another vendor application's wrapper.
