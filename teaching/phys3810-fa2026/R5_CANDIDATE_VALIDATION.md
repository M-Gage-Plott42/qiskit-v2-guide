# R5 protected local candidate evidence

Executed October 31, 2026. **Protected local integration and runtime checks
passed.** A fresh read of upstream found no new commits beyond the published
Grover base. All 13 accepted local commits retain their original IDs; no
rebase, cherry-pick, conflict repair, or merge was necessary. A separate durable
candidate worktree preserves both existing checkouts and their indexes.

This closes R5's local integration/preparation task, not classroom readiness
or publication. Rick's decisions, human pacing, native-platform coverage, the
native editor UI gap, matching PDFs, final packaging, and publication remain
open under [RELEASE_READINESS_PLAN.md](RELEASE_READINESS_PLAN.md).

## Candidate and upstream identity

- Accepted branch: `feat/phys3810-qpe`, preserved at
  `0570863f17971473977a65ad6d4623c27aca61c8` in the original integration worktree
  `artifacts/local-integration-2026-10-30/worktree` beneath the original repo.
- New branch: `candidate/phys3810-fa2026-v0.2.0-rc1`.
- New worktree: `/home/gage/src/github/M-Gage-Plott42/qiskit-v2-guide/artifacts/local-candidate-2026-10-31/worktree`.
- Refreshed `origin/main` and merge base:
  `3894391f2026d4fd9351b346b44b5eda453a17da`. Old and new values are equal.
  The accepted branch is 13 commits ahead and zero behind that refreshed ref.
  There are no upstream path changes to reconcile or fixes to discard.
- Initial candidate tree: `ddd86dccef98d3e150d0be17b3ea193f4de3d37a`, identical
  to accepted `0570863`. Runtime validation used that exact source content;
  subsequent R5 edits are limited to Markdown context/evidence/publication drafts.
  The final candidate commit is the commit introducing this R5 record, recorded
  explicitly in the ignored `completion.json` receipt. No self-referential
  hash is embedded here.

The actual fetch was:

```bash
git fetch --no-tags --no-write-fetch-head origin refs/heads/main:refs/remotes/origin/main
```

It updated only the remote-tracking reference if needed, with no tag mutation
or remote write. Existing local `main`, original development branch, accepted
integration branch, and Grover tag were retained. A prunable old preview worktree
entry was observed and left untouched; no cleanup of unrelated state occurred.

The [publication draft](CLASSROOM_PUBLICATION_DRAFT.md) identifies proposed
code version `v0.2.0-rc1`, tag `phys3810-fa2026-v0.2.0-rc1`, and future asset
`PHYS3810-Fall2026-v0.2.0-rc1.zip`. No tag or archive was created. A read-only
exact `git ls-remote --tags` query found no advertised match on October 31;
that is neither a reservation nor a GitHub draft-release inventory. Recheck
before publication. Its first sandboxed attempt failed on an SSH system-config
ownership check; the approved read-only execution succeeded without changing
SSH configuration. The final successful query is the availability evidence.

## Accepted-to-candidate commit mapping

Every entry below maps to itself; full hashes and subjects are retained in
`upstream-inspection.json`. R5 adds a documentation commit after this chain.

1. `b16d235` → `b16d235`: documentation and delivered Grover v0.2 PDFs.
2. `f277e21` → `f277e21`: QFT implementation and tests.
3. `e365d38` → `e365d38`: QPE implementation and tests.
4. `695c425` → `695c425`: accepted phase-review follow-ups.
5. `6ed4d19` → `6ed4d19`: HHL/Shor contracts.
6. `234c608` → `234c608`: HHL implementation.
7. `a85a88a` → `a85a88a`: compiled N=15 Shor implementation.
8. `ec07359` → `ec07359`: HHL/Shor review reconciliation; 160-test baseline.
9. `9e73b82` → `9e73b82`: readiness plan.
10. `6b70fbd` → `6b70fbd`: R1 fresh-install evidence.
11. `4c589fd` → `4c589fd`: R2 interactive evidence.
12. `07831f4` → `07831f4`: R3 native procedures.
13. `0570863` → `0570863`: R4 provisional run sheets and timings.

## Recovery and preservation

The original dirty checkout/index and its October 30 recovery checkpoint remain
unchanged. R5 additionally saved a complete accepted-history Git bundle before
fetching, under the original repository's
`artifacts/local-candidate-2026-10-31/evidence/accepted-history.bundle`.
Its SHA-256 is
`eae37c5ee66c88c5e8107442f8af872e1b5d6529bb5499d70acdf5513f38bd22`.

`git bundle verify` passed. A local bare clone of that bundle passed
`git fsck --full`, and all 118 accepted tracked file hashes matched the restored
commit. The restored repository is retained at `evidence/restored-history.git`.
This is a recovery artifact, not a student ZIP or GPT Pro handoff.

The final preservation check compares the original 87 files/modes, original
HEAD/branch/raw index/status, all 118 accepted files/modes and its HEAD/branch/
raw index/clean status, all 17 earlier recovery files, seven immutable assets,
and 110 frozen R1 source files. It also compares the three existing interpreter/
environment configuration and installed-distribution metadata snapshots. That
environment check does not hash every package-code/cache/OS byte.

The seven immutable assets include both delivered Grover document-v0.2 PDFs,
the published Grover ZIP and two original PDFs, and the two retained algorithm
review ZIPs. The full-byte PDF hashes remain:

- Student: `e5f9aa3813a38756c3568a42695b56b45f2005d1e78e93e7978722e8673755bc`.
- Instructor: `9048e56ee2cbca9c8757112558471862cfb4d843de0798f70b6a3c51bd9a1c72`.
- Original Grover ZIP: `c46d8f2ac837f2742a99384cee1bc637478b4387909a4c399e4599655b11e686`.

