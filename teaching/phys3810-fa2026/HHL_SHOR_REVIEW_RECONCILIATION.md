# HHL/Shor independent review reconciliation

October 30, 2026. **Accepted: no blocking mathematical, source-code, or notebook
execution defect was found in the supported HHL/Shor families.** The received
review's D1 documentation correction is repaired. Optional O1/O2 teaching and
validation improvements are adopted and locally verified. No algorithm source,
QPE input bound, dependency, PDF, or published release asset changed.

## Reviewed snapshot and actual file access

The received report identifies source
`a85a88aa1fa148b8e64c739444899d5882202973`, archive
`PHYS3810-HHL-Shor-2026-10-30-a85a88aa1fa1.zip`, **122,699 bytes**, SHA-256
`3458908bf5877a1992ee51e1e2660df88c49ed78d4296848300d26d3abdda762`.
It explicitly states that no supplied file changed: all 44 exported files and
43 manifest entries remain unchanged. No replacement ZIP or patch is required.

The attached report and retained archive under the integration worktree's
`artifacts/shor-2026-10-30/review-final/` are accessible locally. Its prior desktop
copy is no longer present; the retained archive matches the receipt. No missing
reviewer-generated change is assumed. The reviewer environment and extra probe
scripts were not supplied or mounted here. Private paths are not file transfer.

Local checks verified the ZIP hash/size, 43 manifest entries, 35 canonical files
against the identified Git revision, and all four exported mathematical contract
bodies against their pre-adaptation source sections. This last comparison is
**local provenance evidence**: GPT Pro correctly limited its independent claim
to the exported sections it could inspect. The reviewed archive stays immutable;
this reconciliation creates a later local revision, not a relabeled review ZIP.

## Independent execution received

GPT Pro reports **158 tests, eight fresh-kernel notebooks, 50 nonempty code
cells, and 16 PNG figures passed**, with all source notebooks output-free.
It also visually inspected the six HHL/Shor figures. Its environment was reused
from the preceding phase review: Linux x86_64/glibc 2.39, CPython **3.12.14**,
Qiskit **2.6.1**, Aer **0.17.2**, NumPy **2.5.4**, nbclient **0.11.0**,
nbformat **5.10.4**, ipykernel **7.4.0**, Matplotlib **3.11.2**, and JupyterLab
**4.6.4**. All 114 installed packages covered by active constraints matched.
No fresh installation or dependency change occurred during this review.

The reviewer executed `python scripts/validate_classroom.py` from its extracted
folder, with BLAS/OpenMP threads limited to two; exit status was zero. The
158 tests comprise 97 earlier regressions, 23 HHL source, nine HHL notebook,
19 Shor source, and ten Shor notebook tests. Its 18.779-second number refers
only to unit tests, not installation or end-to-end notebook performance.

HHL sign/decoding, reciprocal operator, raw success/failure vectors, probability,
normalization, relative complex phase, and both-branch count cleanup were
accepted. Shor's complete modular domain, controlled phases, four-residue-qubit
builder, Fourier sign, conservative recovery, and GCD extraction were accepted.
The source costs and teaching limits remain bounded: no general sparse HHL,
scalable arithmetic, or quantum-advantage claim is established.

## Finding disposition

### D1: stale availability statements — required, repaired

Reproduced both statements in the reviewed archive and current checkout:
preflight cell `finish` said HHL/Shor were pending; QPE cell `qpe-wrapup` said
they were unimplemented and still needed the phase review first. The preflight
now links all five available lessons. The QPE conclusion links HHL/Shor while
retaining evolution sign, scaling, wrapping, precision, prepared-state, and
register-role cautions. Both outdated claims are absent and links resolve.
Only these two Markdown cells changed in those notebooks; code, cell order,
IDs, execution metadata, and all other cells are preserved. No permanent test
was added solely for this prose edit.

### O1: require all three HHL/Shor figures — optional, adopted

The original two-PNG minimum was reproduced with real temporary notebooks for
both lessons. It matched the original contract but did not protect the third
teaching figure. Both minima are now **three**, with the written figure
requirements updated explicitly. Two new real-kernel regressions establish
that two figures fail with preserved executed output and three figures pass;
source notebook bytes stay unchanged. The six earlier runner test methods
remain unchanged. This strengthens a presentation gate, not an algorithm's
supported inputs or mathematical scope.

