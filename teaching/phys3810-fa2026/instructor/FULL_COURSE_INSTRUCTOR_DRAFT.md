# PHYS 3810 full-course instructor companion

**Document v0.1 draft · October 31, 2026 · proposed code v0.2.0-rc1.**
This is provisional instructor material, including answer cues. The candidate
contains all five bounded algorithm lessons, but its full-course download and
matching PDFs are **unpublished**. This Markdown draft has not been rendered,
visually reviewed, or OCR-checked as a new PDF.

Use the separate [student setup companion](../handouts/FULL_COURSE_SETUP_DRAFT.md)
for onboarding. The proposed future archive is
`PHYS3810-Fall2026-v0.2.0-rc1.zip`, with top-level folder `phys3810-fa2026`;
no live download URL or available package is implied. The candidate baseline
is `d491b3b59fe08e92aec29cfbdcb74b4eaa816556`, whose runtime source preserves
the accepted implementation. See [the document input record](../R6_DOCUMENT_INPUTS.md)
for the draft/source relationship and remaining handoff inputs.

The older Grover document-v0.2 PDFs describe code-v0.1.0-rc1, not this proposed
five-lesson candidate. Their document number does not make them full-course
guides. Keep those editions, their links, and the published Grover assets intact.

## Teaching decisions remain provisional

Rick's reply is pending. Dates, number and duration of meetings, in-class versus
outside-class coverage, student Python/Jupyter preparation, delivery role,
platforms, assessment, and preferred examples remain unconfirmed. The three
sessions below are a proposed route, not an assigned schedule or grading plan.
Providing all five tested implementations does not settle which topics receive
classroom time.

Check the intended prerequisite level: complex amplitudes and normalization,
tensor products, eigenvalues/eigenvectors, measurement, circuit controls, and
modular arithmetic/GCDs. Use the short refreshers in the run sheets rather than
assuming those topics have been covered. A setup activity before the first
meeting is proposed; its deadline and delivery method are not assigned here.

The notebook code, assertions, and explanatory cells already reveal worked
results. Keeping this instructor guide out of a student package does **not**
make the remaining notebooks assessment-safe. Agree solution release,
collaboration, and submission expectations before creating any assessed variant.
No graded variant or homework assignment has been created by this draft.

## Environment and evidence that can be claimed

Use 64-bit CPython 3.12 with the unchanged requirements and constraints:
Qiskit 2.6.1, Aer 0.17.2, and the documented pip 26.2.2 installer. Git, IBM
accounts, credentials, GPUs, and hardware jobs are unnecessary for default
classroom execution. Installation needs access to the pinned packages;
subsequent default validation and demonstrations are local.

- **Fresh installation passed:** [R1](../R1_FRESH_LINUX_VALIDATION.md) used a
  new application environment on Ubuntu 26.04.1 LTS x86_64 with CPython 3.12.15.
  It passed 160 tests and all eight notebooks. This was not a newly installed
  operating system or Python interpreter.
- **Interactive JupyterLab passed:** [R2](../R2_INTERACTIVE_VALIDATION.md)
  observed Chrome/JupyterLab 4.6.4, explicit named-kernel selection, restart/run
  all, all 16 figures, save, shutdown/relaunch, and selected reruns. To preserve
  the frozen environment, it used an isolated `JUPYTER_DATA_DIR` and
  `ipykernel install --user`, with the kernelspec pointing to the retained
  interpreter in a sibling `venv`. It did not execute the ordinary
  `--sys-prefix` registration in a newly created in-project `.venv` through UI.
  That historical R2 result does not certify the ordinary path; the later R6
  walkthrough below supplies separate evidence for the student-guide sequence.
- **Current runtime checks passed:** [R5](../R5_CANDIDATE_VALIDATION.md) reused
  the R1 environment and reran the required checks on unchanged runtime source:
  160 tests, eight fresh-kernel notebooks, 50 nonempty code cells, and 16 PNGs.
  It did not reinstall packages, perform a new UI run, or test a sealed student
  archive. The separate unit and validator invocations repeat the same 160 tests.
