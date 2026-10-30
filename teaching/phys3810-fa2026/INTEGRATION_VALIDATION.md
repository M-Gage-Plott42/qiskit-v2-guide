# Local documentation and QFT integration

October 30, 2026. The original development checkout and index are preserved.
The integration branch `integration/phys3810-docs-qft-2026-10-30` starts from
refreshed `origin/main`, which remains published Grover revision
`3894391f2026d4fd9351b346b44b5eda453a17da`.

## Recovery and commit scope

A private recovery checkpoint is retained at
`artifacts/local-integration-2026-10-30/recovery` relative to the original
repository. It contains a Git bundle, staged and unstaged binary patches,
untracked/full-source archives, the raw index, file hashes/modes, checksums,
and a restoration script. Ignored environments and prior artifacts remain in
place in the original checkout; they are not part of the source archives.

Restoration into a new temporary clone passed for **87 files**, including
**29 untracked files**, full file permissions, the index entries, both patch
layers, and porcelain status. The first rehearsal exposed safe-tar permission
normalization from 0664 to 0644; restoring modes from the manifest corrected
it, and a complete fresh rehearsal then passed. The original files and raw
index were verified unchanged. No original branch switch, reset, stash, clean,
or staging operation was used.

The durable worktree is at
`artifacts/local-integration-2026-10-30/worktree` in the original repository.
The separate local changes are:

1. **Documentation/PDF commit:** `b16d235ca01ebc9c7f610dcfeb64f081d5d6b453`.
   Its 18 paths contain only Markdown and the two supplied v0.2 PDFs. All
   40 runtime/dependency/workflow files matched published main. Pre-commit
   passed; a clean detached checkout confirmed PDF tracking/hashes and all
   121 relative documentation links. It retains Grover's 50-test/four-notebook
   runtime and does not contain QFT implementation files.
2. **QFT commit:** the subsequent commit containing this report. It carries
   the existing QFT source, exports, tests, notebook, validator registration,
   preflight wording, and matching documentation. The six transferred runtime
   files match the preserved development checkout byte for byte. Grover source,
   its tests/notebook, dependency pins, workflows, smoke wrapper, and preview
   builder/renderer remain unchanged from published main.

The final commit IDs and clean-worktree verification are also recorded in the
private integration receipt and final task response; this report does not
attempt to embed its own commit hash.

## Executed classroom checks

Platform: Linux x86_64 (glibc 2.43). Classroom interpreter: CPython **3.12.15**,
with Qiskit **2.6.1**, Aer **0.17.2**, nbclient **0.11.0**, and NumPy **2.5.4**.
The existing pinned classroom environment was reused; this is not a fresh
installation. Separate Python 3.12 maintainer tools provide Ruff **0.15.22**,
yamllint **1.38.0**, and pre-commit **4.7.0**. No classroom dependency changed.

Commands ran from the integration worktree; `python` below denotes the selected
Python 3.12 environment (the separate tool environment for Ruff). BLAS/OpenMP
threads were limited to two; notebook kernels were bound to the classroom
interpreter. Local logs remain outside Git.

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

- Dependency consistency: **passed**.
- Unit tests: **64 passed**, retaining the 50 Grover/onboarding/runner tests
  and 14 independent QFT mathematical/input tests.
- Strict classroom validator: **passed**, including its own 64-test run and
  five notebooks in fresh kernels. All **27 nonempty code cells** executed;
  no error outputs were retained. Preflight/Grover/QFT produced 2/3/2 PNGs.
  Source notebooks retain empty outputs and execution counts.
- Ruff: **passed**.
- Original Bash smoke workflow: **passed**, executing both original smoke
  notebooks with the selected environment.
- Final staged `pre-commit run --all-files`: **passed** (Ruff, YAML, and
  Markdown hooks). All 135 relative documentation links and diff whitespace
  checks passed. No source fixes were needed after the passing runtime checks.

Executed notebook copies are in the integration worktree's ignored
`artifacts/executed-classroom/` and `artifacts/executed-local-smoke/` directories.
Detailed logs, transfer hashes, and recovery evidence are in
`artifacts/local-integration-2026-10-30/` relative to the original repository.

## PDF and publication identity

Both PDFs are tracked, unchanged from the authoritative delivered copies,
including appended provenance. The [receipt](handouts/README.md) records the
original mismatch and corrected disposition. Full-file SHA-256 values are:

- Student: `e5f9aa3813a38756c3568a42695b56b45f2005d1e78e93e7978722e8673755bc`.
- Instructor: `9048e56ee2cbca9c8757112558471862cfb4d843de0798f70b6a3c51bd9a1c72`.

The Grover rc1 tag remains at `3894391`; its original ZIP SHA-256 remains
`c46d8f2ac837f2742a99384cee1bc637478b4387909a4c399e4599655b11e686`.
No tag, release, or release asset was changed. The new commits remain local;
no push, PR, merge, external message, or hardware job was performed.

## Limits and next action

**Skipped:** optional IBM Runtime/cloud and GPU paths, outside classroom
validation. **Untested:** remote CI for these unpublished commits, native
Windows/macOS, interactive editor/browser setup, and live classroom timing.
The QPE, HHL, and Shor lessons remain unimplemented; no passes are claimed for
them. Historical remote Grover CI does not establish remote QFT validation.

QPE is the next implementation in the integration worktree. Preserve the
original checkout as recovery material. **GPT Pro sync: not needed for this
integration**; the next substantive review remains after QFT/QPE and before
HHL/Shor. Instructor scheduling/platform/teaching feedback can proceed alongside
local development. No manual user code audit is required.
