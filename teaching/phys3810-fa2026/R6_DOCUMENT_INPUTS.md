# R6 provisional document inputs and handoff readiness

Prepared October 31, 2026 from candidate `d491b3b`; subsequently updated with
[the student-guide walkthrough](R6_GUIDE_WALKTHROUGH_VALIDATION.md) of committed
source `7b8a8e2ed74bbcd7ceea27cd377fd73802d4927a`. **The Ubuntu setup/UI path
passed; the returned review-draft PDFs are now verified and integrated.** See
[the reconciliation](R6_DOCUMENT_REVIEW_RECONCILIATION.md) for the received ZIP,
exact receipts, companion mapping, and P3-01 clarification. No local PDF authoring,
student publication, or external message occurred. Final classroom approval
remains open under [the readiness plan](RELEASE_READINESS_PLAN.md).

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
  and 16 PNGs**, with three figures each for HHL/Shor. The original Markdown
  preparation carried those results forward. The later R6 walkthrough separately
  installed fresh dependencies and reproduced the full validator result.
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

## Literal student-command walkthrough — passed

The [walkthrough receipt](R6_GUIDE_WALKTHROUGH_VALIDATION.md) records the tested
source/guide hashes, fresh in-folder `.venv`, unchanged dependency installation,
ordinary `ipykernel install --sys-prefix` registration, and actual JupyterLab
launch/select/restart/run/inspect/save/shutdown/reopen actions. All eight UI
notebooks completed with 50 code cells and 16 inspected figures. Preflight and
Shor were cleared, restarted, run, and saved again after reopening. Both server
sessions stopped and the task tabs closed. No setup-command repair was needed.

This is separate from R2's historical preservation-specific external kernelspec
and sibling environment. The new run used task-local Jupyter/IPython/cache
settings, authenticated loopback, and manual opening of the printed browser URL.
Those isolation choices preserve existing settings; they do not certify arbitrary
user configuration, automatic browser opening, native editor UI, or another OS.
Python 3.12.15 already existed on the host. An internal committed-source export
was used, so no unpublished download or sealed package extraction is certified.

The student guide now states this result. Its executable Bash/Python blocks
remain identical to the tested draft; the test receipt retains the exact earlier
whole-file hash. R1/R2 source, staging, and environments remain preserved.
If a later reviewer changes setup commands, rerun the affected route and record
its new guide/source identity before claiming the changed instructions passed.

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
   metadata, and which links are live versus explicitly planned. Keep the
   completed Linux walkthrough linked to unchanged commands and recheck any
   instruction changes introduced during document review.

For final classroom editions, resolve the relevant decisions and support claims
before treating the documents as final. A separately requested review-draft
handoff may retain explicit provisional assumptions; it must not imply those
decisions or missing platform/rehearsal checks are complete. The completed walkthrough did not authorize new deliverables by itself. The
subsequent explicit handoff task authorizes this review ZIP and desktop copy,
not local PDF generation, student publication, or outreach.

## GPT Pro document handoff — return received and reconciled

The attached report and all six members of the Downloads return ZIP are locally
accessible, including both PDFs, two revised companions, export-based patch,
and machine-readable receipt. The report identifies the exact outgoing archive
and source. Reviewer raw execution logs and OCR/render artifacts are referenced
by receipt hashes but were not delivered; their execution remains attributed
to the reviewer. Filename cards, screenshots, or private sandbox links alone
would not establish file access, but this integration uses verified local bytes.

Prepare the evidence and exact prompt before recommending that sync. Under the
existing [workflow](WORKFLOW.md), the later technical/document-review transfer
uses one standalone runnable ZIP copied to the Ubuntu desktop, with its prompt
separately in chat. Such a review ZIP is distinct from a final student package.
Include the needed source, tests, notebooks, dependencies, license, setup,
the two audience-separated document inputs, and concise validation evidence.
Exclude prompts, policy/chat files (including this coordination record), unrelated
history, duplicate exports, caches, credentials, environments, and generated
notebook outputs. Verify the extracted bundle and its manifest before transfer.
The [handoff receipt](R6_DOCUMENT_REVIEW_HANDOFF.md) now identifies the verified
50-file desktop ZIP frozen at `c63381a`, its manifest/adaptations, and extracted
160/eight/50/16 result in the reused R6 environment. The exact prompt is supplied
separately in chat. That outgoing ZIP includes no PDF and remains unchanged.
The subsequent document-only return contains the new supplied PDFs. This coordination record and the
prompt are excluded; the included root README and concise evidence supply
necessary context without exporting policy/chat history.

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

## Preparation checks and current boundary

The original Markdown preparation checked lint, links, command syntax,
notebook/contract/count/pin consistency, audience separation, Git scope, and
preservation. It did not execute the setup sequence. The later walkthrough adds
actual fresh-install/validator/UI evidence in its separate receipt. Neither
step certifies rendered PDF layout, OCR, future URL availability, unavailable
native platforms, or human pacing.

**Passed at the original Markdown checkpoint:** all 365 local file links across tracked Markdown/notebook prose,
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
All original R5 evidence remains unchanged. The later walkthrough evidence is
under `artifacts/r6-walkthrough-2026-10-31/`; its fresh runtime run is distinct
from the earlier Markdown-only checks.

**GPT Pro sync: not needed immediately.** The actual report and returned files
are reconciled, with unchanged PDF bytes and visible Markdown/PDF correspondence.
Only hidden local lint annotations were added to the companions. Removed
packet-only links and the remaining literal evidence reference are mapped in
the reconciliation. P3-01 qualifies phase-fraction decoding in the next authored
instructor edition before final classroom distribution; the current reading
note is in [the instructor index](instructor/README.md). Native/editor, teaching,
and human-pacing gates remain open. The [R7 local preview](R7_PREVIEW_VALIDATION.md)
is now built and verified with unchanged student PDF bytes and instructor
material excluded. Next prepare a read-only/local R8 readiness proposal; no
manual code audit, publication, or external message is part of that proposal.
