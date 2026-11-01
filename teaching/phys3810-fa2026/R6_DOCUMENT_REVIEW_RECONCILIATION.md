# R6 document-review reconciliation

Received and reconciled October 31, 2026. **Accept the delivered v0.1 PDFs as
provisional review drafts**, with one nonblocking instructor wording follow-up
recorded below. The supplied PDF bytes are integrated unchanged. The student
and instructor Markdown companions retain their reviewed visible text and
fenced blocks; each has one nonrendering lint directive for its edition line.
This is not a student release, final classroom approval, or confirmation of
Rick's teaching decisions.

The [outgoing handoff](R6_DOCUMENT_REVIEW_HANDOFF.md) identifies the reviewed
snapshot and export adaptations. The [readiness plan](RELEASE_READINESS_PLAN.md)
continues to govern platform, teaching, package, and publication gates.

## Actual access and reviewed identity

The attached review report was readable. The user also supplied the actual
downloaded `PHYS3810_Full_Course_Documents_v0.1_REVIEW_DRAFT.zip` in Ubuntu
Downloads. All six members were accessible after local integrity/path checks:

- The student and instructor PDFs.
- Both revised Markdown companions at their declared course-relative paths.
- `DOCUMENT_COMPANIONS.patch`, based on the exported input companions.
- `REVIEW_RECEIPT.json`, including file hashes, source identity, PDF inventories,
  execution claims, and page-level quality-assurance records.

The reviewer’s raw install/validator logs, rendered-page images, and OCR output
files were not delivered. Their reported hashes and QA records do not make
those private work files locally accessible. No screenshot, filename card,
private sandbox reference, or same-account login was used as a substitute for
the downloaded ZIP's actual bytes.

The received report and receipt identify the exact outgoing review:

- Source commit: `c63381a8e6fbe900103b9d2053fe978310798e9a`.
- Outgoing archive: `PHYS3810-Document-Review-2026-10-31-c63381a8e6fb.zip`.
- Outgoing size: **164550 bytes**.
- Outgoing SHA-256:
  `f0af2bfd8507a5c1c6aedc04d67bfacee86faf34d678a4e77e70fd42e853980c`.
- Outgoing manifest SHA-256:
  `33cac3de0b22632ce838152e8aebf4436e5e7cbda2f458a348629f0899de5c35`.

These values match the retained handoff. The reviewer reports that all 49
manifest-listed payloads matched and all 50 original members, including the
manifest, remained unchanged after its work. Runtime files, tests, notebooks,
pins, and algorithm contracts were not returned as modified files.

## Delivered bytes and repository placement

The downloaded return ZIP is **176121 bytes**, with SHA-256
`45520beb2780f713d903f225970541b35d9d71041b6bb4d1af5f77eb8916b927`.
It matches the review's final retrieved-archive receipt. A retained copy and
the six extracted files are kept under ignored reconciliation evidence; the
Downloads file was not replaced or rewritten.

- [Student PDF](handouts/PHYS3810_Full_Course_Student_Setup_v0.1_REVIEW_DRAFT.pdf):
  **73883 bytes, four US Letter pages, three HTTPS link annotations**.
  SHA-256: `e6a950111470dbaa1d20781f4eb17391e73b7ca247e0a4ec54c879b922ea1053`.
- [Instructor PDF](instructor/PHYS3810_Full_Course_Instructor_Guide_v0.1_REVIEW_DRAFT.pdf):
  **80911 bytes, six US Letter pages, two HTTPS link annotations**.
  SHA-256: `204d8cc180776cc4c4d7de024d457ec8198db62bbb38672791e0e3bc88696d71`.
- The unchanged [delivered review receipt](validation/FULL_COURSE_DOCUMENTS_v0.1_REVIEW_RECEIPT.json)
  records both PDFs and companion/patch hashes. Its SHA-256 is
  `91564733635134b5093de1177791156aa9fc1c88098060c57e2830f914df48a3`.

These hashes identify the complete PDF members inside the downloaded return
ZIP, including any bytes after the PDF end marker. They do not identify
separately uploaded previews. No PDF was regenerated, optimized, flattened,
or stripped of provenance during integration. The earlier Grover document-v0.2
PDFs and original rc1 assets remain separate, unchanged editions.

The titles match the receipt: **PHYS 3810 Full-Course Student Setup - v0.1
REVIEW DRAFT** and **PHYS 3810 Full-Course Instructor Guide - v0.1 REVIEW DRAFT**.
Author fields are empty; no new author or institutional endorsement is inferred.
Creation/modification date fields are absent. Both use 612×792-point pages and
display their review-draft status throughout.

## Reproduced findings and disposition

All four reported document issues were reproduced against the outgoing export.
The returned editions resolve them within the provisional document scope:

