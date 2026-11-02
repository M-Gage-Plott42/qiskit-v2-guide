# Focused guided-route review reconciliation

November 2, 2026. The independent review accepts the computational examples
and strict validator, but identifies a required beginner instruction repair
before student follow-along. This record separates the unchanged reviewed kit,
new reviewer execution, local reproductions, and corrected packet evidence.

## Actual access and reviewed identity

The returned review text is accessible. The reviewer explicitly changed no
files; no returned patch or replacement ZIP is needed. The retained Ubuntu
desktop archive is readable and its exact bytes were verified locally:

- `PHYS3810-Guided-Review-v0.1-e4fea10e5f28.zip`, 167,563 bytes.
- SHA-256 `fac5fff2122ae1da5a21a7df8ff0d7db13f4ae6a77c81b6ffc7af28806f08c6a`.
- Source `e4fea10e5f280d0d5f79f53739321a1e608e7bec`, tree
  `fab413a48f3eb39b68f059afd7184f3f3417a7da`.
- Manifest SHA-256 `e3fc24cf828a2f88c957285d13de9005b8c44bba79d99034e69c3717fe101d06`.
- All 54 payload sizes/hashes and archive integrity match; the old kit is
  preserved, not relabeled as the correction.

The local starting head was `d94366057881e5997f9a060cea0af26c9d26f782`; its
change after the kit source is a delivery/status receipt, not algorithm work.
Private reviewer sandbox links and probe scripts are not locally available.
The reproductions below are equivalent local actual-cell cases, not claims
of running an inaccessible reviewer script.

## Newly reported independent execution

The reviewer reports a fresh application venv on an existing Ubuntu 24.04.3 /
CPython 3.12.14 host with unchanged requirements and constraints. The extracted
kit passed **197 tests, eleven fresh-kernel notebooks, 74 code cells, 27 PNGs**,
dependency consistency, all required cells, and 44 relative links. All eleven
guided figures were visually inspected. All supplied payloads remained unchanged.

That fresh install is separate from the earlier local reused-3.12.15 results.
The reviewer did not repeat document rendering/OCR, interactive Jupyter/native
editor operation, Windows/macOS, GPU/Runtime/hardware, or human pacing. Earlier
evidence retains those boundaries. The review found no unresolved QFT/QPE sign,
bit-order, eigenstate, scope, or strict execution-policy defect.

## R1: execute the edited parameter cell first

**Reproduced and repaired.** Several notebook and presenter directions omitted
execution of the edited parameter cell, telling beginners to run only downstream
cells. Editing document text leaves the running namespace unchanged. Existing
assertions can therefore pass against an internally consistent old result.

Local direct execution of the actual cells reproduced all four negative controls,
then verified the corrected sequence:

- Grover target `01` to `10`: downstream-only retains `01` in all 512 samples;
  executing the parameter cell first produces `10` in all 512 samples.
- Grover iterations 1 to 2: downstream-only retains marked probability 1;
  parameter-first execution gives 1/4.
- QFT basis `01` to `10`: downstream-only recovers index 1; parameter-first
  execution recovers index 2 and updates the complex-pattern caption.
- QPE 3/8 to 1/8: downstream-only retains `011` and 0.375; parameter-first
  execution gives `001` and 0.125 with updated expected labels and captions.

The corrected run-sheet positions are **4, 6, 8, 10, 12** for Grover;
**4, 6, 8, 10** for QFT; **12, 14, 15, 17** for QPE. The parameter step is
explicit in every affected explanation. Visible notebook section titles and
first-code-line cues make those positions easier to find. The quickstart's
already-correct parameter-first rule remains intact. Notebook code is unchanged.
The final consistency scan also corrected the same ambiguity in Day 1's closing
note and the current setup/course summaries. Those entry points now agree with
the detailed sequences. Day 1 was rerun through the strict engine afterward;
its code cells and all mathematical behavior remain unchanged.

Four actual-cell regressions preserve pending edited code separately from the
running namespace, show the stale-result negative control, then verify the
corrected sequence and captions. They test behavior rather than searching for
a particular sentence. The original guided regressions remain intact.

