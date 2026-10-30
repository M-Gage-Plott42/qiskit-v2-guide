# PHYS 3810 · Fall 2026 course plan

Three invited lecture/lab sessions for UTC **Introduction to Quantum Information
Science and Technology**, planned for mid-to-late November 2026. This is a
proposed teaching sequence; actual session dates are **not yet confirmed**.

## Requested deliverables

Rick Mukherjee requested a brief, linked PDF covering Python environment
creation and Qiskit installation in basic steps, plus working, tested,
commented code for **Grover's algorithm, QFT, QPE, HHL, and Shor's algorithm**.
Students will use this public repository. Downloading a release archive must
be sufficient; Git knowledge, IBM accounts, credentials, and QPUs are not
prerequisites.

Milestone 1 supplies a draft setup guide for validation. Early setup/instructor
review PDFs may be prepared now; produce the final classroom PDF after its
instructions have been validated and feedback incorporated. Grover has since
been implemented as milestone 2; QFT, QPE, HHL, and Shor are later work. See
[STATUS.md](STATUS.md) for current validation and review state.

## Scheduling and preparation

UTC has no classes **November 25–29, 2026**; **November 30, 2026** is the last
class day. These constraints were checked against the
[official UTC academic calendar](https://www.utc.edu/academic-affairs/registrar/calendars-and-schedules/academic-calendar-fall-2026-summer-2027)
on October 29, 2026. They do not establish dates for the invited sessions.

Confirm with the instructor before finalizing lesson depth and exercises:

- Session dates, room, and whether each meeting allows 50 or 75 minutes.
- Students' Python/Jupyter experience and access to supported computers.
- Prior coverage of complex vectors, tensor products, eigenvalues, phase,
  measurement, and circuit notation.
- Assessment expectations: participation, submitted notebooks, graded problems,
  collaboration policy, and accommodations.

Proposed preparation is the setup/preflight notebook before session 1. Until
background is known, include short refreshers and provide runnable examples
alongside optional exercises. No grading scheme is assumed.

## Proposed sessions

### 1. Grover: phase oracles and amplitude amplification

**50-minute core:** 5 minutes to confirm preflight and notation; 10 minutes on
phase marking and the oracle contract; 10 minutes on the diffusion operation;
20 minutes to inspect a small search circuit and compare its probabilities
with the analytic result; 5 minutes for a prediction/check discussion.

**75-minute expansion:** add 15 minutes to vary the marked state or marked set
and 10 minutes to examine too many iterations. Students should explain why
success probability oscillates and distinguish oracle cost from query count.

### 2. QFT and QPE: extracting phase

**50-minute core:** 5 minutes reviewing complex phase and bit order; 15 minutes
connecting QFT to the Fourier matrix; 10 minutes on controlled powers and
inverse QFT in QPE; 15 minutes predicting and checking exact phase examples;
5 minutes interpreting the output register.

**75-minute expansion:** add 15 minutes on a nonexact phase and its distribution
and 10 minutes varying precision. Use asymmetric exact phases so reversing bits
changes the answer. Students should connect resolution to counting qubits.

### 3. HHL and Shor: applications and limits

**50-minute core:** 5 minutes recalling QPE; 20 minutes tracing a small HHL
example, its postselection, and normalized solution state; 20 minutes tracing
small-instance Shor order finding through classical factor extraction;
5 minutes discussing assumptions and resource costs.

**75-minute expansion:** add 15 minutes comparing HHL with a classical solve,
including relative sign and uncomputation, and 10 minutes exploring successful
and unsuccessful order/factor recovery. These are restricted instructional
examples; explain state preparation, readout, and arithmetic costs explicitly.

## Milestones and acceptance criteria

1. **Scope, environment, onboarding — review correction completed.** Inventory the
   existing repository; record the actual base and audit relationship; provide
   the course landing page, plan, status, setup draft, and preflight notebook.
   Resolve an exact Python 3.12 dependency environment with visualization and
   notebook support. Retain smoke checks, add assertions and an offline `.env`
   test, and execute classroom notebooks in fresh kernels. Record actual
   installed versions, results, and platform limitations. Prepare independent
   review before implementing algorithms. The assistant handles technical
   review and remediation using [WORKFLOW.md](WORKFLOW.md); the user is not
   expected to inspect the diff or run tests manually.
2. **Grover lesson — reviewed and corrected; preview preparation underway.** Follow
   [the explicit input and test contract](GROVER_PLAN.md).
   Add commented canonical source, notebook explanation and
   exercises, and independent tests of basis-state oracle action and analytic
   amplification probabilities. Check SDK reference agreement and fresh-kernel
   execution in the supported environment.
   Prepare a clearly marked standalone preview and draft guides for instructor
   feedback before all five algorithms are finished. Publication remains a
   separately authorized action through the normal repository workflow.
3. **QFT/QPE lessons — next implementation stage.** Compare the QFT operator with the full Fourier matrix;
   test QPE on asymmetric exact phases and a nonexact phase distribution.
   Document sign/bit conventions and verify SDK references and fresh kernels.
4. **HHL/Shor lessons.** Specify supported small cases and limitations. For HHL,
   test postselection, uncomputation, normalization, and relative sign against
   a classical solve. For Shor, independently test modular arithmetic, order
   recovery, and factor extraction, including failure cases. Execute notebooks
   in fresh kernels; avoid removed HHL/Shor imports and unsupported advantage
   claims.
5. **Teaching release.** Validate setup instructions on the claimed classroom
   platforms, render and inspect the short linked PDF, rehearse the timed
   sessions, and check every notebook from a downloaded archive. Record any
   intentionally unsupported platforms and unresolved teaching decisions.
   Publication requires a separate maintainer action after review.

Use current SDK circuits and V2 primitives. Canonical reusable implementations
live in `src/phys3810/`, tests in `tests/`, and teaching notebooks in this
directory's `notebooks/`. See [AGENTS.md](../../AGENTS.md) for validation and
public-artifact conventions, and [STATUS.md](STATUS.md) for observed progress.
Maintainer coordination, per-turn recommendations, and GPT Pro checkpoints are
recorded in [WORKFLOW.md](WORKFLOW.md).