1. **Misleading native-procedure link — corrected.** The incoming instructor
   link labeled “Native procedures” led to a platform-evidence summary because
   the full procedures were excluded from the bundle. The returned guide
   removes the misleading availability claim and states which native platforms
   and editor paths remain untested.
2. **Stale PDF-QA statement — corrected.** The incoming instructor opening said
   rendering, visual inspection, and OCR had not yet occurred. That incoming-state
   sentence is absent from the returned edition. Actual local checks and
   reviewer-reported QA are distinguished below.
3. **Coordination/history in teaching pages — corrected.** Historical milestone
   narration and instructions about model/file transfer, provenance, and package
   production are removed from the finished instructor material. Teaching
   assumptions, bounded mathematical contracts, answer cues, and pending
   decisions remain.
4. **Bundle-relative links in a document-only return — corrected.** Course
   references are now readable paths inside the complete course folder.
   The only clickable Markdown/PDF destinations are the five supplied official
   documentation URLs. No unpublished release URL was invented.

The revised guides retain the 160-test/eight-notebook/50-cell/16-PNG inventory,
the proposed 50/75-minute routes, platform/editor limitations, and distinction
between worked notebooks and an answer-free assessment. Source-grounded review
and independent scalar checks confirmed the Grover probabilities, QFT sign and
swap conventions, asymmetric/nonexact QPE cues, HHL raw branches/complex phases/
fixed-C scaling, and compiled Shor order/factor examples. QPE's one/two-target
limit and Shor's separate four-residue-qubit builder remain unchanged.

### P3-01: qualify phase-fraction decoding in the next instructor edition

On instructor page 3, under “Grover and QFT: exact conventions,” the sentence
about decoding a count string as `int(bits, 2) / 2**m` does not explicitly limit
that conversion to a phase-estimation counting register. The formula is valid
in that domain, but the heading can invite an overbroad reading. Ordinary
Grover search labels and QFT basis labels denote integer indices; `011` is
index 3. The [QPE contract](QPE_PLAN.md) applies division by `2**m` specifically
to the phase-estimation count register.

**Disposition:** low-severity clarity follow-up, nonblocking for these provisional
review drafts. Correct it in the next ChatGPT-authored instructor edition before
final classroom distribution. Suggested wording:

> Displayed bitstrings label the integer `int(bits, 2)`. For an m-qubit
> phase-estimation counting register, the phase estimate is
> `int(bits, 2)/2**m`; HHL then applies its stated phase-to-eigenvalue conversion.

This correction is recorded outside the delivered PDF/companion body to retain
their synchronization. No runtime or algorithm-contract repair is required.
The student setup edition is unaffected. The local disposition therefore
accepts provisional use with this follow-up; it does not repeat an unrestricted
“no remaining issue” claim or certify a final instructor edition.

## Markdown integration and navigation mapping

Both exported base hashes and the committed-source hashes match the return
receipt and outgoing manifest. `git apply --check` passed against isolated
copies of the two exported companions. Applying that patch to those copies
produced the returned Markdown bytes exactly. It was not blindly applied to
the differently linked canonical instructor base.

All **six student fenced blocks**, including the expected-output block and
fence language labels, are byte-identical to the outgoing student input. The
combined block-content hash matches the receipt, and the longest command line
is the unchanged 99-character kernel-registration command. No tested command
or dependency pin required repair.

The returned companions remove the old bundle-only clickable navigation rather
than carrying packet-only URLs into the repository. Their printed course paths
refer to existing notebooks, contracts, course plan, and presenter run sheets.
The instructor's inline `VALIDATION_EVIDENCE.md` literal identifies evidence
supplied in the retained outgoing review bundle. For repository navigation,
that reference maps to the [walkthrough evidence](R6_GUIDE_WALKTHROUGH_VALIDATION.md),
[outgoing packet receipt](R6_DOCUMENT_REVIEW_HANDOFF.md), and this reconciliation.
No nonexistent repository link is manufactured, and no printed text is silently
changed to break correspondence with the supplied PDF.

The two integrated companions each add exactly one nonrendering
`<!-- markdownlint-disable-next-line MD036 -->` comment before the bold edition
metadata line. This resolves the heading-style lint finding without altering
visible prose, page-break markers, fenced content, or global lint configuration.
The delivered originals remain in the retained return ZIP. Repository hashes
therefore differ from delivered Markdown hashes by this disclosed adaptation:

- [Student companion](handouts/FULL_COURSE_SETUP_DRAFT.md): delivered
  `bd7bd8c499b432307e1845af9ef806a8edf79fa52a28b93977408ee738e33875`;
  repository `f26919ac85fd8bd4419e19ac118a9cb0eca4e1f72348cf84e3a65fa91deaa631`.
