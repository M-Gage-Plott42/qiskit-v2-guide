# Instructor document editions

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

This is the nonblocking P3-01 clarification for the next authored instructor
edition before final classroom distribution. It does not modify the delivered
PDF or its synchronized body text. Keep instructor answer material outside a
student-only package; the existing notebooks still contain worked results.
