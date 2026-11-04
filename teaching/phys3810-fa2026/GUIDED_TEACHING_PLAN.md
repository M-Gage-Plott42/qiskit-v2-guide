# Beginner guided-practice contract

November 2, 2026. Material development: **Gage Plott**. The current teaching
requirements are two or three classes before Thanksgiving, no assumed Python
experience, and instructor demonstrations repeated on student laptops. There
is no grading, evaluation, assignment, or submitted work. Receipt of materials
is acknowledged; detailed approval and delivery after a walkthrough remain open.

## Route and boundaries

The proposed route is Python/Qiskit; Grover; QFT/QPE. With only two meetings,
use Python/Qiskit plus Grover, or substitute the preferred single algorithm day.
HHL and the full compiled-N=15 Shor lesson remain references. A short Shor
demonstration requires an explicit replacement, not an added block. All five
tested implementations remain available with unchanged mathematical contracts.

Use the listed 85-minute period: 75 minutes planned activity plus ten minutes
of margin, retaining a 50-minute fallback. The provisional November 16/19/23
dates are not confirmations; November 19 is Thursday and conflicts with the
listed Monday/Wednesday pattern. Final dates/count, algorithm priority, laptop
setup/support, prior quantum coverage, and delivery responsibility after the
walkthrough remain open. No private calendar details or correspondence belong
in the teaching materials.

## Notebook contract

Three new notebooks under `notebooks/guided/` import canonical implementations.
Existing eight reference/validation notebooks remain unchanged and output-free.

- **Day 1:** cells and execution order, variables/numbers/text/lists, imports,
  function calls, circuit methods, X/H, sampling and histograms, save/restart.
  Explain terminal versus notebook code. Read-only setup/support code is marked;
  learners need not know loops, arrays, matrix construction, or classes.
- **Day 2:** two qubits, one target among `00`, `01`, `10`, `11`, and iteration
  count 0, 1, or 2. Independent target probabilities are 1/4, 1, 1/4. Every
  advertised edit recomputes circuit, counts, analytic expectation, and caption.
- **Day 3:** two-qubit QFT basis inputs `01` and `10`, visible real/imaginary
  amplitudes, and inverse-QFT recovery. Fourier sign is positive; full output
  swaps are used. QPE separately uses three counting qubits and one target,
  explicitly initialized to the eigenstate |1>. Supported guided phases are
  3/8 and 1/8, yielding `011` and `001`. Qubit 0 is the rightmost/least-significant
  bit. Divide a counting label by 8 for its phase; basis labels alone are integers.

Keep nonexact phases, target mixtures, SDK convention normalization, and advanced
derivations outside this core. Every example is complete: no TODO blanks,
withheld solutions, or submissions. Rebuilding from a fresh circuit prevents
gate accumulation on rerun. Seeds and shot counts are explicit. Finite samples
are distinguished from exact probabilities; simulated examples assert no
quantum advantage or scalable oracle/arithmetic construction.

## Validation acceptance

The default validator retains exactly the existing eight-notebook inventory.
`python scripts/validate_classroom.py --profile all` adds the guided three
through the same strict engine, for eleven total. Preserve dynamic `ROOT` and
`NOTEBOOKS` overrides, Python/pin checks, fresh kernels, every required code cell,
skip/error rejection, figure checks, and partial output on failure.

Focused independent regressions cover all advertised target/iteration/phase
edits, asymmetric labels, QFT complex amplitudes, exact recovery, reset/rerun,
dynamic expected values/captions, strict profile failures, and isolated import
resolution. Keep existing 160 regressions and pins. Report measured totals for
this revision; do not relabel the old 160/eight/50/16 evidence as a new run.

Run the full suite once through the all-profile validator for source acceptance,
plus lint/smoke and relevant focused probes. A second full run is required from
the exact final ZIP extraction because that validates a different deliverable.
Retain separate source and package receipts and fresh-versus-reused labels.

## Review-kit acceptance

The [four concise entrance documents](guided/START_HERE.md) explain the route,
decisions, student operation, and presenter cell transitions. The dedicated
exporter places them at the root and the complete runnable tree under `runtime/`.
It preserves canonical source/tests/dependencies, all eleven notebooks, license,
and needed technical references, with manifest origins and payload hashes.
Exclude old PDFs, prompts, policy/history, correspondence, credentials, caches,
environments, and executed outputs. Do not modify frozen release builders.

Extract into a separate path containing spaces, verify all paths/links/hashes,
execute the all profile, confirm course imports stay inside that extraction,
and confirm source payload bytes remain unchanged. Render the four concise
documents and all three executed guided notebooks to HTML/PNG for visual and
OCR checks. OCR corroborates readable text; independent numerical tests establish
correctness. This does not claim new PDF, native-platform, interactive UI, or
human-pacing validation. Historical PDF editions remain unchanged and excluded.

Only the current name **Gage Plott** belongs in new editable teaching materials.
Student/instructor-facing prose must not contain model names or internal
coordination notes. Technical test results and input limits remain explicit.
The two archived Grover PDF/companion pairs retain their historical attribution;
a corrected supplied edition is needed before reusing them as current handouts.

## Primary-source research, November 2

- [Python 3.12 tutorial](https://docs.python.org/3.12/tutorial/index.html) and
  [virtual environments](https://docs.python.org/3.12/tutorial/venv.html):
  use only the concrete syntax needed here and isolate the pinned environment.
- [JupyterLab notebooks](https://jupyterlab.readthedocs.io/en/stable/user/notebook.html)
  and [commands](https://jupyterlab.readthedocs.io/en/stable/user/commands.html):
  cells, kernels, saving, and restart/run operations. Online docs can be newer
  than pinned 4.6.4; no dependency upgrade is inferred.
- [Qiskit installation](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
  and [StatevectorSampler](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.primitives.StatevectorSampler):
  local isolated setup, measurements, reproducible seeded samples.
- [Bit ordering](https://quantum.cloud.ibm.com/docs/en/guides/bit-ordering),
  [QFTGate](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.QFTGate),
  and [phase estimation](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qiskit.circuit.library.phase_estimation):
  least-significant bit, positive Fourier sign, and target-eigenstate requirement.
- [Grover iteration analysis](https://quantum.cloud.ibm.com/learning/en/courses/fundamentals-of-quantum-algorithms/grover-algorithm/number-of-iterations):
  the four-candidate single-target case has sin-squared success probabilities
  1/4, 1, 1/4 for zero, one, two iterations. Exact math, not OCR, checks this claim.
