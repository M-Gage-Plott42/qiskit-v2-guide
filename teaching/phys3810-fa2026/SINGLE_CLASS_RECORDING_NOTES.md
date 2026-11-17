# Single-class recording platform notes

The presenter is Gage Plott; the recording platform is Ubuntu/Linux with OBS.
The current route is 15–20 minutes of setup, then RNG, Bell, and the full
reference QFT, QPE, and HHL notebooks. Grover and compiled N=15 Shor remain
optional. There is no fixed total-duration gate. Student pauses and
installation waits can take longer than the edited video. Delivery is through
Canvas; nothing is assigned, graded, evaluated, or submitted.

The operator reports a successful Ubuntu/OBS pilot with voice, pause/resume,
and playback. Fit to Screen is confirmed by the operator. The corrected saved
media has not been independently inspected here. This is reported pilot
evidence, not a new independent capture/audio inspection; another pilot is
not a prerequisite for proceeding to the final recording.

The tool-documentation research below was checked November 16, 2026.

## ONLYOFFICE and desktop capture

The installed Snap metadata identifies ONLYOFFICE Desktop Editors **10.0.0**,
revision **1706**, on Ubuntu 26.04.1 LTS x86_64 using Wayland. This is a read-only
package inventory, not an observed feature or export test in the application.

The current [ONLYOFFICE export documentation](https://helpcenter.onlyoffice.com/docs/userguides/presentation-editor/tools-and-settings/export-animation-video)
describes presentation export to MP4 or WebM, with slide range, resolution, and
per-slide duration settings. Desktop access is through File → Export. The
[desktop changelog](https://helpcenter.onlyoffice.com/desktop/desktop-changelog)
lists this export feature under version 10.0.0, released October 13, 2026.

Those documented slide-export controls do not establish live terminal/Jupyter
screen capture, microphone narration, or the Windows PowerPoint recording
workflow. No equivalent integrated screen-and-microphone recording workflow
was verified in the consulted current ONLYOFFICE documentation. This is a
documentation limitation, not proof that every extension or future version
lacks such a feature. Do not translate Windows shortcuts into assumed Linux
features or claim the installed editor has passed a recording test.

The [OBS official quick start](https://obsproject.com/kb/quick-start-guide)
documents Linux display/window capture sources, microphone/audio selection,
local recording, and a test recording. A dedicated recorder such as OBS is
the selected recorder: show terminal and JupyterLab directly, with slides only
if useful. The earlier documentation research did not itself test recording.
The operator-reported pilot above is separate evidence from the actual Ubuntu
workflow; it is not an independently inspected final video.

## Supplied recording-script revision

The supplied recording-script v0.2 now replaces the Windows desktop PowerPoint
assumption with an Ubuntu/OBS workflow. Its exact Word/Markdown bytes are
retained locally; see the [focused reconciliation](SINGLE_CLASS_REVIEW_RECONCILIATION.md)
for receipt verification and the old-candidate navigation correction. That
four-chapter script is historical; align the current narration to setup, RNG,
Bell, QFT, QPE, and HHL, followed by the optional Grover/Shor signpost. Use
`02_qft.ipynb`, `03_qpe.ipynb`, and `04_hhl.ipynb`, rather than the earlier
combined guided QFT/QPE notebook. Keep the invitation to pause and both intro
shot-count changes: run section 2, then 4, then 5; rerun Bell section 7 if
already displayed. Intro defaults remain 128 shots and seed 2026. Match narration
to the reviewed candidate, current quickstart commands, stable cell IDs, and
figures. Use **Python (PHYS 3810 Intro)** throughout and compare interpreter
paths when opening each notebook. Do not use a historical download that lacks
the intro lessons.

For the normal final-take check, play back the actual delivery file and
confirm readable code at laptop size, clear voice, visible pointer, complete
framing, and an intact ending. Check the beginning, notebook transitions, and
end after any editing. This final-file check does not reopen the completed
pilot or impose a total-duration limit.

Keep Jupyter authentication enabled. Pause recording during server launch and
authentication so terminal tokens and authentication URLs stay out of the
video. Jupyter documents token-based access in its
[server security guide](https://jupyter-server.readthedocs.io/en/latest/operators/security.html).
If installation waits are shortened in editing, say so; do not imply that the
edited duration is a guaranteed installation time.

Keep the Canvas video and supplied kit matched to the same reviewed revision.
Ubuntu/Linux, Canvas delivery, and the ungraded format are settled.
