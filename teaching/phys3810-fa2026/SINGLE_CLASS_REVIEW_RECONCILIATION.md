# Focused single-class review reconciliation

November 16, 2026. The focused review of the RNG/Bell candidate is received.
It reports no additional blocking scientific or advertised-rerun defect and
identifies one required exported-navigation repair, M1. The current work fixes
that defect and verifies a separately identified candidate; the original
reviewed archive and supplied recording documents remain unchanged.

## Received identity and accessible files

The reviewed archive is `PHYS3810-Single-Class-Review-v0.1-754ec33d6200.zip`,
source `754ec33d620033faf1d2f3754cba811e04d22ad5`, 179,296 bytes. Its SHA-256 is
`477e7a8aced1cd516f90714437137bfcc06ad2edd2b7660d4cc80e75c0b47274`;
its manifest SHA-256 is
`c2c15bfd5f4f51302b57f75c80a288069d281bfc74736124efe142079529bb1f`.
The reviewer verified all 55 payload files plus the manifest and reports no
payload modifications. This candidate is a local commit; the reviewer used
the actual attachment after its remote commit lookup found no commit. No
remote provenance or substitution of main is claimed.

The actual return ZIP was found locally in Downloads:
`PHYS3810_Recording_Sync_v0.2_754ec33d6200.zip`, **67,428 bytes**, SHA-256
`e4abb69164f960339385d14865afb261bc5d4cd365b2bef10ca98517c315259c`.
Its CRC, safe paths, four-member inventory, and all three receipt-listed file
hashes match the supplied receipt and the checksum in the received review.
Accessible bytes are the Word script, matching Markdown, detailed text review,
and `RECEIPT.json`; the previously inaccessible-script status is superseded
for this v0.2 edition. The older v0.1 Word edition is referenced, not newly
received. No access to the reviewer's private execution directory is claimed.

Supplied full-file identities:

- `PHYS3810_Single_Class_Video_Script_v0.2_Ubuntu_754ec33d6200.docx`:
  50,008 bytes; SHA-256
  `e803b40e147ea96fb3e175cdf0faa2068b4cee3f71a91afcb3a39530c2fcc935`.
- `PHYS3810_Single_Class_Video_Script_v0.2_Ubuntu_754ec33d6200.md`:
  27,141 bytes; SHA-256
  `ce3c89151ef7f591ccdffcf151aab2986230fb626e53e565a479c91995bbb771`.
- Detailed return review: 12,178 bytes; SHA-256
  `6061ff261d9a3f28524062ef456c4e26b981d19d13531b7709ececa3b9f78ff9`.

Exact received files and raw review/receipt stay under the ignored
`artifacts/single-class-review-2026-11-16/` evidence directory. The recording
script includes maintainer coordination and old-candidate statements about M1;
it is preserved as a local recording draft rather than silently edited or
copied into public student materials. This reconciliation carries the later
navigation disposition separately. Its source defaults, notebook paths, cell
IDs, parameter sequence, and setup commands remain unchanged by the M1 repair.

**Local document verification passed:** all ten Word pages were rendered and
visually inspected, then OCR-checked with Tesseract 5.5.0. Normalized token
recall ranged from 98.83% to 100%; code/hash/glyph recognition differences were
checked against source text and page images. All 189 normalized Word/Markdown
text blocks and ten quickstart terminal commands match. Title, author **Gage
Plott**, and all nine hyperlink destinations agree with the supplied receipt;
the nine official reference URLs opened successfully. Document QA used its
separate managed CPython 3.12.14 runtime and LibreOfficeDev 26.8.0.0.alpha0,
not the classroom interpreter or a native Word/ONLYOFFICE UI. QA intermediates
stay local and no new student PDF was produced.

The exact supplied Markdown has nine MD025 lint findings from its page-based
H1 headings. They are recorded without altering the companion bytes or claiming
the supplied document passed repository Markdown lint. It is outside the
committed teaching files and runnable package. Pages 1 and 6 retain old-candidate
M1 instructions; those refer to the frozen v0.1 export and are superseded for
the corrected candidate by this reconciliation, not by an edited script.

## M1 reproduction and correction

