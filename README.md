# Build Omarchy Packages

Take an existing Linux application from upstream release to a tested Omarchy package contribution.

Six portable Agent Skills guide source selection, PKGBUILDs, desktop integration, clean Arch builds, PRs and ongoing updates. Use them with Codex, Claude Code and other Agent Skills hosts. Stability Matrix is the first worked example; its draft package contribution illustrates the workflow, with live acceptance explicitly tracked separately from CI.

## Start here

Ask your agent: **“Use the Omarchy packaging skills to package this upstream application for omarchy-pkgs, validate it, and prepare a PR.”**

| Skill | Use it for |
|---|---|
| omarchy-package-inspect | Upstream, existing packages, licensing and architecture decisions |
| omarchy-package-build | Pinned source/binary recipes and upstream release watches |
| omarchy-package-integrate | Desktop launchers, libraries, permissions and self-updates |
| omarchy-package-test | Clean builds, artifact inspection and live lifecycle checks |
| omarchy-package-submit | Focused PRs, CI evidence and exact tester instructions |
| omarchy-package-maintain | Upstream updates, rebuilds, regressions and rollback |

## Install

From this checkout, install for Codex:

```bash
python3 scripts/install_agent_skills.py --target codex --scope user
```

For Claude Code, use `--target claude`. Other supported targets are agents, cursor, gemini and opencode. Run from the desired project directory with `--scope project` for project installation, or use `--target generic --destination /absolute/path/to/skills` for an explicit location. Preview with `--dry-run`; update with `--update`; inspect local changes with `--update --diff`; remove managed skills with `--uninstall`. The installer refuses conflicting local edits and preserves unrelated skills. Review a diff before using `--force`.

ChatGPT personal skill installation is a separate host operation. A local CLI installation does not install skills into ChatGPT, and a ChatGPT installation does not install them on your XPS.

## What counts as done

A recipe, a passing build, a working desktop application and a published repository package are separate outcomes. These skills report the evidence for each. They keep user data outside package-owned application files, preserve release policy and distinguish source licensing from binary redistribution terms.

Build Omarchy Apps covers application development. This bundle covers packaging existing upstream software. Plugins and themes use their respective bundles. Existing bundles are not automatically modified by installing this one.

## Validate

```bash
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
```

The bundle itself needs Python 3 and PyYAML for validation. Creating packages additionally needs the target repository's documented build tools; clean builds require Arch tooling or its supported container builder. Live desktop/hardware testing requires an appropriate Omarchy machine.

## Sources and maintenance

The repository workflow snapshot was reviewed on 2026-09-30. Every skill instructs agents to read the current omarchy-pkgs contract before acting. Primary references are linked from each stage. See [the worked example](skills/omarchy-package-test/references/stabilitymatrix.md).

The receipt-based installer and its lifecycle tests are adapted from Tom Ballard's MIT-licensed Build Omarchy Plugins bundle. No application binaries or vendor EULAs are redistributed in this bundle.

Community tooling by Tom Ballard. This bundle is not an Omarchy project endorsement.
