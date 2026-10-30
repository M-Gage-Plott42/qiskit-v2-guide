# Grover preview preparation

Publication through the normal PR and required-check workflow was authorized
on October 29, 2026. The course prerelease tag is
`phys3810-fa2026-grover-v0.1.0-rc1`; it was absent on October 29, 2026 but has
not been reserved. Existing repository releases use `vMAJOR.MINOR.PATCH`, with
`v1.0.0` latest. The course-prefixed prerelease is a separate namespace and
must not replace the latest stable release.

## Scope and assets

The preview contains onboarding plus the corrected, bounded 2–5-qubit Grover
lesson, independent tests, pinned dependencies, and the strict validator.
QFT/QPE/HHL/Shor are excluded from this first student preview. The root folder
of the curated ZIP remains `phys3810-grover`.

Planned assets:

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

Prepare the Grover-only branch from remote main
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

Authorization covers this preview's push, PR, merge only after required checks
pass, and prerelease publication. It does not authorize messages to instructors
or unrelated releases. Use the normal contribution workflow, wait for required checks, publish the identified
revision as a prerelease, attach validated assets, and set the real download
link in the synchronized setup source/PDF. The intended asset URL is
[the versioned standalone ZIP](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip).
Generate the release PDFs with that URL and `--tests 50` using the renderer from
the merged revision. The link becomes live when the release is published.

Native Windows/macOS, interactive Jupyter/editor use, and timed delivery remain
unvalidated. State these limits in release notes. Session dates, student
preparation, preferred meeting length, platforms, and assessments remain unknown.
Draft feedback can improve later modules while QFT/QPE development continues;
final materials must still be frozen and rehearsed before each confirmed session.