- **Student-guide walkthrough passed:**
  [R6](../R6_GUIDE_WALKTHROUGH_VALIDATION.md) used a new in-project `.venv`,
  installed the unchanged pins, registered the named kernel with `--sys-prefix`,
  and passed the full 160-test/eight-notebook/50-cell/16-PNG validator. Actual
  JupyterLab UI execution also covered all eight notebooks and all 16 figures;
  shutdown/reopening and cleared-output preflight/Shor reruns passed. Jupyter
  settings were isolated to preserve existing user configuration, and the local
  browser URL was opened manually. Automatic browser opening, a fresh Python/OS
  install, and an unpublished package download were not tested. No setup-command
  repair was needed; later guide edits record evidence without changing commands.
- **Untested:** native Windows x64, macOS ARM64 and Intel, native VS Code/Cursor
  interpreter/kernel selection, and human pacing rehearsal. Exact Chrome version
  remains unverified. [Native procedures](../R3_NATIVE_PLATFORM_VALIDATION.md)
  are prepared; package resolution and Linux execution are not native-host
  evidence. Required classroom platforms or alternatives await agreement.

Do not alter pins to resolve an ad hoc student setup problem. Record the actual
OS, selected interpreter, command, and error, then correct the supported setup
path and its evidence. A passing terminal validator and a wrong interactive
kernel can coexist; compare the notebook's printed interpreter with the terminal.

## Notebook inventory and preparation checks

Run `python scripts/validate_classroom.py` from the complete course-folder root
using the selected environment. It checks dependencies, runs the mathematical
and runner tests, and starts a separate interpreter-bound kernel for each
required notebook. No skip tag or tolerated error may hide an unexecuted cell.
Sources remain output-free; executed copies go to `artifacts/executed-classroom/`.

1. [Preflight](../notebooks/00_setup_preflight.ipynb): 4 code cells, 2 PNGs.
2. [Local statevector smoke](../../../notebooks/00_local_statevector_smoke.ipynb):
   3 code cells, no PNG requirement.
3. [Local Aer smoke](../../../notebooks/01_local_aer_smoke.ipynb): 4 code cells,
   no PNG requirement.
4. [Grover](../notebooks/01_grover.ipynb): 9 code cells, 3 PNGs.
5. [QFT](../notebooks/02_qft.ipynb): 7 code cells, 2 PNGs.
6. [QPE](../notebooks/03_qpe.ipynb): 8 code cells, 3 PNGs.
7. [HHL](../notebooks/04_hhl.ipynb): 7 code cells, 3 PNGs.
8. [Compiled Shor](../notebooks/05_shor.ipynb): 8 code cells, 3 PNGs.

The total is **50 code cells and 16 PNGs**, with all three figures required in
both HHL and Shor. Smoke notebooks are setup checks, not two extra lessons.
The expected final line is `PASSED: classroom validation`; optional Runtime/GPU
execution is explicitly skipped, not passed. Inspect errors and incomplete
execution rather than trusting a remembered histogram or printed success alone.

Before presenting, make an execution copy, restore the defaults, select the
correct kernel for every notebook, and run all cells. Retain a real executed
copy for diagnosis or a clearly labeled fallback. Before predictions, restart
the live kernel and clear displayed outputs. Keep separate notebook kernels;
shared variable names do not imply shared state. After an editable parameter
changes, rerun the dependent calculation and plotting cells in order.

All reference and expansion code remains required in validation even if live
discussion uses only a core route. A skipped discussion segment is not evidence
that learners completed it. If live execution fails, say so; retained output
may support explanation but cannot establish that the current run passed.

## Proposed three-session route

