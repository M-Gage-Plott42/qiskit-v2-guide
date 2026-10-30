# Grover document v0.2 receipt

Received and inspected October 30, 2026. These are **verified review drafts**
for unchanged code release `phys3810-fa2026-grover-v0.1.0-rc1`, source commit
`3894391f2026d4fd9351b346b44b5eda453a17da`. These files are included in this local documentation change; they have not
been published as release assets. Both files display document v0.2 dated October 29, 2026. A corrected
delivery receipt was subsequently received and independently checked locally;
the original hash discrepancy is closed. Keep the existing files unchanged.

## Student guide

[Student setup PDF](PHYS3810_Student_Setup_Grover_RC1_v0.2.pdf), 3 pages,
97,906 bytes. [Markdown companion](../preview/SETUP_REVIEW_DRAFT.md).

- Authoritative delivered-file SHA-256, verified locally:
  `e5f9aa3813a38756c3568a42695b56b45f2005d1e78e93e7978722e8673755bc`.
- Superseded pre-delivery SHA-256, retained as historical evidence:
  `1161dded4dfbbe97e2a898fca426372e4fa9d857e6e1c6328d8d80460612d51e`.
- Current identity check: **passed against the corrected delivery receipt**.

## Instructor guide

[Instructor review PDF](../instructor/PHYS3810_Grover_Instructor_Guide_RC1_v0.2.pdf),
2 pages, 95,073 bytes. [Markdown companion](../preview/INSTRUCTOR_REVIEW_DRAFT.md).
Keep this guide separate from the student ZIP.

- Authoritative delivered-file SHA-256, verified locally:
  `9048e56ee2cbca9c8757112558471862cfb4d843de0798f70b6a3c51bd9a1c72`.
- Superseded pre-delivery SHA-256, retained as historical evidence:
  `3f0a4a0f08a370e5f320bc9a3d4316d010e2fb0ed32376b9167c9f6f7fcafc57`.
- Current identity check: **passed against the corrected delivery receipt**.

## Inspection and handling

Both repository copies match their received files byte for byte. No PDF was
regenerated or edited; the source downloads were retained. All five rendered
pages were visually inspected, without visible clipping or overlap. Text
checks confirm the moved-environment correction, `pymanager install 3.12`,
50 tests/four notebooks, visible authorship, and document/code version labels.
Both have meaningful `/Title` and `/Author` metadata. Ten student and seven
instructor link annotations use expected HTTPS destinations with valid
rectangles; no out-of-page glyphs or replacement characters were found.
This checks embedded targets and geometry, not every website's availability.
The reviewer reports OCR; Codex did not rerun it.

## Corrected receipt and cause

The initial comparison failed against the handoff's pre-delivery hashes; that
historical result is retained. ChatGPT subsequently retrieved the final
downloadable copies, reproduced the delivered-file hashes above, and supplied
them as the authoritative integration receipts. No replacement PDFs are needed.

Local read-only checks confirmed each delivered file contains a prefix whose
SHA-256 equals the old pre-delivery hash, followed by **24,961 appended bytes**
containing C2PA provenance information. The student prefix is 72,945 bytes;
the instructor prefix is 70,112 bytes. Repository and Downloads copies match.
The earlier comparison used different byte extents; duplicate-file cleanup did
not resolve it. Full delivered-file hashes now govern integration/publication.

The reviewer independently reports identical per-page extracted text,
title/author metadata, 17 link annotations, and pixel-identical renders of all
five pages at 150 dpi versus the pre-delivery originals. Those comparison runs
are reviewer evidence; Codex verified the full-file/prefix hashes and preserved
the earlier local visual checks. No C2PA signature validation is claimed.

Do not regenerate, optimize, alter metadata, or strip appended provenance from
these files. Prefix hashes were calculated in memory without writing modified
PDFs. Preserve the delivered bytes and record any future edition separately.

The original rc1 ZIP and release assets remain unchanged. The full technical
disposition is in [the release audit reconciliation](../GROVER_RELEASE_RECONCILIATION.md).
Integration acceptance includes `git ls-files` coverage, exact hashes, and
working relative links from an isolated checkout. The original development
index remains untouched; only the separate integration worktree is staged.
