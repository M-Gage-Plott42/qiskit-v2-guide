# Repository guidance

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing this repository. Keep
changes scoped, preserve existing work, and retain required workflow/job names,
checks, and the solo-maintainer contribution policy. Do not change repository
rulesets as part of instructional work.

## Source and notebook conventions

- Canonical reusable algorithm code belongs in `src/phys3810/`; mathematical
  tests belong in `tests/`. Grover, QFT, QPE, HHL, and the
  compiled N=15 Shor example are implemented there; retain their explicit bounds.
- Course notebooks belong in `teaching/phys3810-fa2026/notebooks/`. Import
  canonical implementations instead of maintaining separate notebook copies.
  Keep explanations, parameter choices, exercises, and short demonstrations in
  notebooks; comment non-obvious implementation steps in source.
- Use current SDK circuits and V2 primitives. Prefer `QFTGate`,
  `phase_estimation()`, and `grover_operator()` for reference comparisons.
  Do not add deprecated class wrappers or removed `qiskit.algorithms` HHL/Shor
  imports.
- Declare bit order, register roles, supported inputs, approximation choices,
  and random seeds. Commit notebooks without execution outputs or counts;
  write executed copies to ignored `artifacts/` for review.
- Default runs must be local and credential-free. IBM Runtime and GPU paths
  remain optional and excluded from classroom validation. Never submit jobs
  or contact IBM during offline tests; mock service construction in tests.

## Validation

Use the documented Python 3.12 classroom environment. From the repository root:

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

The Python validator is the cross-platform classroom entry point; the Bash
command retains the existing smoke workflow. Run each required notebook from a
fresh kernel, with the selected environment's interpreter, and fail on cell
errors. Printed output and stored notebook output are not proof of correctness.
Required nonempty code cells must all execute: reject `skip-execution`, force
errors to raise even with `raises-exception`, and check execution counts and
error outputs before reporting a pass. Preserve partial executed notebooks on
failure. Handle intentional exception demonstrations inside successful cells.

For algorithm milestones, use independent mathematical expectations in addition
to SDK comparisons, with explicit floating-point tolerances:

- QFT: compare the complete operator with the Fourier matrix, including sign
  convention and bit ordering.
- QPE: test asymmetric exact phases and a nonexact phase against the expected
  outcome distribution; avoid cases that conceal reversed bit order.
- Grover: verify oracle action on every basis state and amplification
  probabilities against the analytic expression.
- HHL: verify postselection probability, ancilla uncomputation, normalization,
  and relative sign against a classical linear solve on stated supported cases.
- Shor: verify reversible modular arithmetic, order recovery, and factor
  extraction independently, including unsuccessful or invalid cases.

Record commands, installed versions, platform, and outcomes. **Passed** means
the check ran successfully; **failed** means it ran and did not meet its
criterion; **skipped** means it was deliberately excluded with a reason;
**untested** means no execution evidence exists. Never relabel skips as passes.

## Claims and public artifacts

State toy-example restrictions and resource costs. Do not imply generality,
scalability, or quantum advantage unsupported by the implementation and evidence.
Do not put private correspondence, credentials, account identifiers, or student
data in public code, notebooks, documentation, outputs, or validation logs.

## PHYS 3810 collaboration and handoffs

**Current position, November 1, 2026:** the explicitly authorized full-course
preview is published at `phys3810-fa2026-v0.2.0-rc1`, source `f717aea`, after
normal PR #113 and all nine required checks. Published ZIP/checksum bytes were
verified anonymously. See [the publication receipt](teaching/phys3810-fa2026/PUBLIC_PREVIEW_RELEASE.md).
The reviewed PDFs remain unchanged prepublication references; current public
README/SETUP and a notice govern availability. No final classroom approval is
claimed, and P3-01/teaching/native/editor/pacing decisions remain open.
The user also explicitly requested clean Git state. The formerly dirty original
checkout is now clean main; its exact original work/index are recoverable from
verified stash `2705385616e21718a10b73765946e430597dc4bf` and both recovery records.
The accepted integration checkout remains a historical snapshot. Preserve that
recovery data; do not use old active-checkout equality checks to reject the
intentional fast-forward or discard/pop the recovery stash.
After final completion documentation is pushed/merged, **wait for Rick's reply,
a concrete defect, or a specific new request**. Do not repeat unchanged tests,
packages, PDF reviews, or readiness planning. This completed authorization does
not cover another release, external human messages, or hardware jobs.

