# R6 provisional document-review handoff receipt

Prepared October 31, 2026. **One standalone runnable review ZIP is verified and
copied to the Ubuntu desktop.** Its review prompt is supplied separately in chat,
not inside the ZIP. This is a document-review bundle for provisional PDFs, not
a student release or final classroom approval. No transfer to GPT Pro, new PDF,
publication, external message, or hardware job was performed by this task.

## Exact archive and source

- File: `PHYS3810-Document-Review-2026-10-31-c63381a8e6fb.zip`.
- Size: **164550 bytes**.
- ZIP SHA-256: `f0af2bfd8507a5c1c6aedc04d67bfacee86faf34d678a4e77e70fd42e853980c`.
- Desktop copy: `/home/gage/Desktop/PHYS3810-Document-Review-2026-10-31-c63381a8e6fb.zip`.
- Frozen source: `c63381a8e6fbe900103b9d2053fe978310798e9a`.
- Source tree: `b41d83f0d3f668192f7b3b34051e863dc8d99f17`.
- Top directory: `phys3810-fa2026/`.
- `MANIFEST.json` SHA-256:
  `33cac3de0b22632ce838152e8aebf4436e5e7cbda2f458a348629f0899de5c35`.

The ZIP contains **50 files**. The manifest records hashes/sizes/modes and
source/adaptation information for the other **49**; the outer ZIP checksum
identifies the manifest itself without a circular self-checksum. The desktop
copy was created without overwriting another file and independently hash/size
checked against the sealed archive.

The source was frozen from the clean candidate before this handoff/status
documentation was written. Later local commits recording the handoff do not
change the reviewed archive's source identity. The retained local ZIP is under
`artifacts/r6-doc-review-2026-10-31/sealed/` in the candidate worktree. Earlier
algorithm-review ZIPs and Grover rc1 assets remain unchanged.

## Contents and disclosed adaptations

**36 files retain exact committed bytes:** the seven reusable Python source
files, 13 tests, both validation/smoke runners, all eight required notebooks,
requirements/constraints, CI requirements wrapper, Ruff configuration, license,
and the student setup companion. No algorithm, test, notebook cell/metadata,
dependency pin, or supported input was changed for export. The mocked backend
configuration helper/tests remain because they are part of the 160 regressions;
no real `.env` or credential file is included.

**13 guidance files are adapted or generated:**

- Five technical contracts replace repository status/navigation headers and
  remove trailing coordination history. Their complete retained API,
  mathematical, acceptance, resource, and teaching bodies are verified source
  substrings with recorded hashes. Historical 64-/97-test milestone baselines
  inside those bodies are explicitly labeled as earlier regression baselines;
  current package validation is 160 tests/eight notebooks.
- The instructor companion and three presenter run sheets change only local
  navigation links, plus one filename link label, to the included concise
  evidence and course overview. Their teaching text is unchanged. Original and
  adapted hashes/link replacements are recorded in the manifest. Some links
  now summarize evidence; a native-platform procedure is not thereby included.
- A short setup pointer preserves the preflight notebook's original setup link.
  A course outline doubles as the three-run-sheet index. The root README
  identifies the review artifact, and `VALIDATION_EVIDENCE.md` provides concise
  source-specific validation, machine timings, platform limits, and pending
  decisions. These are standalone navigation/evidence replacements, not copied
  policy or chat records.

The two audience-separated document inputs remain **document v0.1 drafts** for
proposed **code v0.2.0-rc1**. The archive's identity is distinct from the future
unpublished `PHYS3810-Fall2026-v0.2.0-rc1.zip`. Instructor answers are separate
from student setup; the existing notebooks still contain worked results and
are not declared answer-free assessments.

Excluded: prompts/prompt files, agent/policy/chat documents, unrelated history,
old PDFs/releases, nested archives, Git metadata, environments, caches,
credentials, private correspondence/student data, execution logs, and generated
notebook outputs. No local PDF renderer was used. The prompt is retained only
in ignored handoff evidence outside the ZIP and delivered in a chat code block;
only the ZIP was copied to the desktop.

## Extracted verification — passed

The sealed archive was extracted outside the checkouts to
`/tmp/phys3810-r6-document-review-2026-10-31-xt8f4_iz/phys3810-fa2026`.
ZIP integrity, unique safe relative paths, regular-file modes, the exact
inventory, all manifest entries, and exclusions passed. Independent payload
inspection also verified all canonical bytes and technical-body/navigation
adaptations. **100 relative file links and heading fragments** resolve inside
the standalone payload. All eight notebook sources have empty outputs/counts.
Python's ZIP extractor was used and the recorded Unix modes were applied before
execution; this is not a graphical archive-extraction or native-Windows test.

