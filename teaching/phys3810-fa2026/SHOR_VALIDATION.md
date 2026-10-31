# Shor and combined HHL/Shor local validation

Current review status: the independent HHL/Shor review has been received and
accepted. [The reconciliation](HHL_SHOR_REVIEW_RECONCILIATION.md) records the
reviewed 158-test snapshot and subsequent 160-test local follow-up. The original
milestone evidence below retains its historical counts and pre-review status.

## Original milestone record

October 30, 2026. **158 tests and eight required fresh-kernel notebooks passed.**
The compiled N=15 Shor milestone follows HHL commit
`234c6084c414664a33b6c5856f22b0aa322325ca`, retaining all **129 existing tests**.
The new tests comprise 19 source tests and ten actual-notebook regressions.
See [SHOR_PLAN.md](SHOR_PLAN.md) for the supported family and
[HHL_PLAN.md](HHL_PLAN.md) for HHL's exact-spectrum contract. The combined
independent GPT Pro review is pending; local self-review is not that review.

## Implemented behavior and independent checks

`src/phys3810/shor.py` provides `modular_multiplier_15`, `order_finding_15`,
`recover_order_15`, `factors_from_order_15`, and `classical_factor_15`.
The multiplier acts on all 16 residue basis states, fixing 0 and 15 with +1
phase. Bases/multipliers are units modulo 15, including deliberately unproductive
base 1. The classical precheck separately accepts bases 1-14. Counting widths
are 4-6, output strings are strict binary, and invalid types/ranges/noncoprime
inputs fail explicitly. No implicit modulo reduction or general-N fallback exists.

The order-finding circuit prepares residue |1> from all zeros, uses constants
`pow(base, 2**j, 15)`, skips only identity constants, and invokes canonical inverse
QFT with swaps. Four residue qubits follow the counting register, giving full
state order residue tensor count. Count[j] maps directly to phase[j]; no reversal
is applied. QPE source and its one/two-target input contract remain unchanged.

Source tests independently check:

- All **128 multiplier basis images**, full-domain bijection, inverse gates,
  and all 64 pairwise compositions (1,024 basis images).
- All **256 controlled basis images** and coherent control superpositions,
  including 0 and 15. Full matrices retain phase, not just probabilities.
- All **24 base/width combinations**, comparing the entire prepared complex
  state to a scalar modular/Fourier sum, plus norm, counting marginal, residue
  support, register roles, controlled constants, and resource bounds.
- All **896 supported counting strings across bases and widths**, against
  independent finite-fixture orders and exact reduced denominators; every zero,
  insufficient, oversized, or nonminimal candidate remains inconclusive.
- All **112 base/order candidates** for factor extraction, including odd orders,
  wrong/nonminimal periods and trivial roots. The 14 classical GCD prechecks
  are separate from quantum construction. Inputs/instances remain independent.
- Seeded local V2 sampling, exact shot accounting, allowed-bin checks, and
  six binomial standard errors plus one shot. Order recovery and factor
  extraction are tested as separate outcomes.

All complex operator/state/norm/probability checks use `rtol=0, atol=2e-11`.
Classical results use exact integer arithmetic. Recovery verifies the sampled
exact denominator as a minimal period; it never tries multiples, searches for
an order to fill missing information, or uses a production order table.

The teaching notebook imports canonical source and contains **15 cells, eight
nonempty code cells**, and three figures. Actual-cell tests change bases and
widths, independently check closed orbit amplitudes, plot labels/values, recovery
and factor counts, and exercise invalid inputs and deliberately bad sampled
histograms. Expansion uses exactly two further batches, for bases 11 and 14;
there is no automatic retry loop. Source notebooks have empty outputs/counts.

## Observed example and costs

For default base 2, width 4, seed 2026, 2048 shots, the observed bins were
`0000:494`, `0100:511`, `1000:519`, `1100:524`. Each ideal bin has probability
1/4. The two quarter-phase bins recovered order 4 and factors (3,5): 1035 shots.
Zero and half-phase samples remained inconclusive. These particular counts are
observations, not exact-count acceptance requirements.

