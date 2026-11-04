# November 1 full-course audit and document reconciliation

Disposition: **accept the independent technical audit and the new full-course
document-v0.2 review editions**. Reconcile documentation locally without
changing algorithms, environments, packages, Git history/indexes, or publication.
This is not final classroom approval. The user requested documentation only
and no commit/push; the optional code finding remains deferred.

The subsequent CP-and-park instruction authorizes a documentation commit and
push on `docs/phys3810-november-review`. The local-only statements below record
the completed reconciliation pass; this follow-up changes delivery authority,
not the reviewed source, supplied PDFs, or finding dispositions. Stop after
the push; no new code repair, release, or external human message is authorized.

## Accessible inputs and source identities

The audit text attachment and actual Downloads bytes of
`PHYS3810_Rick_Review_2026-11-01.zip` are accessible. The ZIP is **367,541 bytes**,
SHA-256 `1cdaf4d9a94f646c8ded8a8f7b937c7bde0b3284db1589878babb15ed5843608`.
Its eight members are two PDFs, two Markdown companions, the unchanged published
code ZIP/checksum, `START_HERE.txt`, and `REVIEW_RECEIPT.json`. All were read.
Private download links are not used as evidence of access. The original
Downloads ZIP remains unchanged; a verified local evidence copy is retained.
Reviewer execution directories and extra probe scripts are not locally mounted;
the received receipt records those results, not transferred execution logs.

The audited main is `f4990b47887b686f561602cbe713abfb1a4aff94`, tree
`e49271c0f7d6ff07c07a96fa0c3bac837afb7762`; local HEAD matches that baseline.
Recent commits show PR #113 publishing the preview and PR #114 recording its
completion/recovery. The published tag/source remains
`f717aea99c68a25ad1c68597f11d1ca12c45c56a`. The nested published ZIP is
206,868 bytes, SHA-256
`1e62f76080052979f874577aca6b426faca037486b68f69185d736548149bed1`.
No new upstream query or release operation was needed for this reconciliation.
See [the original publication receipt](PUBLIC_PREVIEW_RELEASE.md).

## Executed review evidence versus this local pass

The reviewer reports a fresh application venv on existing Ubuntu 24.04.3 /
CPython 3.12.14, unchanged requirements/constraints, 114 matching application
distributions plus pip 26.2.2, Qiskit 2.6.1, Aer 0.17.2, and JupyterLab 4.6.4.
Current source and exact published ZIP each passed **160 tests, eight notebooks,
50 nonempty code cells, 16 PNGs**, pip consistency, and zero notebook errors.
The ZIP execution reused that new audit venv. These are two runs of the same
160 tests, not 320 distinct tests. The reviewer separately reports Bash smoke
and Ruff 0.15.22 success and observed remote CI checks.

This turn did **not** reinstall dependencies or rerun the application suite.
No source, tests, pins, notebook, or builder changed. Existing execution evidence
carries forward with its original identities. No new browser/editor, native
Windows/macOS, GPU, Runtime, hardware, OCR, or human pacing pass is claimed.
The reviewer reports OCR and visual review; local render inspection and text
comparison below are distinct checks, without a repeated OCR claim.

## New document editions, preserved exactly

- [Student PDF v0.2](handouts/PHYS3810_Full_Course_Student_Setup_v0.2_REVIEW_DRAFT.pdf):
  74,713 bytes, four pages, SHA-256
  `4dc39dd536cf1e3c2e1a712dc92cbae6a605ba02d135e848523e78e0644a31b0`.
- [Student Markdown v0.2](handouts/FULL_COURSE_SETUP_v0.2_REVIEW_DRAFT.md):
  9,784 bytes, SHA-256
  `95c024b9663d8b18c9550d29851b5e3f01c0ee9e3eca3259e7a38a8a84d26035`.
- [Instructor PDF v0.2](instructor/PHYS3810_Full_Course_Instructor_Guide_v0.2_REVIEW_DRAFT.pdf):
  84,527 bytes, six pages, SHA-256
  `0255da43e512d36582bb33451fcc8027f9b0cbccbe8217afdfa8f256147dd896`.
- [Instructor Markdown v0.2](instructor/FULL_COURSE_INSTRUCTOR_v0.2_REVIEW_DRAFT.md):
  16,920 bytes, SHA-256
  `32ed2c10b74522de489c0f90bc74617221522654bf9ebc82c181395f5b808e40`.

All four use new paths from the receipt and match delivered bytes. No local PDF
generation, optimization, metadata alteration, or provenance removal occurred.
The old full-course v0.1 pairs, all Grover editions, and builders stay unchanged.
The published ZIP continues to contain the v0.1 student pair; these v0.2 editions
are separate review documents, not replacement release assets.

**P3-01 is resolved in the new instructor edition.** It limits division by
`2**m` to a phase-estimation counting register; Grover/QFT labels remain integer
indices and HHL applies its stated eigenvalue conversion. The old v0.1 edition
still requires [its reading note](instructor/README.md). Former bundle evidence
links now identify immutable repository sources, and run sheets are clearly
online instructor references outside the student ZIP.

The new documents predate the user's scheduling clarification. Preserve their
50/75-minute proposals and open-duration wording as supplied; current scheduling
is recorded separately below. Do not change synchronized Markdown alone or
request another PDF merely to communicate that caveat during instructor review.

## Finding dispositions