**Reproduced:** in the exact v0.1 extraction, the notebook-linked inner
`runtime/teaching/phys3810-fa2026/intro/START_HERE.md` is readable through
`FileContentsManager(root_dir=runtime)`. Its `../../../../START_HERE.md` redirect
resolves to the outer guide, which exists on disk but returns **HTTP 404** from
the contents manager as outside the served root. Section 5 contains only that
redirect, so an existing anchor does not provide a usable optional menu.
The same issue affects generated SETUP/COURSE_PLAN and contract-header links.
The local reproducer uses the existing Ubuntu CPython 3.12.15 application
environment; it is a direct contents-manager check, not a browser click.

**Fixed in the exporter:** the correction retains a complete quickstart and optional menu inside
`runtime/`, redirects related generated navigation to served destinations,
and preserves the mathematical contract bodies and outer entrance. A production
export check and regressions must reject any advertised runtime link that
escapes the root, including the old stub; outside-root access must remain 404.
The full inner quickstart is an exact copy of the committed guide. The generated
validation note now lives at `runtime/VALIDATION.md`; the outer quickstart stays
available for offline review. No notebook/script command, default, cell ID,
mathematical contract body, or algorithm implementation changes.

Three new exported-kit regressions follow the actual intro notebook links to
the full guide, verify setup/recovery text and the five-algorithm menu, check
anchors and contents-manager access, reject the original outside-root stub,
and reject encoded traversal/absolute local links. Independent internal scope
review found no blocking issue and verified protected source/document bytes.
This is internal integration review, not a second external review.

## Corrected source validation

**Passed:** `python scripts/validate_classroom.py --profile all` measured
**224 tests / 13 fresh-kernel notebooks / 85 nonempty code cells / 32 PNGs**.
All required cells executed without error, and source notebooks remain output
free with null execution counts. The validator includes package consistency
and the full unit suite; no duplicate unittest discovery was run afterward.

This uses the **reused** current-pins application environment from the initial
single-class work: Ubuntu 26.04.1 LTS x86_64, Linux 7.0.0-43-generic, glibc 2.43,
CPython 3.12.15, Qiskit 2.6.1, Aer 0.18.2, JupyterLab 4.6.5, ipykernel 7.4.0,
NumPy 2.5.4, Matplotlib 3.11.2, pip 26.2.2. No fresh source installation is claimed.

These additional gates also **passed**:

```bash
python -m ruff check src scripts tests teaching/phys3810-fa2026/notebooks notebooks/00_local_statevector_smoke.ipynb notebooks/01_local_aer_smoke.ipynb
bash scripts/smoke_local.sh artifacts/single-class-review-2026-11-16/smoke
pre-commit run --all-files
```

Ruff 0.15.22/pre-commit 4.7.0 use the separate reused tool environment and
workspace hook/npm caches. Task-local Matplotlib/IPython paths avoid changing
personal settings. Source logs and exact per-notebook counts/hashes are in
`artifacts/single-class-review-2026-11-16/`. Earlier executed outputs were
preserved before this run. New source acceptance does not establish exact
archive execution; the separate delivery receipt follows that gate.

## Corrected candidate and exact extraction

**Passed and delivered locally:** the existing exporter produced a new v0.2
archive, retaining the original v0.1 archive and return package unchanged.

- Source commit: `2dcda953e8fbd03d85a6b11bedc4b6f9cd4c2d0e`.
- Source tree: `d38d4c0e5b5849c501d98c7e307da540b18beed0`.
- ZIP: `PHYS3810-Single-Class-Review-v0.2-2dcda953e8fb.zip`.
- Size: **184,190 bytes**; **56 files / 55 manifest entries**.
- ZIP SHA-256: `737d5c200e2732732ba124e662973d65a53680c65cd51f0ab93261d4e0b64173`.
- Manifest SHA-256: `a5fe43884ec5ba234a2087ebf9ab4c659c177aabb140e51eef333f4886455140`.
- Static relative-link checks: **49**.

The exact archive was extracted outside the checkout into
`/tmp/PHYS3810 single class v0.2 2dcda95/phys3810-single-class-review`.
A **fresh application `.venv`** was created inside its `runtime/`, using the
existing CPython 3.12.15 interpreter, pip 26.2.2, and the unchanged requirements.
All 114 application distributions match their active pins. This is separate
from the reused source environment and is not a new Python installation.

