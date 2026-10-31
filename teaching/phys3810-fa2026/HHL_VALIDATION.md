# HHL local validation

October 30, 2026. **The exact-spectrum HHL milestone passes local validation:
129 tests and seven required fresh-kernel notebooks.** This change follows
local design commit `6ed4d19d219db2eac3f2abccd7f53624c0c9c483` and retains all
97 existing regression tests. The exact supported family and acceptance
criteria are in [HHL_PLAN.md](HHL_PLAN.md). This is implementation and execution
evidence, not a received independent GPT Pro review of HHL.

## Implemented scope

- `src/phys3810/hhl.py` exports `hhl_circuit(matrix, rhs)` and
  `hhl_reciprocal_rotation()`. Inputs are copied and validated: finite numeric
  2x2 Hermitian A with eigenvalues in 1-7, normalized complex length-two b,
  and absolute admission tolerance 1e-12 with zero relative tolerance.
- Five qubits have tensor order success, system, count: count is qubits 0-2,
  system is 3, success is 4. Starting from all zeros, prepare b, estimate
  `exp(+i*pi*A/4)`, apply seven complete-pattern controlled reciprocal rotations,
  then invert the same QPE block. Neither b preparation nor the flag is undone.
- Three counting bits encode the eigenvalue directly as y. The flag receives
  `RY(2*asin(1/y))` for y=1-7, with identity at zero. Dense classical spectral
  decomposition constructs the small evolution matrix, not the solution state.
  Full evolution phase is retained; no spectrum rescaling or off-grid fallback
  is added. The existing QFT/QPE computational source and QPE contract are unchanged.
- `tests/test_hhl.py` adds **23 tests**. Complete reciprocal-operator tests cover
  eight counting labels and both input flag states. Full-state tests use every
  one of the 28 unordered eigenvalue pairs, seeded complex eigenbases/states,
  independent classical solves, and known-spectrum failure references.
- `tests/test_hhl_notebook.py` adds **nine actual-cell tests**. Seven editable
  input fixtures verify raw amplitudes, branch probabilities, conditioned phase,
  plot values, and aligned-shot postselection. Remaining checks cover selection
  alignment, handled invalid inputs, and the sampling cell's explicit failure
  for an empty selected sample; no artificial conditioned mean is invented.
- `notebooks/04_hhl.ipynb` has 13 cells, **seven nonempty code cells**, and three
  figures. It imports canonical HHL source, puts predictions before core answers,
  and provides a 20-minute core plus 15-minute expansion. Pacing is proposed,
  not timed classroom evidence. The strict validator requires the notebook and
  at least two figures; it produces three.

## Independent mathematical evidence

The complete expected state is
`|0>flag (sqrt(I-A^-2)b) |000>count + |1>flag (A^-1 b) |000>count`.
Tests verify both raw branches, total norm, success probability, and cleanup
before normalizing the successful branch. No phase fit or arbitrary output
rescaling is used. Expectations come from linear solves, closed fixtures, and
known spectral generators, rather than invoking the algorithm to predict itself.

For `A=[[1.5,0.5],[0.5,1.5]]` and b=(1,0), raw success is (3/4,-1/4), probability
5/8, and the conditioned state is (3,-1)/sqrt(10). The failure vector is
(sqrt(3)/4,sqrt(3)/4). Other basis/eigenstate inputs, a relative complex phase,
explicit matrix scaling, an alternate matrix, and scalar matrices 1I/3I/7I
check sign, phase, state preparation, zero failure, and global evolution phase.
Doubling A changes success to 5/32 while preserving the normalized answer.

Tests use `rtol=0`, full-state/operator/probability/norm `atol=1e-10`, conditioned
state `atol=1e-9`, and nonzero-count projection norm at most 1e-9 on each branch
and jointly. Input boundary tests distinguish representation errors within
1e-12 from unsupported spectra/norms/Hermiticity beyond it. Singular, negative,
wrapped-at-eight, and materially nonexact spectra are rejected.