- The assistant owns implementation, technical review, testing, repairs, and
  documentation. Do not assign manual code/diff review to the user.
- End each substantive turn with the outcome and validation status, one
  recommended next action, and `GPT Pro sync: due / recommended / not needed`
  with a reason. State any user input actually needed; otherwise say none.
- End every final response with a copyable fenced `text` block containing the
  recommended next instruction for the user to paste back into this Codex
  conversation. Put all explanation, validation, sync status, and input needs
  before that final block. Make the instruction concrete about scope and
  completion criteria; distinguish it from prompts intended for GPT Pro.
  Complete the currently authorized work before proposing the next turn;
  the closing prompt is not a reason to stop early or repeat an existing
  approval request. A planning prompt does not itself execute the proposed work.
- Continue authorized routine local work without repeated approval requests.
  Ask only for missing decisions or actions outside the authorized scope.
  Preserve the current local-only boundary: no push, PR, merge, publication,
  external messages, or IBM hardware jobs without applicable authorization.
- Keep [STATUS.md](teaching/phys3810-fa2026/STATUS.md) current. Follow the
  sequence and handoff protocol in [WORKFLOW.md](teaching/phys3810-fa2026/WORKFLOW.md).
  Prepare the evidence and exact review prompt before recommending a GPT Pro
  sync; do not ask the user to assemble or audit the evidence.
- For future GPT Pro handoffs, copy one standalone runnable ZIP to the Ubuntu
  desktop and put the review prompt in a copyable code block in the final chat
  response. Exclude prompt files, policy/chat documents, unrelated history,
  duplicate text exports, caches, credentials, and generated outputs from the
  ZIP. Include needed source, notebooks, dependencies, tests, setup instructions,
  license, and concise validation evidence; verify the extracted bundle.
- Treat GPT Pro feedback as review input: reproduce actionable findings, fix
  them, and record disposition and test evidence. Self-review is not an
  independent GPT Pro review, and a model opinion is not an executed test.
- ChatGPT authors, renders, visually reviews, OCR-checks, and supplies course
  PDFs. Integrate its supplied bytes; do not silently regenerate them with the
  local renderer. Verify hashes, metadata, links, and repository placement;
  retain synchronized Markdown companions. Record mismatches and obtain a
  corrected receipt or file before publishing the edition as independently
  reviewed. Student PDFs belong under the course `handouts/` directory;
  instructor PDFs belong separately under `instructor/`.
  Hash the exact delivered bytes, including appended provenance. Do not
  optimize, strip provenance from, or otherwise rewrite a supplied PDF.
- Keep document editions distinct from code releases. Preserve the original
  Grover rc1 tag, ZIP, and assets. A replacement standalone ZIP needs a new
  candidate version and its matching ChatGPT-supplied guide.
- Do not infer that another chat sees local files or that a sync has happened.
  Record the reviewed snapshot and actually received response. Keep private
  chat text out of public docs; retain only technical conclusions.
- At every sync, state which local files/attachments are actually accessible
  and which reviewer files are only referenced. A screenshot, filename card,
  private `sandbox:` link, or same-account login is not proof of file transfer.
  For an unchanged-snapshot review, a report identifying the ZIP/manifest and
  declaring no file changes is sufficient; no return ZIP is required. If GPT
  Pro creates/edits files, request a real downloadable ZIP or patch with base
  revision, relative paths, and hashes of the delivered bytes, then require
  those bytes to be attached or made locally available before integrating them.
  Never claim to have read or applied an inaccessible private-sandbox copy.

