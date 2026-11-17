# Student support v0.3 reconciliation

November 16, 2026. The audit of merged `d669587` accepts the existing Canvas
kit and numerical behavior. The supplied student-support revision requires
a new kit because the included guide changes. The scope is simpler entrance
wording, practical help/contact information, exact document integration, and
the corresponding exporter edition paths/hashes. No algorithm, notebook code,
mathematical contract, dependency pin, or recording route changes.

## Received files and source identity

The actual Downloads packet is
`PHYS3810_Student_Support_Update_2026-11-16_d669587.zip`, **148,221 bytes**,
SHA-256 `01b51e81db8e684020c3d8690a8ea7e9da09226f1e7a7cb0d63fb959cb58f0e5`.
CRC, safe paths, the fifteen-member inventory, and all fourteen receipt-listed
file sizes/full hashes passed locally. The receipt identifies source
`d669587b0120ff6e684f07f6a405c23397ad46fb`, tree
`2d2d784e6014ebed5dde0371767bea4dd6b13a51`, matching the checkout base.

The earlier sealed kit remains
`PHYS3810-Canvas-Kit-v0.1-d998b69170ad.zip`, SHA-256
`64b44615825c915e57add92d111261a7f32534e01f6f4d73a2ae8fce35763a3b`.
Its source `d998b69` legitimately differs from the later status-only merge;
that alone is not a reason to rebuild. This update creates a distinct v0.2
package specifically to carry student guide v0.3.

Exact new files are indexed in the
[public integration receipt](handouts/STUDENT_SUPPORT_v0.3_RECEIPT.json):
student PDF/Markdown under `handouts/recording-v0.3/` and the presenter insert
under `instructor/support-v0.1/`. All old editions remain unchanged. The
original full receipt, audit, and coordination text are retained in ignored
`artifacts/student-support-v03-2026-11-16/`, not copied into student material.

## Document checks

The four-page student guide and one-page presenter insert were rendered and
all five pages visually inspected locally. Titles, Gage Plott author metadata,
PDF Info/XMP, XMP hashes, and all eight link annotations match the supplied
receipt. All used text fonts are embedded; an unused standard Helvetica
resource does not affect that finding. Every normalized Markdown source token
is present in extracted PDF text. All twelve student terminal commands match
the previous tested entrance exactly and remain in their original order.

Tesseract OCR recall was 99.61% for the student guide and 99.20% for the insert.
The small glyph/number differences were checked against source text and all
rendered pages; no visible clipping, overlap, or missing characters were found.
Complete PDF bytes and metadata are preserved, with no regeneration,
optimization, or cryptographic-provenance claim. The supplied student's
page-based H1 headings use a directory-scoped MD025 accommodation. Both exact
companions intentionally contain a plain email address; their edition folders
also disable MD034, which offers no email-only option in the pinned linter.
All other root rules remain inherited. No supplied bytes were changed to make
the address a link; the exporter still rejects unsupported URL schemes.

## Technical disposition

The entrance now explains terminal/notebook/cell/kernel/shot/seed in plain
language and follows the new help sequence for Python prerequisites, wrong
folders, installation failures, absent kernels, stale state, Markdown preview,
and moved environments. It gives the explicitly supplied public support
contact `gage-plott@utc.edu` as plain text. Numbered anchors, all twelve tested
commands, menu links, kernel name, parameter-first reruns, and Bell's optional
section 7 dependency are retained.

The existing exporter selects only the v0.3 student PDF/Markdown pair, with
both exact delivered hashes updated together, and uses kit version v0.2.
Generated links stay inside Jupyter's served `runtime/`. Instructor inserts,
old student editions, and coordination files remain excluded. A focused
regression checks real entrance/guide command agreement, the support wording,
plain-text contact, and edition selection; the old guide is explicitly rejected
as an extra payload. Strict execution and mathematical tests are unchanged.

## Evidence categories and communication status

The independent review's reused Debian 13/CPython 3.12.14 attempt **failed** its
full validator: 221 of 227 tests passed, six kernel-dependent tests failed, and
none of the thirteen notebook launches completed under a host transport
restriction. All thirty package cases passed. This is not a full local pass.

Separately, the reviewer inspected successful merged-head Ubuntu CI at
[workflow 43994820764](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/runs/43994820764)
and downloaded its executed artifact: 227 tests/thirteen fresh-kernel notebooks,
85 cells/32 PNGs, with matching cell sources and no error/missing-count outputs.
Earlier workstation source/extraction evidence remains separately recorded;
the new document/package acceptance below will be measured independently.

The received audit records an advance-copy email and a follow-up support promise
as already sent; the advance material was withheld from student distribution.
Only that necessary status is retained here. The referenced screenshots/private
email bodies were not independently received in this packet and are not
published. Printing was separately reported by the user. Final recording,
ordinary playback, and transfer of video/new kit/v0.3 guide to Rick for Canvas
remain future actions. No incoming reply or final delivery is inferred.

## Acceptance and handoff

