# PHYS 3810 guided-practice review kit

Material development: **Gage Plott**. For the November 3, 2026 walkthrough. This is a review and rehearsal kit, not
final classroom approval or a replacement for the published full-course preview.

1. Read the **one-page review agenda**:
   [PDF](https://github.com/M-Gage-Plott42/qiskit-v2-guide/blob/d0f2c7d37fa07c4ea48aafe8fb202a5a6ed336f8/teaching/phys3810-fa2026/guided/pdf/PHYS3810_Guided_Review_Agenda_v0.2_REVIEW_DRAFT.pdf)
   or [Markdown](REVIEW_AGENDA.md).
2. Read the **three-page instructor run sheet**:
   [PDF](https://github.com/M-Gage-Plott42/qiskit-v2-guide/blob/d0f2c7d37fa07c4ea48aafe8fb202a5a6ed336f8/teaching/phys3810-fa2026/guided/pdf/PHYS3810_Guided_Instructor_Run_Sheet_v0.2_REVIEW_DRAFT.pdf)
   or [Markdown](INSTRUCTOR_RUN_SHEET.md).
3. Skim the **two-page student quickstart**:
   [PDF](https://github.com/M-Gage-Plott42/qiskit-v2-guide/blob/d0f2c7d37fa07c4ea48aafe8fb202a5a6ed336f8/teaching/phys3810-fa2026/guided/pdf/PHYS3810_Guided_Student_Quickstart_v0.2_REVIEW_DRAFT.pdf)
   or [Markdown](STUDENT_QUICKSTART.md).

The agenda and run sheet are enough for a first pass. The PDFs are REVIEW
DRAFTS of the accepted guides and accompany the unchanged
`PHYS3810-Guided-Review-v0.2-b393f63fd8b3.zip`; they are separate attachments,
not extra files inside that sealed archive. Open the guided notebooks below
only as time permits before the walkthrough. They contain complete worked examples.

## The small classroom route

- Day 1: [Python and Qiskit](../notebooks/guided/01_python_and_qiskit.ipynb).
  Start with no programming experience: run cells, change values, and sample X/H circuits.
- Day 2: [Grover follow-along](../notebooks/guided/02_grover_follow_along.ipynb).
  Search four candidates and see why extra iterations can reduce success.
- Day 3, if available: [QFT and QPE follow-along](../notebooks/guided/03_qft_qpe_follow_along.ipynb).
  See complex phase, undo a QFT, and estimate an explicitly prepared eigenstate's phase.

The two-day route is Day 1 plus Grover. It does not squeeze all five algorithms
into two meetings. Each proposed period is 85 minutes: 75 minutes of activity
and 10 minutes of margin. These are planning budgets, not measured human pacing.
No grading, assignments, evaluation, or submissions are part of this route.

## What else is in the kit

The exported kit keeps the complete runnable support tree under `runtime/`.
There are **eleven notebooks total**: three guided lessons and eight existing
reference/validation notebooks. The five-algorithm library remains available;
HHL and full compiled-Shor lessons are references outside the proposed core.
Implementation files, tests, receipts, validation logs, and the eight reference
notebooks support running the kit; none is part of the first-pass reading task.

The root `MANIFEST.json` identifies the source and every payload's hash and size;
`VALIDATION.md` gives execution evidence and limits. These are support records,
not student reading. Installation requires internet; default lessons then run
locally without IBM credentials or quantum hardware. Only the Linux path has
prior interactive evidence. Other laptop platforms and human classroom pacing
remain untested.
