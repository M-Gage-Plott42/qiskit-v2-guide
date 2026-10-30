# GPT Pro handoff: milestone 1

Prepared October 29, 2026. **Review received; required correction demonstrated.**
This file preserves the original request for source snapshot `06e22d9b5d2a`.
See [REVIEW_RECONCILIATION.md](REVIEW_RECONCILIATION.md) for the received findings
and subsequent local evidence. Do not resend this historical request as if its
review were still pending. The subsequent Grover milestone uses a standalone
desktop ZIP and a separate prompt in chat, following [WORKFLOW.md](WORKFLOW.md).

The implementation assistant packages this prompt with the source snapshot
and validation evidence in one local text attachment. The user can send that
packet to the existing planning conversation without reviewing code or
assembling files. If newer planning decisions exist there, the reviewer should
identify their implications explicitly.

## Original review request

Review the attached snapshot of `M-Gage-Plott42/qiskit-v2-guide` against our
PHYS 3810 Fall 2026 plan. The user wants the assistants to own technical review,
testing, and recommendations. Do not assign a manual code audit to the user.

Only milestone 1 has been implemented: scope, environment, and onboarding.
No QFT, QPE, Grover, HHL, or Shor lesson has been implemented, and final PDF
production remains deferred. Preserve the proposed Grover; QFT/QPE; HHL/Shor
teaching sequence, with 50-minute cores and 75-minute expansions. Actual
session dates, student background, and assessment expectations remain unknown.

The local feature branch is `feat/phys3810-m1-onboarding`. HEAD/base remains
`fb41ae02f2ece3e093e60c9286ef72ae91686530`. It is 12 commits behind the supplied
audit `bf6f362ded70767d3891db996a0a3e0cd152b34d`; no reset or rebase occurred.
The attached working-tree snapshot includes the original staged implementation
and later coordination-document edits. No changes were published or merged.

Reported execution evidence: CPython 3.12.15, Qiskit 2.6.1, Aer 0.17.2;
19 offline tests, three fresh-kernel notebooks with embedded figures, original
smoke checks, a clean archive install without Git, optional local Runtime
fake-backend execution, and lint/pre-commit passed. `VALIDATION.md` contains the
commands and installed-package inventory. This coordination update did not
rerun the Python suite. Distinguish previously recorded results from tests you
actually execute. If execution is unavailable, explicitly say static review.

Please check these concrete questions:

1. Does the implementation satisfy milestone 1, and what specific omissions
   or correctness bugs must be fixed before starting Grover?
2. Are the dependency resolution, Python/kernel selection, offline defaults,
   `.env` precedence, mathematical assertions, and notebook failure reporting
   correct and adequately evidenced? Check executable source, not just prose.
3. Are platform claims honest? Native Windows/macOS, interactive editor/browser
   use, and remote CI remain untested. Compatible wheels are not native tests.
   No IBM Runtime service or GPU execution should be inferred as passed.
4. Is the proposed Grover scope appropriate: a small phase-oracle module,
   independent basis-state and analytic amplification tests, SDK comparison,
   and a fresh-kernel teaching notebook? Identify any missing test contract.
5. Do newer decisions in our planning conversation conflict with this snapshot?
   If so, provide a concise technical delta for the implementation assistant.

Return actionable findings with file/function references, reasoning, a proposed
fix, and a test that would demonstrate resolution. Separate must-fix defects
from optional improvements and unresolved teaching/platform questions. Do not
require unrun platforms to be called passed or recommend a broad rewrite
without a concrete defect. Retain required checks and the scoped contribution
workflow. Do not suggest publishing, merging, or hardware jobs as part of review.

End with one recommendation: **proceed to Grover**, **fix listed issues first**,
or **resolve a named design decision first**. Include the next recommended GPT
Pro checkpoint. The implementation assistant will reproduce findings, apply
fixes, and update tests/docs; the user only relays your response.

## Evidence to inspect first

- [VALIDATION.md](VALIDATION.md): base, inventory, actual test evidence, limits.
- [ENVIRONMENT.md](ENVIRONMENT.md), [SETUP.md](SETUP.md), and
  [installed versions](validation/installed-linux-py312.txt).
- [COURSE_PLAN.md](COURSE_PLAN.md), [STATUS.md](STATUS.md), and
  [WORKFLOW.md](WORKFLOW.md).
- Root requirements/constraints, `.env` helper and tests, classroom validator,
  preflight and smoke notebooks, changed workflows, and `AGENTS.md`.

Feedback disposition is now recorded in the reconciliation record. No manual
review task or repeated permission request is assigned to the user by this file.
