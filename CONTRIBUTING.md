# Contributing

Thanks for contributing to `qiskit-v2-guide`.

By participating, you agree to follow this repository's [Code of Conduct](CODE_OF_CONDUCT.md).

## Scope

This repository is focused on reproducible Qiskit 2.x smoke-test workflows:

- local Statevector and Aer simulation paths,
- local Runtime testing mode with fake backends,
- optional IBM Runtime cloud execution.

Keep changes tightly scoped and reviewer-friendly.

## Local Validation Before a PR

From the repo root:

```bash
python -m pip install -r requirements-ci.txt
bash scripts/smoke_local.sh
pre-commit run --all-files
```

`requirements-ci.txt` uses `constraints-ci.txt` for pinned CI-aligned environments.

## Pull Request Guidance

1. Keep one logical change per pull request.
2. Update docs (`README.md`, `docs/...`) when behavior or setup changes.
3. Include validation commands/output in the PR description.
4. Use the PR template checklist.

## Runtime Credentials and Safety

- Never commit real credentials or `.env`.
- Keep examples backend-agnostic (no hardcoded `ibm_*` backend names).
- Prefer robust backend discovery and selection patterns already used in this repo.
