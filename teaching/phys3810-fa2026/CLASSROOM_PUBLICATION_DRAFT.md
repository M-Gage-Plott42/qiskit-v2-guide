# Authorized provisional preview publication

November 1, 2026. The user requested a new preview publication, pushing the
work, and clean Git state this turn. [R8_READINESS_AUDIT.md](R8_READINESS_AUDIT.md)
records the live repository gates and scope. This authorizes the normal workflow
for the named technical preview, not final classroom approval or outreach.

## Release identity and assets

- Tag: `phys3810-fa2026-v0.2.0-rc1`.
- Title: **PHYS 3810 Fall 2026 — full-course provisional preview v0.2.0-rc1**.
- Status: prerelease, not latest stable.
- Assets: `PHYS3810-Fall2026-v0.2.0-rc1.zip` and `.zip.sha256`.
- Top directory: `phys3810-fa2026`.
- Source: the exact normal-workflow merge commit, determined after required CI.

The old Grover rc1 tag/ZIP/PDFs and R7 local source `135d5d0`/archive remain
unchanged. The new public builder is separate from the local R7 builder.
It produces 47 payload files plus a manifest. Required source/tests/notebooks,
pins, license, and the reviewed student PDF/Markdown stay exact. Instructor
answer documents are excluded from the named ZIP; the repository itself still
contains instructor material and worked results. Nothing is assessment-safe by
virtue of that packaging distinction.

## Current instructions and preserved PDFs

The [current setup page](SETUP.md) and package README govern availability.
The reviewed PDF and paired Markdown are preserved as prepublication references,
with an explicit [publication notice](handouts/PUBLICATION_NOTICE.md) explaining
that their old unpublished-download statement describes review-time state.
No PDF is edited or offered as a separately updated PDF asset. All six tested
student command/output blocks remain unchanged in the current setup page.
This is a disclosed publication adaptation, not a newly reviewed PDF edition.

## Merge and verification gates

Push the candidate branch and open a PR into main. Preserve accepted history
with a merge commit only after all nine required checks succeed on the actual
head and GitHub's merge gates are clear. Do not use the available admin bypass
or change rulesets. Record any concrete CI finding and its repair.

After merging, build from that exact commit and validate an isolated extraction:
manifest, links, exclusions, source/PDF bytes, and 160 tests/eight notebooks/
50 cells/16 PNGs. Record reused versus fresh environment. Create the prerelease
only after those checks, then retrieve public assets without authentication and
verify hashes, manifest, source commit, and tag target. The checksum file is
outside the ZIP to avoid circular identity.

Record the actual outcome and recovery location locally and push completion
documentation through the normal workflow. Preserve original dirty work in a
verified named stash/checkpoint before switching/fast-forwarding its main branch.
No destructive reset, clean, or stash pop is part of that cleanup.

## Remaining classroom gates

The evidence supports the documented Ubuntu/Linux path. Native Windows/macOS,
native editor UI, automatic browser opening, and human pacing remain untested.
Rick's dates, coverage, delivery, preparation, platform, assessment, and solution
policy decisions remain pending. P3-01 applies to the next final instructor
edition and is not a blocker for this student preview. The guide and final
classroom package must be revisited when those inputs change.

After this authorized delivery, wait for instructor feedback or a specific
new request. More unchanged test, package, PDF, or planning rounds would add
little. No new algorithm scope, dependency change, PDF regeneration, external
human message, or hardware job is included here.
