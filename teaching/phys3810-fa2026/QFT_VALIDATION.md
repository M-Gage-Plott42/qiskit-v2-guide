# QFT milestone validation

October 29, 2026. **QFT is implemented and locally validated.** This record
covers the development checkout, not the Grover-only preview commit. QPE,
HHL, and Shor remain unimplemented. The next substantive independent checkpoint
is after QFT/QPE and before HHL/Shor.

## Implementation and expectations

`src/phys3810/qft.py` builds the exact transform from H, controlled-phase, and
optional SWAP gates on 1–6 qubits. `qft_circuit` is exported from the course
package. It introduces no measurements, classical bits, or ancillas and retains
all rotation angles. See [QFT_PLAN.md](QFT_PLAN.md) for the complete contract.

For `N=2**n`, the forward matrix is
`F[j,k]=exp(+2*pi*1j*j*k/N)/sqrt(N)` in Qiskit's rightmost-qubit-0 ordering.
With `R` denoting bit reversal, the no-swaps operator is `R @ F`, while its
inverse is `F.conj().T @ R`. The inverse is the adjoint of the selected full
forward circuit, not a separately reversed output-label convention.

`tests/test_qft.py` adds **14 tests**. Independent NumPy matrices cover every
entry of the Fourier, inverse, and two no-swaps operators for each supported
size. Further checks cover both composition orders, normalized complex states,
asymmetric phase ramps, strict input validation, and V2 sampling of independently
prepared known phase-gradient states. SDK `QFTGate` comparison is additional;
the expected mathematics is not derived from that reference. Exact matrix
checks retain global phase, sign, and normalization.

## Teaching notebook

[02_qft.ipynb](notebooks/02_qft.ipynb) has **16 cells, 7 executable**. It covers
the first 20 minutes of the combined session: 5 minutes refreshing phase/bit
conventions and 15 minutes connecting matrices, phase patterns, and inversion.
Core exit questions belong inside that time. Additional complex-state/swap
practice is explicitly follow-up work; QPE will complete the 50/75-minute plan.

The notebook imports canonical source, compares full complex matrices, and
shows that equal computational-basis probabilities do not identify a Fourier
phase pattern. It independently prepares a known gradient and uses inverse QFT
plus V2 sampling to recover its label. This is explicitly not a QPE algorithm.
Editable parameters drive expectations, titles, and sampled labels.

Two figures were rendered and visually inspected: a three-qubit circuit and
real/imaginary amplitudes with the corresponding uniform-probability panel.
Sources remain output-free. Before-class Run All and in-class prediction-first
instructions are distinct.

## Executed validation

Environment unchanged: Linux x86_64, CPython **3.12.15**, Qiskit **2.6.1**,
Aer **0.17.2**, nbclient **0.11.0**. No package migration or new classroom
dependency was needed.

- `python -m unittest discover -s tests -p test_qft.py -v`: **14 passed**.
- Additional source self-check: **24 full matrix cases**, **12 SDK comparisons**,
  and **12 roundtrip cases** passed across 1–6 qubits.
- Notebook execution from its own folder: **passed**, all seven code cells,
  two PNGs, and default inverse-gradient counts `{'011': 256}`.
- Four isolated notebook parameter variations passed: three-qubit labels `001`
  and `110`, two-qubit `10`, and four-qubit `1010`.
- `python scripts/validate_classroom.py`: **passed**, including `pip check`,
  **64 tests**, and **five required fresh-kernel notebooks**. This retains
  the 50 corrected Grover/onboarding tests and adds 14 QFT tests.
- Python/Markdown/YAML/shell/Actions lint, source-notebook checks, local links,
  and diff whitespace checks passed during integration.

The runner now requires the QFT notebook and its two PNGs, and reports only
QPE, HHL, and Shor as unfinished. Its prior forced-error, skip rejection,
execution-count, and partial-output safeguards remain intact.

Local evidence is under ignored `artifacts/qft/`. The corrected Grover preview
was independently validated from its own extracted ZIP with 50 tests and four
notebooks; those are intentionally different versioned deliverables.

## Limits and next step

Native Windows/macOS, interactive editor/browser use, other Python patch builds
for QFT, hardware/GPU execution, remote CI, and timed teaching rehearsal remain
untested here. The logical gate count is quadratic; full matrix checking,
arbitrary input preparation, and readout have separate costs. No classical-FFT
speedup or quantum advantage is claimed.

Proceed to QPE using the stated sign and register-order conventions, including
asymmetric exact phases and a nonexact distribution. GPT Pro sync is not needed
for QFT alone; the planned substantive check follows QFT/QPE before HHL/Shor.

Primary references: [IBM QFTGate](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.QFTGate)
and [IBM bit ordering](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering).

## Subsequent local integration, October 30

Documentation and verified PDF bytes are tracked in local commit
`b16d235ca01ebc9c7f610dcfeb64f081d5d6b453`. The following QFT commit carries
forward the existing implementation and its evidence; see
[INTEGRATION_VALIDATION.md](INTEGRATION_VALIDATION.md) for the new execution
results. The original checkout/index and published Grover rc1 assets remain
intact. QPE is next. No new release or instructor message was sent.

## Combined QFT/QPE checkpoint, October 30

QPE is now locally validated with the shared Fourier convention and explicit
SDK output-order normalization. The current suite passes 92 tests and six
notebooks; see [QPE_VALIDATION.md](QPE_VALIDATION.md). This earlier QFT-only
evidence remains historical. The combined independent review is now due.
