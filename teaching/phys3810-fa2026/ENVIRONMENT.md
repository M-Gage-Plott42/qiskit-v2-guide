# Classroom environment decision

Decision date: October 29, 2026. Use **64-bit CPython 3.12**, **Qiskit 2.6.1**,
and **Qiskit Aer 0.17.2** for local CPU execution. The tested interpreter is
3.12.15. The independent reviewer additionally reported a passing initial
classroom run on 3.12.14 with the same package versions; see
[the review record](REVIEW_RECONCILIATION.md). The corrected validator has been
executed here on 3.12.15; other environments must run the same checks.

## Why this version

The supplied audit and current checkout pinned Qiskit 2.5.1 in CI, while
`qiskit~=2.5` allowed later 2.x releases in ordinary installs. The
[maintainer-published Qiskit 2.6.1 package](https://pypi.org/project/qiskit/2.6.1/)
was released October 22, 2026 and declares Python >=3.10. We selected that exact
release, tested the existing V2 smoke paths against it, and aligned the default
and CI installs. This is a classroom pin, not a promise of indefinite upstream
support or compatibility with future Qiskit releases.

[IBM's installation guide](https://quantum.cloud.ibm.com/docs/en/guides/install-qiskit)
recommends isolated environments and explains local simulation, visualization,
and platform support. No IBM account is needed for this course's default path.
Grover now has its own [implementation and validation evidence](GROVER_VALIDATION.md).
QFT, QPE, HHL, and Shor remain future work; onboarding does not validate them.
Reference interfaces for the algorithm milestones are `QFTGate`,
`phase_estimation()`, and `grover_operator()` with V2 primitives.

## Dependency structure

- `requirements.txt`: exact direct classroom versions, including
  `qiskit[visualization]`, JupyterLab, ipykernel, nbconvert/nbclient/nbformat,
  ipywidgets, and python-dotenv for the offline configuration tests.
- `constraints-ci.txt`: complete resolved dependency union for classroom CPU
  use and the optional Runtime package, restricted during resolution to
  CPython 3.12. Platform markers retain macOS/Windows-only dependencies.
  Constraints do not install optional packages by themselves.
- `requirements-ci.txt`: uses the same classroom requirements as students.
- `requirements-runtime.txt`: adds Runtime 0.49.0 explicitly for optional
  fake-backend or hardware notebooks. GPU packages are not installed by either
  path. Optional execution is excluded from the classroom validator.

The lock is a full version resolution, not a hash-verified artifact lock. It
is generated across platforms rather than by freezing a Linux-only install.
`pip==26.2.2` is the documented installer; it is not an application dependency.
Use a fresh virtual environment to avoid unrelated packages from previous work.
Actual installed versions and test evidence appear in [VALIDATION.md](VALIDATION.md).

## Platforms and evidence

Linux x86_64 is the locally executed platform. The universal resolution includes
Windows x64 and macOS ARM64/Intel markers, but resolution alone does not establish
native installation, plotting, or notebook execution. Those native platforms
remain **untested** until a maintainer runs the setup and validator there. Do not
advertise them as passed. Windows ARM64 and 32-bit Python are outside this
classroom target. Keep unsupported machines on an instructor-provided environment.

## Maintainer updates

Use a separate Python 3.12 tool environment so lint/update tools do not alter
the classroom's installed-package evidence:

```bash
python -m pip install uv==0.13.6 ruff==0.15.22 yamllint==1.38.0 pre-commit==4.7.0
python scripts/update_constraints_ci.py
```

The Python updater resolves declared direct packages with
[uv's universal resolver](https://docs.astral.sh/uv/pip/compile/), preserving
platform markers and excluding the old constraints while resolving. The Bash
updater remains a compatibility wrapper. Regeneration intentionally refreshes
transitives; review the full resulting diff. Students need neither uv nor Git.

After a lock update, install with pip in a **new** classroom environment, run
`python -m pip check`, `python scripts/validate_classroom.py`, and the original
`bash scripts/smoke_local.sh`; inspect installed versions against the constraints.
Repeat native platform validation before claiming portability. Run Ruff,
Markdown/YAML/shell/Actions lint and `pre-commit run --all-files` before a PR.
Keep existing required job names, contribution policy, and repository rulesets.
