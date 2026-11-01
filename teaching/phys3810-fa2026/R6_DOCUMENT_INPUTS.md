# R6 provisional document inputs and handoff readiness

Prepared October 31, 2026 from candidate
`d491b3b59fe08e92aec29cfbdcb74b4eaa816556`. **Markdown input preparation only.**
No new PDF, package, GPT Pro transfer, publication, or external message occurred.
R6's PDF delivery/review gate remains open under the
[readiness plan](RELEASE_READINESS_PLAN.md).

## Two separate companions

- [Full-course student setup draft](handouts/FULL_COURSE_SETUP_DRAFT.md):
  student-facing installation, validation, kernel use, return workflow,
  notebook navigation, and troubleshooting. It carries no instructor answer
  key, private correspondence, Git integration instructions, or model-review
  coordination. The required setup output and test counts are operational
  checks, not assessment answers.
- [Full-course instructor guide draft](instructor/FULL_COURSE_INSTRUCTOR_DRAFT.md):
  bounded contracts, teaching options, selected answer cues, evidence limits,
  and unresolved delivery/assessment decisions. It links the existing detailed
  [presenter run sheets](R4_PRESENTER_RUN_SHEETS.md).

Both are **document v0.1 drafts** for proposed **code v0.2.0-rc1**. Their names
and scopes distinguish them from the unchanged Grover document-v0.2 PDFs and
code-v0.1.0-rc1 preview. A document number does not identify a code release.
The two files are new companions; existing `SETUP.md`, course `README.md`,
Grover Markdown guides, receipts, links, and delivered PDFs remain unchanged.

The [provisional publication identity](CLASSROOM_PUBLICATION_DRAFT.md) proposes
tag `phys3810-fa2026-v0.2.0-rc1`, future archive
`PHYS3810-Fall2026-v0.2.0-rc1.zip`, and top-level folder `phys3810-fa2026`.
They are unpublished proposals. There is no full-course download URL to test
or put forward as live. The student must receive the matching complete folder;
the existing Grover-only ZIP is not a substitute for these eight-notebook notes.

## Evidence carried into the drafts

- CPython 3.12, Qiskit 2.6.1, Aer 0.17.2, and the unchanged requirements and
  constraints remain the setup contract. The documented bootstrap pip is
  26.2.2. Installation needs network access; default classroom execution needs
  neither cloud credentials nor quantum hardware.
- The demonstrated host is Ubuntu 26.04.1 LTS x86_64. R1 established a fresh
  application environment using CPython 3.12.15; R5 reused it for the full
  required checks. Neither is a new operating-system/Python-installation test.
- R5 passed **160 tests, eight required notebooks, 50 nonempty code cells,
  and 16 PNGs**, with three figures each for HHL/Shor. This Markdown-only turn
  carries those results forward; it does not claim a new runtime execution.
- The notebook inventory is six course files (`00_setup_preflight.ipynb`
  through `05_shor.ipynb`) plus the two root `notebooks/` smoke files. All are
  required by validation, even when live classroom discussion uses a subset.
- R2 observed JupyterLab 4.6.4 in Chrome: named-kernel selection, restart/run-all,
  figure inspection, save, shutdown/relaunch, and reruns. Exact Chrome version
  remains unverified. Native VS Code/Cursor UI is untested.
- Windows x64 and macOS ARM64/Intel remain untested; their prepared procedures
  and package markers are not native execution evidence. Windows ARM64 and
  32-bit Python remain outside the stated target. No classroom alternative
  has been agreed merely because it could be offered.
- Grover, QFT, QPE, exact-spectrum HHL, and compiled full-domain N=15 Shor retain
  their existing contracts. No source, notebook, test, dependency, or supported
  input changes accompany these documents.

## Literal student-command verification still needed

The student guide keeps the ordinary in-folder `.venv` and
`ipykernel install --sys-prefix` route from existing setup documentation.
R2 instead used a sibling R1 environment and a separately located named
kernelspec, registered with `--user` under an isolated `JUPYTER_DATA_DIR`, to
preserve the frozen environment. The guide states that its exact fresh-folder
command sequence has not yet had a complete walkthrough. R2 validates observed
Jupyter behavior, not every literal command or conventional environment path
in this new draft. Syntax checking cannot close that distinction.

**Next executable check:** export an identified committed snapshot to a separate
local working copy, then follow the new student guide in order on the accessible
Ubuntu host with a new CPython 3.12 environment. Keep existing environments,
R1/R2 staging, source checkouts, and evidence intact. Use the ordinary named
kernel registration in that new environment; actually launch/select/restart/
run/inspect/save/shut down/reopen through available browser UI. Record the guide
hash, commands, interpreter/kernel paths, versions, saved counts/figures, observed
UI actions, errors, and any scoped documentation repair. Run the full strict
validator there. Do not manufacture an available download: this would validate
an internal source copy, leaving actual package extraction/download to R7/R8.

That check is recommended for a later authorized task and was **not executed**
during this Markdown preparation. No new environment, package installation,
kernel registration, or UI session was created here.

