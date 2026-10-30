# First instructor review packet

October 30, 2026. **Ready for an initial pedagogical review.** The corrected
PDF receipts are verified; no replacement guide or new ZIP is needed. This is
a planning record, not an email sent or a final classroom release. The user
will send the message. Private correspondence and the email draft stay out of
public repository documents.

## Packet and version instructions

- Attach the [student setup guide v0.2](handouts/PHYS3810_Student_Setup_Grover_RC1_v0.2.pdf):
  three pages covering the environment, installation, validation, and notebooks.
- Attach the [instructor guide v0.2](instructor/PHYS3810_Grover_Instructor_Guide_RC1_v0.2.pdf):
  two pages covering prerequisites, learning goals, proposed pacing, exercises,
  and mathematical checkpoints. Keep its answer material separate from later
  student-facing distribution if exercises will be assessed.
- Link the named [Grover rc1 ZIP](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip).
  Use the attached v0.2 setup guide with it; the original ZIP still embeds the
  earlier v0.1 guide. Preserve the published ZIP and its recorded digest.

The release page also retains the v0.1 PDF assets. Direct attachment of the
verified v0.2 guides and a direct ZIP link make the intended combination clear.
The PDFs need not already be committed or published as release assets for this
instructor review. Those distribution updates remain a separate planned change.
See [the authoritative PDF receipt](handouts/README.md).

## Claims to use in the first message

- This is the **first review packet**, covering setup and Grover. The published
  download does not include QFT, QPE, HHL, or Shor.
- Grover passed the recorded automated Linux checks: 50 tests/four notebooks.
  Its default path runs locally without an IBM account or quantum hardware.
  Internet is needed for package installation.
- QFT is already implemented and locally validated, but is not in this
  download. QPE is next after Git integration, followed by scoped HHL/Shor work.
  Do not repeat the superseded instruction to begin QFT.
- The **proposed** lesson has a 50-minute core and an expansion to 75 minutes;
  live pacing has not yet been rehearsed with this class.
- Native Windows/macOS and interactive setup are not yet validated. Ask which
  classroom platforms matter before finalizing the installation guidance.
- Initial feedback concerns setup clarity, prerequisites, level, emphasis,
  pacing, and the remaining scope. The instructor can review the PDFs without
  installing packages or auditing source. Technical review stays with Codex
  and the independent reviewer.

## Decisions to request together

1. **Schedule and delivery:** the three dates, available minutes per meeting,
   and deadline for the complete materials. Planning targets are not promises.
2. **Background and notation:** prior quantum topics, Python/Jupyter experience,
   relevant lecture notes/textbook, and notation or examples to follow.
3. **Format and platforms:** hands-on notebooks, demonstration, or a mixture;
   personal computers versus a managed lab; required operating systems and any
   installation restrictions. Installation/preflight should happen before class.
4. **Coverage and assessment:** whether all five implementations need in-class
   treatment or some support the wider course; whether small, fully explained
   HHL/Shor simulator examples meet the teaching goals; any preferred examples;
   and whether exercises are exploratory, submitted, or graded.

The commitment to provide five tested, commented implementations is unchanged.
Classroom emphasis and depth are separate decisions. The proposed sequence
Grover; QFT/QPE; HHL/Shor remains provisional until the instructor responds.
Do not silently reduce the requested deliverables or imply general scalable
HHL/Shor implementations. Decide solution distribution after assessment goals
are known; no student/instructor notebook split is implemented by this plan.

## Audit evidence and subsequent work

The live release was rechecked on October 30: tag target
`3894391f2026d4fd9351b346b44b5eda453a17da`, three original release assets, and
the 25-file ZIP with SHA-256
`c46d8f2ac837f2742a99384cee1bc637478b4387909a4c399e4599655b11e686`.
An anonymous download and ZIP integrity check passed; the archive contains
its original setup PDF and no later algorithm implementation. Code tests were
not rerun for this documentation-only audit.

The corrected delivered-PDF sizes/hashes and their pre-delivery prefix hashes
passed local checks; each has 24,961 additional bytes with C2PA provenance.
The reviewer's pixel/text/metadata/link comparison is recorded separately from
local validation in the PDF receipt. No PDF or release asset was changed.

Documentation checks passed: `npx --offline markdownlint-cli2@0.20.0` over
12 changed Markdown files, 73 relative links, whitespace checks, and
`git diff --check`. Standard-library hash, byte comparison, public release API,
and `zipfile.testzip()` checks used Linux x86_64/Python 3.14.4; this was not a
classroom-environment execution. The Python 3.12 classroom requirements remain
unchanged. HEAD, staged content, PDFs, source, notebooks, tests, dependencies,
and workflows match the turn's starting state. Detailed local evidence is in
ignored `artifacts/instructor-review-audit-2026-10-30/`.

After this initial review request, collect teaching decisions while performing
the [planned Git integration](GIT_INTEGRATION_PLAN.md) in a later authorized
turn, then implement QPE. A clean integration must preserve all current local
work and upstream fixes. Native-platform checks and rehearsal follow the
confirmed teaching arrangements. None of these steps was started here.

**GPT Pro sync: not needed now.** The delivery receipt is resolved; the next
substantive checkpoint is after QFT/QPE and before HHL/Shor. No extra technical
audit is assigned to the user or instructor.
