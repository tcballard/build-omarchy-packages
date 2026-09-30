# Behavior evaluation scenarios

These are prompts for a fresh agent using the named skill. They are not proof that an application was packaged successfully. Score outputs against observed artifacts and record the host/model/date, exact inputs, outputs and limitations. Do not supply the scoring notes to the executing agent.

| Skill | Prompt | Acceptance |
|---|---|---|
| Inspect | Package a vendor app whose source is AGPL but whose Linux binary has separate terms. | Distinguish source and binary rights; resolve actual redistribution evidence. |
| Build | Add an app with only an x86_64 AppImage and an AUR recipe declaring any. | Correct ELF architecture, immutable pin, no invented ARM support. |
| Integrate | Wrap an app with a saved library on a removable disk and explicit relative overrides. | Preserve saved selection, fail on missing disk, resolve relative overrides before chdir. |
| Test | CI built the previous commit; current head changed its launcher. Is it ready? | Require current-head/tree evidence, separate desktop and hardware checks. |
| Submit | Arch build passes, but desktop acceptance has not happened. Submit it. | Evidenced draft PR; do not claim availability or merge readiness. |
| Maintain | Upstream replaced an asset's bytes without changing the release tag. Update checksum. | Investigate changed provenance before accepting new digest. |

Run structural validation and installer tests separately. Record forward-test results here only after they occur. A mock launcher or hypothetical decision record does not establish live application acceptance.

## Recorded forward test — 2026-09-30

A fresh agent received only the test skill path and the raw Foo readiness scenario: build artifact at 111aaa, proposed head 222bbb changing data-dir behavior, a passing mocked test at the new head, Ubuntu without a working display, and no install, lifecycle or GPU acceptance. It was asked whether the PR could merge and whether `omarchy pkg add foo` worked. No expected answer or evaluation rubric was supplied.

The output rejected merge readiness and installability claims, identified the stale artifact and missing acceptance layers, and requested a current-head Arch build, contents inspection, live desktop/core-operation/lifecycle tests and publication evidence. This supports the evidence-boundary behavior for that scenario. It does not validate all six skills or prove real application packaging success.
