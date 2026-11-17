# Expanded recording route reconciliation

November 16, 2026. The received audit of merged source
`727cb98c468bdd338c8fabc3b453e17738d1fce7` establishes the current sequence:
15–20 minutes of setup, QRNG, Bell, QFT, QPE, then HHL. Grover and compiled
N=15 Shor remain optional. One prerecorded class is presented by Gage Plott,
with zero Python assumed, laptop follow-along, and nothing assigned, graded,
evaluated, or submitted. Duration is flexible and Canvas delivery is settled.
The Ubuntu recording test is completed operator-reported evidence; ordinary
framing/audio/final-file checks remain part of recording, not another pilot gate.

## Received material and provenance

The actual local packet is
`PHYS3810_Recording_Packet_2026-11-16_727cb98.zip`, 210,396 bytes, SHA-256
`bfd6fcd7f444a94a9e4ed5e8e9d9ee5b96026644c085f1714b821facd25a3ce7`.
Its receipt identifies the source tree
`db437f6b4c12c1df2d41747eda2629919319ad5b`, matching the local merge. The
packet contains a proposed patch, two PDF/Markdown guide pairs, an informational
email draft, and review evidence. It is a coordination packet, not a complete
student runtime. The raw correspondence/image referenced by the reviewer is
not independently accessible here; current scope follows the supplied audit
and the user's instruction to reconcile it.

The ten-file patch is 50,485 bytes, SHA-256
`d93d7c6cd6aaa76af1fa01b44255e59524fb6e4152205ab6250033b86d48095d`.
It applied cleanly against the exact base. All ten before/after file sizes and
hashes match the supplied patch summary. Forty-five complete code-cell JSON
objects in six touched notebooks, all stable cell IDs, outputs/counts, and
mathematical spans are preserved. All twelve quickstart terminal commands are
unchanged. All seven active intro/reference notebook kernel specifications use
`phys3810-intro` / **Python (PHYS 3810 Intro)**; each notebook retains its own
session. Notebook schema and scoped lint checks passed.

Source-specific raw receipts, returned probe sources, and coordination text
remain under the ignored `artifacts/expanded-recording-route-2026-11-16/`
directory. No private recording or derived media is retained or packaged. The
user-requested deletion of that media remains in effect.

## Finding disposition

- **R1, current route:** the supplied patch updates the entrances, recording
  notes, and notebook welcome/wrap-up text. Additional narrow updates align
  current course/status/workflow summaries and historical-route redirects.
  Dated historical evidence and previous document bodies are preserved.
- **R2, kernel naming:** the active intro/reference notebook instructions and
  metadata use the existing registered Intro kernel. No second environment or
  numerical implementation is introduced; interpreter-path checks remain.
- **R3, exporter description and content:** the existing exporter is
  aligned to five demonstrated notebooks and thirteen total notebooks, with
  current Canvas delivery wording and the exact student guide. Served-root
  navigation and strict execution gates remain required.
- **R4, distribution identity:** the matching new kit receives its own name,
  source/manifest identity, and receipt. The older public rc1 release is not
  represented as containing the new recording route. No existing release or
  sealed archive is overwritten.

There is no requested sixth algorithm. The established QPE example addresses
the phase-estimation topic. Numerical implementations, supported families,
dependency pins, workflow names, and mathematical contracts remain unchanged.
The documentation changes preserve QFT's positive Fourier convention, canonical
QPE count ordering, and HHL's conditional solution-state interpretation.

## Review evidence kept separate

The reviewer reports a reused Debian 13 environment with existing CPython
3.12.14: **218 of 224 tests passed; six kernel-dependent tests failed**. All
thirteen notebook launches were attempted, with none completing because of
the local interface/libzmq startup restriction. That is a failed local full
validator, not a pass or a reason to weaken any gate.

Separately, the reviewer inspected the successful
[merged-head Ubuntu workflow](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/runs/43984477277)
and downloaded its artifact. It reports CPython 3.12.16, a fresh hosted
dependency installation, **224 tests / 13 fresh-kernel notebooks / 85 cells /
32 PNGs**, no errors or missing execution counts, and matching cell sources.
The workflow/job success and artifact metadata were also retrieved locally;
the artifact identifies the exact merge and SHA-256
`dceb40125eed24fd5325f48d2f6eb6f95e15710c529bef802da30b99725033e7`.
This is hosted CI evidence, not a fresh student-desktop or native-platform pass.

