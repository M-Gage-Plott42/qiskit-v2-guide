# Shor milestone: compiled full-domain N=15 contract

October 30, 2026. **Design only; implementation and circuit acceptance tests
are untested.** Choose a **compiled modular-permutation demonstration for N=15**,
with full four-qubit residue encoding. This is not a general reversible-arithmetic
library or a scalable factoring implementation. Its future source belongs in
`src/phys3810/shor.py`, tests in `tests/`, and lesson in `notebooks/05_shor.ipynb`.

## Model and QPE boundary

The existing `qpe_circuit` accepts only one/two target qubits and stays unchanged.
An N=15 residue register needs **four** target qubits, so implement a separately
scoped order-finding builder using the existing exact inverse QFT. Do not route
a four-target gate through QPE, widen its input bound, or describe dense powers
as general modular arithmetic. This is an explicit new bounded algorithm block.

For each supported multiplier, construct its full 16x16 permutation matrix and
wrap it as a current SDK `UnitaryGate`; controlled versions act on five qubits.
All 16 target basis states have a defined reversible action. This is a compiled
full-domain model, not a two-qubit encoding of only a known orbit. General
adder/multiplier networks with work-register uncomputation are a later scope.
IBM's [Shor tutorial](https://quantum.cloud.ibm.com/docs/en/tutorials/shors-algorithm)
discusses this permutation construction and its synthesis cost. Use its
mathematics, not deprecated QFT imports or hardware-service examples.

## Planned public interfaces and input behavior

- `modular_multiplier_15(multiplier)` returns a four-qubit gate.
- `order_finding_15(base, *, num_counting_qubits=4)` returns an unmeasured circuit
  with prepared residue `|1>`, no classical bits, and no extra work ancillas.
- `recover_order_15(base, outcome)` returns an integer order or `None` using the
  conservative exact-rational rule below. `outcome` is a counting bitstring.
- `factors_from_order_15(base, order)` returns sorted nontrivial factors or `None`.
- `classical_factor_15(base)` performs the separate GCD precheck, returning a
  sorted factor pair or `None`, without constructing a quantum circuit.

Base/multiplier/width/order inputs accept `numbers.Integral` except booleans.
Convert accepted integer scalars to Python integers. Do not silently reduce
negative/out-of-range arguments modulo 15. Quantum/recovery/factor functions
require base in the units `{1,2,4,7,8,11,13,14}`. The multiplier accepts the same
set, including identity 1 for powered constants. Base 1 is intentionally allowed
as an unproductive identity fixture; the default classroom trial uses base 2.

The classical precheck accepts bases 1 through 14. A noncoprime base such as 3,
5, or 6 gives a classical factor immediately; it is invalid input to the
quantum builder because multiplication would not be bijective. Do not count
that shortcut as successful quantum order finding.

Counting widths **4 through 6** are supported, default 4. Outcome strings must
contain only `0`/`1`, have one of those lengths, and contain no spaces or register
separators. The `order` argument to `factors_from_order_15` is restricted to
integers 1 through 14; a denominator derived during recovery can be larger and
then yields `None`, as specified below. Unsupported types raise
`TypeError`; malformed/range/noncoprime inputs raise `ValueError`. Well-formed
but inconclusive phase data or unsuccessful factor extraction returns `None`.
There is no arbitrary-modulus parameter or implicit general-N fallback.

## Full-domain reversible multiplication

For b in the unit set, define

`M_b |x> = |(b*x) mod 15>` for `0 <= x < 15`, and `M_b |15> = |15>`.

The corresponding matrix has coefficient **+1** at destination row/source
column and zero elsewhere; there are no hidden basis-dependent or global phases.
Both `|0>` and `|15>` are fixed. An all-X complement implements `15-x`, which
swaps those two states even though it agrees with multiplication by 14 on
1 through 14. Such a circuit fails this contract even if the `|1>` orbit looks
correct. Check all basis states, not only the states reached by the lesson.

Compute each powered constant as `b_j = pow(base, 2**j, 15)` and construct
`M_b_j` directly. Do not discover the order first, hard-code expected phase
peaks, initialize an order-dependent eigenstate, or exponentiate larger dense
matrices as a substitute for this declared oracle. Identity b_j=1 blocks may
be omitted by that value check; no known-order table drives construction.

## Registers, phases, and prepared-state expectation