1. **A, optional GPU diagnostic: reproduced; repair deferred.** The exact fifth
   cell in `notebooks/04_aer_gpu_smoke.ipynb` was executed with standard-library
   synthetic inputs: CPU-only intentionally skips, while advertised GPU plus
   a constructor failure prints the error and suppresses the exception.
   No Qiskit service/GPU was used. This is outside classroom defaults and is
   not an algorithm or required-validator failure. A later code-edit instruction
   can add absent/failing/successful mocks and make actual execution failure
   observable; this documentation-only turn does not implement that repair.
2. **B, repository notice links: confirmed and repaired.** The root-relative
   `MANIFEST.json` and `VALIDATION.md` targets do not exist in the repository.
   The notice now links repository publication evidence and describes the
   archive manifest. Package-template links and frozen archive bytes remain
   unchanged; repository and extracted-package navigation are checked separately.
3. **C, future-tense availability: confirmed and repaired** in current README,
   setup, and notice navigation. Historical delivered pairs remain untouched.
4. **D, validator inventory: confirmed and repaired** in the general environment
   guide. `scripts/validate_classroom.py` requires eight notebooks, not just
   preflight and two smoke notebooks. The tested command remains unchanged.
5. **E, stale next steps: confirmed and repaired.** Course plan, workflow,
   status, readiness, and presenter navigation distinguish completed milestones
   from current pending decisions. Historical evidence stays identified as such;
   it is not authority to repeat completed integration/review/publication.

## Scheduling evidence and outstanding decisions

The user-supplied course listing shows **12:40–2:05 PM, 85 minutes**, with a
Monday/Wednesday meeting pattern. An earlier proposal names **November 16, 19,
and 23, 2026**. Standard-library calendar arithmetic yields Monday, Thursday,
Monday: November 19 needs confirmation as a special meeting or correction.
No date was silently substituted. The earlier proposal named QFT, Shor, and
Grover; QPE/HHL are later deliverables, with their in-class allocation unresolved.
Only these planning conclusions are recorded; private correspondence and
screenshots are not copied into repository documents.

The [course plan](COURSE_PLAN.md) and [presenter index](R4_PRESENTER_RUN_SHEETS.md)
retain 50-minute fallbacks and 75-minute content routes, reserving ten minutes
of questions/transition/recovery margin inside the 85-minute period. This does
not prove that two advanced hands-on labs fit one class. Final dates/count,
topic priorities, outside-class work, background, platform access, delivery,
assessment/solution distribution, and human pacing remain unresolved. Rick's
reply is still pending; the assistant sent no message.

## Local verification and preservation

The receipt checks passed: exact safe eight-member inventory, no duplicate paths
or symlinks, CRC, all seven payload hashes/sizes, reviewed main/tree, both
companion bases, and nested ZIP/checksum. The nested manifest's 47 payloads / 48
files, source hashes, 37 exact committed files, and builder hashes match local
Git objects at the declared source. All 41 extracted-package relative links
resolve; six immutable repository PDF-link targets match local Git objects.
External URL availability was not newly tested.

Both PDFs match receipt metadata, empty authors, absent creation/modification
dates, page counts, and all 16 annotations including destination/rectangle/page.
All ten pages were rendered and visually inspected without clipping, overlap,
missing glyphs, or broken command wrapping. Normalized visible text matches the
companions (1,762 student and 3,173 instructor tokens). All six student fenced
blocks match the preserved v0.1 companion, and each command line appears complete
in the PDF. Supplied hidden lint directives are preserved.

Local machine-readable evidence, the received ZIP copy/receipt, and verification
script are retained under ignored `artifacts/november-review-2026-11-01/` in the
original repository. Rendering/extraction used a separate `/tmp` directory;
existing environments and earlier R1/R2 staging were not used or altered.
Final focused Markdown/link, whitespace, and preservation results are recorded
with that evidence; application tests are intentionally not repeated for prose.

Focused validation passed: markdownlint-cli2 0.20.0 checked all 20 changed/new
Markdown files with zero errors; 293 repository relative-link targets resolve;
`git diff --check` passes. The default offline npm cache lacked the lint tool,
so it was obtained using a task-local `/tmp` cache; no classroom environment was
changed. All 84 protected tracked non-Markdown files and old full-course
companions match the baseline. All six current setup fenced blocks are unchanged.
Local HEAD remains `f4990b4`, the original index is byte-identical, and both
other worktrees remain clean at their recorded heads (`f4990b4` and `0570863`).
Recovery stash `2705385616e21718a10b73765946e430597dc4bf` remains intact.
Only 17 existing Markdown files and five new document/receipt files are in the
working changes; nothing is staged, committed, or pushed.

## Stop point

The [instructor review plan](INSTRUCTOR_REVIEW_PLAN.md) identifies the verified
packet and the narrower outstanding questions. The user can send it with the
scheduling caveat; delivery is not assumed. While waiting, the optional GPU
diagnostic fix is concrete bounded maintenance if separately requested, and a
voluntary solo Grover rehearsal can measure presenter time. There is no reason
to add content, regenerate PDFs, rebuild packages, repeat unchanged tests, or
start a new readiness cycle. No manual technical audit is assigned to the user.

**GPT Pro sync: not needed.** This audit is the current independent review;
reopen review for material changed requirements, algorithms/dependencies, a
relevant native-platform issue, or a concrete unresolved defect.
