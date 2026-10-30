# Repository guidance

Read [CONTRIBUTING.md](CONTRIBUTING.md) before changing this repository. Keep
changes scoped, preserve existing work, and retain required workflow/job names,
checks, and the solo-maintainer contribution policy. Do not change repository
rulesets as part of instructional work.

## Source and notebook conventions

- Canonical reusable algorithm code belongs in `src/phys3810/`; mathematical
  tests belong in `tests/`. Grover is implemented there; extend this layout for
  the remaining algorithm milestones.
- Course notebooks belong in `teaching/phys3810-fa2026/notebooks/`. Import
  canonical implementations instead of maintaining separate notebook copies.
  Keep explanations, parameter choices, exercises, and short demonstrations in
  notebooks; comment non-obvious implementation steps in source.
- Use current SDK circuits and V2 primitives. Prefer `QFTGate`,
  `phase_estimation()`, and `grover_operator()` for reference comparisons.
  Do not add deprecated class wrappers or removed `qiskit.algorithms` HHL/Shor
  imports.
- Declare bit order, register roles, supported inputs, approximation choices,
  and random seeds. Commit notebooks without execution outputs or counts;
  write executed copies to ignored `artifacts/` for review.
- Default runs must be local and credential-free. IBM Runtime and GPU paths
  remain optional and excluded from classroom validation. Never submit jobs
  or contact IBM during offline tests; mock service construction in tests.

## Validation

Use the documented Python 3.12 classroom environment. From the repository root:

```bash
python -m pip check
python -m unittest discover -s tests -v
python scripts/validate_classroom.py
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh
pre-commit run --all-files
```

The Python validator is the cross-platform classroom entry point; the Bash
command retains the existing smoke workflow. Run each required notebook from a
fresh kernel, with the selected environment's interpreter, and fail on cell
errors. Printed output and stored notebook output are not proof of correctness.
Required nonempty code cells must all execute: reject `skip-execution`, force
errors to raise even with `raises-exception`, and check execution counts and
error outputs before reporting a pass. Preserve partial executed notebooks on
failure. Handle intentional exception demonstrations inside successful cells.

For algorithm milestones, use independent mathematical expectations in addition
to SDK comparisons, with explicit floating-point tolerances:

- QFT: compare the complete operator with the Fourier matrix, including sign
  convention and bit ordering.
- QPE: test asymmetric exact phases and a nonexact phase against the expected
  outcome distribution; avoid cases that conceal reversed bit order.
- Grover: verify oracle action on every basis state and amplification
  probabilities against the analytic expression.
- HHL: verify postselection probability, ancilla uncomputation, normalization,
  and relative sign against a classical linear solve on stated supported cases.
- Shor: verify reversible modular arithmetic, order recovery, and factor
  extraction independently, including unsuccessful or invalid cases.

Record commands, installed versions, platform, and outcomes. **Passed** means
the check ran successfully; **failed** means it ran and did not meet its
criterion; **skipped** means it was deliberately excluded with a reason;
**untested** means no execution evidence exists. Never relabel skips as passes.

## Claims and public artifacts

State toy-example restrictions and resource costs. Do not imply generality,
scalability, or quantum advantage unsupported by the implementation and evidence.
Do not put private correspondence, credentials, account identifiers, or student
data in public code, notebooks, documentation, outputs, or validation logs.

## PHYS 3810 collaboration and handoffs

- The assistant owns implementation, technical review, testing, repairs, and
  documentation. Do not assign manual code/diff review to the user.
- End each substantive turn with the outcome and validation status, one
  recommended next action, and `GPT Pro sync: due / recommended / not needed`
  with a reason. State any user input actually needed; otherwise say none.
- Continue authorized routine local work without repeated approval requests.
  Ask only for missing decisions or actions outside the authorized scope.
  Preserve the current local-only boundary: no push, PR, merge, publication,
  external messages, or IBM hardware jobs without applicable authorization.
- Keep [STATUS.md](teaching/phys3810-fa2026/STATUS.md) current. Follow the
  sequence and handoff protocol in [WORKFLOW.md](teaching/phys3810-fa2026/WORKFLOW.md).
  Prepare the evidence and exact review prompt before recommending a GPT Pro
  sync; do not ask the user to assemble or audit the evidence.
- For future GPT Pro handoffs, copy one standalone runnable ZIP to the Ubuntu
  desktop and put the review prompt in a copyable code block in the final chat
  response. Exclude prompt files, policy/chat documents, unrelated history,
  duplicate text exports, caches, credentials, and generated outputs from the
  ZIP. Include needed source, notebooks, dependencies, tests, setup instructions,
  license, and concise validation evidence; verify the extracted bundle.
- Treat GPT Pro feedback as review input: reproduce actionable findings, fix
  them, and record disposition and test evidence. Self-review is not an
  independent GPT Pro review, and a model opinion is not an executed test.
- Do not infer that another chat sees local files or that a sync has happened.
  Record the reviewed snapshot and actually received response. Keep private
  chat text out of public docs; retain only technical conclusions.

Milestone 1's independent review was received and its required correction was
demonstrated on October 29, 2026; see the
[reconciliation record](teaching/phys3810-fa2026/REVIEW_RECONCILIATION.md).
The Grover review was received and its exercise correction was demonstrated;
see [the reconciliation](teaching/phys3810-fa2026/GROVER_REVIEW_RECONCILIATION.md).
Review-draft setup/instructor PDFs may be prepared now; final classroom PDFs
still require platform validation and instructor feedback. An intentional
instructional PDF may accompany a standalone preview; this does not authorize
including generated notebook outputs or prompts in a review bundle.
The [Grover preview](teaching/phys3810-fa2026/PREVIEW_PLAN.md) is a separate,
identified source revision; keep QFT development out of that first preview.
No additional GPT Pro round is needed for the evidenced Grover repairs. The
next substantial checkpoint remains after QFT/QPE and before HHL/Shor.