The order-finding circuit assumes **all m+4 input qubits start at zero** and
includes residue preparation; unlike `qpe_circuit`, it is not a caller-prepared
target block. `count` occupies qubits `0..m-1`; `residue` occupies the next four.
Prepare residue `0001` with X on its least-significant qubit. Count starts at zero.
Apply H to each counting qubit, let count[j] control `M_b_j`, then apply
`qft_circuit(m, inverse=True, do_swaps=True)` to count. Full-state tensor order
is **residue tensor count**. There are no intermediate measurements.

Measure count[j] into classical bit j of a named `phase` register. A displayed
bitstring means `y=int(bits,2)` and phase `y/2**m`, with no output reversal.
The initial residue `|1>` is generally a superposition of multiplier
eigenstates; its mixture of phase outcomes is expected. The source never needs
to construct those eigenstates or know their order.

With `Q=2**m`, the independent full-state expectation is

`psi[z,y] = (1/Q) * sum(exp(-2*pi*i*x*y/Q) * [z == pow(a,x,15)] for x in range(Q))`.

This scalar modular/Fourier expression, not the implemented gate, defines the
test oracle. For true order r, supported outcomes are `y=s*Q/r`, each with
probability `1/r`. All N=15 unit orders divide four, so supported widths produce
exact grid phases. Default width 4 is a classroom choice, not a necessary or
general Shor precision guarantee; generic modulus precision/recovery is outside
this contract. Four **residue** qubits and four default **counting** qubits are
different design decisions.

## Conservative order recovery and factor extraction

General order recovery uses rational approximation/continued fractions; reduced
denominators can hide factors of the true order. See the
[IBM order-finding explanation](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/phase-estimation-and-factoring/shor-algorithm).
For this exact-grid, fixed-N model, deliberately use the narrower rule:

1. Validate input. Reject y=0 as inconclusive (`None`) before any order search.
2. Reduce the exact fraction `Fraction(y, 2**len(outcome))`; call its denominator q.
   If q is not below 15, return `None`.
3. Require `pow(base,q,15)==1`. If it fails, return `None`; do not try multiples
   of q or use a stored order table to fill in the missing period.
4. Require q to be minimal: for each distinct prime p dividing q,
   `pow(base,q//p,15)` must differ from 1. Reject nonminimal periods with `None`.
5. Return q only after those checks. Do not approximate off-grid fractions,
   aggregate samples by LCM, or reduce a nonminimal candidate in this first API.

The minimality check is sufficient: if the true order r is a proper divisor of
a verified q, some prime dividing q/r makes r divide q/p. Thus that check finds
any nonminimal verified period. It verifies a sampled candidate; it does not
brute-force the unknown order. Returning `None` is an expected trial outcome.

`factors_from_order_15` independently verifies the candidate period/minimality,
requires an even order, and calculates `x=pow(base,order//2,15)`. Reject x=1 or
x=14, then calculate `gcd(x-1,15)` and `gcd(x+1,15)`. Return only factors strictly
between 1 and 15 whose product is 15, sorted as `(3,5)`. Do not return x-1/x+1
without taking GCDs. Invalid types/ranges are errors; failed mathematical
conditions return `None`. The notebook uses one 2048-shot batch per explicitly
selected base: base 2 in the core, then bases 11 and 14 in the expansion, at
most three batches/6144 shots for that sequence. A selected batch may fail to
produce factors. There is no automatic or unbounded base-retry loop.

## Fixed fixtures and failure cases

- Base 2: orbit `(1,2,4,8)`, order 4, midpoint 4, factors `(3,5)`.
- Base 7: orbit `(1,7,4,13)`, order 4, midpoint 4, factors `(3,5)`.
  Bases 8 and 13 also have order 4; their respective orbits are `(1,8,4,2)`
  and `(1,13,4,7)`.
- Base 4: orbit `(1,4)`, order 2, midpoint 4, factors `(3,5)`.
- Base 11: orbit `(1,11)`, order 2, midpoint 11; GCDs are 5 and 3, not 10 and 12.
- Base 14: orbit `(1,14)`, order 2, midpoint 14. Order recovery can succeed,
  but factor extraction returns `None` because the GCDs are 1 and 15.
- Base 1: order 1, all-zero phase, no recovered order or factor. Supplying its
  actual odd order 1 to factor extraction also yields `None`.

For m=4 and order 4, bins `0000`, `0100`, `1000`, `1100` each have probability
1/4. For order 2, `0000` and `1000` each have probability 1/2. Scale integer
bin locations by `Q/16` for m=5/6; do not reverse strings.

