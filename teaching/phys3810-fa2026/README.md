# PHYS 3810 · Start here

Welcome to the Fall 2026 invited lecture/labs for UTC **Introduction to Quantum
Information Science and Technology**. You will run small quantum circuits on
your computer using Python and Qiskit. You do not need Git experience, an IBM
account, a GPU, or access to a quantum computer.

**Current status:** onboarding and the [Grover lesson](notebooks/01_grover.ipynb)
are implemented and tested locally. Grover's independent review was received
and its exercise correction was validated.
There is no course release yet. QFT, QPE, HHL, Shor, and the final setup PDF are
still planned; older repository releases may not contain this folder. A
Grover-only preview and review-draft guides are being prepared for feedback;
they are not yet public download links.
See [STATUS.md](STATUS.md) for validation results and remaining work.

## Before the first session

1. When the instructor designates a course release, download its **Source code
   (zip)** archive and extract it. Keep the whole extracted folder together.
2. Follow the [setup guide](SETUP.md) to create the Python 3.12 environment,
   install the pinned packages, and run the local validator.
3. Open [the setup/preflight notebook](notebooks/00_setup_preflight.ipynb) in
   JupyterLab, select **Python (PHYS 3810)**, and restart the kernel and run all
   cells. Expect version checks, Bell-state probabilities, measurement counts,
   and two figures.
4. Continue with [Grover search](notebooks/01_grover.ipynb): predict oracle and
   amplification behavior, inspect exact states, and sample a local circuit.

Package installation needs internet access. The classroom validation and local
notebooks run without internet after installation. If a check fails, keep the
error text and ask the instructor for help; a notebook preview on GitHub does
not execute the code.

## Planned learning sequence

- **Grover — available:** [phase marking and amplitude amplification](notebooks/01_grover.ipynb).
- **QFT/QPE:** the Fourier transform and extracting a quantum phase.
- **HHL/Shor:** small examples of linear-system solving and order finding,
  including their assumptions and limitations.

Session dates and assessment expectations are not confirmed. The
[course plan](COURSE_PLAN.md) gives a 50-minute core and 75-minute expansion for
each session. The available Grover lab has a 50-minute core and 25 minutes of
additional exercises. For environment troubleshooting, use preflight and the existing
[Statevector smoke notebook](../../notebooks/00_local_statevector_smoke.ipynb)
and [Aer smoke notebook](../../notebooks/01_local_aer_smoke.ipynb).

For repository-wide information, see the [main README](../../README.md).
