# Inspection record

Record: upstream URL; inspected tag/commit; existing package recipes and their commits; application version; source/binary choice; source license; binary terms; supported architecture assets; runtime and build dependencies; display backend; executable entry point; data paths; self-update mechanism; optional downloads; migration plan; missing evidence.

Use the upstream repository, release API and vendor distribution/license pages as primary sources. Inspect AUR recipes as inputs, not as authority for redistribution rights, dependency correctness or safe file modes. Verify ELF architecture and dynamic libraries with readelf/file without treating `arch=('any')` in an existing recipe as proof.

Source routes must pin a release archive or exact VCS revision. Binary routes must select the correct architecture, preserve required notices and verify the complete downloaded asset. AppImage extraction should use an archive tool where possible; executing the AppImage to extract it executes vendor code and must be reviewed as such.

Primary references (check their current contents):
- https://github.com/omacom/omarchy-pkgs
- https://wiki.archlinux.org/title/PKGBUILD
- https://wiki.archlinux.org/title/Arch_package_guidelines
- https://wiki.archlinux.org/title/Creating_packages

Do not claim native Wayland support from successful XWayland launch. Do not claim GPU support from a successful GUI startup or --help run.