- [Instructor companion](instructor/FULL_COURSE_INSTRUCTOR_DRAFT.md): delivered
  `1a2b41822632bc3335464419a97a4df143b4a2e1c57ab036717e1e70fa67d657`;
  repository `7b4d0216d83d5667d549d5342dcc6e068a120c37039451aa9f593b848e6262ed`.

## Local PDF verification and reviewer-reported evidence

**Passed locally:** exact return ZIP/member sizes and hashes; source/manifest
identity; PDF metadata, page counts/sizes, five link destinations and annotation
rectangles; visible font embedding/Unicode maps; text geometry; and normalized
PDF-body/Markdown correspondence. Every line of the student's six fenced blocks
survives PDF text extraction unchanged. All five official documentation URLs
were opened successfully; this is not a PDF-reader click-behavior test.

Read-only Poppler rendering at **150 dpi** produced all ten pages, and each
full-page image was visually inspected locally. No clipped text, damaged math,
overlap, missing glyph, or page-layout defect was observed. The long registration
command remains one unclipped line. Rendering for inspection did not rewrite
the supplied PDFs.

The first text-normalization assertion failed because the page-furniture
recognizer assumed one space around a header slash while extraction returned
two. Only that audit recognizer was corrected; exact normalized body matching
then passed. The original diagnostic is retained. This was not a PDF defect
and caused no PDF or companion-content edit.

**Reported by GPT Pro, not newly executed here:** a fresh isolated application
environment on Ubuntu 24.04.3 LTS, Linux 6.18.57 x86_64/glibc 2.39, using an
existing CPython 3.12.14 interpreter. The receipt reports 114 application
versions matching active supplied constraints plus pip 26.2.2, dependency
consistency, **160 tests, eight fresh-kernel notebooks, 50 cells, 16 PNGs,
zero notebook errors, validator exit 0**, and all 50 input members unchanged.
It explicitly does not claim a new OS/interpreter installation or interactive
student-guide walkthrough.

The reviewer also reports rendering all ten pages at 150 dpi for visual review
and 300 dpi for Tesseract OCR, page-level QA, and final downloadable-byte
retrieval. The delivered receipt includes the page-level results; the raw OCR
and runtime logs were not supplied. **Local OCR was not rerun.** Local exact
text/metadata/link checks and ten-page visual inspection independently support
the document integration, while the fresh-install and OCR claims retain their
reviewer-reported attribution.

The full Python suite is not rerun solely for these document/prose changes.
Canonical algorithm source, tests, notebooks, pins, and supported contracts
remain unchanged; earlier local runtime evidence and the identified new review
are separate records. Final documentation lint/link and preservation checks are
recorded in the local completion evidence rather than invented as a new runtime
or UI pass.

**Final local checks passed:** 378 repository file links, seven Bash syntax
blocks across changed guidance, six unchanged student fenced blocks, and the
configured pre-commit hooks (Ruff, yamllint, markdownlint). All 115 unchanged
tracked files retain their bytes/modes. The original/accepted checkouts and
indexes, existing environments/staging, old recovery/assets, both outgoing ZIP
copies, incoming Downloads ZIP, and 30 prior handoff evidence files passed
preservation checks. The completion receipt identifies the local commit and
clean candidate worktree; no old archive was rewritten.

## Remaining gates and next local task

Rick's reply remains pending. Dates, coverage, assessment/solution distribution,
delivery responsibility, required classroom platforms, and human pacing are
not established by document acceptance. Native Windows/macOS, native editor UI,
automatic browser opening, and other unexecuted surfaces retain their recorded
limits. Existing Grover guides/assets, prior reviewed archives, environments,
and both prior checkouts/indexes remain preserved. No email, publication,
hardware job, or new classroom commitment occurred.

**Recommended next task:** prepare R7 as a **local preview packaging** milestone:
a new scoped full-course builder and candidate ZIP using the verified student
review-draft PDF and current 160-test/eight-notebook source. Exclude instructor
answer documents/PDFs from that student-facing payload; do not describe its
worked notebooks as answer-free assessments. Verify the sealed extraction,
manifest, exclusions, links, source cleanliness, and complete validator counts.
Preserve the original Grover and review archives. A local preview does not close
teaching/platform/pacing gates or authorize publication. P3-01 remains attached
to the instructor's next edition before final classroom distribution.

**GPT Pro sync: not needed solely for this reconciliation.** Carry P3-01 into the
next instructor-document revision with any later teaching feedback. A new or
changed setup command, supported scope, or delivered-byte discrepancy would
require an appropriate new check or sync; no such runtime change is introduced
here.

Ignored evidence is under `artifacts/r6-doc-reconciliation-2026-10-31/`: access
and retained-byte receipts, extracted return files, text/patch audit, PDF and
visual-review records, normalization diagnostics, integration hashes, and
preservation/completion checks. The raw review report is retained only as local
evidence; this repository record contains technical conclusions rather than
private chat text.