Milestone 1's independent review was received and its required correction was
demonstrated on October 29, 2026; see the
[reconciliation record](teaching/phys3810-fa2026/REVIEW_RECONCILIATION.md).
The Grover review was received and its exercise correction was demonstrated;
see [the reconciliation](teaching/phys3810-fa2026/GROVER_REVIEW_RECONCILIATION.md).
Review-draft setup/instructor PDFs may be prepared now; final classroom PDFs
still require platform validation and instructor feedback. An intentional
instructional PDF may accompany a standalone preview; this does not authorize
including generated notebook outputs or prompts in a review bundle.
The [Grover preview](teaching/phys3810-fa2026/PREVIEW_PLAN.md) is a separate,
identified source revision; keep QFT development out of that first preview.
The authorized Grover publication workflow is complete: PR #112 merged after
all required checks, and `phys3810-fa2026-grover-v0.1.0-rc1` is published from
`3894391f2026d4fd9351b346b44b5eda453a17da`. This does not authorize unrelated
releases, instructor messages, or hardware jobs.
QFT is locally validated in the development checkout; its
[evidence](teaching/phys3810-fa2026/QFT_VALIDATION.md) is separate from the
50-test Grover-only preview. QPE is now locally validated as well; see its
[contract](teaching/phys3810-fa2026/QPE_PLAN.md) and
[evidence](teaching/phys3810-fa2026/QPE_VALIDATION.md).
Local integration now carries the verified documentation/PDFs and QFT forward
from published main in separate commits. The original development checkout and
index remain intact; continue in the integration worktree and never reset the
original checkout as a cleanup shortcut.
An additional published-Grover audit was received on October 30, 2026; see the
[release reconciliation](teaching/phys3810-fa2026/GROVER_RELEASE_RECONCILIATION.md).
It independently reports 50 tests/four notebooks passing and closes the Grover
repairs. The v0.2 PDF discrepancy is closed: the corrected receipt identifies
the delivered files including appended C2PA provenance; full-file and original
prefix hashes were verified locally. Keep those existing PDFs unchanged.
The [instructor review plan](teaching/phys3810-fa2026/INSTRUCTOR_REVIEW_PLAN.md)
uses the two verified v0.2 guides plus the unchanged published rc1 ZIP. The user
reported sending the initial setup/Grover email on October 30; a reply is pending.
Only the student setup attachment is confirmed by the supplied screenshot, not
the entire recommended packet. Keep private correspondence out of public docs
and do not send follow-ups without explicit authorization.
The independent QFT/QPE review has been received and accepted: no blocking
defects, a fresh Linux CPython 3.12.14 install, and 92 tests/six notebooks passed.
Four optional follow-ups were reconciled locally; see the
[review disposition](teaching/phys3810-fa2026/QFT_QPE_REVIEW_RECONCILIATION.md).
The reconciled 97-test phase revision adds regression coverage and presentation/docstring
clarity without changing QFT/QPE computational logic. No new GPT Pro round is
needed solely for those evidenced updates. Keep the final response block for
the next instruction back to Codex. The QFT/QPE technical review bundle uses
version-matched Markdown setup and excludes the Grover-only PDF editions;
those reviewed PDF bytes remain unchanged in the repository. This review
snapshot does not replace the Grover rc1 ZIP or publish a new student release.
The [HHL contract](teaching/phys3810-fa2026/HHL_PLAN.md) is now implemented;
[validation](teaching/phys3810-fa2026/HHL_VALIDATION.md) records 129 tests and
seven fresh-kernel notebooks. All 97 phase-review regressions remain intact.
HHL uses exact three-bit eigenphases for bounded 2x2 positive Hermitian systems;
its raw success/failure amplitudes and both-branch count cleanup are tested.
The [Shor contract](teaching/phys3810-fa2026/SHOR_PLAN.md) is now implemented:
a compiled full-domain N=15 example with four residue qubits and a separate
order-finding builder. The existing QPE one/two-target contract is unchanged.
The independent HHL/Shor review has been received and accepted: the unchanged
158-test snapshot passed eight fresh-kernel notebooks in a reused Linux
CPython 3.12.14 environment. See the
[review reconciliation](teaching/phys3810-fa2026/HHL_SHOR_REVIEW_RECONCILIATION.md).
The two stale notebook availability statements are corrected; all three HHL/Shor
figures are now required, and Shor displays theoretical recovery probabilities.
The current local suite passes 160 tests/eight notebooks; all prior regressions
remain. Algorithm source and supported families are unchanged. Preserve the
reviewed archive as historical evidence rather than relabeling it as this revision.
No additional GPT Pro round is needed solely for these evidenced P3 follow-ups.
The [classroom-release readiness plan](teaching/phys3810-fa2026/RELEASE_READINESS_PLAN.md)
inventories the local commits and remaining gates. R1 passed on October 31:
a fresh isolated CPython 3.12.15 environment installed unchanged pins and ran
160 tests/eight notebooks/50 code cells/16 PNGs from source `9e73b82`. See
[the fresh-install evidence](teaching/phys3810-fa2026/R1_FRESH_LINUX_VALIDATION.md).
R2's Linux/Chrome JupyterLab path has also passed through actual UI execution,
figure inspection, shutdown/relaunch, and reruns; see
[interactive evidence](teaching/phys3810-fa2026/R2_INTERACTIVE_VALIDATION.md).
Native VS Code/Cursor UI remains untested because native app control is disabled;
exact Chrome version remains unverified after its internal version URL was blocked.
Do not infer those results from headless execution or bypass browser policy.
R3 host inventory/procedure preparation is complete; see
[native-platform procedures](teaching/phys3810-fa2026/R3_NATIVE_PLATFORM_VALIDATION.md).
Only Ubuntu is accessible, and the user confirmed no additional host. Windows
x64 and macOS ARM64/Intel remain untested; Linux evidence carries forward without
a redundant rerun. Do not provision infrastructure or simulate a native pass.
R4's provisional three-session run sheets and separate demonstration timings are
prepared; see [the presenter index](teaching/phys3810-fa2026/R4_PRESENTER_RUN_SHEETS.md)
and [timing evidence](teaching/phys3810-fa2026/R4_DEMONSTRATION_TIMINGS.md).
Three trials of all eight canonical notebooks and six derived cases passed
(42 fresh-kernel runs). Algorithm source, tests, pins, and notebooks are unchanged; the
160-test result carries forward, not a newly executed unit suite.
Keep proposed teaching minutes, headless machine seconds, actual UI evidence,
and human rehearsal distinct. R4's preparation is complete, but human pacing
remains untested and Rick's teaching decisions remain pending.
R5 protected local integration is complete; see
[the candidate evidence](teaching/phys3810-fa2026/R5_CANDIDATE_VALIDATION.md) and
[publication draft](teaching/phys3810-fa2026/CLASSROOM_PUBLICATION_DRAFT.md).
The October 31 fetch confirmed origin/main remains `3894391`; all 13 accepted
commits through `0570863` retain their IDs. Continue in the new durable
`artifacts/local-candidate-2026-10-31/worktree` on
`candidate/phys3810-fa2026-v0.2.0-rc1`, relative to the original repo. Preserve
both the original dirty checkout/index and the accepted integration checkout
at `0570863`. Required checks reran successfully with 160 tests/eight notebooks,
50 cells/16 PNGs; this reused R1's environment, not a fresh installation or UI run.
The candidate version/name is provisional and no tag/package exists. R6's
separate full-course student/instructor Markdown drafts are prepared; see
[the document input record](teaching/phys3810-fa2026/R6_DOCUMENT_INPUTS.md).
They are document v0.1 drafts for proposed code v0.2.0-rc1, distinct from the
unchanged Grover editions. The later
[student-guide walkthrough](teaching/phys3810-fa2026/R6_GUIDE_WALKTHROUGH_VALIDATION.md)
passed on Ubuntu with a fresh in-project `.venv` and ordinary `--sys-prefix`
kernel registration: 160 tests/eight notebooks/50 cells/16 PNGs, plus actual UI
execution of all eight notebooks and shutdown/reopen reruns. R1/R2 remain
preserved; this separate result closes the ordinary Linux guide-route gap without
relabeling R2's adapted test. Task-local settings and manual browser opening are
disclosed; native editor/Windows/macOS and human pacing remain untested. No guide
command repair was needed; only validation-status prose changed. The subsequent
[document-review handoff](teaching/phys3810-fa2026/R6_DOCUMENT_REVIEW_HANDOFF.md)
is now prepared: a single desktop ZIP frozen at `c63381a`, 50 files/49 manifest
entries, all canonical runtime/notebook/student-guide bytes preserved, and a
separate chat prompt. Extracted verification passed 160 tests/eight notebooks/
50 cells/16 PNGs using the reused walkthrough environment. The document review
has now returned with an accessible six-file ZIP from Downloads; see
[the reconciliation](teaching/phys3810-fa2026/R6_DOCUMENT_REVIEW_RECONCILIATION.md).
The supplied four-page student and six-page instructor PDFs are integrated
unchanged with verified delivered hashes, metadata, links, and synchronized
Markdown. All six student fenced blocks are unchanged. Only nonrendering local
MD036 annotations were added to the companions; no command or visible text changed.
The reviewer reports a fresh Ubuntu CPython 3.12.14 run of 160 tests/eight
notebooks/50 cells/16 PNGs; that is separate from local execution evidence.
Accept these as provisional review drafts, not final classroom approval. P3-01
clarifies phase-register decoding before the next final instructor edition;
its [reading note](teaching/phys3810-fa2026/instructor/README.md) applies now
without altering supplied PDF bytes. No immediate new GPT Pro round is needed.
The [R7 builder and local preview](teaching/phys3810-fa2026/R7_PREVIEW_VALIDATION.md)
now pass packaging acceptance and extracted validation. The ZIP is frozen at
`135d5d0`, with 47 files/46 manifest entries/37 exact committed files, including
unchanged reviewed student PDF/Markdown bytes. Instructor documents are excluded;
worked notebooks/tests/contracts remain, so it is not an answer-free assessment.
The 160-test/eight-notebook/50-cell/16-PNG extracted run reused the R6 environment;
no new installation/UI/native-platform claim is made. Twenty actual builder
acceptance cases and reproducibility checks passed. Keep the old Grover builder
and all earlier archives unchanged. Next prepare only a read-only/local R8
readiness audit and publication proposal; no push/PR/merge/release authority is
inferred from this local package. P3-01 and teaching/platform/pacing gates stay open.
Returned packet-only clickable links were removed editorially; the remaining
literal evidence filename is mapped to repository records in the reconciliation.
Filename cards/private links alone still do not establish returned-file access.
Keep student instructions free of maintainer coordination and instructor answer
cues. Separate instructor files do not make the existing worked notebooks an
answer-free assessment. Teaching decisions, solution distribution, and actual
human pacing remain open; do not infer agreement from document preparation.
Editor and native-platform checks, final classroom documents, final package
freeze, and publication approval remain open.
Earlier local-only milestone records remain historical. The November 1
preview authorization above permits its PR/merge/release and recoverable Git
cleanup; it does not authorize unrelated releases, outreach, or hardware jobs.
Preserve the original work in its verified checkpoint/stash and retain rc1 assets.
