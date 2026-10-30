# Preserving and integrating the local Git state

Current integration snapshot, October 30: this local documentation/PDF change
is based on published main `3894391`. The original development checkout and
index have a verified recovery checkpoint and remain intact. QFT code and its
64-test/five-notebook evidence are outside this revision and will follow in a
separate commit. Its runtime remains the published Grover 50-test/four-notebook
scope. Older planning and validation entries below retain their dated context.

October 30, 2026. **Plan only; no staging, commit, stash, branch switch, reset,
worktree cleanup, or publication was performed during this reconciliation.**
The dirty tree is accumulated work, not a reason to discard files. The assistant
owns comparison and technical review; the user is not assigned a manual audit.

## Observed starting state

- Active branch: `feat/phys3810-m1-onboarding`, HEAD
  `fb41ae02f2ece3e093e60c9286ef72ae91686530`.
- Recorded `origin/main`: published Grover commit
  `3894391f2026d4fd9351b346b44b5eda453a17da`. `HEAD...origin/main`
  contains 0 local-only commits and 13 main-only commits.
- The index contains 28 paths from the earlier onboarding preparation. Many
  now also have newer unstaged content. The index is not the final release or
  a complete QFT snapshot; committing it blindly would preserve the wrong scope.
- At the start of this turn, a byte comparison of all 81 nonignored source/doc
  files against the recorded main tree found 63 identical files, 14 differing
  files, and four local additions. No main path was missing. This includes
  files untracked relative to the old local HEAD, which a simple Git diff
  against main can misleadingly present as deletions.
- The four additions were `src/phys3810/qft.py`, `tests/test_qft.py`,
  `notebooks/02_qft.ipynb` in this course directory, and `QFT_VALIDATION.md`.
  The 14 differences include QFT exports/validator/preflight changes and
  development/publication documentation. This turn adds further documentation
  and two PDF candidates; refresh the inventory before integration.
- The former temporary Grover-preview worktree is registered but its directory
  is absent. Its registration is prunable. The published commit is still
  available; do not confuse temporary-directory loss with lost committed work.

## Recommended integration sequence for a later turn

1. **Preserve the current state first.** Save a local recovery checkpoint with
   HEAD/branch identity, separate binary staged and unstaged patches, all
   nonignored untracked files, and a content/mode manifest. Verify the recovery
   material before changing Git state. Existing ignored artifacts/environments
   remain in place; secrets must not enter a public commit or review bundle.
   The inspection manifest alone is not a restorable backup.
2. **Use a durable separate worktree from current main.** Refresh the remote
   baseline and inspect any newer changes before choosing the integration base.
   Start from the published history, retaining upstream fixes. Leave this
   original working tree and index intact. Use a persistent location, not a
   temporary directory. Inspect stale worktree registrations before any prune.
3. **Prepare the documentation change independently.** Carry forward the
   publication/review records, setup corrections, and PDF policy. Use the
   [corrected delivered-file receipts](handouts/README.md), now verified, for
   the existing reviewed PDFs. Preserve their appended provenance. Stage only
   the chosen documentation/PDF paths in
   the new worktree; verify their hashes, relative links, and Markdown checks.
   Confirm tracked PDF paths with `git ls-files` after the local commit.
   Keep this commit coherent on its own: QFT-dependent links and availability
   statements belong with the QFT change, not in an incomplete documentation
   snapshot that refers to files absent at that commit.
4. **Carry QFT forward as a separate logical change.** Transfer its source,
   exports, tests, notebook, validator registration, preflight wording, and
   matching course documentation. Compare actual file bytes, including local
   additions, against the chosen baseline. Do not copy the entire stale tree
   over current main or reintroduce already-merged onboarding/Grover changes.
5. **Validate the integrated result.** Run the documented Python 3.12 checks
   after carrying QFT forward; the existing baseline is 64 tests/five notebooks.
   Check both commits' scope and a clean worktree. Publish only under applicable
   authorization and normal required checks. Never bypass repository rules.
6. **Resume QPE after integration.** Retain the full-matrix QFT evidence and
   require asymmetric exact phases plus a nonexact distribution. Prepare the
   combined GPT Pro review after QFT/QPE, before HHL/Shor.

The old checkout can remain as a preserved recovery location while development
continues in the new clean worktree. Retiring it is a separate deliberate step
after verifying every local change is preserved. Do not use `reset --hard`,
`clean`, or an indiscriminate stash/pop sequence as the reconciliation plan.

The next execution prompt covers steps 1-5 only. Return the verified recovery
location, refreshed base, durable worktree path, separate local commit IDs,
validation outcomes, exact PDF hashes, and a clean integration worktree. Preserve
the original checkout/index. Step 6, QPE implementation, follows separately;
no push, PR, merge, release update, instructor message, or hardware job is part
of this local integration scope. End with the next copyable Codex instruction
as specified in [WORKFLOW.md](WORKFLOW.md).

## Documentation/publication boundary

The earlier authorization completed PR #112 and the original rc1 prerelease.
It does not initiate a new documentation PR or release-asset update this turn.
For a later authorized update, add distinct v0.2 PDF asset names and link the
documentation commit. Preserve the original tag, ZIP, and assets. Replacing the
bundled guide requires a newly versioned bundle and matching reviewed PDF.