The [presenter index](../R4_PRESENTER_RUN_SHEETS.md) links the detailed prediction,
transition, exercise, debrief, and fallback sequence. Each 75-minute route adds
25 minutes to its 50-minute core. These budgets are proposed human teaching
minutes; [machine timing results](../R4_DEMONSTRATION_TIMINGS.md) are separate.
No completed human rehearsal or learner exercise-completion time is claimed.

1. [Grover run sheet](R4_SESSION_1_GROVER.md): 5 minutes readiness/notation,
   10 oracle, 10 diffusion, 20 small search and sampling, 5 exit/debrief.
   Add 15 minutes marked sets/input-contract practice and 10 overshooting.
2. [QFT/QPE run sheet](R4_SESSION_2_QFT_QPE.md): 5 minutes phase/bit order,
   15 QFT, 10 QPE controlled powers, 15 exact phases, 5 decoding/debrief.
   Add 15 minutes nonexact distributions and 10 precision/wrap-around.
3. [HHL/Shor run sheet](R4_SESSION_3_HHL_SHOR.md): 5 minutes QPE refresher,
   20 HHL, 20 compiled Shor, 5 limitations. Add 15 minutes HHL scaling/complex
   states and 10 successful versus unsuccessful order/factor recovery.

Budget explanations and transitions inside those blocks; fast simulation does
not create extra teaching time. The third core traces two prepared examples;
it does not derive general HHL or reversible arithmetic from scratch. Record a
real presenter run-through and revise segments before finalizing delivery.

## Algorithm contracts and instructor answer cues

Across displayed binary strings, the rightmost bit is qubit 0 and is least
significant. A counting result `bits` means `int(bits, 2) / 2**m` unless a
separate phase-to-eigenvalue conversion is stated. Do not add an unexplained
string reversal to make a histogram match expectations.

### Grover: marking changes phase; diffusion changes probabilities

The [Grover contract](../GROVER_PLAN.md) supports 2–5 qubits, a finite nonempty
set of distinct marked strings of the correct width, and explicit nonnegative
integer iterations. The all-marked set, duplicates, malformed strings, and
boolean/fractional counts are rejected. The search circuit prepares the uniform
state and applies `D O` per iteration; returned circuits are unmeasured.

**Prediction and answer:** with `N=4, M=1`, one iteration gives total marked
probability 1, while two iterations reduce it to 1/4. With `N=8, M=1`, two
iterations give 121/128. With `N=8, M=2`, one iteration gives 1. The independent
formula is `sin((2*r+1)*theta)**2`, `theta=asin(sqrt(M/N))`; zero iterations give
`M/N`. An oracle's minus sign alone does not change basis probabilities.

Acceptance checks cover the oracle on every basis state and analytic
amplification, with an additional SDK comparison. The notebook's three-qubit
sampling uses 2048 shots, seed 2026. Enumerated targets and oracle construction
are explicit costs; these small ideal examples do not establish search advantage.

### QFT: relative phases carry information that probabilities hide

The [QFT contract](../QFT_PLAN.md) supports exact 1–6-qubit transforms, all
controlled rotations retained, no ancillas or measurements. With swaps enabled,
`F[j,k]=exp(+2*pi*i*j*k/N)/sqrt(N)`; the inverse is `F.conj().T`. With bit-reversal
permutation R and swaps disabled, the forward operator is `R @ F` and its
inverse is `F.conj().T @ R`. Omitting swaps is a convention change, not the same
operator with an insignificant drawing difference.

**Prediction and answer:** for three qubits and input `011` (integer 3), the
first amplitude is `1/sqrt(8)` and the phase at output index 1 is `+3*pi/4`.
All eight probabilities are 1/8. Input `001` also has uniform probabilities,
but different relative phases. Inverse QFT of the correctly prepared phase
gradient returns the original string; the notebook samples 256 shots, seed 2026.

Acceptance uses the complete independently calculated Fourier matrix, including
sign, normalization, and swaps, plus complex-state and SDK checks. A successful
forward/inverse round trip alone is insufficient. Full dense validation grows
exponentially; state loading and amplitude readout are not free FFT speedups.