### O2: theoretical recovery probabilities — optional, adopted

Shor's core and expansion now show theoretical per-shot order-recovery and
factor-success probabilities beside empirical counts. The comparison figure
also marks the theoretical values. Base 1 has 0/0; base 2 and base 11 have
1/2 and 1/2; base 14 has 1/2 and 0. All eight supported units are covered by
independent finite teaching fixtures. The explanation uses the exact order-2/4
family and coprime phase numerators; it does not insert an order table or search
into production recovery. Existing actual-cell tests now check displayed values
and plotted markers as well as observed counts. No new algorithm tests or
notebook cells are needed. A small negative plot margin keeps the zero marker
fully visible without changing any probabilities.

## Local mathematical reproduction

Additional probes used the unchanged reviewed implementation:

- Twelve HHL cases with spectra (1,7), (2,6), (3,5), (7,7), complex eigenbases,
  and complex/global-phase inputs. The independent failure reference interpolates
  a polynomial in A, avoiding the implementation's eigendecomposition. Worst raw
  amplitude error was **4.51e-15**; worst joint count leakage norm **3.84e-15**.
- Three Shor joint-state cases (13,6), (14,5), (1,4), using an orbit array and
  normalized NumPy FFT. Worst error was **2.45e-14**.
- Eight random complex controlled-input checks: worst error **2.26e-14**.
- Independent finite order search and integer-GCD denominator reduction:
  all **896 recovery** and **112 factor** cases passed.
- The explicitly supplied HHL input A=[[3,i],[-i,3]],
  b=exp(0.37i)*(1,0), and Shor base 13/width 6 passed actual-cell checks using
  the reviewed ZIP notebook/helper bytes. HHL raw success, probability 5/32,
  and X/Y/Z=(0,3/5,4/5) matched the stated expectations.

The review did not supply its random inputs or probe scripts, so the random
checks above are **equivalent local probes**, not claims to rerun those exact
scripts or reproduce their precise maxima. No phase fit or output rescaling
was used. These scratch probes are separate from the permanent test count.

## Current local validation

The current revision passes **160 tests**, retaining all 158 existing tests and
adding only the two figure-gate regressions. Eight fresh-kernel notebooks still
execute **50 nonempty code cells** and produce **16 PNGs**. All three HHL/Shor
figures are now required for each lesson. The updated Shor comparison was
visually checked; sources remain output-free.

Reused local environment: CPython **3.12.15**, Linux x86_64/glibc 2.43, with the
same Qiskit/Aer/NumPy/nbclient/nbformat/ipykernel/Matplotlib pins above. Separate
Python 3.12 maintainer tools provide Ruff 0.15.22, yamllint 1.38.0, and pre-commit
4.7.0. The following required commands passed:

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

Documentation links, notebook schema/cleanliness, scoped-diff checks, and original
checkout/index/PDF/release/archive preservation checks passed. Detailed outcomes,
D1 before/after evidence, O1/O2 checks, extra probe scripts, and final commit
receipt are ignored under `artifacts/hhl-shor-review-2026-10-30/`.

## Remaining work and next decision

**GPT Pro sync: not needed for these evidenced P3 follow-ups.** The independent
technical checkpoint is accepted and no algorithm/environment scope changed.
Do not overwrite the reviewed 158-test archive or distribute it as though it
contains these later corrections. A future package needs its own revision,
manifest, expected counts, and extracted verification. No new archive was
requested or produced for this reconciliation.

Next prepare a local classroom-release readiness plan: identify the unpublished
integration commits, remaining native-platform/interactive checks, pacing
rehearsal, and version-matched PDF/package requirements. Rick's reply remains
pending; dates, student preparation, delivery responsibility, platform targets,
and assessment are not invented. No additional code audit is assigned to the user.

**Skipped:** optional Runtime/cloud and GPU. **Untested:** fresh installation for
this snapshot, native Windows/macOS, interactive setup, remote CI for the local
commits, and timed teaching. The reviewer did not rerun local Ruff, pre-commit,
Bash smoke, or original-checkout checks; those remain separately evidenced local
checks. No push, PR, merge, publication, external message, or hardware job occurred.
