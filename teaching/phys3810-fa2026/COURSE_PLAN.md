# PHYS 3810 · Fall 2026 course plan

Updated November 2, 2026. Material development: **Gage Plott**.
The teaching route is now designed for **two or three classes before
Thanksgiving**, starting with **zero Python experience**. Use live instructor
demonstrations that students repeat on their laptops. There is no grading,
evaluation, assignment, or submitted work. Complete worked examples are intentional.

Rick has acknowledged receiving material and offered to deliver the sessions
after a walkthrough. The detailed review and final delivery arrangement remain
open; receipt is not final classroom approval. Gage's contribution is material
development unless a separate delivery arrangement is agreed.

Start with the [guided review entrance](guided/START_HERE.md),
[student quickstart](guided/STUDENT_QUICKSTART.md), and
[presenter run sheet](guided/INSTRUCTOR_RUN_SHEET.md). The
[guided-teaching contract](GUIDED_TEACHING_PLAN.md) records the bounded examples
and validation requirements.

## Proposed classroom route

Use the listed **12:40–2:05 PM Eastern period (85 minutes)**: 75 minutes of
planned activity and 10 minutes for questions, transitions, and recovery.
These are planning budgets, not measured learner pacing. Each day has a shorter
stopping point in the presenter run sheet.

1. **Day 1: Python and Qiskit.** Open and run cells; use numbers, text, small
   lists, imports, and function calls; construct one-qubit X/H circuits; sample
   and interpret histograms; save, restart, and rerun. No independent coding
   experience, loops, matrix construction, or external Python reading is required.
2. **Day 2: Grover follow-along.** Use two qubits and one target among four
   candidates. Compare zero, one, and two iterations, with exact target
   probabilities 1/4, 1, and 1/4. Change the target and iteration count together
   with the instructor, rerunning the dependent cells and captions.
3. **Day 3, if available: QFT and QPE.** Inspect a two-qubit phase pattern,
   undo QFT, then prepare a target eigenstate for three-counting-qubit QPE.
   Use exact phases 3/8 and 1/8, yielding `011` and `001`. A probability
   histogram alone does not show the QFT's complex phase pattern.

The **two-day fallback is Day 1 plus Grover**. If phase estimation is the
priority, it replaces Grover as the single algorithm day. A brief compiled-N=15
Shor demonstration may replace an agreed segment; it is not appended to a full
day. HHL and the full Shor lesson remain supporting references. Do not compress
all five algorithms into two periods.

## Setup and preparation

The opening activity assumes students can open a working environment.
Installation on unknown laptops is not included in that time estimate. Confirm
operating systems, installation permissions, available help, and when assisted
setup can occur. **No independent setup homework is assumed.** If setup takes
class time, use the shorter Day 1 route or the presenter's demonstration and
record what students actually completed.

The demonstrated environment is Ubuntu/Linux, 64-bit CPython 3.12, Qiskit 2.6.1,
Aer 0.17.2, and JupyterLab. Native Windows/macOS and native editor workflows remain
untested. Local examples require no IBM account, credentials, GPU, or quantum
hardware; installing dependencies requires internet access. The existing
preflight notebook is diagnostic support, not the first Python lesson.

## Remaining decisions

- Two classes or three, exact dates, and final delivery responsibility after
  the walkthrough. Presenter availability or coverage remains unconfirmed.
- Grover and QFT/QPE priorities, or the specific substitution if Shor is needed live.
- Laptop/setup arrangements, operating systems, permissions, and support.
- Prior quantum coverage: amplitudes, phase, measurement, eigenstates, gates,
  and any preferred notation or examples.

The earlier proposal named **November 16, 19, and 23, 2026**. These remain
provisional. November 19 is Thursday, inconsistent with the listed
Monday/Wednesday pattern. Confirm a special meeting or corrected date; do not
silently substitute November 18. The earlier three-topic request named QFT,
Shor, and Grover; five implementations are available regardless of live emphasis.

The [official UTC academic calendar](https://www.utc.edu/academic-affairs/registrar/calendars-and-schedules/academic-calendar-fall-2026-summer-2027)
was checked on October 29: November 25–29 are no-class days and November 30 is
the last class day. Those recorded constraints do not confirm these sessions.
The current request is to finish the teaching meetings before Thanksgiving.

## Complete technical library and preserved editions

Canonical reusable source under `src/phys3810/` implements Grover, QFT, QPE,
bounded HHL, and compiled full-domain N=15 Shor. The three guided notebooks
import that code; they do not replace it. The eight original reference and
validation notebooks remain available, so the new review kit includes eleven
notebooks in total. Default validator membership remains eight;
`python scripts/validate_classroom.py --profile all` includes all eleven and
uses the same strict fresh-kernel checks. See [current evidence](STATUS.md) for
measured test, cell, and figure totals for each source revision.

The [published full-course preview](PUBLIC_PREVIEW_RELEASE.md) remains frozen at
`phys3810-fa2026-v0.2.0-rc1`, source `f717aea`, with its recorded 160 tests/eight
notebooks/50 cells/16 PNGs. The new guided review kit is a separate review
artifact, not a new public release. All earlier PDF/Markdown editions and
published assets remain unchanged. They predate this beginner route and do
not establish its current teaching requirements.

The [October 30–November 1 course-plan snapshot](https://github.com/M-Gage-Plott42/qiskit-v2-guide/blob/7600e85c773db53cf0e99c9642dc85b806bd8a29/teaching/phys3810-fa2026/COURSE_PLAN.md)
and [earlier presenter sheets](R4_PRESENTER_RUN_SHEETS.md) retain the historical
Grover / QFT–QPE / HHL–Shor proposal. Their completed technical milestones and
machine timings remain evidence for their identified sources; they are not the
current beginner schedule or a completed human rehearsal.
