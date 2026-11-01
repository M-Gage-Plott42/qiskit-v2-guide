# R7 local preview packaging evidence

Executed October 31, 2026. **The scoped full-course builder and sealed local
preview passed packaging acceptance and extracted runtime validation.** The
archive remains unpublished. This does not close teaching, platform, pacing,
final-document, or publication gates in
[RELEASE_READINESS_PLAN.md](RELEASE_READINESS_PLAN.md).

## Exact source and artifact

- Build source: `135d5d00e3197708a26b547013a0fd8105194385`.
- Source tree: `92dd2f84e83c47fdb43fbd39d084b6a15edbde64`.
- Archive: `PHYS3810-Fall2026-v0.2.0-rc1-local-135d5d00e319.zip`.
- Retained path in the candidate worktree:
  `artifacts/r7-preview-2026-10-31/sealed/PHYS3810-Fall2026-v0.2.0-rc1-local-135d5d00e319.zip`.
- Size: **200130 bytes**.
- SHA-256: `7cd1cb0a75b268141a8962d512fe38deb3fe1a38911e90577d736fe445a2f79f`.
- Manifest SHA-256:
  `357e595858ba98c90490cdb805dee0205b5df625c2d61b7a109338cd14522d58`.

The [builder](../../scripts/build_classroom_preview.py), its committed templates,
and the [package contract](R7_PREVIEW_PACKAGE.md) were committed before building.
All payload inputs came from the resolved source commit. Later status/evidence
commits are separate from the source identified inside the ZIP. The local
filename includes a source suffix; no public tag or download URL was created.

## Payload and guide correspondence

The archive contains **47 regular files** under `phys3810-fa2026/`:

- **37 exact committed files:** reusable source, all 13 classroom test files,
  validation/smoke runners, eight notebooks, dependencies, license, lint
  configuration, and the reviewed student Markdown/PDF pair.
- **Five technical-contract exports:** complete retained mathematical/API/
  acceptance/resource/teaching bodies, with repository navigation/status and
  trailing coordination history removed. Historical milestone test counts are
  explicitly distinguished from the current 160-test/eight-notebook inventory.
- **Four rendered navigation templates:** README, setup pointer, lesson index,
  and validation/limits page. Their source templates and substitutions are
  identified in the manifest.
- **One `MANIFEST.json`:** hashes, sizes, modes, source/adaptation provenance,
  builder identity, and expected validation counts for the other 46 files.

The manifest cannot hash itself; the archive checksum identifies its complete
bytes. The build sidecar records the ZIP checksum separately. Its statement
`validation_status: not executed by this builder` remains true: this record and
the extraction receipt establish the actual subsequent runtime result.

The mandatory student PDF retains **73883 bytes** and SHA-256
`e6a950111470dbaa1d20781f4eb17391e73b7ca247e0a4ec54c879b922ea1053`.
The matching repository Markdown retains SHA-256
`f26919ac85fd8bd4419e19ac118a9cb0eca4e1f72348cf84e3a65fa91deaa631`.
No PDF metadata, provenance, page, or content was regenerated. These are the
reviewed document-v0.1 student inputs for proposed code-v0.2.0-rc1, distinct
from the older Grover document-v0.2 files.

The entire instructor folder, instructor PDFs, presenter answer sheets,
policy/chat/history records, prompts, raw review receipts/patches, old archives,
Git metadata, environments, caches, credentials, and generated outputs are
excluded. The builder and its templates are not redundant student payload files.
Worked notebook results, mathematical fixtures, and tests remain available;
this is **not an answer-free assessment package**.

## Builder review, refusal cases, and reproducibility

Two implementation issues were corrected before the build-source commit:

1. Source/test inventory is checked using the resolved Git tree before archive
   attributes can hide files. An added regression marked `export-ignore` now
   causes a profile mismatch instead of being silently omitted.
2. Protocol-relative links and HTTP(S) links without a hostname are rejected.
   They cannot be accepted as local self-links or valid external URLs.