Verification **reused** the earlier R6 walkthrough interpreter:
`/tmp/phys3810-r6-guide-2026-10-31-qwwuuf8b/phys3810-fa2026/.venv/bin/python`.
It is CPython 3.12.15 on Ubuntu 26.04.1 LTS x86_64, Linux 7.0.0-42-generic,
glibc 2.43. The 115 installed distributions include the previously verified
114 application pins plus pip 26.2.2. Qiskit 2.6.1, Aer 0.17.2, JupyterLab
4.6.4, NumPy 2.5.4, Matplotlib 3.11.2, nbclient 0.11.0, and nbformat 5.10.4
are unchanged. **No new dependency installation or UI run occurred here.**

The following commands ran from the extracted root, with that interpreter and
task-local settings/caches, bytecode writes disabled, user site packages disabled,
and inherited Python-path overrides removed:

```bash
python -m pip check
python scripts/validate_classroom.py
bash scripts/smoke_local.sh
```

All passed. The validator ran **160 tests** and **eight fresh-kernel notebooks**.
Saved-output inspection independently counted **50 completed nonempty code
cells and 16 PNGs**, including three each for HHL/Shor, with complete consecutive
execution counts and no errors. The extra Bash smoke run does not add new
required notebook names. Imports resolve to this extracted source, not an older
checkout. All **50 delivered files**, including the manifest, retained their
bytes/modes after execution, and the sealed ZIP was unchanged.
Ruff also passed against the extracted payload using the existing separate
maintainer tools; no tool package was added to the classroom environment.

The earlier R6 fresh installation and actual JupyterLab walkthrough remain
separate evidence in the concise payload report. In particular, this extraction
test does not repeat those UI actions or establish native Windows/macOS, native
editor UI, automatic browser opening, human pacing, or classroom approval.

## Transfer and return expectations

**GPT Pro sync: recommended now.** The user can upload the single desktop ZIP
and paste the separately supplied prompt into the existing GPT Pro planning
conversation. No manual code audit or evidence assembly is assigned to the user.
The packet is ready locally; uploading it and receiving a response are still
unobserved actions. No reviewer-produced files have arrived for this edition.

The prompt asks for accessible-file confirmation, manifest/source identification,
document correctness/usability review, and two clearly labeled review-draft PDFs.
Student pages must omit maintainer/model-review coordination; instructor pages
retain appropriate technical/teaching limits without document-transfer process
notes. No author metadata, endorsement, schedule, grading, delivery arrangement,
or live download URL should be invented. Rick's decisions, native/editor gaps,
human pacing, and final classroom approval remain provisional.

The requested return is a **real downloadable ZIP** containing both PDFs,
synchronized Markdown companions, and a machine-readable receipt: reviewed
source, relative paths, exact delivered sizes/SHA-256 hashes, page counts,
title/author metadata, and link inventory. The ZIP checksum belongs outside
that ZIP. Rendered-page visual and OCR checks must be reported as performed or
unavailable. Whole-file receipts must cover actual downloadable bytes, including
any appended provenance; unverified pre-delivery hashes are not substitutes.

Filename cards, screenshots, or inaccessible private links do not establish
returned-file access. If the reviewer changes Markdown, the supplied export
paths are the patch base. During local reconciliation, reverse or map the
manifested bundle-only navigation adaptations before applying editorial changes
to repository companions; do not overwrite repository links with packet-only
paths. Reproduce actionable findings and run affected checks. Preserve the old
Grover PDFs and never regenerate/strip supplied PDF bytes locally.

## Local receipts and preservation

Ignored evidence under `artifacts/r6-doc-review-2026-10-31/` includes the frozen
source inventory, builder/templates, ZIP metadata, independent payload audit,
extracted commands/logs/output checks, interpreter/module-origin record, desktop
hash receipt, separate prompt receipt, and final preservation/completion records.
The ZIP's included evidence predates sealing and explicitly defers the final
extraction result to this external receipt; the archive was not edited afterward.

Original and accepted checkouts/indexes, recovery material, seven immutable
assets, R1/R2 staging, existing environments, the R6 walkthrough's 123 saved
source files, and its environment/kernelspec remain preserved. Environment
checks cover interpreter/configuration/distribution metadata, not every code,
cache, or OS byte. The candidate worktree receives only these local Markdown
status/handoff updates; its final commit and clean state are in the completion
receipt. No push, PR, merge, publication, external message, or hardware job is
part of this handoff preparation.
