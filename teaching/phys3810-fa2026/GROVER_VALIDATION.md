# Grover milestone validation

October 29, 2026. **Grover was independently reviewed; its small exercise
correction is locally validated.** This record covers the Grover-only preview;
QFT development is separate. QPE, HHL, Shor, final classroom PDFs, and publication
remain future work. No IBM Runtime service or GPU was used.

## Source and scope

Work remains local on `feat/phys3810-m1-onboarding`, based on
`fb41ae02f2ece3e093e60c9286ef72ae91686530`. Earlier uncommitted milestone-1 work
and the existing index were preserved. There was no commit, push, PR, merge,
or release. The original audited commit remains 12 commits ahead of that base;
eventual upstream integration must preserve its newer fixes.

- `src/phys3810/grover.py` and `__init__.py`: phase oracle, exact diffusion,
  Grover iteration, and uniformly prepared search circuits.
- `tests/test_grover.py`: 20 independent mathematical/input-contract tests.
- `teaching/phys3810-fa2026/notebooks/01_grover.ipynb`: 20 cells, including
  9 executable cells; 50-minute core and 25-minute expansion.
- `scripts/validate_classroom.py`: Grover is the fourth required notebook;
  it must produce three PNG figures. Error/skip/completion safeguards remain
  active. The unfinished list now names only QFT, QPE, HHL, and Shor.
- `tests/test_grover_notebook.py`: five regressions execute editable exercise
  cells with alternative marked pairs and an M=2 plot. Expectations, messages,
  and legends follow the selected parameters.
- Student instructions separate preclass Run All from in-class prediction;
  the circuit diagram labels preparation, oracle, and diffusion blocks.

The [contract](GROVER_PLAN.md) restricts the implementation to 2–5 qubits,
distinct enumerated binary targets, uniform preparation, and explicit
nonnegative iteration counts. The rightmost string bit is qubit 0. Empty and
all-marked sets, duplicates, malformed targets, and invalid integer parameters
are rejected, even when iterations are zero. Outputs have no measurements,
classical bits, or ancillas. Oracle construction costs are acknowledged; no
scalability or quantum-advantage claim is made.

## Independent mathematical checks

The tests calculate expectations directly from matrices, amplitude updates,
and the analytic formula; SDK agreement is an additional check.

- All **60 single-target operators** across 2–5 qubits are compared against
  independent diagonal matrices, checking every input basis state and every
  off-diagonal entry. Multiple-target and asymmetric `001`/`011` cases are added.
- Diffusion equals `2|s><s| - I`, including complex-amplitude reflection about
  the mean. Iteration equals `D O`, with exact relative and global conventions.
- Full states agree with a classical amplitude recurrence; normalization holds.
- **90 analytic cases** span supported sizes, several marked fractions, and
  iteration counts 0–5. All five required rational fixtures pass: zero-step
  `M/N`, single-target probabilities `1` and `121/128`, multiple-target `1`,
  and overshooting to `1/4`.
- The SDK reference oracle is built from an independent diagonal matrix;
  only the `grover_operator()` comparison allows an irrelevant global phase.
- Seeded V2 samples satisfy shot accounting, bitstring support, and a six-sigma
  binomial tolerance; the source circuits remain unmeasured.

Primary references checked for the implementation are IBM's
[Grover operator API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.grover_operator),
[bit-ordering guide](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering),
and [circuit API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.QuantumCircuit).
The code uses `MCXGate` without deprecated class wrappers or synthesis-mode arguments.

## Executed checks

Environment: Linux x86_64, CPython **3.12.15**, Qiskit **2.6.1**, Aer **0.17.2**,
nbclient **0.11.0**, NumPy **2.5.4**, Matplotlib **3.11.2**. Dependency files are
unchanged from the validated classroom environment.

- `python -m unittest discover -s tests -p test_grover.py -v`: **20 passed**.
- `python scripts/validate_classroom.py`: **passed** in the corrected Grover-only
  checkout, including `pip check`, **50 tests**, and four required notebooks in
  fresh interpreter-bound kernels. This adds five exercise tests to the original
  45-test suite; all configuration, mathematics, and runner regressions remain.
- The final Grover notebook was also executed from its own directory, and
  through the strict runner after a presentation-only adjustment: **passed**,
  all 9 code cells and 3 embedded PNGs. Source outputs/counts remain empty.
- The circuit, histogram, and probability-iteration curve were visually
  inspected. Seed 2026 gave **1940 marked shots out of 2048** for target `001`
  after two iterations, consistent with the exact probability `121/128`.
- `bash scripts/smoke_local.sh artifacts/milestone2-grover/executed-local-smoke`:
  **passed**, retaining both original smoke notebooks.
- Ruff, pre-commit/Markdown/YAML checks, shellcheck, actionlint, local links,
  source notebook-format checks, and diff whitespace checks: **passed**.

The first full run preceded a small legend/global-phase presentation refinement;
targeted execution and the exported-source run checked the final notebook.
No algorithm code changed after its passing mathematical tests.

## Standalone bundle check

A source ZIP from the original Grover milestone was extracted into a path with
spaces, without `.git`, and its validator passed **45 tests and all four notebooks**. This reused the existing
classroom interpreter and installed packages; it was not a new dependency
installation. Runtime code, tests, dependency files, and the final Grover
notebook were verified byte-for-byte against the tested export.

The requested final delivery is one curated standalone ZIP, with canonical
runtime files and concise bundle-specific setup/orientation documentation.
It excludes prompts, policy/chat documents, unrelated history, duplicate text
exports, Git metadata, caches, credentials, logs, and generated notebook outputs.
The review prompt is supplied separately in the chat response.

Original curated-bundle validation: **passed**, with **45 tests and all four notebooks**
executed from the extracted standalone folder. The 23-file export contains
20 canonical project files and three adapted orientation documents (README,
setup, and short course overview). The check reused the existing classroom
environment; native Windows/macOS and a new dependency installation were not
tested. Final packaging changes only this evidence note and README clarification;
all runtime files are verified against the executed candidate. Detailed logs
remain local under ignored `artifacts/milestone2-grover/`, outside the bundle.

The independent reviewer reproduced the original 45-test/four-notebook result
on Linux CPython 3.12.14 using the same installed pins; no new dependency install
was claimed for that review. It confirmed the algorithm and prior M1-01 fix,
then identified the editable-target/legend issue. The corrected preview's
50-test result is local CPython 3.12.15 evidence, not a claim that GPT Pro
retested the correction. Current correction logs are in `artifacts/grover-review/`.

## Limits and next step

- **Untested:** native Windows/macOS, interactive JupyterLab/editor use, remote
  CI and failure-artifact upload, and other Python patch builds for Grover.
- **Skipped:** IBM Runtime service, hardware jobs, and GPU execution. The
  earlier fake-backend smoke is not a new Grover or hardware validation result.
- **Not implemented:** QFT, QPE, HHL, and Shor.
- **Pending at source preparation:** remote preview CI and final platform
  validation. A proposed preview is not an existing public release.

The next development action is QFT, with a separate Grover-only preview prepared
for instructor feedback. No manual code audit is assigned to the user. Keep the
later QFT/QPE-before-HHL/Shor checkpoint; no extra review round is needed solely
for the demonstrated small notebook corrections.