The final builder also verifies its own bytes against the selected commit,
checks required regular files against their raw Git blobs, rejects transformed
or missing canonical inputs, pins the reviewed PDF/Markdown pair, and refuses
existing output paths. Notebook/figure inventories are read from the validator
AST without executing it; static method/cell counts guard profile drift but
are not represented as runtime tests.

**All 20 real CLI acceptance cases behaved as required** in an owned disposable
Git repository at `/tmp/phys3810-r7-builder-acceptance-ts5qzey4/fixture`.
Three success cases covered a valid build, reproducibility, and ignoring dirty
working-tree payload edits in favor of committed bytes. Seventeen expected
refusals covered overwrite attempts, an invalid ref, a changed running builder,
PDF/guide mismatch, missing/unexpected tests, a symlink source, stored notebook
outputs, skip tags, validator inventory drift, unresolved template placeholders,
missing link/anchor targets, protocol-relative/hostless URLs, and a hidden
`export-ignore` test addition. No protected checkout was changed to test failure.
These packaging cases are separate from the unchanged 160-test classroom suite.

The actual primary archive was also rebuilt with the explicit source SHA after
the first `HEAD` build. Both copies are byte-identical and share the archive
SHA-256 above. Output-directory and `source_ref` sidecar fields may differ;
the archive itself depends on the resolved commit and fixed tool versions.

## Independent payload inspection

A separate local assistant audit, not a new GPT Pro review, confirmed 47 unique
safe regular ZIP paths, no
case collisions or symlinks, all 46 manifest entries, all 37 exact source files,
builder/tree/source hashes, the five retained contract bodies, and the four
template renders. It verified the student document pins and every exclusion.
All eight notebook files retain their original committed bytes, empty outputs,
and null execution counts. **50 relative file/fragment links** resolve within
the standalone payload. External URL availability was not rechecked here.

The audit found no remaining blocking payload defect. Its static count of 160
test methods is only an inventory check; actual execution is recorded below.

## Isolated extraction and runtime checks

The sealed archive was extracted outside the checkouts to:

`/tmp/phys3810-r7-preview-2026-10-31-wbtv00lj/phys3810-fa2026`

Python's ZIP reader was used after checking paths/types, and stored Unix modes
were applied before execution. This does not test a graphical archive utility
or native Windows/macOS extraction behavior.

Verification **reused** the R6 walkthrough interpreter:

`/tmp/phys3810-r6-guide-2026-10-31-qwwuuf8b/phys3810-fa2026/.venv/bin/python`

This is CPython **3.12.15**, Ubuntu 26.04.1 LTS x86_64, Linux 7.0.0-42-generic,
glibc 2.43. No dependency installation occurred for R7. Recorded versions include
Qiskit 2.6.1, Aer 0.17.2, NumPy 2.5.4, Matplotlib 3.11.2, JupyterLab 4.6.4,
ipykernel 7.4.0, nbclient 0.11.0, nbformat 5.10.4, and pip 26.2.2. Source and
validator imports were confirmed to resolve within the extracted folder.

The following commands ran from that extraction using its selected interpreter:

```bash
python -m pip check
python scripts/validate_classroom.py
bash scripts/smoke_local.sh
```

All passed. The classroom validator ran **160 tests** and **eight separate
fresh-kernel notebooks**. Saved-output inspection confirmed complete consecutive
counts, no error outputs, **50 executed nonempty code cells**, and **16 PNGs**:

- Preflight: 4 cells, 2 PNGs.
- Statevector smoke: 3 cells, 0 PNGs.
- Aer smoke: 4 cells, 0 PNGs.
- Grover: 9 cells, 3 PNGs.
- QFT: 7 cells, 2 PNGs.
- QPE: 8 cells, 3 PNGs.
- HHL: 7 cells, 3 PNGs.
- Compiled Shor: 8 cells, 3 PNGs.

PNG records include actual byte counts and dimensions. This is output validation,
not another browser figure-inspection session or a human pacing rehearsal.
The extra Bash smoke run repeats the two existing smoke notebooks; it does not
increase the required notebook inventory. Optional Runtime/GPU execution remains
deliberately skipped, not passed. No hardware job was submitted.

