# Contribution handoff

PR body fields: resulting behavior; canonical upstream and revision; existing AUR recipe consulted; locally owned packaging rationale; source/binary architecture support; license/notices; release watch; data ownership and migration; self-update handling; build and desktop/lifecycle evidence; unresolved acceptance.

In September 2026, omarchy-pkgs PR tooling ran from the base branch and overlaid package directories from the PR head. Vouched authors/collaborators or maintainer build-approved labels controlled access to builders. Check current workflows before relying on these rules. Tooling changes and recipe changes in one PR may test the recipe with old tooling; separate those contributions when necessary.

Verify exact tree/commit matching when CI reuses artifacts. A package artifact proves the corresponding package directory built, not that its installation or functional operation was tested. Do not merge another contributor's work or promote release channels solely because CI is green.

If a connector cannot perform a requested operation, follow available plugin/browser fallback guidance; prepare all reviewable content before any necessary user handoff. A failed create request is not evidence a PR exists. Verify the final remote object and give its real URL.
