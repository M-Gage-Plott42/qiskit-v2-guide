# R8 preview publication readiness

Audited November 1, 2026. The initial read-only request was superseded by the
user's explicit request to publish a new preview, push the work, and leave Git
clean this turn. This authorizes the named provisional preview through the
normal PR/required-check merge/release workflow; it does not authorize unrelated
releases, human outreach, hardware jobs, or rewriting supplied PDF bytes.

## Live repository findings

Read-only GitHub queries found `main` at
`3894391f2026d4fd9351b346b44b5eda453a17da`, unchanged from R5. The proposed
`phys3810-fa2026-v0.2.0-rc1` tag has no matching ref or release in the visible
release inventory. This is an observation, not a reservation; recheck before
creation. No open PR existed at the audit.

The active [main-pr-required-checks ruleset](https://github.com/M-Gage-Plott42/qiskit-v2-guide/rules/12879933)
applies to the default branch. A legacy branch-protection API response says
“Branch not protected”; that refers to the legacy endpoint, not absence of the
active ruleset. Required checks, with strict up-to-date enforcement, are:

- `local-smoke`, `ruff`, `markdownlint`, `yamllint`.
- `actionlint`, `shellcheck`, `dependency-review`.
- `Analyze (python)` and `Analyze (actions)`.

PRs and resolution of review threads are required. The configured approving-
review count is zero, with no code-owner or last-push approval requirement.
The API also reports `require_extra_approval_for_unattributed_changes=true`;
respect any additional server-evaluated gate rather than guessing it away.
Admin bypass is available but will not be used. Existing merge/squash/rebase
methods are allowed; a merge commit preserves the accepted local history.
The observed main checks cover the old Grover source, not the new candidate.
The PR-only dependency check must run on the new PR. Zero legacy commit statuses
must not be misread as a failed Checks API result.

## Three distinct outcomes

1. **Verified local preview:** R7 source `135d5d0`, archive SHA-256
   `7cd1cb0a75b268141a8962d512fe38deb3fe1a38911e90577d736fe445a2f79f`,
   47 files and 160 tests/eight notebooks/50 cells/16 PNGs. It remains immutable.
   The actual path uses `artifacts/local-candidate-2026-10-31/worktree`; the
   prior chat's October 30 candidate-directory link was incorrect, not a moved
   or missing package. The eight file changes between the package
   source and the R7 completion snapshot are documentation-only.
2. **Provisional public preview:** authorized now. It needs current publication
   entry points, exact merged source identity, nine successful required checks,
   a newly built and validated archive, and published-byte verification. It may
   honestly retain Linux-only evidence and open teaching/pacing decisions.
3. **Final classroom release:** still requires the relevant instructor scope,
   preparation, delivery, assessment/solution/platform decisions, human rehearsal,
   and applicable native/editor validation or an agreed supported alternative.
   P3-01 must enter the next final instructor edition. No such approval is
   inferred from publishing a technical preview.

## Publication adaptation

The R7 archive must not simply be relabeled as public: its README/templates say
unpublished/local, and the reviewed PDF/companion say the full-course download
is unpublished. A separate prerelease builder therefore preserves the R7
builder and artifact, while supplying current README/SETUP/validation entry
points and an explicit publication notice.

The PDF and its paired Markdown stay exact prepublication review references.
Their old availability statement is plainly identified as review-time text,
outdated after this prerelease. The current setup page governs availability;
all six tested command/output blocks and subsequent instructions stay unchanged.
No new or revised PDF is claimed, and no standalone updated-PDF release asset
is planned. The student ZIP excludes instructor answer documents; notebooks,
contracts, and tests still contain worked results and are not assessment-safe.

## Concrete execution proposal

- Publish tag `phys3810-fa2026-v0.2.0-rc1` as a prerelease, not latest stable.
- Assets: `PHYS3810-Fall2026-v0.2.0-rc1.zip` and its `.zip.sha256` file.
- Push the candidate branch, open a PR into main, and merge only after all nine
  required checks pass on its actual head and GitHub's merge gates are clear.
- Fetch the merged revision without force/reset. Build the public package from
  that exact source, verify its manifest/paths/links/unchanged reviewed bytes,
  and run the extracted 160/eight/50/16 validator before creating the release.
- Verify the tag target, then anonymously retrieve both published assets and
  compare hashes and manifest. Preserve Grover rc1 and every earlier package.
- Record completion through the same normal workflow; leave tracked working
  states clean and all deliverable commits pushed.

The original dirty checkout has a verified recovery checkpoint. All 87 saved
paths occur in the accepted candidate: 68 unchanged, 12 older versions retained
in ancestry, and seven appropriately advanced documentation files. No unique
unintegrated implementation was found. After successful publication, preserve
its exact raw index/status again, make a named `stash --include-untracked`, verify
its tracked/index/untracked trees against the recovery manifest, then switch
and fast-forward local main. Keep the stash and old recovery; do not use `--all`,
`stash pop`, force-reset, or `git clean`. The accepted integration worktree remains
a historical clean snapshot. This is recoverable cleanup explicitly requested
by the later user instruction, not disposal of old work.

## Stop after delivery

After the preview is published and Git is clean, pause speculative course work
until Rick replies, a concrete defect appears, or the user requests a specific
change. Repeated packaging, test, PDF, or planning rounds without changed inputs
would add little. No new GPT Pro round is needed solely for this disclosed
publication adaptation; a final instructor edition later needs P3-01 and any
confirmed teaching changes.

The missing Downloads-copy exception remains recorded; the verified retained
return ZIP and supplied PDFs are intact. Read-only audit receipts are under
`artifacts/r8-readiness-2026-10-31/`; publication/cleanup receipts are under
`artifacts/public-preview-2026-11-01/`. This document describes the authorized
execution; final outcomes are recorded after actual checks and publication.