Ruff passed against the extracted source using the existing separate maintainer
tools. All ten exported Markdown files passed lint under the unchanged repository
profile. The initial exported-Markdown invocation used standalone defaults and
flagged long lines allowed by that profile; the harness was corrected to select
the existing profile. The failure logs remain under `extracted-markdownlint-defaults.*`.
No payload, guide, or lint configuration was edited to obtain the pass.

All **47 delivered files**, including the manifest, retained their hashes and
modes after execution. Source notebook outputs stayed empty, and the sealed
ZIP remained unchanged. Generated outputs are retained only in the isolated
extraction's ignored `artifacts/` directories. No execution output was added to
the preview archive.

## Evidence limits, preservation, and next step

R7 adds a verified local package, not a new fresh-install, actual UI, native-host,
remote-CI, public-download, or classroom-readiness result. The existing
[R6 walkthrough](R6_GUIDE_WALKTHROUGH_VALIDATION.md) remains separate evidence.
The supplied PDF's statement that the public full-course download is unpublished
is still correct; publication wording and final document identity must be
reassessed before an actual release.

P3-01 belongs to the excluded instructor edition and remains open before final
instructor distribution. Rick's decisions, native Windows/macOS, native editor
UI, automatic browser opening, human pacing, and final classroom approval remain
open. Excluding instructor files does not settle assessment or solution access.

The preservation check covers prior checkouts/indexes, original recovery and
Grover assets, reviewed archives/PDFs/companions, existing environments, and
retained staging. The final local completion receipt records preservation,
documentation checks, and the clean candidate commit. No original archive is
overwritten, and the Grover-only builder remains unchanged.

The final strict check found one external-path exception: the original
`/home/gage/Downloads/PHYS3810_Full_Course_Documents_v0.1_REVIEW_DRAFT.zip`
was present at the start but absent at the final check. Its disappearance is not
attributed to a user or process without evidence. No R7 operation targeted that
path for modification, and it was not recreated or deleted during reconciliation
of this observation. The retained copy at
`artifacts/r6-doc-reconciliation-2026-10-31/received/PHYS3810_Full_Course_Documents_v0.1_REVIEW_DRAFT.zip`
still matches all 176121 bytes and SHA-256
`45520beb2780f713d903f225970541b35d9d71041b6bb4d1af5f77eb8916b927`.
The reviewed PDFs/companions and both outgoing review-ZIP copies remain intact.
The original baseline and failed strict check are retained; final preservation
evidence must explicitly report the missing Downloads path rather than claim
that location was preserved. The preview build uses committed PDF bytes and
does not depend on that Downloads copy.

The current `preservation/external-absence-check.json` reports
`passed_with_external_absence`: every other baseline entry matches exactly and
the retained return ZIP is independently hash/size verified. The original
baseline, strict harness, prior baseline-era `final-check.json`, and the failed
strict-run log remain unchanged. No missing-file data was fabricated from the
retained copy. This is not an unqualified path-preservation pass.

Final repository checks passed for **397 local file links**, five Bash syntax
blocks across changed guidance/templates, and the configured pre-commit hooks.
All 123 unchanged initial tracked files retain their bytes/modes. The archive's
50 internal links/anchors and ten exported Markdown files were checked in their
deployed layout; template links intentionally use that layout.

Receipts and logs are retained under `artifacts/r7-preview-2026-10-31/` in the
candidate worktree: build sidecar, acceptance cases, reproducibility check,
independent payload audit, extraction/environment/output records, lint results,
and preservation/completion records. Temporary extraction is retained evidence,
not a durable source backup or a published download.

**Recommended next task:** prepare an R8 **read-only/local readiness audit and
publication proposal**. Recheck current upstream/tag availability, repository
rules and required checks, source/package correspondence, and unresolved guide/
teaching/support gates. Produce a concrete local proposal without pushing,
opening a PR, merging, publishing, messaging, or submitting hardware jobs.
Do not turn this local-preview pass into authorization for those actions.

**GPT Pro sync: not needed solely for this byte-preserving packaging step.**
The next authored PDF revision should address P3-01 and any agreed teaching or
publication wording changes; prepare its concrete evidence and prompt when due.