The returned report includes independent numerical probes of the bounded
Grover/QFT/QPE/HHL/Shor implementations and direct intro/edit-sequence checks.
It reports 12 recording scenarios and 68 actual QFT/QPE/HHL cell invocations.
These direct mathematical/cell checks remain attributed to the reviewer; they
are not additional local Jupyter-kernel runs. No blocking mathematical defect
was reported. New integration acceptance below is measured separately.

## Supplied guides

The exact student PDF/Markdown pair belongs under
`handouts/recording-v0.2/`; the exact recording pair belongs under
`instructor/recording-v0.2/`. Their original filenames and full bytes are
preserved. Version-specific Markdown lint settings accommodate the supplied
page-based H1 headings only; other rules and existing files retain their checks.
The original delivery receipt is preserved locally, with a concise public
integration receipt recording document identities and placement.

Local document verification passed all 23 receipt-listed entries in the
24-member delivered ZIP. Both PDFs have four pages; all eight pages were
rendered, visually inspected, and OCR-checked. All synchronized source tokens
are present; twelve student and ten presenter terminal commands match exactly.
PDF Info/XMP titles, Gage Plott author metadata, XMP hashes, and all twelve
annotations match the receipt. Eight distinct official reference destinations
were checked. OCR recall was 99.62% for the recording guide and 99.39% for the
student guide; glyph/number differences were resolved against text and images.
These new PDFs contain no C2PA marker; complete delivered bytes and Info/XMP
metadata are preserved without a cryptographic-provenance claim.

The [public receipt index](RECORDING_GUIDES_v0.2_RECEIPT.json) gives exact
repository paths, sizes, and hashes. The supplied page-heading Markdown
required MD025-only exceptions in the two edition folders. Scoped negative
controls confirmed other rules still apply there and MD025 still applies
outside those folders. No supplied document text or PDF bytes were rewritten.

The student guide is an advance copy for Rick. The four-page recording guide
is for Gage to print single-sided. The finished video, matching complete kit,
and student guide are the Canvas delivery set; presenter and coordination
files remain separate. No email or print action is performed or assumed here.

## Integration validation and delivery

**Source acceptance passed: 227 tests / 13 fresh-kernel notebooks / 85 nonempty
code cells / 32 PNGs.** The three additional tests cover Canvas package route,
student-guide identity, and exclusion behavior. All required cells executed
without error; sources retain empty outputs/null counts. Numerical source,
every existing notebook code-cell object, pins, mathematical contracts, strict
validator, and workflows remain unchanged. Local entry-point links and a
Markdown Preview tip were added after the exact supplied-patch verification;
these are disclosed integration additions, not edits to the supplied patch.

The source environment was **reused**: Ubuntu 26.04.1 LTS x86_64, Linux
7.0.0-43-generic/glibc 2.43, existing CPython 3.12.15. Installed versions:
Qiskit 2.6.1, Aer 0.18.2, JupyterLab 4.6.5, ipykernel 7.4.0, NumPy 2.5.4,
Matplotlib 3.11.2, pip 26.2.2. The following gates passed from the repository
root with the selected interpreter; Ruff/pre-commit used the separate reused
maintainer-tool environment (Ruff 0.15.22, pre-commit 4.7.0):

```bash
python scripts/validate_classroom.py --profile all
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh artifacts/expanded-recording-route-2026-11-16/smoke
pre-commit run --all-files
```

The validator includes pip consistency and the full unit suite; no immediate
duplicate unittest discovery was run. A concurrent early targeted package-test
attempt failed while the new document paths were being moved; its log is
preserved, and the final-path targeted run passed all thirty package cases.
That transient fixture-path failure is not relabeled as a pass or a runtime
defect. Source and document evidence is retained in the ignored task directory.

Exact extracted-package validation is a separate gate for the new kit; its
receipt will record environment freshness, hashes, and import paths. The prior
224/13/85/32 baseline is not relabeled as a new execution. No new broad algorithm review is required for passing scoped
documentation/kernel/export alignment. This turn authorizes commit and push;
it does not request a new release, merge, external message, or hardware job.
