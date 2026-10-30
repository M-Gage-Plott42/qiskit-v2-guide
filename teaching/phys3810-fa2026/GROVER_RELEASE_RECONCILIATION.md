# Published Grover audit reconciliation

October 30, 2026. An additional independent GPT Pro audit was received for
the published Grover rc1 snapshot. This turn reconciles planning, documentation,
and supplied PDF files only. It does not begin Git integration or QPE work.
The subsequent same-day receipt correction closes the initial PDF discrepancy;
see the dated follow-up below and the [instructor review plan](INSTRUCTOR_REVIEW_PLAN.md).

## Reviewed snapshot and execution evidence

The review identifies [PR #112](https://github.com/M-Gage-Plott42/qiskit-v2-guide/pull/112),
merged commit `3894391f2026d4fd9351b346b44b5eda453a17da`, and the
[Grover prerelease](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-grover-v0.1.0-rc1).
The reviewed ZIP has SHA-256
`c46d8f2ac837f2742a99384cee1bc637478b4387909a4c399e4599655b11e686`.
The reviewer reports exact correspondence with the published assets and 21
canonical source files; the other four files are three adapted orientation
documents and the instructional setup PDF.

**Reviewer-reported execution:** dependency consistency, 50 tests, and all four
required notebooks passed on Linux, CPython 3.12.14, Qiskit 2.6.1, and Aer
0.17.2. The review reused the pinned environment; it was not a fresh install.
The editable-target/legend regressions passed, closing G1 independently.
No Grover implementation blocker remains in the received review.

**Observed remote evidence:** the review checked all nine required PR checks,
the [PR classroom run](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/runs/40984800543),
and the [merged-commit classroom run](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/runs/40985140436).
Both classroom runs used Ubuntu x64/CPython 3.12.15 and passed 50 tests/four
notebooks. Successful artifact upload was observed. These are prior executions,
also recorded during publication; no workflow was rerun for this reconciliation.
PR #112's merged state and commit were rechecked through GitHub on October 30.

Native Windows/macOS, interactive notebook/editor setup, hardware/GPU, live
classroom timing, and deliberate remote failure-path upload remain unvalidated.
The supplied review did not inspect local QFT work. Its recommendation to begin
QFT is superseded by existing QFT evidence in the preserved development checkout: 64 tests
and five notebooks passed before this turn. QPE remains the next implementation.

## Findings and disposition

- **Grover repairs: closed.** The independent 50-test result now supplements
  the earlier local correction evidence; historical review records are retained.
- **Moved environment advice: confirmed and corrected in Markdown.** Recreate
  `.venv` at the destination, reinstall pinned requirements, then register the
  kernel. Re-registration alone is insufficient. This follows the
  [Python venv documentation](https://docs.python.org/3.12/library/venv.html).
- **Windows install-manager command: adopted.** Use `pymanager install 3.12`
  to avoid ambiguity with the older `py` launcher, consistent with
  [Python's Windows documentation](https://docs.python.org/3/using/windows.html).
  This documentation check is not native Windows execution evidence.
- **Repository PDF placement: prepared locally, not committed.** The received
  student guide is under `handouts/`; the instructor guide is under `instructor/`.
  Landing/setup pages link the student draft. Both copies preserve the received
  bytes and their Downloads originals. Tracking and clean-checkout acceptance
  remain pending the later Git integration step.
- **PDF provenance: initially unresolved, now closed.** Both received files
  differed from the initial handoff's hashes. Visible authorship, title/author metadata, version labels,
  commands, five rendered pages, 17 HTTPS link annotations, and page bounds
  passed local inspection. Those checks alone did not establish identity with
  the reviewer's hashed files. The later corrected delivery receipt resolves
  that distinction; see the [exact receipt and cause](handouts/README.md).
- **PDF ownership: adopted.** ChatGPT authors, renders, visually reviews,
  OCR-checks, and supplies PDFs. Codex verifies and integrates supplied bytes,
  maintains Markdown companions, and handles authorized packaging/publication.
  The existing renderer is a utility, not a replacement for supplied editions.
- **Distribution: deferred.** Preserve the rc1 tag, ZIP, and original assets.
  With provenance now resolved, prepare a documentation change and distinct
  v0.2 assets for a separately authorized publication. A revised ZIP needs a
  new candidate version and its matching ChatGPT-supplied PDF.

## Initial documentation validation

The local inspection used Linux x86_64, CPython 3.12.15, pypdf 6.21.4,
pdfplumber 0.11.10, and Poppler. `pdftotext -layout`,
`pdftoppm -scale-to 1600 -png`, and Python PDF/hash/link/boundary checks inspected
the actual received files. Local detail is retained in ignored
`artifacts/grover-audit-2026-10-30/`.

- **Passed:** `npx --yes markdownlint-cli2@0.20.0` over the 15 changed Markdown
  files, 82 relative documentation links, whitespace checks, and `git diff --check`.
- **Passed:** both repository PDF copies equal their received Downloads files;
  rendered page/content/metadata/link/boundary checks passed as detailed above.
- **Initially failed:** both PDF identities against the original handoff's
  expected SHA-256 values. The later corrected receipt closes the discrepancy;
  the files still do not equal the superseded pre-delivery hashes.
- **Passed:** HEAD and the staged binary-diff hash match the turn's starting
  state. Only 15 Markdown files and the two PDF copies changed; source,
  notebooks, tests, dependencies, and workflows were preserved byte for byte.

OCR was not rerun by Codex. Application tests and notebooks were deliberately
not rerun for this documentation-only turn; no new algorithm pass is claimed.

## October 30 delivery receipt correction and instructor packet audit

The received correction identifies the full delivered hashes as authoritative.
Local checks reproduced both full-file hashes and sizes, and both old hashes
using the original prefixes. Each file contains 24,961 additional bytes with
C2PA provenance. The reviewer's independent comparison reports identical text,
metadata, links, and all five rendered pages at 150 dpi. Codex did not repeat
that rendering comparison or validate C2PA signatures. No PDF bytes were changed.
The duplicate-file hypothesis did not resolve the mismatch: the remaining
Downloads copies already matched the repository files before this correction.

The supplemental packet recommendation is accepted with updated wording:
QFT is already locally validated; the 50/75-minute pacing is proposed; use the
v0.2 attachment instead of the older setup guide embedded in the unchanged ZIP.
The follow-up's generic assertion that hashes were unchanged did not itself
resolve identity; the subsequently supplied exact corrected receipt did.

An anonymous download and integrity check reproduced the original 25-file ZIP
and its recorded SHA-256. The release still has its three original assets and
tag target `3894391f2026d4fd9351b346b44b5eda453a17da`. No new code execution,
publication, repository commit, or external message occurred during this audit.

**Recommended next action:** the user sends the two verified v0.2 PDF review
drafts and existing rc1 ZIP link for instructor feedback. The
[instructor review plan](INSTRUCTOR_REVIEW_PLAN.md) records the questions and
scope; the email draft/private correspondence stays outside public docs.
Then follow [the Git integration plan](GIT_INTEGRATION_PLAN.md) before QPE in
a later implementation turn. No manual user audit is needed.

**GPT Pro sync: not needed now.** The delivered-file receipt issue is closed.
The next substantive mathematical checkpoint remains after QFT/QPE and before
HHL/Shor. Later Git integration and implementation were not started here.
