# Single-class recording platform notes

Research checked November 16, 2026. These are production-planning notes, not a
recorded pilot or a replacement narration script. The presenter is Gage Plott;
the confirmed recording platform is Ubuntu/Linux. No new class date or total
class window is confirmed. The proposed 43-minute video remains an untested
target: 18 minutes setup, 10 RNG, 12 Bell states, and 3 optional exploration.
Student pauses and installation waits can make the session longer.

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
therefore a supported candidate for the production plan: show terminal and
JupyterLab directly, with slides only if useful. This is a recommendation based
on documented capabilities; no recorder installation, source permission,
microphone capture, encoder performance, or exported-video test was performed.
The exact capture-source choice must be checked on the actual Wayland session.

## Next recording-script revision

Replace the Windows desktop PowerPoint assumption with an Ubuntu workflow.
Keep four replaceable chapters, the invitation to pause, and the two notebook
shot-count changes. Match narration to the exact reviewed candidate, current
quickstart commands, stable cell headings, default shots/seed, and figures.
Do not use a historical release download that lacks the intro lessons.

Before the final take, record and play back a 30–60 second pilot containing a
code cell, histogram, window change, pointer, and voice. Confirm readable code
at normal laptop playback size, clear audio, visible pointer, correct framing,
and an intact ending in the actual delivery file. This pilot and the recording
application's UI require a human on the desktop; native app control is not
available in this workspace. These checks are **untested**, not failed.

Keep Jupyter authentication enabled. Pause recording during server launch and
authentication so terminal tokens and authentication URLs stay out of the
video. Jupyter documents token-based access in its
[server security guide](https://jupyter-server.readthedocs.io/en/latest/operators/security.html).
If installation waits are shortened in editing, say so; do not imply that the
edited duration is a guaranteed installation time.

The remaining logistical decisions before the final recording are the total
class window and the video/matching-kit delivery location. Ubuntu/Linux is
settled. No grading, assignment, or submission decision needs reopening.
