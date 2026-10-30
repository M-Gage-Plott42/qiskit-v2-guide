# QFT milestone: exact transform contract

The next local module follows the reviewed Grover lesson. This contract is the
QFT portion of the planned QFT/QPE session; QPE remains a separate subsequent
implementation. A combined phase-convention review is due after both are tested,
before HHL/Shor work.

## Supported API and conventions

`qft_circuit(num_qubits, *, inverse=False, do_swaps=True)` returns an unmeasured
`QuantumCircuit` with no classical bits or ancillas. The teaching scope is exact
transforms on **1 through 6 qubits**, with all controlled-phase rotations retained.
Qubit counts accept `numbers.Integral` values excluding booleans. Both flags must
be Python booleans. Wrong types raise `TypeError`; out-of-range counts raise
`ValueError`.

In the basis indexed by displayed bitstrings, qubit 0 is the rightmost and least
significant bit. With `N = 2**num_qubits`, the default forward transform is

`F[j, k] = exp(+2*pi*1j*j*k/N) / sqrt(N)`.

`inverse=True` gives the inverse of the selected forward circuit. Let `R` be
the permutation that reverses the bits of each row index:

- Forward, swaps enabled: `F`.
- Forward, swaps disabled: `R @ F`.
- Inverse, swaps enabled: `F.conj().T`.
- Inverse, swaps disabled: `F.conj().T @ R`.

The placement of `R` differs for the inverse because it reverses the entire
selected circuit. Omitting swaps is not silently treated as the same operator.
Reference comparison uses current `QFTGate`, never the deprecated `QFT` class.

## Acceptance checks

- Build full complex Fourier matrices independently for every supported size;
  compare every matrix entry, including sign and normalization, with explicit
  tolerances. Check inverse and both swap conventions.
- Verify forward/inverse composition and recovery of complex normalized states.
- Use asymmetric basis/phase examples so reversal changes the interpretation.
- Compare with `QFTGate` as an additional reference, not the source of expected
  mathematics. Do not ignore global phase in the exact matrix contract.
- Test invalid counts/flags and confirm no measurements or ancillas.
- Execute `notebooks/02_qft.ipynb` from a fresh interpreter-bound kernel and
  add it to required classroom validation. Preserve Grover and runner regressions.

## Teaching and limitations

The notebook covers the first **20 minutes of session 2**: a 5-minute phase/bit
refresher followed by 15 minutes connecting QFT circuits with the Fourier matrix.
QPE will complete the planned 50-minute core and 75-minute expansion. Extra QFT
matrix exercises are follow-up practice, not uncounted scheduled minutes.

The implementation uses explicit H, controlled-phase, and optional SWAP gates.
Its circuit has quadratic controlled-phase gate count, while this small full
matrix validation grows exponentially. Arbitrary data loading and full amplitude
readout are not free; these examples do not demonstrate a general classical-FFT
speedup or quantum advantage. The next substantive GPT Pro checkpoint remains
after QFT/QPE, before HHL/Shor.
