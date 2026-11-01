# PHYS 3810: full-course instructor guide

<!-- markdownlint-disable-next-line MD036 -->
**REVIEW DRAFT · Document v0.1 · Proposed code v0.2.0-rc1**

This provisional guide includes instructor answer cues for five bounded algorithm lessons. It is **not final classroom approval**. The full-course student download is **unpublished**. Use the separate student setup guide for onboarding; the earlier Grover-only edition does not cover all five lessons.

## Teaching decisions remain open

Rick's reply is pending. Confirm dates, meeting count and duration, in-class versus outside-class coverage, Python/Jupyter preparation, delivery role, classroom platforms or alternatives, assessment and solution expectations, and preferred examples. Providing five implementations does not settle how much classroom time each receives.

Check prerequisites: complex amplitudes and normalization, tensor products, eigenvalues/eigenvectors, measurement, circuit controls, and modular arithmetic/GCDs. Use the run-sheet refreshers rather than assuming prior coverage. A setup activity before the first meeting is proposed; no deadline or delivery method is assigned here.

**Worked answers are already present.** Notebook code, assertions, and explanations reveal results. Withholding this instructor guide does not make the notebooks assessment-safe. Agree collaboration, solution release, and submission expectations before creating an assessed variant. This draft creates no graded variant or homework assignment.

## Proposed three-session route

Each 75-minute option adds 25 minutes to its 50-minute core. These are **proposed teaching budgets**; human pacing and learner completion times are untested.

| Session | 50-minute core | Add 25 minutes for 75 |
| --- | --- | --- |
| Grover | 5 readiness/notation; 10 oracle; 10 diffusion; 20 search/sampling; 5 debrief. | 15 marked sets/input contracts; 10 overshooting. |
| QFT/QPE | 5 phase/bit order; 15 QFT; 10 controlled powers; 15 exact phases; 5 decoding/debrief. | 15 nonexact distributions; 10 precision/wrap-around. |
| HHL/Shor | 5 QPE refresher; 20 HHL; 20 compiled Shor; 5 limitations. | 15 HHL scaling/complex states; 10 order/factor successes and failures. |

Budget explanations and transitions inside these blocks. The third core traces two prepared examples; it does not derive general HHL or reversible arithmetic from scratch. Rehearse and revise the route before finalizing delivery. Machine execution times do not establish teaching pace.

Course references are paths in the complete course folder. Under `teaching/phys3810-fa2026/`, see `COURSE_PLAN.md` and the three presenter run sheets: `instructor/R4_SESSION_1_GROVER.md`, `instructor/R4_SESSION_2_QFT_QPE.md`, and `instructor/R4_SESSION_3_HHL_SHOR.md`.

<!-- pagebreak -->

## Environment, evidence, and preparation

Use **64-bit CPython 3.12**, Qiskit 2.6.1, Aer 0.17.2, and pip 26.2.2 with the unchanged requirements and constraints. Installation needs package access; default validation and demonstrations then run locally. Git, IBM accounts, credentials, GPUs, and hardware jobs are unnecessary.

### Recorded course evidence

The supplied `VALIDATION_EVIDENCE.md` records Ubuntu 26.04.1 LTS x86_64 / CPython 3.12.15 checks. R6 followed the student guide in a new in-project `.venv`: `--sys-prefix` registration, validation, and actual JupyterLab 4.6.4 execution of eight notebooks and 16 figures, save, shutdown/reopening, and selected reruns. This was a fresh application environment, not a fresh OS or Python installation.

R6 isolated Jupyter settings and opened the local URL manually; automatic opening was untested and the Chrome version is unverified. R5 and the separately reported sealed-archive check reused environments. These supplied records are not a new browser test by this review.

**Untested:** native Windows x64, macOS ARM64/Intel, VS Code/Cursor interpreter/kernel UI, human pacing, IBM Runtime, GPUs, and hardware. Windows ARM64 and 32-bit Python are outside the draft's target. Linux/package-resolution results do not certify native hosts.

### Required notebook inventory

Run `python scripts/validate_classroom.py` from the complete course root in the selected environment. The required check is **160 tests, eight fresh-kernel notebooks, 50 nonempty code cells, and 16 PNGs**.

| Notebook | Code cells | PNGs |
| --- | --- | --- |
| Preflight | 4 | 2 |
| Local statevector smoke | 3 | 0 |
| Local Aer smoke | 4 | 0 |
| Grover | 9 | 3 |
| QFT | 7 | 2 |
| QPE | 8 | 3 |
| HHL | 7 | 3 |
| Compiled Shor | 8 | 3 |
| **Total** | **50** | **16** |

Smoke notebooks are setup checks, not extra lessons. Success ends with `PASSED: classroom validation`; Runtime/GPU execution is **skipped**, not passed. No skip tag or tolerated error may hide an unexecuted cell. Sources remain output-free; executed copies go to `artifacts/executed-classroom/`.

### Prepare the live session

Restore defaults in a copy, compare each notebook's interpreter with the terminal, and run all cells in separate kernels. After edits, rerun dependent cells in order. Before predictions, restart and clear outputs. Keep an executed fallback, but disclose live failures: old output is not a current pass. Validation still requires all reference and expansion code, even when discussion uses only the core route.