Bases 11 and 14 each produced 1043 useful half-phase samples out of 2048.
Both recovered order 2; base 11 obtained (3,5), while base 14 obtained no factors.
The complete notebook sequence uses three batches, **6144 shots**. This contrasts
order recovery, unsuccessful factor extraction, and the separate classical GCD
shortcut without converting a failed trial into a success.

Logical resource bounds are 8-10 qubits and at most two nonidentity controlled
16x16 multipliers (32x32 with control). The default circuit actually transpiled
to **813 u gates and 489 cx gates, depth 923**, using Qiskit 2.6.1,
`basis_gates=['u','cx']`, optimization level 1, seed 2026, and no hardware target
or coupling restriction. Its complete prepared state was rechecked. These are
local synthesis counts, not hardware cost or performance. Dense construction,
small fixed modulus, and exact dyadic orders do not establish general Shor
scaling or a quantum advantage. No scalable arithmetic network is claimed.

## Required execution and preservation

Reused environment: CPython **3.12.15**, Linux x86_64/glibc 2.43, Qiskit **2.6.1**,
Aer **0.17.2**, NumPy **2.5.4**, nbclient **0.11.0**, nbformat **5.10.4**,
ipykernel **7.4.0**, Matplotlib **3.11.2**. No dependency change or fresh install
is claimed. Separate Python 3.12 maintainer tools provide Ruff 0.15.22,
yamllint 1.38.0, and pre-commit 4.7.0. Caches are local; BLAS/OpenMP use two threads.

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

All commands **passed**. The strict validator reran 158 tests and all eight
notebooks in fresh interpreter-bound kernels: **50 nonempty code cells**,
no error outputs, **16 PNG figures**. Its skip rejection, forced errors,
execution-count checks, and partial-output preservation remain intact. Shor is
required with at least two PNGs; it produced three, all visually inspected.
The original Bash smoke entry point also passed.

Source notebook schema/output cleanliness, local documentation links, whitespace,
and baseline-byte preservation checks passed. Original checkout/index, staged
and untracked work, verified v0.2 PDFs, original Grover rc1 tag/ZIP/PDF assets,
and the earlier QFT/QPE review ZIP remain unchanged. No existing algorithm
computational source, prior test, dependency pin, workflow, or ruleset changed.
Only the package exports and required-notebook inventory extend earlier code.

Detailed logs and receipts are ignored under `artifacts/shor-2026-10-30/` in the
integration worktree. The standalone combined-review ZIP has its own exact
commit/hash, manifest, canonical-byte/adaptation checks, and extracted execution
receipt. That verification runs outside both checkouts; an existing pinned
interpreter is explicitly a reused environment, not a fresh installation.

## Review and remaining work

**GPT Pro sync: due** for the combined HHL/Shor technical review before publication.
The packet includes all regression dependencies, output-free notebooks, pinned
requirements, mathematical contracts, concise evidence, and standalone setup.
It excludes prompts, policy/chat records, unrelated history, PDFs for the older
Grover snapshot, generated outputs, caches, credentials, and Git metadata.
Code/tests/notebooks/dependencies retain exact committed bytes. Contract exports
may adapt only navigation/status context, with mathematical sections verified
unchanged; the repository QPE contract is preserved byte for byte.

**Skipped:** optional Runtime/cloud and GPU. **Untested:** native Windows/macOS,
interactive setup, remote CI for local milestones, timed classroom delivery,
and independent HHL/Shor review. The instructor reply remains pending. No
publication, external messages, release changes, or hardware jobs occurred.
After the actual review returns, reproduce findings and reconcile its disposition;
then plan teaching refinements, platform checks, and the final publication path.

Primary references: [Shor's paper](https://arxiv.org/abs/quant-ph/9508027),
[IBM modular-permutation tutorial](https://quantum.cloud.ibm.com/docs/en/tutorials/shors-algorithm),
and [UnitaryGate control API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.UnitaryGate).
