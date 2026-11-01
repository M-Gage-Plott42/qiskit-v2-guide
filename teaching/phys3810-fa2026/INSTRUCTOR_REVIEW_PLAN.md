# First instructor review packet

October 30, 2026. **Initial setup/Grover email sent by the user; reply pending.**
The user supplied a sent-message screenshot showing one student setup PDF
attachment. The instructor guide and direct ZIP link were recommended below,
but their delivery is not confirmed by that evidence. No attachment-byte hash
was supplied with the email record; do not turn its filename into a new PDF
receipt. The repository's verified v0.2 PDF bytes remain unchanged.

The outstanding decisions are three visits versus broader five-topic coverage,
in-class versus outside-class work, Python/Jupyter preparation, hands-on versus
demonstration format, assessment, possible preparation/platform survey, who will
deliver the sessions, and preferred lecture notes or HHL/Shor examples. These
are pending questions, not agreed changes to the course. No reply is recorded.
Local module development continues under the bounded contracts while awaiting
feedback. Record only teaching decisions from a later reply; keep private email
text, addresses, and screenshots out of public repository files. The assistant
has not sent an email or scheduled a follow-up.

## Recommended packet (delivery beyond setup draft unconfirmed)

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
The PDFs are tracked in the local documentation integration commit. Adding v0.2
as public release assets remains a separate planned action.
See [the authoritative PDF receipt](handouts/README.md).

## Scope and claims for subsequent discussion

- This is the **first review packet**, covering setup and Grover. The published
  download does not include QFT, QPE, HHL, or Shor.
- Grover passed the recorded automated Linux checks: 50 tests/four notebooks.
  Its default path runs locally without an IBM account or quantum hardware.
  Internet is needed for package installation.
- QFT and QPE are implemented and locally validated, but are not in this
  Grover download. Their combined independent review is accepted; later module progress is tracked
  in [STATUS.md](STATUS.md).
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

Await the instructor's reply; the QFT/QPE independent review is already accepted.
[Git integration](GIT_INTEGRATION_PLAN.md) is complete and preserved
all original work and upstream fixes. QFT, QPE, HHL, and Shor are now locally
validated and independently accepted; the
[review follow-ups](HHL_SHOR_REVIEW_RECONCILIATION.md) are reconciled. Native-platform checks and
rehearsal follow confirmed teaching arrangements. The original Grover PDF
editions remain unchanged as the first instructor packet.

**GPT Pro sync: not needed for the reconciled QFT/QPE follow-ups.** The delivery
receipt and independent phase-convention checkpoint are resolved. No extra technical
audit is assigned to the user or instructor.

## Subsequent local integration, October 30

Documentation and verified PDF bytes are tracked in local commit
`b16d235ca01ebc9c7f610dcfeb64f081d5d6b453`. The following QFT commit carries
forward the existing implementation and its evidence; see
[INTEGRATION_VALIDATION.md](INTEGRATION_VALIDATION.md) for the new execution
results. The original checkout/index and published Grover rc1 assets remain
intact. That integration step sent no instructor message; the later user-sent
setup email is recorded at the top of this document. No new release was made.
