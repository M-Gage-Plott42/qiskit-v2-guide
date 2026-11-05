# Aer 0.18.2 dependency validation

Date: November 4, 2026. Scope: dependency PR #117 after refreshing it onto main
`826d48f8945023c966081f326a6519941fbdc101`. The refreshed PR head before this
version-contract repair is `057001c854be11c004b57f097c954b6e03313833`.

## Problem and repair

The dependency PR changes Aer to 0.18.2, while the terminal validator and
preflight notebook still require 0.17.2. CI correctly rejected that inconsistent
environment. Both checks now require **Qiskit 2.6.1 and Aer 0.18.2** exactly.
Current checkout documentation identifies the same pair; version checks remain
strict. The notebook's only source edits are its Aer guard and expected-version
text. Stored outputs/counts are empty.

The [Aer release notes](https://qiskit.github.io/qiskit-aer/release_notes.html)
identify 0.18.2 as the corrected publication of the 0.18.1 fixes. That upstream
description is separate from the executed repository checks below.

## Executed local evidence

A new isolated **Linux x86_64 CPython 3.12.15** application environment installed
`requirements-ci.txt` with **pip 26.2.2**, using the PR's existing constraints.
All **114 application distributions** match active Linux constraints, plus the
documented pip version. Qiskit is 2.6.1, Aer 0.18.2 and JupyterLab 4.6.4. The
optional Runtime package is not needed for classroom validation.

Passed:

- `python scripts/validate_classroom.py --profile all`: pip consistency,
  **205 tests**, **eleven fresh-kernel notebooks**, **74 nonempty code cells**
  and **27 PNG figures**. Required cells executed without retained errors.
- `bash scripts/smoke_local.sh`: the original Statevector and Aer smoke routes.
- Ruff **0.15.22** across `src`, `scripts`, `tests`, classroom notebooks and
  both local smoke notebooks.

The classroom validator already runs unit discovery; no redundant separate
unit-suite invocation was added. Executed copies stay under ignored `artifacts/`.
The required pre-push maintainer gate is `pre-commit run --all-files`, using the
repository-pinned Ruff, YAML and Markdown hooks; passing gate results belong
with this PR's commit/CI evidence.

Validation input SHA-256 values:

- `requirements.txt`: `95fb8e6abd1e2d2ee79036e8de205820a83e3ce9025b581a882afe7270e54001`.
- `constraints-ci.txt`: `596d704dd7c369362b4e1980829e1144e83dc87742eba2365d12fc4242f33cd5`.
- `scripts/validate_classroom.py`: `523295607ed7eb81949190a77d62bf63ad3b6558e49a3c01f42e6dcf857ebced`.
- `notebooks/00_setup_preflight.ipynb` under this course: `e99b80e33c1d6400ce3fdaa9f5b9610b9eb9ee5e979d268dea02d90027f91888`.

## Preserved boundaries

Canonical algorithm source, contracts, tests, accepted guides, supplied PDFs and
companions, frozen release builders, published assets and sealed review kits
are unchanged. Earlier Aer 0.17.2 execution/review records remain historical;
their results are not reassigned to this dependency revision. No new archive,
PDF, teaching review or release was produced.

Optional IBM Runtime/cloud and GPU execution were deliberately **skipped** by
the classroom route. Windows/macOS and native editor/browser UI behavior remain
**untested** for this update; Linux headless execution does not establish them.
No external quantum job or human message was sent. Teaching work remains parked
pending instructor feedback. This is PR repair/validation evidence, not merge
approval or final classroom acceptance.
