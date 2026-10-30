# Grover preview publication

Published October 29, 2026:
[phys3810-fa2026-grover-v0.1.0-rc1](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-grover-v0.1.0-rc1).
The course-prefixed release is explicitly a prerelease. Existing stable
release `v1.0.0` remains latest; this was verified after publication.

The original candidate `9f16c0a` received publication-link updates in `8f7074f`.
[PR #112](https://github.com/M-Gage-Plott42/qiskit-v2-guide/pull/112) passed all
nine required checks with no unresolved review threads, then merged normally
as `3894391f2026d4fd9351b346b44b5eda453a17da`. No rule or check was bypassed.
The published tag points to that merged revision, and subsequent main workflows passed.

The final 25-file ZIP (including the setup PDF) was rebuilt from the merged
revision and passed extraction validation with 50 tests/four notebooks using
the existing classroom environment. Its SHA-256 is
`c46d8f2ac837f2742a99384cee1bc637478b4387909a4c399e4599655b11e686`.
Both PDFs were regenerated with the actual versioned download URL; all five
pages, link annotations, and text bounds were checked. All three public assets
downloaded without authentication and matched local hashes. QFT development
remains separate and is not in the released source or ZIP.

## October 30 audit and document v0.2 follow-up

The additional independent audit reports the published ZIP passing 50 tests
and four notebooks on Linux CPython 3.12.14 using the existing pinned
environment. It verified required PR checks and the
[PR](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/runs/40984800543) and
[merged-commit](https://github.com/M-Gage-Plott42/qiskit-v2-guide/actions/runs/40985140436)
classroom runs on Ubuntu x64/CPython 3.12.15. Remote success-path artifact upload
was observed; deliberate remote failure-path upload remains untested.

ChatGPT supplied document v0.2 editions for unchanged rc1 code. They are now
local repository review drafts in `handouts/` and `instructor/`, with
synchronized Markdown companions. The initial receipt hashed pre-delivery
files; the corrected receipt now identifies the complete delivered copies,
including appended C2PA provenance. Both full-file and prefix hashes passed
local checks. [The receipt](handouts/README.md) records the resolution; keep
the existing PDFs unchanged. See [the reconciliation](GROVER_RELEASE_RECONCILIATION.md).

The [initial instructor review packet](INSTRUCTOR_REVIEW_PLAN.md) is ready for
the user to send as two v0.2 attachments plus the named rc1 ZIP link. Explain
that the attached setup guide supersedes the older guide embedded in that ZIP.
No new PDF, archive, or algorithm release is needed for this initial feedback.

Later work: preserve the dirty checkout, prepare a scoped documentation change
from current main, verify tracked PDFs and clean-checkout links, and request
applicable publication authorization. Add distinct v0.2 PDF assets and link the
documentation commit in release notes. Preserve the original tag, ZIP, and
assets; a refreshed ZIP requires a new candidate version and matching PDF.
No commit, PR, release-asset update, or algorithm work was performed this turn.

## Scope and assets

The preview contains onboarding plus the corrected, bounded 2–5-qubit Grover
lesson, independent tests, pinned dependencies, and the strict validator.
QFT/QPE/HHL/Shor are excluded from this first student preview. The root folder
of the curated ZIP remains `phys3810-grover`.

Published assets:

- `PHYS3810-Grover-v0.1.0-rc1.zip`: standalone runnable source, tests, notebooks,
  setup instructions, license, concise evidence, and the intentional setup PDF.
- `PHYS3810_Setup_Review_Draft_2026-10-29.pdf`: student setup review draft v0.1.
- `PHYS3810_Grover_Instructor_Review_Draft_2026-10-29.pdf`: instructor review draft
  with prerequisites, timing, answers, and unresolved teaching decisions.

The setup and instructor PDFs are instructional deliverables, not saved notebook
execution output. Prompts, agent policies, unrelated history, credentials,
caches, venvs, logs, and executed notebooks stay out of the standalone ZIP.
The instructor guide may accompany the review packet separately from the
student ZIP. Editable sources and the renderer are retained in the repository.

## Source and integration

The published Grover-only branch was prepared from remote main
`bf6f362ded70767d3891db996a0a3e0cd152b34d`, preserving the existing development
working tree and its index. The six upstream-changed files were inspected.
Newer setup-python, upload-artifact, and CodeQL pins are preserved; shared
application dependency pins in the selected universal lock are equal to or
newer than main. Do not replace that lock with the older Linux-only freeze.

Identify the local preview commit before building release candidates. The
standalone builder reads an explicit Git revision, not an uncommitted directory.
Record the commit and archive hash in the local release manifest. If publication
uses a different merged commit, rebuild from that commit and verify the assets
again. Do not label an unpushed commit URL as publicly accessible.

## Required checks and publication boundary

Run local mathematical, notebook, archive, lint, and PDF rendering checks.
Remote CI remains a separate requirement: `local-smoke`, `ruff`, `markdownlint`,
`yamllint`, `actionlint`, `shellcheck`, `dependency-review`, `Analyze (python)`,
and `Analyze (actions)`. Preserve the PR workflow, strict check requirements,
and resolved-review-thread rule; do not use bypass privileges.

The user authorized this preview's push/PR, green-check merge, and prerelease
workflow. Those actions are complete. No instructor message, hardware job, or
unrelated publication was authorized or performed. Future release work must
retain the normal contribution workflow and version-matched source/assets.

The [standalone download](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip)
is live. The original v0.1 PDFs were produced with `--tests 50` and that URL
using `scripts/render_review_guides.py`. That renderer remains a maintainer
utility; it must not regenerate or substitute the supplied v0.2 editions.
ChatGPT owns PDF authorship/rendering/OCR; Codex verifies and integrates bytes.
The publication receipt is retained locally in `artifacts/grover-preview/publication-plan.json`.

Native Windows/macOS, interactive Jupyter/editor use, and timed delivery remain
unvalidated. State these limits in release notes. Session dates, student
preparation, preferred meeting length, platforms, and assessments remain unknown.
Draft feedback can improve later modules while QFT/QPE development continues;
final materials must still be frozen and rehearsed before each confirmed session.