### QPE: decode the declared counting register directly

The [QPE contract](../QPE_PLAN.md) supports 1–6 counting qubits and numeric
unitaries on **one or two target qubits**. The caller prepares the target state
and zero count input; the helper does not prepare or certify an eigenstate.
Count qubits occupy `0..m-1`, targets follow, and full-state tensor order is
target then count. Count qubit j controls `U**(2**j)`, followed by inverse QFT
with swaps. Measure count[j] into classical bit j.

For `U|u>=exp(+2*pi*i*phi)|u>`, the phase is modulo one. **Prediction and answer:**
three bits give `1/8 -> 001`, `3/8 -> 011`, and `6/8 -> 110`; reverse neither
the displayed strings nor the canonical circuit. The pinned SDK reference has
an explicitly reconciled output reversal, which belongs only in that comparison.

For nonexact phase 1/3, outcomes form a distribution. Its most likely bin is
3/8 for three bits and 11/32 for five bits, with errors 1/24 and 1/96. More
counting bits refine the grid without guaranteeing every sampled result is
closer. A superposition of eigenstates with different phases generally entangles
target and count; measuring only count gives the weighted phase distribution.
A superposition within one degenerate eigenspace need not create entanglement. The notebook uses 2048 shots per
chosen precision and seed 2026.

Independent acceptance checks compare asymmetric exact cases, the nonexact
distribution, full complex states/operators, target preservation, and global
phase on U. Dense 2x2/4x4 validation and powered gates are disclosed small-case
choices; m controlled-power blocks do not imply m general black-box U calls.

### HHL: check raw branches before conditioning

The [HHL contract](../HHL_PLAN.md) accepts finite 2x2 Hermitian A with eigenvalues
in `{1,2,3,4,5,6,7}` and a normalized complex length-two b. Complex eigenbases
and repeated eigenvalues are supported. The family is positive definite with
condition number at most 7. Zero, negative, off-grid, or aliased eigenvalues,
unnormalized b, and other dimensions are rejected; no implicit rescaling or
approximate fallback is provided.

The five-qubit circuit starts from all zero and prepares b itself: count 0–2,
system 3, success flag 4; tensor order is success, system, count. Fix
`U=exp(+i*pi*A/4)`, so phase is lambda/8 and the three-bit integer label is
`y=lambda`. The high bit is not a sign bit. Fix C=1 and rotate the flag by
`2*asin(1/y)` for y=1–7; label zero is the identity. Then invert the same QPE
block on count/system. Do not invert b's preparation or reset the success flag.
Count clears to `000` on both branches only under this exact-spectrum contract.

**Prediction and answer:** for `A=[[1.5,0.5],[0.5,1.5]]`, `b=(1,0)`, raw success
is `(3/4,-1/4)`, success probability is 5/8, and the normalized successful state
is `(3,-1)/sqrt(10)`. Raw failure is `(sqrt(3)/4,sqrt(3)/4)` with probability 3/8.
The flag-conditioned X/Y/Z means are `-3/5,0,4/5`; Z alone misses relative sign.
For `b=(1,i)/sqrt(2)`, the answer is `(3-i,-1+3i)/sqrt(20)` and X/Y/Z are
`-3/5,4/5,0`. Doubling A for the default b leaves the normalized answer unchanged
but lowers success to 5/32 because C stays fixed.

Acceptance compares raw success amplitudes with a classical linear solve,
independent failure amplitudes, both-branch count cleanup, total norm, success
probability, and relative complex phase. Sampling uses 4096 shots per X/Y/Z
basis, seed 2026; condition the system on the flag from the **same shot**.
An empty selected sample has no defined conditional mean. This returns a
postselected quantum state, not a free classical solution vector. Dense
exponentiation, seven-entry reciprocal lookup, loading, synthesis, postselection,
and readout are costs; generic sparse-HHL scaling is not demonstrated.