Recovery fixtures must include:

- Base 2, `0100` or `1100`: return 4; factors then `(3,5)`.
- Base 2, `1000`: return `None` because denominator 2 is not its period.
- Any base, all-zero result: `None`; never manufacture an order from it.
- Base 11, `1000`: return 2; factors `(3,5)`.
- Base 14, `1000`: return 2; factor extraction still fails.
- Base 2, off-support `0010`: denominator 8 is a period but not minimal,
  so return `None`. Base 11 with `0100` similarly rejects nonminimal period 4.
- Noncoprime bases fail quantum/recovery validation; the separate classical
  GCD precheck succeeds for 3/5/6. Wrong widths, symbols, types, or order ranges
  are rejected. Wrong but well-formed candidate orders are unsuccessful results.

## Independent acceptance gates

1. Check all **128 basis images** across eight multiplier gates, including 0
   and 15, with exact +1 phase. Verify bijection, inverse multipliers, and
   `M_a M_b = M_(ab mod15)` over the entire domain.
2. Check every controlled basis image (16 residues times two control values per
   multiplier), including superposed control coherence. With local control bit
   least significant, its matrix is `I_16 tensor |0><0| + M_b tensor |1><1|`.
3. Verify powered constants, output/register roles, input immutability, lack of
   measurement/extra ancillas, and preservation of QPE's rejection of four targets.
4. Compare the complete prepared complex output and counting marginal against
   the independent scalar/Fourier formula for all bases and widths 4-6. Check
   norm, exact fixtures, and absence of unsupported basis outcomes. Do not fit
   away a phase or normalize away an error.
5. Test classical recovery independently of circuit construction. For every
   supported bitstring/base/width, compare against the known finite-fixture
   orders and exact reduced denominator; test all failure cases above. Those
   fixture orders belong in tests, never in production recovery/construction.
6. Test GCD prechecks and factor extraction independently, including odd orders,
   incorrect/nonminimal periods, trivial square roots, and sorted products.
7. Use local V2 sampling with seed 2026, explicit shot accounting, and six-sigma
   binomial bounds plus one-shot allowance for allowed bins. Unexpected bins
   fail the ideal simulation check; successful order recovery and successful
   factor extraction must be reported separately.

Use exact integer arithmetic for classical results. Use `rtol=0, atol=2e-11`
for complex operators, states, normalization, and probabilities. Preserve all
existing tests/strict notebook safeguards; no dependent runtime or hardware job
is part of classroom acceptance.

## Resources, teaching, and design evidence

The ideal circuit uses **m+4 = 8-10 logical qubits**. Each compiled multiplier
is 16x16; its controlled matrix is 32x32. Constants follow
`[a, a*a mod15, 1, ...]`, so at most two controlled multipliers are nonidentity.
Omitting identity constants is permitted; actual active counts are two for
order-4 bases, one for order-2 bases, and zero for base 1. `2**m-1` describes
naive repeated access to one U, not the number of multiplier blocks executed by
this design. Record actual decomposition/transpilation counts later with basis
and seed; no unexecuted gate-depth claim is made now.

Dense permutation storage/synthesis scales exponentially with residue width.
The known small modulus, exact dyadic orders, classical constants, simulation,
and readout are disclosed conveniences. This does not demonstrate a general
Shor speedup or practical cryptographic factoring. The relationship to the
general algorithm follows [Shor's original paper](https://arxiv.org/abs/quant-ph/9508027);
this contract specifies only a bounded teaching instance.

Session 3 reserves 20 core minutes for base 2: trace its orbit, predict the
phase bins, verify one useful denominator, and extract the GCD factors. The
10-minute expansion contrasts an inconclusive sample, base 11's GCDs, and
base 14's factor failure. Deriving a general arithmetic network or a continued
fraction approximation algorithm is not inside that time budget.

Later implementation must import canonical code into `05_shor.ipynb`, put
predictions before outputs, retain failed trials as honest outcomes, and add
fresh-kernel validator coverage with at least two meaningful figures (compiled
circuit and counting-distribution/recovery comparison). Keep sources output-free.

Classical design checks confirmed all 128 domain images, 1,024 composition
images, the listed orbits/GCDs, and exact-rational failure fixtures. No quantum
circuit or factoring implementation was built or run. Scratch evidence is
ignored under `artifacts/hhl-shor-design-2026-10-30/`. **Implementation tests
remain untested.** The existing 97-test/six-notebook baseline is unchanged.