## Remaining decisions and inputs

These are unresolved facts or choices, not approvals inferred from the drafts.
The user has already asked the instructor; a reply remains pending, and no
additional outreach is part of this task.

1. **Teaching arrangement:** actual dates, number and length of meetings,
   deadline, presenter responsibility, and in-class versus outside-class topic
   coverage. The three 50-minute cores/75-minute routes remain proposals.
2. **Learners and delivery:** Python/Jupyter/quantum preparation, hands-on
   versus demonstration format, access needs, room/display, personal versus
   managed computers, and required native platforms or an agreed alternative.
3. **Assessment and solutions:** whether exercises are graded/submitted,
   collaboration expectations, and when solutions may be available. Keeping
   this instructor guide separate does not make the current notebooks an
   answer-free assessment: they already contain calculations, assertions,
   expected outcomes, and runnable reference implementations. Do not silently
   remove tests or create assessed variants to hide those facts.
4. **Mathematics and pacing:** requested notes/notation/examples, acceptance
   of the stated toy scopes, and a real presenter rehearsal with segment times.
   Fast machine execution is not observed teaching or learner-completion time.
5. **Document and package freeze:** confirm the final code/tag/asset identity,
   folder layout, document titles/editions, distribution scope, author/attribution
   metadata, and which links are live versus explicitly planned. Complete the
   literal student-command check and resolve any resulting text changes.

For final classroom editions, resolve the relevant decisions and support claims
before treating the documents as final. A separately requested review-draft
handoff may retain explicit provisional assumptions; it must not imply those
decisions or missing platform/rehearsal checks are complete. This turn authorizes
neither a new PDF nor a package.

## Later GPT Pro document handoff

All source files and both new Markdown companions are locally accessible.
No new reviewer-produced files have been received, and no other chat is assumed
to see these local edits. At the next sync state the exact snapshot and which
attachments were actually transferred. Filename cards, screenshots, or private
sandbox links alone do not establish accessible returned bytes.

Prepare the evidence and exact prompt before recommending that sync. Under the
existing [workflow](WORKFLOW.md), the later technical/document-review transfer
uses one standalone runnable ZIP copied to the Ubuntu desktop, with its prompt
separately in chat. Such a review ZIP is distinct from a final student package.
Include the needed source, tests, notebooks, dependencies, license, setup,
the two audience-separated document inputs, and concise validation evidence.
Exclude prompts, policy/chat files (including this coordination record), unrelated
history, duplicate exports, caches, credentials, environments, and generated
notebook outputs. Verify the extracted bundle and its manifest before transfer.
Nothing is packaged or copied to the desktop in this turn.

The document request should state the precise draft/final purpose and open
decisions. ChatGPT authors/renders/visually reviews/OCR-checks the PDFs and
returns downloadable bytes with exact edition, base revision, relative paths,
page counts, metadata/link inventory, sizes, and full-file SHA-256 receipts.
If it edits the Markdown companions, request those actual changed files in a
downloadable return ZIP or patch as well. Do not invent receipt counts before
the new documents exist or reuse Grover's page/link counts for them.

Once the returned files are actually available locally, verify delivered hashes
including provenance, metadata, links, placement, and Markdown correspondence.
Keep student PDFs under `handouts/` and instructor PDFs under `instructor/`.
Do not locally regenerate, optimize, or strip supplied PDF bytes. A corrected
receipt or corrected delivered file must resolve any mismatch before independent
review/publication claims. Avoid a guide containing the checksum of the ZIP
that contains that guide. Published links and final package bytes require their
own later verification.

## This turn's checks and boundary

Local checks cover Markdown lint, relative file links, command syntax, notebook/
contract/count/pin consistency, student/instructor separation, Git scope, and
preservation. They do not execute the new setup sequence or certify rendered
PDF layout, OCR, URL availability, native platforms, or human pacing.

**Passed:** all 365 local file links across tracked Markdown/notebook prose,
five Bash block syntax checks and two inline Python command parses, the source-
based notebook/count/pin checks, assistant content review, and the configured
pre-commit hooks (Ruff, yamllint, markdownlint). All 114 unchanged candidate
files retain their bytes/modes; all 51 earlier R5 evidence files remain intact.
Preservation also checks both prior checkouts/indexes, the older recovery
materials/assets, frozen R1 source, and existing environment identity and
distribution metadata. It does not hash every installed code/cache/OS byte.

Evidence is retained under the candidate's ignored
`artifacts/r6-markdown-2026-10-31/`, including the pre-edit source/R5-evidence
hashes, checks, preservation receipts, and final commit/clean-state receipt.
All original R5 evidence remains unchanged. Runtime checks are deliberately
not repeated solely for prose edits; their last complete execution remains R5.

**GPT Pro sync: not needed for this provisional Markdown step.** The next
recommendation is the literal Ubuntu guide walkthrough above; teaching feedback
and unavailable-platform/human-rehearsal gates remain open in parallel.