### Compiled Shor: recovered order and extracted factors are different outcomes

The [Shor contract](../SHOR_PLAN.md) fixes N=15 and unit bases
`{1,2,4,7,8,11,13,14}`, with four residue qubits and 4–6 counting qubits.
It uses a separate order-finding builder, leaving QPE's one/two-target limit
unchanged. The compiled 16x16 permutation acts as `|x> -> |a*x mod15>` for
0–14 and fixes 15, with coefficient +1. Both 0 and 15 stay fixed; matching
only the orbit of 1 is insufficient. Noncoprime bases belong to a separate
classical GCD precheck, not a successful quantum trial.

Start all m+4 qubits at zero. The builder prepares residue `0001`, uses count
qubits `0..m-1` controlling multipliers `pow(a,2**j,15)`, and applies inverse
QFT with swaps. Tensor order is residue, count. The residue is a superposition
of multiplier eigenstates; its counting outcomes form a phase distribution.
The circuit uses 8–10 logical qubits and no extra work register. Dense compiled
permutations are not a scalable reversible-arithmetic implementation.

**Prediction and answer:** base 2 has orbit `(1,2,4,8)` and order 4. With four
count bits, `0000`, `0100`, `1000`, `1100` each have probability 1/4. Quarter
phases certify order 4 and factors `(3,5)`; zero is inconclusive, and 1/2's
denominator 2 is not base 2's period. Theoretical per-shot order and factor
success probabilities are both 1/2. For base 11, `1000` certifies order 2 and
GCD factors `(3,5)`; base 14 can yield order 2 but only trivial GCDs, so factor
extraction fails. An unsuccessful result is retained, not repaired by guessing.

Recovery reduces the exact measured fraction, rejects zero, verifies a period
below 15 and its minimality, then requires an even order and nontrivial square
root before taking GCDs. It does not try denominator multiples, general
continued-fraction approximation, LCM aggregation, or an automatic retry loop.
The lesson uses 2048 shots per explicitly selected base, seed 2026; the base
2/11/14 sequence is at most three batches. Exact dyadic phases for this N=15
family do not establish a general factoring precision guarantee.

Acceptance covers all 128 multiplier basis images, controlled coherence,
independent complete modular/Fourier states, each supported width/base, and
classical order/factor failures. The modest high-level circuit is not evidence
of low hardware synthesis cost or practical cryptographic factoring capability.

## Before the document handoff and classroom distribution

Use [R6_DOCUMENT_INPUTS.md](../R6_DOCUMENT_INPUTS.md) as the current input and
decision record. Before final PDFs, settle the teaching choices above; decide
the actual supported student platform path and close its setup/UI gaps; perform
and record the presenter rehearsal; settle solution distribution; and freeze
the intended source, document edition, package layout, and download wording.
Keep unvalidated targets explicitly untested if a provisional review occurs.

The literal Ubuntu student-guide walkthrough has now passed in an isolated
working copy, with R1/R2 preserved. Keep its exact source/guide identity and
configuration limits in the linked receipt. The next local step can prepare a
provisional document-review handoff; no final teaching decision or unsupported
platform claim should be inferred from the successful Linux setup check.

The subsequent GPT Pro document handoff must contain actually accessible files
and identify the exact reviewed snapshot. Rendering, visual inspection, OCR,
metadata, and link checks belong to that PDF creation/review step; this Markdown
turn supplies none of those PDF results. Returned files need downloadable bytes
and hashes of the delivered files, including provenance, before integration.
Do not infer file transfer from a screenshot, filename card, or private link.

After supplied PDFs are verified, a separately scoped package step must build
the new full-course archive and verify an extraction with all required content
and counts. Preserve original reviewed archives and Grover assets. No existing
Grover-only ZIP, guide, or package-builder whitelist substitutes for the new
candidate. Publication remains a later authorized workflow, not a consequence
of this draft's presence in the repository.