From the extracted `runtime/`, its own interpreter ran
`python scripts/validate_classroom.py --profile all` with no inherited
`PYTHONPATH`: **224 tests / 13 fresh-kernel notebooks / 85 code cells / 32
PNGs passed**. Required execution counts and absence of error output were
checked. Canonical imports resolve inside this extraction's `runtime/src/`.
All 55 payload sizes, hashes, and modes match before and after validation;
the manifest remains unchanged. The new ZIP was copied to the Ubuntu desktop
and verified byte-for-byte, without replacing the earlier ZIP.

The full inner quickstart and all notebooks are unchanged source bytes, so
their earlier visual/OCR evidence carries forward; this navigation fix did not
reproduce unchanged figures or claim a new lesson-render review. The supplied
Word script's separate local ten-page QA is recorded above. Recording documents
and prompts remain outside the runnable ZIP.

## Authenticated Jupyter navigation

**Passed:** a real JupyterLab server started from the extracted environment
with `runtime/` as its served root and authentication enabled. HTTP contents
and file requests followed **27 link traversals across 16 documents**, including
both intro titles, Bell's finish/menu anchor, substantive setup/recovery text,
all five optional notebook destinations, and the generated setup/plan/contract
links. Contract evidence resolves to the served `runtime/VALIDATION.md`.
The actual outside-root HTTP request still returns **404**. No root restriction
was relaxed. The registered `phys3810-intro` kernel points to the extraction's
exact `.venv/bin/python`; authenticated test-server shutdown succeeded.

The startup command used `python -m jupyterlab --no-browser --ip=127.0.0.1
--port=8880 --ServerApp.port_retries=0`, with task-local Jupyter/IPython/Matplotlib
paths. These are disclosed test adaptations, not extra student setup commands.
The navigation evidence is real authenticated HTTP, not a browser click-through.
The browser access host was unavailable, so **interactive UI remains untested**.

M1 is reproduced, corrected, regression-covered, and verified in the exact
package through contents-manager and HTTP checks. The remaining operational
check is the human browser/recording walkthrough. Receipts, logs, exact received
documents, a current script-reading note, and extracted executed copies are
preserved under `artifacts/single-class-review-2026-11-16/`; private tokens and
raw review coordination are excluded from shareable artifacts.

## Independent review evidence and its limits

The reviewer reports a **fresh application installation** from supplied pins
on **Debian GNU/Linux 13 x86_64**, using an **existing CPython 3.12.14**
interpreter. All 114 application distributions matched the active constraints.
This is neither Ubuntu validation nor a new Python-interpreter installation.

The full validator **failed with exit 1**: **221 tests ran, 215 passed, six
failed**. The six kernel integration tests and all thirteen notebook launches
encountered an operation-not-permitted local-interface/libzmq restriction before
the kernel-info reply. Thus the notebook gate completed **zero notebooks,
zero code cells, and zero PNGs**. These are executed failures, not skips or a
full pass. No source change or weaker execution policy is justified by that
environmental restriction.

All fifteen intro actual-cell tests passed. Separately, two fresh direct
IPython processes executed the unchanged intro lessons: **eleven code cells
and five PNGs**, all figures visually inspected by the reviewer. That narrower
success does not replace Jupyter fresh-kernel validation. The prior local
Ubuntu result of **221 tests / 13 notebooks / 85 cells / 32 PNGs** remains
attributed to [the original candidate evidence](SINGLE_CLASS_VALIDATION.md).

## Recording and next actions

The supplied v0.2 script replaces the Windows PowerPoint assumption with an
Ubuntu/OBS workflow. ONLYOFFICE may display optional slides; slide export alone
does not establish live terminal/Jupyter/microphone capture. Retain the
30–60 second pilot with normal voice, window switching, circuit/histogram,
scrolling, pause/resume, and playback of the actual saved file. Keep Jupyter
authentication enabled and pause capture before launching/authenticating.

The one-class, zero-Python, no-assessment scope is unchanged. The core lesson
edits remain 128 → 1024 → 128 using sections 2 → 4 → 5, with Bell section 7
rerun whenever already displayed. Section 3 does not depend on shots; section
6 is explanatory text. Keep the X-basis extension optional in the video.

**Untested:** browser click-through and native recording/audio/playback here;
the browser access host is unavailable and native application control is
disabled. The passed authenticated HTTP checks above are separate. Human pacing,
the total class window including pauses, delivery location, and assistance for
students lacking the required Python environment remain open. The 43-minute
target is proposed, not measured. No new broad review is needed solely for an
evidenced M1 fix; the next human action is the recording pilot and core rehearsal.
No push, publication, merge, external message, or hardware job is performed.