Candidate PDF copies are checked against those same hashes. Their bytes,
including provenance, are not regenerated or rewritten. The old reviewed ZIPs
remain identified as 92-/158-test snapshots rather than the current candidate.

## Executed environment and required checks

R5 **reused** R1's validated interpreter at
`/tmp/phys3810-r1-2026-10-31-gt5hru30/venv/bin/python`: CPython 3.12.15 on
Ubuntu 26.04.1 LTS x86_64, Linux 7.0.0-42-generic, glibc 2.43. No installation
or dependency upgrade occurred. Qiskit 2.6.1, Aer 0.17.2, NumPy 2.5.4,
Matplotlib 3.11.2, nbclient 0.11.0, nbformat 5.10.4, ipykernel 7.4.0, and
JupyterLab 4.6.4 remain installed. The environment receipt records all 115
distributions; earlier fresh-install/pin-parity evidence remains R1's result.

Commands ran from the candidate root. Runtime commands used that selected
interpreter; Ruff and pre-commit used the existing separate Python 3.12
maintainer tools. Application settings/output paths were directed to ignored R5
locations; maintainer tools reused their existing ignored caches. No package
install was hidden in the checks. Python bytecode writes
and user site packages were disabled. OpenMP/OpenBLAS used two threads.

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

- **Passed:** dependency consistency; standalone discovery ran all **160 tests**.
- **Passed:** classroom validator independently reran the same 160 tests and
  all **eight required notebooks** in fresh kernels bound to the selected
  interpreter. The two suite invocations are not 320 distinct regressions.
- **Passed:** saved output inspection counted exactly **50 nonempty code cells
  and 16 PNGs**, including three each for HHL/Shor. Every count sequence begins
  at one and is complete; no error output remains. Canonical sources stay
  output-free. Printed summaries alone were not used as proof.
- **Passed:** Ruff and the original Bash smoke entry point. Its two smoke
  notebook executions are additional checks, not new required notebook names.
- **Skipped:** optional Runtime/cloud/GPU execution, outside classroom defaults.
- **Untested in R5:** fresh installation, actual UI execution, native Windows/
  macOS, human rehearsal, a new package extraction, and remote CI. No such pass
  is inferred from local tests or historical reviews.

**Passed:** final pre-commit (Ruff, yamllint, markdownlint), all 311 local file
links across tracked Markdown/notebook prose, output-free source checks, Git
scope/whitespace, and preservation. All 113 unchanged accepted files retain
their bytes and filesystem modes. Results are recorded in `checks.json`,
`verification.json`, and `preservation/final-check.json` alongside the final
candidate commit/clean-state receipt.

An initial Markdownlint run found one extra blank line in `STATUS.md`; it was
removed and all hooks passed. The first auxiliary mode assertion compared full
filesystem permissions with Git's normalized mode bits, incorrectly flagging
a file that was 0664 in both worktrees. The harness now compares against the
preserved accepted filesystem modes and passes; no file permission or algorithm
repair was needed. Original failure evidence and dispositions remain retained
in `pre-commit-initial.log`, `checks-initial.json`, and `repair-notes.json`.

## Effect on earlier evidence

The candidate audit verified 68 source/test/notebook/setup/pin/workflow/policy
files against accepted `0570863`, and 51 runtime/test/notebook/pin/workflow files
against R1 source `9e73b82`. All 16 `.github` files and `CONTRIBUTING.md` match
refreshed upstream. No source repair, supported-input change, job-name change,
or ruleset change was needed. Live rulesets were not queried or altered here.

- **R1:** the existing fresh-install evidence remains applicable to identical
  runtime/pins; this turn adds a reused-environment run in the new worktree.
- **R2:** the observed Linux/Chrome JupyterLab behavior remains evidence for
  its original separate UI copy and external-kernelspec adaptation. Moving the
  candidate does not establish a new UI run at this path. Native editor UI is
  still untested and exact Chrome version remains unverified.
- **R3:** Windows x64 and macOS ARM64/Intel remain untested. No host was added.
- **R4:** the run sheets stay provisional. The recorded source/input-specific
  machine timings are retained; no new timing trial or human rehearsal occurred.
- **Independent reviews:** unchanged accepted commits preserve their review
  identities. No extra algorithm review is needed solely for this documentation
  candidate. A later substantive repair would need reassessment.

## Evidence locations and remaining work

All R5 logs/receipts are under the original repository's
`artifacts/local-candidate-2026-10-31/evidence/`: start state, upstream inspection,
full commit mapping, candidate identity/tag-query result, recovery restoration,
environment versions, check commands/logs, notebook counts, candidate audit,
link/scope checks, and preservation receipts. Candidate executed notebooks are
under its ignored `artifacts/executed-classroom/` and `artifacts/executed-local-smoke/`.

Continue future work in this candidate worktree. Preserve the older integration
checkout at `0570863` as the accepted baseline. The
[publication description](CLASSROOM_PUBLICATION_DRAFT.md) is concrete local
planning text; it does not create a PR, release, or available download.

Next prepare **provisional R6 Markdown inputs only** using the proposed candidate
identity and actual platform claims. Teaching decisions and the real presenter
rehearsal remain pending; matching PDFs wait for stable inputs and the prescribed
ChatGPT delivery/review workflow. The current Grover-only entry points remain
valid for their edition. The old `build_grover_preview.py` whitelist/counts are
not a full-course package builder and must not silently ship a truncated course
under the new name; R7 owns a new scoped builder and extraction validation.

GPT Pro sync is not needed for this unchanged-runtime R5 result. Prepare the
document/teaching handoff when its inputs are ready. No push, PR, merge into
main, publication, external message, hardware job, new PDF, or algorithm-scope
expansion occurred.
