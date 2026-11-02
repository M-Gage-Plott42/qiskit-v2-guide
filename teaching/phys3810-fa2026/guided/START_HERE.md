# PHYS 3810 guided-practice review kit

Material development: **Gage Plott**. For the November 3, 2026 walkthrough. This is a review and rehearsal kit, not
final classroom approval or a replacement for the published full-course preview.

1. Read the [review agenda](REVIEW_AGENDA.md) to choose two or three meetings.
2. Use the [student quickstart](STUDENT_QUICKSTART.md) to open a working notebook.
3. Present from the [instructor run sheet](INSTRUCTOR_RUN_SHEET.md), with the
   three guided notebooks below. They contain complete worked examples.

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
The instructor need only follow the three guided lessons for this proposal.

The root `MANIFEST.json` identifies the source and every payload's hash and size;
`VALIDATION.md` gives execution evidence and limits. These are support records,
not student reading. Installation requires internet; default lessons then run
locally without IBM credentials or quantum hardware. Only the Linux path has
prior interactive evidence. Other laptop platforms and human classroom pacing
remain untested.