Primary research used [Jupyter's code-execution and kernel-state documentation](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Running%20Code.html)
and [JupyterLab notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html).
These distinguish editing the document from executing code in the kernel.
The [nbclient reference](https://nbclient.readthedocs.io/en/latest/reference/nbclient.html)
also confirms the existing strict error controls; that execution policy is
preserved. No dependency upgrade follows from newer online documentation.

## Small follow-ups

- **O1, stopping point:** the phase notebook and run sheet now both stop after
  QFT/inverse recovery on the 50-minute route. A presenter-only default QPE
  demonstration is optional only when additional time is available.
- **O2, setup responsibility:** quickstart and the current handout index ask
  learners to confirm supported setup and assistance. They no longer promise
  an arrangement that the agenda still leaves open. Ubuntu evidence and
  untested-platform labels are unchanged.
- **O3, export receipt consistency:** the old exporter accepted a synthetic
  receipt with 16 PNGs although the all profile requires 27. The reviewed kit
  actually reported and produced 27, so its execution result remains valid.
  The correction derives the minimum from the selected profile's figure
  requirements and verifies the selected validator revision. Receipts claiming
  16 or 26 are rejected; a matching 27-figure receipt is accepted. This checks
  receipt consistency and does not replace execution or alter runtime policy.

## Validation and corrected delivery

Local evidence is retained under ignored
`artifacts/guided-review-reconciliation-2026-11-02/`. The corrected source must
pass the full all-profile validator, relevant lint, and refreshed affected
document rendering/OCR. Its newly identified v0.2 review ZIP must then pass a
separate isolated extraction with manifest/link/import/payload checks and the
full validator, with actual counts and environment reuse recorded.

**Source acceptance passed:** reused CPython 3.12.15 application environment,
unchanged Qiskit 2.6.1/Aer 0.17.2/JupyterLab 4.6.4 pins, Linux x86_64/glibc 2.43.
`python scripts/validate_classroom.py --profile all` passed **205 tests, eleven
fresh-kernel notebooks, 74 nonempty code cells, 27 PNGs, zero notebook errors**.
The eight new regressions are four R1 sequence cases and four exporter receipt/
revision cases; all prior 197 remain. Bash smoke passed separately. No fresh
application installation is claimed. Notebook code cells and the validator's
execution-policy bytes match the reviewed revision exactly.

**Focused checks passed:** fifteen actual-cell guided tests, twenty-four export
acceptance tests, Ruff/Markdown/YAML hooks including new files, whitespace, and
433 repository relative-link targets. The new figure guard was also checked
through direct CLI and isolated-file import; no Git-backed code execution is
used to discover historical profile requirements.

**Refreshed visual/OCR checks:** two affected Markdown documents and all three
freshly executed guided notebooks, including the final Day 1 clarification.
Recognition substitutions are checked against source/HTML/rendering. All 24 code cells
match the rendered HTML. Nine student terminal command lines matched OCR after
whitespace normalization; an instructor-command underscore substitution was
checked visually. No clipping, overlap, or remaining rendering defect was found.
Unchanged entrance and agenda source bytes match the previous snapshot;
their prior visual/OCR evidence carries forward, not a new rendering claim.
HTML/PNG rendering is neither new PDF production nor interactive UI testing.

Canonical algorithms, supported inputs, dependency pins, default eight-notebook
membership, reference notebooks, original PDFs/companions, frozen release
builders, published assets/tags, and the recovery stash remain preserved.
The kit still contains three guided plus eight reference notebooks; no new
PDF, GPU repair, dependency update, hardware job, or external human message is
part of this reconciliation. Current attribution remains **Gage Plott**, and
student/instructor prose stays free of internal model/coordination notes.

## Next action

Use the corrected packet for the walkthrough and await teaching feedback.
**GPT Pro sync: not needed again solely for these demonstrated repairs.**
No broad algorithm audit or new PDF round is needed. Reopen independent review
for material runtime/mathematical or execution-policy changes, or a concrete
unresolved defect. Dates/count, priorities, setup assistance, prior quantum
coverage, and final delivery remain instructor decisions; no manual code audit
is assigned to the user or instructor.
