# Instructor route and historical document editions

The current route is one prerecorded beginner class presented by **Gage Plott**:
15–20 minutes of setup, quantum random bits, Bell states, QFT, QPE, then HHL.
Grover and Shor remain optional; total duration is flexible and Canvas is the
delivery destination. Nothing is assigned, graded, evaluated, or submitted.

Print the four-page [recording guide, edition v0.2](recording-v0.2/PHYS3810_Recording_Guide_v0.2.pdf)
single-sided. Its [synchronized Markdown companion](recording-v0.2/PHYS3810_Recording_Guide_v0.2.md)
contains the same narration cues, stable cell IDs, edits/restores, expected
results, and recovery steps. Both supplied files are preserved unchanged.
Keep the [one-page support insert](support-v0.1/PHYS3810_Recording_Support_Insert_v0.1.pdf)
and its [exact companion](support-v0.1/PHYS3810_Recording_Support_Insert_v0.1.md)
beside that guide for the simpler setup, rerun, recovery, and contact cues.
Only this additional page needs printing if paper cues are wanted.

The separate [student guide v0.3](../handouts/recording-v0.3/PHYS3810_Student_Guide_v0.3.pdf)
is the final support edition; the matching complete kit follows the
[current quickstart](../intro/START_HERE.md) and [delivery status](../STATUS.md).
The [original guide receipt](../RECORDING_GUIDES_v0.2_RECEIPT.json) and
[support-update receipt](../handouts/STUDENT_SUPPORT_v0.3_RECEIPT.json) record exact
delivered bytes. In JupyterLab, use **Open With → Markdown Preview** when a
guide opens as source text and you need to follow its links.

The guided Ubuntu recording test is completed evidence by operator report.
Use the working OBS configuration and check the ordinary final take's framing,
audio, readable code/plots, and saved-file playback. Keep authentication enabled
and token-bearing launch output off camera. Do not restart a pilot milestone
or send another duration/Canvas approval questionnaire solely for this edition.

The earlier Word recording draft remains a separate local edition with its
source identity in the [focused reconciliation](../SINGLE_CLASS_REVIEW_RECONCILIATION.md).

## Earlier guided and full-course editions

For the current beginner proposal, use the [guided presenter run sheet](../guided/INSTRUCTOR_RUN_SHEET.md)
and [walkthrough agenda](../guided/REVIEW_AGENDA.md). Material development:
**Gage Plott**. Start with Python/Qiskit, then Grover, with QFT/QPE as a third
day if available. Use complete worked examples, no assignments or assessment.
Rick has offered to teach after the walkthrough; final delivery remains open.

The PDFs below are historical references, not the current route. They remain
unchanged and are excluded from the new concise kit. Archived Grover documents
retain their original byline; new material uses the credit above.

The [full-course document v0.2 review draft](PHYS3810_Full_Course_Instructor_Guide_v0.2_REVIEW_DRAFT.pdf)
has six pages and an [unchanged supplied Markdown companion](FULL_COURSE_INSTRUCTOR_v0.2_REVIEW_DRAFT.md).
Delivered PDF: 84,527 bytes, SHA-256
`0255da43e512d36582bb33451fcc8027f9b0cbccbe8217afdfa8f256147dd896`.
It identifies the published preview, fixes former-bundle navigation, and
**clarifies phase decoding in this edition** by limiting phase-fraction decoding to
the phase-estimation counting register. See
[the November reconciliation](../NOVEMBER_REVIEW_RECONCILIATION.md).

The supplied v0.2 documents predate the scheduling clarification. Their
50/75-minute routes remain proposed content budgets; current planning uses an
85-minute class period with 10 minutes of margin after the expanded route.
November 16/19/23 are provisional, and November 19 conflicts with the listed
Monday/Wednesday schedule. See [the current course plan](../COURSE_PLAN.md).
Keep the supplied PDF and synchronized companion unchanged; no new edition
is needed solely to communicate this scheduling caveat during review.

The [full-course document v0.1 review draft](PHYS3810_Full_Course_Instructor_Guide_v0.1_REVIEW_DRAFT.pdf)
has six pages and a [synchronized Markdown companion](FULL_COURSE_INSTRUCTOR_DRAFT.md).
It describes proposed code v0.2.0-rc1. It is suitable for provisional review,
not final classroom approval. Its exact supplied PDF bytes are preserved.
The [review reconciliation](../R6_DOCUMENT_REVIEW_RECONCILIATION.md) records
receipt verification, evidence limits, and the remaining decisions.

The earlier [Grover document v0.2 instructor guide](PHYS3810_Grover_Instructor_Guide_RC1_v0.2.pdf)
remains a distinct two-page edition for the published Grover-only rc1. Its
[receipt](../handouts/README.md) and bytes are unchanged.

## Reading clarification for full-course v0.1

On page 3, interpret division by `2**m` as applying to a **phase-estimation
counting register**, not to every measured bitstring. Displayed bitstrings label
the integer `int(bits, 2)`. For an m-qubit phase-estimation counting register,
that integer yields the phase estimate `int(bits, 2)/2**m`; HHL then applies its
stated phase-to-eigenvalue conversion. Grover/QFT basis labels remain integer
indices. See the canonical [QPE convention](../QPE_PLAN.md).

This reading clarification is retained for v0.1; the newer v0.2
edition incorporates it. It does not modify the delivered v0.1
PDF or its synchronized body text. The new guided route contains complete
worked results for open demonstration and follow-along, with no assessment.