**Source acceptance passed: 228 tests / 13 fresh-kernel notebooks / 85 nonempty
code cells / 32 PNGs.** Every required cell has an execution count and no error
output. The one added regression covers the actual entrance/v0.3 command and
contact agreement; mathematical test counts/coverage and notebook code remain
unchanged. Ruff, Bash smoke, and pre-commit also passed.

The source environment was **reused**, on Ubuntu 26.04.1 LTS x86_64,
Linux 7.0.0-43-generic/glibc 2.43, existing CPython 3.12.15. Versions include
Qiskit 2.6.1, Aer 0.18.2, JupyterLab 4.6.5, ipykernel 7.4.0, NumPy 2.5.4,
Matplotlib 3.11.2, and pip 26.2.2. Ruff 0.15.22/pre-commit 4.7.0 use the separate
reused maintainer environment. Commands:

```bash
python scripts/validate_classroom.py --profile all
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh artifacts/student-support-v03-2026-11-16/smoke
pre-commit run --all-files
```

The initial source gate ran but failed one stale package assertion that still
expected v0.1; that assertion now correctly requires v0.2. Its log and executed
notebooks are preserved. Initial Markdown lint also failed on the exact supplied
plain email addresses; narrowly scoped MD034 accommodations preserve those
immutable bytes. Negative controls confirmed other rules remain enforced inside
the edition folders and MD034 remains enforced elsewhere. The corrected gates
passed. No failure was relabeled as an earlier pass, and no duplicate unittest
discovery followed the validator. Exact new archive acceptance is separate.

## Exact replacement kit

**Exact extraction passed independently: 228 tests / 13 fresh-kernel notebooks /
85 nonempty code cells / 32 PNGs.** The new archive was extracted outside the
checkout into `/tmp/PHYS3810 support kit f5ec2e4/phys3810-canvas-kit` and installed
into a **fresh application `.venv`**, using the existing CPython 3.12.15 interpreter.
All 114 application distributions match the supplied active pins; pip is 26.2.2.
This is separate from the reused source environment and does not claim a fresh
Python installation, native-platform pass, or new human recording result.

The extracted interpreter ran `python scripts/validate_classroom.py --profile all`
from its own `runtime/` with no inherited `PYTHONPATH`. All required cells have
execution counts and no errors. All 57 payload sizes/hashes/modes and the
manifest stayed unchanged; canonical imports resolve under this extraction's
`runtime/src/`.

- Source commit: `f5ec2e4649de34ed567f7694c497dfc874e14584`.
- Source tree: `1543c568a1116c91c0283ce7d6df6e72e8cfa3ac`.
- ZIP: `PHYS3810-Canvas-Kit-v0.2-f5ec2e4649de.zip`.
- ZIP size: **259,111 bytes**, **58 files / 57 manifest entries**.
- ZIP SHA-256: `e37d1c7051b3a1b9ea48004f73c22c13b60afc467e0ce488982c4feb138459f9`.
- Manifest SHA-256: `122cbd02d2b9b7e22c4392ac47c36ad3a94cea3980e2ce9c3025f8b7b19bba5f`.
- Five demonstrated notebooks / thirteen total; **75 static local links** checked.
- Exact included student PDF SHA-256:
  `8587c80456183d3c6298d7afbec07304cb0f5b707580d8f229a40b3dfe887169`.
- Exact included student Markdown SHA-256:
  `dd9bda882ebefdeee823a5189ad657bf6d80d191a828f396f68c030b9e6a5293`.

Authenticated Jupyter HTTP checks passed 37 traversals across 18 documents,
plus exact v0.3 PDF response bytes and companion text. The registered Intro
kernel points to this `.venv`; five demonstrated metadata labels match.
Outside-root access remains 404 and authentication stayed enabled. The local
test used `--no-browser`, loopback port 8883, and task-local Jupyter/cache paths;
its server shut down through the authenticated API. This is package verification,
not a new interactive pilot.

The verified ZIP and standard checksum sidecar replace the active desktop kit.
The previous v0.1 ZIP/checksum were moved intact to
`Desktop/PHYS3810_Previous_Kits/`, with the original archive hash verified.
All older repository editions, release assets, and canonical artifact copies
remain unchanged. Raw receipts/logs/executed copies are preserved under the
ignored task directory; no test video or private correspondence is included.

## Non-interactive recording handoff and CP

The [mechanical walkthrough](instructor/RECORDING_WALKTHROUGH.md) names this
exact kit and provides extraction paths, CLI setup, a safe notebook reset,
authenticated launch, OBS mechanics, lesson order, playback and final delivery.
Its actual reset code block was run in a disposable copy: all five notebook
baselines restored, changed copies backed up byte-for-byte, and a wrong archive
rejected before overwrite. User notebooks were not reset by that verification.
The walkthrough is an instructor document outside the sealed student package;
adding it and this completion record does not require another export.

The user requests source/extraction validation and CP with **no new PRs**.
Work is committed and pushed on a scoped branch; protected main and rulesets
are not bypassed. No new PR-triggered remote CI run is claimed for this branch.
The existing main CI and new local source/extraction evidence are kept distinct.

No new broad review, pilot, approval questionnaire, release, external message,
Canvas upload, dependency campaign, or hardware job is needed or performed.
The deleted test video and derived media remain absent.
