# PHYS 3810 · Start here

Welcome to the Fall 2026 invited lecture/labs for UTC **Introduction to Quantum
Information Science and Technology**. You will run small quantum circuits on
your computer using Python and Qiskit. You do not need Git experience, an IBM
account, a GPU, or access to a quantum computer.

**Current status:** onboarding, [Grover](notebooks/01_grover.ipynb),
[QFT](notebooks/02_qft.ipynb), and [QPE](notebooks/03_qpe.ipynb) are implemented
and tested locally. The combined QFT/QPE independent review is pending. Grover's independent review was received
and its exercise correction was validated.
The [Grover-only prerelease](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-grover-v0.1.0-rc1)
and review-draft guides are published for early feedback. QFT/QPE are available
in the development snapshot; HHL, Shor, and final classroom materials are
still planned. Use the instructions included with your downloaded version.
See [STATUS.md](STATUS.md) for validation results and remaining work.

## Before the first session

1. Download [PHYS3810-Grover-v0.1.0-rc1.zip](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip)
   and extract its `phys3810-grover` folder. Keep the whole folder together;
   this named asset matches the review setup guide.
2. Follow the setup guide included in that ZIP to create the Python 3.12
   environment, install the pinned packages, and run the local validator.
   A [received setup PDF v0.2](handouts/PHYS3810_Student_Setup_Grover_RC1_v0.2.pdf)
   and [Markdown companion](preview/SETUP_REVIEW_DRAFT.md) are also available
   locally for that same rc1 download; publication of this revised draft is pending.
   The [development setup guide](SETUP.md) covers the newer repository checkout.
3. Open [the setup/preflight notebook](notebooks/00_setup_preflight.ipynb) in
   JupyterLab, select **Python (PHYS 3810)**, and restart the kernel and run all
   cells. Expect version checks, Bell-state probabilities, measurement counts,
   and two figures.
4. Continue with [Grover search](notebooks/01_grover.ipynb): predict oracle and
   amplification behavior, inspect exact states, and sample a local circuit.
5. In the development version, [QFT](notebooks/02_qft.ipynb) introduces the
   Fourier matrix and phase conventions, followed by [QPE](notebooks/03_qpe.ipynb)
   for controlled powers, counting-register decoding, and finite precision. The
   Grover-only preview has its own version-matched setup instructions.

Package installation needs internet access. The classroom validation and local
notebooks run without internet after installation. If a check fails, keep the
error text and ask the instructor for help; a notebook preview on GitHub does
not execute the code.

## Planned learning sequence

- **Grover — available:** [phase marking and amplitude amplification](notebooks/01_grover.ipynb).
- **QFT/QPE — available locally:** [Fourier transforms](notebooks/02_qft.ipynb)
  followed by [phase estimation](notebooks/03_qpe.ipynb).
- **HHL/Shor:** small examples of linear-system solving and order finding,
  including their assumptions and limitations.

Session dates and assessment expectations are not confirmed. The
[course plan](COURSE_PLAN.md) gives a 50-minute core and 75-minute expansion for
each session. The available Grover lab has a 50-minute core and 25 minutes of
additional exercises. For environment troubleshooting, use preflight and the existing
[Statevector smoke notebook](../../notebooks/00_local_statevector_smoke.ipynb)
and [Aer smoke notebook](../../notebooks/01_local_aer_smoke.ipynb).

For repository-wide information, see the [main README](../../README.md).
