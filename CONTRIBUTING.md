# Contributing

Thanks for contributing to `qiskit-v2-guide`.

By participating, you agree to follow this repository's [Code of Conduct](CODE_OF_CONDUCT.md).

## Scope

This repository is focused on reproducible Qiskit 2.x smoke-test workflows:

- local Statevector and Aer simulation paths,
- local Runtime testing mode with fake backends,
- optional IBM Runtime cloud execution.
- UTC PHYS 3810 course materials and their offline mathematical validation.

Keep changes tightly scoped and reviewer-friendly.

## Local Validation Before a PR

From the repo root:

```bash
python -m pip install -r requirements-ci.txt
python scripts/validate_classroom.py
bash scripts/smoke_local.sh
pre-commit run --all-files
```

`requirements-ci.txt` uses `constraints-ci.txt` for pinned CI-aligned environments.
Use CPython 3.12. The default and CI installs now share the same complete
platform-marked constraints. Runtime is optional via `requirements-runtime.txt`.
See [AGENTS.md](AGENTS.md) for source/notebook conventions and mathematical checks,
and the [environment notes](teaching/phys3810-fa2026/ENVIRONMENT.md) for maintainer
tools and lock regeneration. Existing required checks and scoped PR policy apply.

## Pull Request Guidance

1. Keep one logical change per pull request.
2. Update docs (`README.md`, `docs/...`) when behavior or setup changes.
3. Include validation commands/output in the PR description.
4. Use the PR template checklist.

## Runtime Credentials and Safety

- Never commit real credentials or `.env`.
- Keep examples backend-agnostic (no hardcoded `ibm_*` backend names).
- Prefer robust backend discovery and selection patterns already used in this repo.
