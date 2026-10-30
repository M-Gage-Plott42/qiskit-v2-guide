# Grover: instructor review guide

PHYS 3810 | Review draft v0.1 | October 29, 2026

> {{DOWNLOAD_NOTE}}

This outline accompanies the standalone **phys3810-grover** preview and its setup guide. It is an early teaching draft: session dates, student preparation, assessment expectations, and native platform requirements remain unconfirmed.

## Learning goals and preparation

By the end of the lesson, students should explain phase marking, interpret diffusion as reflection about the mean, predict marked-state probability, and distinguish exact statevector results from finite-shot samples. They should also explain why too many iterations can reduce success.

**Prerequisites:** complex amplitudes, probability as squared magnitude, normalization, Hadamard gates, basis-state labels, and basic Python/Jupyter use. Installation and preflight should be completed before class. Treat the code as a guided experiment; reading every validation assertion aloud would exceed the core period.

**Before teaching:** run the validator and all cells for readiness. For the classroom sequence, restart the kernel and clear outputs. Ask each prediction before executing the corresponding cell. Confirm that students can identify preparation, oracle, and diffusion in the circuit figure.

## 50-minute core

- **0-5 minutes | Readiness and notation.** Confirm the selected kernel. Review the rightmost-bit/qubit-0 convention using `001` and `011`. Address interpretation, not package installation.
- **5-15 minutes | Phase oracle.** Predict what changes after marking `001`. Inspect the amplitude sign and unchanged uniform probabilities. Ask what later interference can use that immediate measurement cannot reveal.
- **15-25 minutes | Diffusion.** Connect `D = 2|s><s| - I` to `a_x -> 2*mean(a) - a_x`. Apply oracle first, diffusion second. Compare the exact expected matrix and amplitude update.
- **25-45 minutes | Single-target lab.** Predict the four-state case, then inspect its circuit. Move to eight candidates and two iterations; compare exact `121/128` with a sampled histogram and explain statistical variation.
- **45-50 minutes | Exit discussion.** Explain phase versus probability, operation order, retaining an unmeasured circuit, and the predicted effect of one extra iteration.

## 75-minute version

Add **15 minutes for marked-set experiments**, including the short input-contract activity: vary the two-target pair, inspect each selected state's probability, and explain why duplicate targets are rejected. Add **10 minutes for overshooting**: compare the analytic curve with exact results, vary the marked count, and read the parameter-aware legend.

The expansion code still executes during validation. Optional discussion time is not permission to skip required correctness cells. A timed rehearsal is still needed to confirm pacing for this class.

References: [IBM Grover operator](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.grover_operator) and [IBM bit ordering](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering). QFT/QPE and HHL/Shor follow later; they are not part of this Grover-only preview.

<!-- pagebreak -->

## Mathematical checkpoints and review questions

Review draft v0.1 | Answers for instructor preparation

## Answer checkpoints

- **Bit order:** `001` has integer index 1; `011` has index 3 and sets qubits 1 and 0. Circuit wire order is distinct from displayed string order.
- **Oracle only:** for a uniformly prepared three-qubit state, marking `001` changes its amplitude sign but leaves every basis-state probability at `1/8`.
- **Diffusion:** every amplitude becomes twice the mean minus its old value. The implementation fixes the exact sign convention for `D`; an overall phase does not alter standalone measurement probabilities.
- **Iteration:** `Q = D O`. Uniform preparation occurs once, before the repeated iterations. Measuring between oracle and diffusion destroys the coherent experiment being illustrated.
- **Probability:** with `N = 2**n`, `M` distinct targets, and `theta = asin(sqrt(M/N))`, total marked probability is `sin((2*r + 1)*theta)**2`.
- **Four candidates, one target:** `r=0 -> 1/4`, `r=1 -> 1`, and `r=2 -> 1/4`.
- **Eight candidates, one target:** one iteration gives `25/32`; two give `121/128`.
- **Eight candidates, two distinct targets:** one iteration gives total probability 1, split as `1/2` for each target. Changing the pair changes the marked labels, not these probabilities.

## Scope and evidence

The reusable implementation supports **2-5 qubits**, explicit distinct binary targets, and nonnegative integer iteration counts. It rejects malformed, empty, duplicate, and all-marked sets. Returned circuits have no measurements or ancillary qubits; the notebook measures a copy for V2 sampling.

The preview expects {{TEST_SUMMARY}} and four required notebooks. This includes the original onboarding checks, exact Grover/operator tests, runner failure regressions, and exercise-variation coverage. The three Grover figures support distinct teaching goals: circuit structure, finite samples, and oscillatory amplification.

Executed evidence is local Linux simulation with pinned Python 3.12/Qiskit 2.6.1/Aer 0.17.2. Native Windows/macOS, interactive editor/browser behavior, hardware, GPU, and remote CI are not established by a PDF review. See the bundle's validation record for the precise runs and limitations.

This enumerated oracle is a teaching construction, not an end-to-end search benchmark. Oracle construction, synthesis, preparation, and readout have costs; counting oracle calls alone does not establish quantum advantage.

## Decisions to confirm with the instructor

- What are the actual session dates and available meeting lengths?
- How much Python/Jupyter, complex-vector, tensor-product, and circuit background can be assumed?
- Which native platforms or managed lab machines must be supported?
- Are exercises exploratory, submitted, or graded? What collaboration and accommodation expectations apply?
- Does the guided prediction-and-interpretation format fit the course, and which extension activities should be retained?
