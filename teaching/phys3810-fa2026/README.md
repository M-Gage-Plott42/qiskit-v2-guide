# PHYS 3810 · Start here

Welcome to the Fall 2026 invited lecture/labs for UTC **Introduction to Quantum
Information Science and Technology**. You will run small quantum circuits on
your computer using Python and Qiskit. You do not need Git experience, an IBM
account, a GPU, or access to a quantum computer.

**Available in this revision:** onboarding and [Grover search](notebooks/01_grover.ipynb).
The [Grover-only prerelease](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-grover-v0.1.0-rc1)
contains the tested first lesson. QFT development is preserved separately and
will follow in its own integration commit; QPE, HHL, and Shor remain planned.
See [STATUS.md](STATUS.md) for evidence and remaining work.

## Before the first session

1. Download [PHYS3810-Grover-v0.1.0-rc1.zip](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip)
   and extract its complete `phys3810-grover` folder.
2. Follow the [student setup PDF v0.2](handouts/PHYS3810_Student_Setup_Grover_RC1_v0.2.pdf)
   or its [Markdown companion](preview/SETUP_REVIEW_DRAFT.md). Use this revised
   guide with the unchanged rc1 download; it supersedes the older guide inside
   the ZIP. The [repository setup guide](SETUP.md) covers this checkout.
3. Open [setup/preflight](notebooks/00_setup_preflight.ipynb) in JupyterLab,
   select **Python (PHYS 3810)**, and restart the kernel and run all cells.
   Expect version checks, Bell-state checks, and two figures.
4. Continue with [Grover search](notebooks/01_grover.ipynb): predict phase marking
   and amplification, inspect exact states, and sample a local circuit.

Package installation needs internet access. Required classroom validation and
local notebooks then run without internet. If a check fails, retain the error
text for help; a notebook preview on GitHub does not execute its code.

## Planned learning sequence

- **Grover — available:** phase marking and amplitude amplification.
- **QFT/QPE — subsequent integration and development:** Fourier transforms and
  phase estimation using explicit phase and bit-order conventions.
- **HHL/Shor — planned:** small linear-system and order-finding examples with
  stated restrictions, assumptions, and resource costs.

Session dates and assessment expectations are not confirmed. The
[course plan](COURSE_PLAN.md) proposes 50-minute cores and 75-minute expansions.
The current Grover lab has a 50-minute core and 25 minutes of extra exercises.
For troubleshooting, use preflight and the existing
[Statevector smoke notebook](../../notebooks/00_local_statevector_smoke.ipynb)
and [Aer smoke notebook](../../notebooks/01_local_aer_smoke.ipynb).

For repository-wide information, see the [main README](../../README.md).
