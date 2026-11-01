# R7 local preview package contract

This is the packaging contract for proposed code **v0.2.0-rc1**, after the
[document-review reconciliation](R6_DOCUMENT_REVIEW_RECONCILIATION.md).
It produces an **unpublished local preview**, not a final classroom release.
It does not authorize GitHub changes, distribution, messages, or hardware jobs.
Follow [the readiness plan](RELEASE_READINESS_PLAN.md) for the remaining gates.

## Build from one committed snapshot

The [full-course builder](../../scripts/build_classroom_preview.py) is separate
from the preserved Grover-only builder. Run it with CPython 3.12 from a checkout
containing the exact builder version in the selected commit:

```bash
python scripts/build_classroom_preview.py --ref HEAD --output-dir artifacts/classroom-preview
```

`--ref` is resolved once to a commit. Runtime files, tests, notebooks, student
guide/PDF, templates, and technical contracts are read from that commit, not
from staged, unstaged, untracked, or user-supplied replacement files. The running
builder must match its committed source. A dirty payload file cannot silently
enter the ZIP. New output names may not overwrite earlier builds.

The archive is named
`PHYS3810-Fall2026-v0.2.0-rc1-local-<commit12>.zip`, with one top-level
`phys3810-fa2026/` directory. The commit suffix distinguishes local iterations.
This name does not establish a tag or live URL. The prospective public asset
name remains a separate publication decision.

Stable commit timestamps, sorted paths, fixed file modes, and deterministic
serialization/compression make repeated builds with the same input/tool versions
reproducible. The sidecar metadata records the builder/source identities and
archive checksum. It remains outside the ZIP; the manifest cannot hash itself.

## Inventory and audience boundary

The preview includes **37 exact committed files**:

- Seven Python source files, including the backend-configuration helper used
  only through mocked offline tests.
- All 13 current test files, two validation/smoke runners, and eight required
  notebooks.
- Requirements, CI requirements wrapper, constraints, Ruff configuration,
  license, and the synchronized student Markdown/PDF pair.

Five technical-contract exports retain supported-input, mathematical,
acceptance, resource, and teaching content while omitting repository
status/navigation headers and trailing coordination history. Earlier milestone
test counts in retained bodies are labeled historical; this preview's expected
inventory is **160 tests/eight notebooks/50 cells/16 PNGs**.

Four standalone pages provide README orientation, a setup pointer, a lesson
index, and validation/limit explanations. Their committed `.md.in` templates
live in `package/`; links are interpreted at their deployed destinations,
not at the template-source location. The builder fills only declared source/
archive identity placeholders. All eight notebook bytes remain unchanged.

The resulting inventory is **46 payload files plus `MANIFEST.json`**, for
47 files. Every payload has size, hash, mode, and source/adaptation provenance.
The builder does not include itself or its templates as redundant student files.

Exclude the entire instructor folder, instructor PDFs, presenter answer sheets,
prompts, policy/chat/history records, raw review receipts/patches, old releases,
Git metadata, environments, caches, credentials, and generated notebook outputs.
The whitelist contains no optional Runtime/GPU notebooks or PDF renderer.

The notebooks, tests, and mathematical contracts do contain worked expectations.
Excluding separate instructor answer documents does **not** make this an
answer-free assessment. Coverage, collaboration, grading, and solution
distribution remain instructor decisions.

## Required guide identity

The mandatory supplied student PDF is
`handouts/PHYS3810_Full_Course_Student_Setup_v0.1_REVIEW_DRAFT.pdf` under this
course directory: **73883 bytes**, SHA-256
`e6a950111470dbaa1d20781f4eb17391e73b7ca247e0a4ec54c879b922ea1053`.
The matching repository Markdown SHA-256 is
`f26919ac85fd8bd4419e19ac118a9cb0eca4e1f72348cf84e3a65fa91deaa631`.
Its one nonrendering MD036 annotation is disclosed in the reconciliation.
The builder requires this exact pair; a different edition needs a scoped
identity update and appropriate review, not an unchecked optional PDF path.

The PDF remains document **v0.1 REVIEW DRAFT** for proposed code **v0.2.0-rc1**.
The older Grover document-v0.2 files are distinct and excluded. No PDF bytes,
metadata, provenance, or page content are rewritten. P3-01 concerns the separate
instructor edition; its [reading note](instructor/README.md) stays outside this
student-facing preview and remains open before final instructor distribution.

## Builder checks and actual acceptance

The builder must reject missing/nonregular required paths, drift in source/test
Python inventory or validator notebook/figure inventories, stored source outputs/
counts, required-cell skip tags, guide mismatch, unresolved local file/fragment
links, unresolved placeholders, unsafe/duplicate/case-colliding archive paths,
and overwrite attempts. Static test-method counts are a drift guard, not proof
that any test ran. The old Grover whitelist and 50-test assumptions are not reused.

A successful build means only that packaging checks passed. **Runtime validation
is not executed by the builder.** Separately unpack the sealed ZIP outside all
checkouts, verify its manifest and exact inventory, confirm source imports come
from that extraction, and run:

```bash
python -m pip check
python scripts/validate_classroom.py
bash scripts/smoke_local.sh
```

Require 160 tests, eight interpreter-bound fresh-kernel notebooks, 50 completed
nonempty code cells, and 16 PNGs without notebook errors. Inspect saved outputs
and execution counts, not just printed summaries. Verify every delivered file's
hash/mode afterward and keep generated outputs outside the sealed archive.
Record environment/platform/versions and fresh-versus-reused installation.
Run relevant source and exported-Markdown lint plus preservation checks.

Actual reproducibility and refusal cases should exercise the real builder and
sealed payload, including mismatched PDF/guide bytes, incomplete source inputs,
stored notebook execution state, and overwrite attempts. Keep destructive
fixtures confined to disposable local repositories; never change the preserved
original/accepted checkout to test a rejection.

Packaging checks do not add a native-platform, editor-UI, browser-launch, human
pacing, or remote-CI pass. A later payload/setup/PDF change requires a newly
identified archive and affected verification. Preserve earlier packages and
Grover rc1 unchanged, and reassess final release inputs before publication.