<!-- pagebreak -->

## Grover and QFT: exact conventions

The rightmost displayed bit is qubit 0 and is least significant. A count string `bits` decodes as `int(bits, 2) / 2**m` unless a separate phase-to-eigenvalue conversion is stated. Do not add a string reversal just to match a histogram. See [IBM's bit-ordering guide](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering).

### Grover: phase marking, then diffusion

`GROVER_PLAN.md` supports 2–5 qubits, a finite nonempty set of distinct marked strings of the correct width, and explicit nonnegative integer iterations. All-marked sets, duplicates, malformed strings, and boolean/fractional counts are rejected. Circuits are unmeasured.

The search prepares the uniform state `|s>` and applies `D O` per iteration: oracle first, diffusion second. The exact diffusion is `D = 2|s><s| - I`. A marked basis amplitude changes sign under the oracle; phase marking alone does not change basis probabilities.

| Prediction | Total marked probability |
| --- | --- |
| N=4, M=1, one iteration | 1 |
| N=4, M=1, two iterations | 1/4: overshooting |
| N=8, M=1, two iterations | 121/128 |
| N=8, M=2, one iteration | 1 |
| Zero iterations | M/N |

The independent formula is `sin((2*r+1)*theta)**2`, with `theta=asin(sqrt(M/N))`. Acceptance checks every oracle basis action and analytic amplification, with an additional SDK comparison. The notebook samples its three-qubit example with 2048 shots, seed 2026. Enumerating targets and constructing the oracle cost resources; these small ideal examples do not establish search advantage.

### QFT: relative phases matter

`QFT_PLAN.md` supports exact 1–6-qubit transforms, retaining every controlled rotation, without ancillas or measurements. With swaps:

`F[j,k] = exp(+2*pi*i*j*k/N)/sqrt(N)`

The inverse is `F.conj().T`. For bit reversal R, disabling swaps gives forward `R @ F` and inverse `F.conj().T @ R`. Omitting swaps changes the operator, not just its drawing.

**Answer cue:** three-qubit input `011` (integer 3) gives first amplitude `1/sqrt(8)` and output-index-1 phase `+3*pi/4`. All probabilities are 1/8. Input `001` also has uniform probabilities but different relative phases. Inverse QFT of the correctly prepared phase gradient returns the input string; sampling uses 256 shots, seed 2026.

Acceptance uses the full independently calculated Fourier matrix, sign, normalization, swaps, complex states, and an SDK comparison. A forward/inverse round trip alone is insufficient. Dense validation grows exponentially; state loading and amplitude readout are not free FFT speedups.

<!-- pagebreak -->

## QPE: register roles and direct decoding

`QPE_PLAN.md` supports **1–6 counting qubits** and numeric unitaries on **one or two target qubits**. The caller prepares the target and zero count input; the helper neither prepares nor certifies an eigenstate. Shor's separate four-residue-qubit builder does not expand this limit.

### Circuit and phase convention

Count qubits are `0..m-1`; target qubits follow. Full-state tensor order is target then count. Count qubit j controls `U**(2**j)`, followed by inverse QFT with swaps. Measure count[j] into classical bit j.

For `U|u> = exp(+2*pi*i*phi)|u>`, phase is modulo one. Decode the count string directly as an integer divided by `2**m`.

| Exact phase, three counting bits | Expected string |
| --- | --- |
| 1/8 | `001` |
| 3/8 | `011` |
| 6/8 | `110` |

Reverse neither these strings nor the canonical circuit. The pinned Qiskit 2.6.1 SDK reference has an explicitly reconciled output reversal; that correction belongs only to the comparison.

### Nonexact phases and mixed phase distributions

For phase 1/3, results form a distribution. The most likely bin is 3/8 with three bits and 11/32 with five bits; absolute errors are 1/24 and 1/96. More bits refine the grid without guaranteeing that every sampled result is closer. The notebook uses 2048 shots per selected precision, seed 2026.

A superposition of eigenstates with different phases generally entangles target and count. Measuring only count gives the eigenstate-weighted phase distribution. A superposition within a single degenerate eigenspace need not create entanglement.

**Global phase matters under control.** A phase multiplying an uncontrolled U becomes a relative phase in controlled-U. Discarding it can change the estimated phase, even though it would not change an isolated target's basis probabilities.

### Acceptance and teaching limits

Independent checks compare asymmetric exact phases, nonexact probability distributions, full complex states/operators, target preservation, and global phase on U. Dense 2×2/4×4 validation and powered gates are explicit small-case choices. Having m controlled-power blocks does not mean m general black-box calls to U; implementing powers has a cost.

Use the exact label predictions before sampling. Ask learners why uniform QFT basis probabilities do not erase the phase information that QPE decodes. The optional nonexact and wrap-around discussion remains a proposed expansion, not promised classroom coverage.

Official background: [IBM's phase-estimation procedure](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/phase-estimation-and-factoring/phase-estimation-procedure). Its general explanation does not enlarge this course helper's supported inputs.

<!-- pagebreak -->

## HHL: inspect both raw branches

`HHL_PLAN.md` accepts finite Hermitian 2×2 A with eigenvalues in `{1,2,3,4,5,6,7}` and normalized complex length-two b. Complex eigenbases and repeated eigenvalues are supported. A is positive definite with condition number at most 7. Zero, negative, off-grid, or aliased eigenvalues, unnormalized b, and other dimensions are rejected. There is no implicit rescaling or approximate fallback.

### Evolution, reciprocal rotation, and uncomputation

The five-qubit circuit starts at all zero and prepares b itself: count qubits 0–2, system 3, success flag 4. Tensor order is success, system, count.

- Fix `U = exp(+i*pi*A/4)`. Phase is lambda/8, so the three-bit integer label is `y=lambda`. The high bit is not a sign bit.
- Fix C=1. Rotate the flag by `2*asin(1/y)` for y=1–7; label zero acts as the identity.
- Invert the **same QPE block** on count/system. Do not invert b's preparation or reset the flag.

Count returns to `000` in **both flag branches** only under this exact-spectrum contract.

### Default answer cues

For `A=[[1.5,0.5],[0.5,1.5]]` and `b=(1,0)`:

| Quantity | Exact result |
| --- | --- |
| Raw success amplitudes | `(3/4,-1/4)` |
| Success probability | `5/8` |
| Normalized successful state | `(3,-1)/sqrt(10)` |
| Raw failure amplitudes | `(sqrt(3)/4,sqrt(3)/4)` |
| Failure probability | `3/8` |
| Conditional X/Y/Z means | `-3/5, 0, 4/5` |

Z measurement alone misses the relative sign. For `b=(1,i)/sqrt(2)`, the successful state is `(3-i,-1+3i)/sqrt(20)` and X/Y/Z are `-3/5,4/5,0`. Doubling A with the default b preserves the normalized answer but lowers success to **5/32**, because C stays fixed.

### Check amplitudes before normalizing

Acceptance compares raw success with a classical linear solve, independent failure amplitudes, both-branch count cleanup, total norm, success probability, and relative complex phase. Sampling uses 4096 shots per X/Y/Z basis, seed 2026. Condition the system on the success flag from the **same shot**. An empty selected sample has no defined conditional mean.

This returns a postselected quantum state, not a free classical solution vector. Dense exponentiation, the seven-entry reciprocal lookup, state loading, synthesis, postselection, and readout all cost resources. The lesson does not demonstrate generic sparse-HHL scaling.

<!-- pagebreak -->

## Compiled Shor: order is not yet factors

`SHOR_PLAN.md` fixes **N=15**, unit bases `{1,2,4,7,8,11,13,14}`, **four residue qubits**, and **4–6 counting qubits**. It uses a separate order-finding builder; QPE's one/two-target limit is unchanged.

### Full-domain coherent multiplication

The compiled 16×16 permutation maps `|x> -> |a*x mod15>` for x=0–14 and fixes 15, with coefficient +1. Both 0 and 15 remain fixed; checking only the orbit of 1 is insufficient. Noncoprime bases belong to a separate classical GCD precheck, not a successful quantum trial.

Start all m+4 qubits at zero. The builder prepares residue `0001`; count qubits `0..m-1` control multipliers `pow(a,2**j,15)`, followed by inverse QFT with swaps. Tensor order is residue then count. The residue is a superposition of multiplier eigenstates, producing a counting-phase distribution.

This uses **8–10 logical qubits**, with no extra work register. Dense compiled permutations are not scalable reversible arithmetic; a short high-level circuit does not establish low hardware synthesis cost.

### Predictions and recovery outcomes

Base 2 has orbit `(1,2,4,8)` and order 4. With four count bits, `0000`, `0100`, `1000`, and `1100` each have probability 1/4.

| Base and observation | Conservative result |
| --- | --- |
| Base 2, phase 1/4 or 3/4 | Order 4; GCD factors `(3,5)`. |
| Base 2, phase 0 | Inconclusive. |
| Base 2, phase 1/2 | Denominator 2 is not a period; no recovered order. |
| Base 11, string `1000` | Order 2; GCD factors `(3,5)`. |
| Base 14, recovered order 2 | Only trivial GCDs; factor extraction fails. |

For base 2, theoretical per-shot order success and factor success are both **1/2**. Preserve unsuccessful outcomes rather than repairing them by guessing.

Recovery reduces the exact measured fraction, rejects zero, verifies a period below 15 and its minimality, then requires an even order and a nontrivial square root before taking GCDs. It does not try denominator multiples, general continued-fraction approximation, LCM aggregation, or an automatic retry loop.

The lesson uses 2048 shots per explicitly selected base, seed 2026; the base 2/11/14 sequence is at most three batches. Exact dyadic phases in this N=15 family do not establish a general factoring precision guarantee.

### Acceptance and limits

Acceptance covers all 128 multiplier basis images, controlled coherence, independent full modular/Fourier states, every supported width/base, and classical recovery failures. This bounded demonstration makes no claim of practical cryptographic factoring capability.