Local V2 sampling uses 4096 shots per X/Y/Z basis with seed 2026. Each shot's
system bit is conditioned on that same shot's flag, using named classical
registers and ordered `get_bitstrings()` results. Probability bounds are six
binomial standard errors plus one shot; conditional observable bounds use the
actual selected-shot count. The fixed sign/complex fixtures have independent
X/Y/Z references. Deterministic amplitude tests remain the primary evidence.

Two scoped review repairs were reproduced and covered: ragged RHS data now
raises the specified `ValueError`; empty selection reports an undefined mean
before a descriptive statistical validation failure. Visual inspection also
found the imaginary-amplitude panel autoscaling numerical roundoff; a common
[-1.05,1.05] amplitude scale now makes zero and complex-state values comparable.

## Executed checks and environment

Reused local classroom environment: **CPython 3.12.15**, Linux x86_64,
glibc 2.43, Qiskit **2.6.1**, Aer **0.17.2**, NumPy **2.5.4**, nbclient **0.11.0**,
nbformat **5.10.4**, ipykernel **7.4.0**, and Matplotlib **3.11.2**. No fresh
installation or dependency change is claimed. Separate Python 3.12 maintainer
tools provide Ruff 0.15.22, yamllint 1.38.0, and pre-commit 4.7.0.
BLAS/OpenMP threads were limited to two and caches written under ignored artifacts.

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

All commands **passed**. Ruff/pre-commit use the separate maintainer environment;
application tests, smoke notebooks, and the strict validator use the pinned
classroom interpreter. The validator reruns all **129 tests** and executes all
seven required notebooks in fresh interpreter-bound kernels: **42 nonempty code
cells**, no retained errors, and **13 PNGs**. Preflight/Grover/QFT/QPE/HHL produce
2/3/2/3/3 figures; both smoke notebooks execute without figure requirements.
The three HHL figures were visually inspected. Source notebooks retain no outputs
or execution counts. Strict skip rejection, forced errors, completion checks,
and preservation of partial failed notebooks remain unchanged.

Whitespace, relative documentation links, unchanged baseline-file checks,
source notebook schema/cleanliness, and preservation receipts **passed**.
Detailed logs, executed notebooks, figure images, machine-readable outcomes,
and the final local commit receipt are ignored under `artifacts/hhl-2026-10-30/`
and `artifacts/executed-classroom/` in the integration worktree.

## Preservation and remaining limits

The original checkout's HEAD, index, staged/unstaged/untracked content, and file
modes remain intact. Existing Grover/QFT/QPE source and prior tests/notebooks,
dependency pins, workflow names, rulesets, QPE target limits, and the Shor
design contract are preserved.
The verified delivered v0.2 PDFs, original Grover rc1 tag/ZIP/PDF assets, and
reviewed QFT/QPE ZIP retain their recorded hashes. Nothing was pushed,
published, messaged externally, or submitted to IBM hardware.

**Skipped:** optional IBM Runtime/cloud and GPU paths. **Unimplemented/untested:**
Shor. **Untested:** native Windows/macOS, interactive setup, remote CI for this
local milestone, timed classroom delivery, and independent GPT Pro HHL review.
The new notebook is a bounded state-preparation demonstration with dense
classical work and compiled reciprocal rotations; no general solver or quantum
advantage is claimed. Five logical qubits, six controlled-power blocks, two QFT
directions, and seven rotations are logical construction counts, not measured
hardware/transpilation resource claims.

The instructor setup email is sent and a reply is pending; see the
[instructor review record](INSTRUCTOR_REVIEW_PLAN.md). Teaching choices may be
refined after that reply without inventing answers or changing verified PDFs.
Next implement the separate Shor contract, then prepare the combined HHL/Shor
review bundle and separate GPT Pro prompt. **GPT Pro sync is not needed for HHL
alone** under the accepted bounded contract; it is planned after Shor, or sooner
if a scope change or unresolved mathematical issue requires review.

Primary references for implementation details: [HHL paper](https://arxiv.org/abs/0811.3171),
[StatePreparation](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.StatePreparation),
[RYGate](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.RYGate),
and [ordered BitArray shot data](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.BitArray).
