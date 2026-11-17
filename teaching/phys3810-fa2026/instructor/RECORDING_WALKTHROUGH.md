# Ubuntu recording walkthrough for the frozen Canvas kit

This is a mechanical recording checklist for Gage Plott, beginning with the
desktop extraction. It uses the final student-support edition and the existing
OBS setup. It does not require another pilot, approval questionnaire, or broad
technical review. The route is setup, QRNG, Bell, QFT, QPE, HHL; Grover/Shor are
optional. Only setup has the 15–20-minute target; total duration is flexible.

Frozen ZIP: `PHYS3810-Canvas-Kit-v0.2-f5ec2e4649de.zip`.
Source: `f5ec2e4649de34ed567f7694c497dfc874e14584`.
SHA-256: `e37d1c7051b3a1b9ea48004f73c22c13b60afc467e0ce488982c4feb138459f9`.
The previous v0.1 ZIP/checksum is archived intact separately. Do not mix an old
extracted folder or old environment into this recording workspace.

Keep the existing four-page [recording guide](recording-v0.2/PHYS3810_Recording_Guide_v0.2.pdf)
beside you. The [one-page support insert](support-v0.1/PHYS3810_Recording_Support_Insert_v0.1.pdf)
adds the simpler terminology/recovery/contact narration. The new
[student guide v0.3](../handouts/recording-v0.3/PHYS3810_Student_Guide_v0.3.pdf)
is the standalone student copy and is also inside the kit. No further advance
email is needed; the next transfer is the completed video, kit, and v0.3 guide.

## 1. Establish the extracted folder off camera

Use a fresh Desktop destination named `PHYS3810-Recording-v0.2`. The ZIP contains
one top-level `phys3810-canvas-kit` folder, so the working directory is:

```text
~/Desktop/PHYS3810-Recording-v0.2/phys3810-canvas-kit/runtime
```

If your Files extraction is already in that destination, skip the `unzip` line
below. Otherwise the command creates that exact layout without overwriting
existing files. An existing extraction somewhere else can remain untouched.
Do not move an already-created virtual environment into this folder.

Open an Ubuntu terminal, then set these variables. They apply to this terminal
session; repeat them if you open a new one later.

```bash
export PHYS3810_ZIP="$HOME/Desktop/PHYS3810-Canvas-Kit-v0.2-f5ec2e4649de.zip"
export PHYS3810_BASE="$HOME/Desktop/PHYS3810-Recording-v0.2"
export PHYS3810_RUNTIME="$PHYS3810_BASE/phys3810-canvas-kit/runtime"

cd "$HOME/Desktop"
sha256sum -c "$(basename "$PHYS3810_ZIP").sha256"
mkdir -p "$PHYS3810_BASE"
unzip -n "$PHYS3810_ZIP" -d "$PHYS3810_BASE"
cd "$PHYS3810_RUNTIME"
pwd
ls requirements.txt constraints-ci.txt src teaching
```

The checksum must say **OK**. The final directory must be the new kit's
`runtime/`, beside the listed files. Stop at a checksum/path error; do not
continue from a different folder. Keep the original ZIP/checksum unchanged.

## 2. Reset rehearsal notebooks off camera

For a newly extracted kit, the notebooks already contain the defaults and no
saved outputs. Use this reset after any practice or when you want a guaranteed
clean starting point. First save anything you want to retain, use Jupyter's
**File → Shut Down**, and wait for its launch terminal to return to a prompt.
Closing a tab alone leaves its kernel alive. Do not run this file reset while
the same notebooks are open in a running server: its autosave could restore
stale content.

Run the following from the new `runtime/` folder, with `PHYS3810_ZIP` set above.
It restores the five demonstrated notebook files from the exact frozen ZIP.
It backs up any changed working copy before replacement. It does not alter the
ZIP, dependencies, source modules, or other notebooks.

```bash
python3.12 - <<'PY'
from datetime import datetime
from pathlib import Path
import hashlib
import json
import os
import shutil
import zipfile

runtime = Path.cwd().resolve()
archive = Path(os.environ["PHYS3810_ZIP"]).expanduser().resolve()
assert runtime.name == "runtime" and runtime.parent.name == "phys3810-canvas-kit"
assert hashlib.sha256(archive.read_bytes()).hexdigest() == "e37d1c7051b3a1b9ea48004f73c22c13b60afc467e0ce488982c4feb138459f9", "Wrong or altered ZIP: stop."
manifest = json.loads((runtime.parent / "MANIFEST.json").read_text())
assert manifest["source_commit"] == "f5ec2e4649de34ed567f7694c497dfc874e14584", "Wrong extraction: stop."
names = ["intro/01_quantum_rng.ipynb", "intro/02_bell_state.ipynb",
         "02_qft.ipynb", "03_qpe.ipynb", "04_hhl.ipynb"]
backup = runtime / "artifacts" / "before-recording-reset" / datetime.now().strftime("%Y%m%d-%H%M%S-%f")
with zipfile.ZipFile(archive) as bundle:
    for name in names:
        relative = "teaching/phys3810-fa2026/notebooks/" + name
        baseline = bundle.read("phys3810-canvas-kit/runtime/" + relative)
        assert hashlib.sha256(baseline).hexdigest() == manifest["files"]["runtime/" + relative]["sha256"]
        notebook = json.loads(baseline)
        assert all(c.get("execution_count") is None and c.get("outputs") == []
                   for c in notebook["cells"] if c["cell_type"] == "code")
        target = runtime / relative
        assert target.is_file(), relative
        if target.read_bytes() != baseline:
            saved = backup / relative
            saved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, saved)
        target.write_bytes(baseline)
print("Five notebooks restored to frozen defaults; outputs/counts are blank.")
print("Changed-copy backups, if needed:", backup)
PY
```

For an in-session reset when the code is already at its defaults, select each
notebook tab, choose **Kernel → Restart Kernel and Clear…**, confirm, and save
with **Ctrl+S**. That clears memory and outputs, but does not restore parameter
edits; the ZIP reset above does both. Leave cells unrun until you narrate them.
Do not use Run All when you want an output-free starting screen.

## 3. Prepare OBS and the recording destination

OBS Studio is already installed as the user Flatpak. Launch it from the app
menu or a separate terminal:

```bash
mkdir -p "$HOME/Videos/PHYS3810"
flatpak run com.obsproject.Studio
```

Keep recordings in that Videos folder, outside the repository and frozen kit.
In OBS:

1. Use the existing scene and **Screen Capture (PipeWire)** source for the
   Ubuntu Wayland display. Select the intended display if permission is asked.
2. Right-click that source → **Transform → Fit to Screen**. The earlier display
   was 2560×1440 while the canvas/output were 1920×1080; fitting prevents the
   right/bottom crop. Do not stretch the picture or rely on an old preview.
3. In **Settings → Video**, keep 1920×1080 canvas/output and 30 fps.
4. In **Settings → Output**, keep the working recording encoder/quality and
   **Hybrid MP4**. Set Recording Path to your `~/Videos/PHYS3810` folder using
   Browse; a GUI field may not expand `~` automatically.
5. Select the actual microphone once in **Settings → Audio**. Keep unnecessary
   Desktop Audio disabled. Speak normally: the meter should respond without
   reaching clipping/0 dB. Avoid capturing the microphone twice.
6. Prepare a dedicated browser window for Jupyter. Hide personal tabs,
   bookmarks, notifications, and unrelated windows. Use full screen and enlarge
   browser/notebook text until the fitted OBS preview is comfortably readable.

This is the ordinary check before the full take, not another pilot milestone.
Keep the same working capture/audio configuration unless something is wrong.

## 4. Begin recording and show setup

Use **Start Recording** in OBS, then switch to the course terminal. Introduce
the route and invite pauses. Explain terminal versus notebook, and that the
first two commands check an existing Python installation. There is no grading
or submission. Run one line at a time from `runtime/`:

```bash
python3.12 --version
python3.12 -c "import struct; print(struct.calcsize('P') * 8)"
python3.12 -m venv .venv
source .venv/bin/activate
python --version
python -c "import sys; print(sys.executable)"
python -m pip install --upgrade pip==26.2.2
python -m pip install -r requirements.txt
python -m ipykernel install --sys-prefix --name phys3810-intro --display-name "Python (PHYS 3810 Intro)"
```

Expect Python 3.12, 64-bit, and an interpreter ending in this kit's
`.venv/bin/python`. Keep that path for the notebook comparison. This environment
is created once per extracted location, not once per lesson. If it already
exists from your own rehearsal of this exact kit, activate/reuse it and say
that the packages are already installed; do not present that as a fresh install.
Do not reuse a moved or different-kit environment. Stop at errors and use the
new guide's troubleshooting instead of changing pins or skipping failures.

Installation can take longer than the edited demonstration. If you pause or
shorten a wait, tell students to wait for their own successful completion.
The maintainer validator is not part of the student recording.

## 5. Launch Jupyter privately, then resume

Type the next command if you want to show it, but **pause OBS before pressing
Enter**. Launch and authenticate while capture is paused:

```bash
python -m jupyterlab
```

Keep this terminal running. If no browser opens, use its printed local URL
while paused. Keep authentication enabled. After authentication, make sure
the browser address no longer contains `token=`. Put Jupyter in its dedicated
window, hide browser chrome/full-screen it, and minimize the launch terminal.
Do not show that terminal, browser history, or a server-list command on camera.
Use a fresh terminal if another safe terminal demonstration is needed.

Resume OBS only after the intended notebook view is ready and no token is
visible. Use the recording controls' Pause/Resume buttons when needed; do not
assume a global hotkey works on Wayland.

## 6. Open and record the five notebooks

From Jupyter's file browser, open the following in order. Select
**Python (PHYS 3810 Intro)** for each new notebook. Each notebook has its own
kernel/session; do not attach a later lesson to another notebook's running
kernel. Run each initial location/import cell and compare **Interpreter:**
with the terminal path. Use **Shift+Enter**, top to bottom, waiting for `[*]`
to finish. Run helper/check cells too, but explain them briefly rather than
reading every implementation line aloud.

1. `teaching/phys3810-fa2026/notebooks/intro/01_quantum_rng.ipynb`: run sections
   1–5. Defaults are `shots = 128`, `seed = 2026`. Show H, exact 1/2 probabilities,
   ordered samples and counts. Edit 128 → 1024 → 128, executing **2 → 4 → 5**
   each time. These are seeded classical samples, not hardware entropy.
2. `teaching/phys3810-fa2026/notebooks/intro/02_bell_state.ipynb`: run sections
   1–5 in its own kernel. Explain H then CX and `00`/`11` correlation; qubit 0
   is the rightmost bit. Use the same **2 → 4 → 5** edits/restores. If section 7
   is already displayed, rerun it after every shot change. The extension is
   optional; a Z-basis correlation histogram alone does not prove entanglement.
3. `teaching/phys3810-fa2026/notebooks/02_qft.ipynb`: run all cells in order.
   Keep three qubits and `basis_label = "011"`; discuss the phase pattern,
   uniform probabilities, and inverse recovery. For `"011" → "001" → "011"`,
   run the edited parameter cell and **every following code cell** each time.
   Inverse samples are respectively 256 counts of the chosen label.
4. `teaching/phys3810-fa2026/notebooks/03_qpe.ipynb`: keep three counting qubits
   and `exact_phase = 3/8`. Demonstrate 3/8 → 1/8 → 6/8 → 3/8, rerunning the
   edited cell and **every subsequent code cell**. Exact labels are
   `011 → 001 → 110 → 011`, with 2048 shots. Do not reverse them. Briefly show
   the separate nonexact `1/3` example; retain its supported input range.
5. `teaching/phys3810-fa2026/notebooks/04_hhl.ipynb`: keep
   `matrix_entries = [[1.5, 0.5], [0.5, 1.5]]` and `rhs_amplitudes = [1, 0]`.
   Run from the top. Expected success is 5/8 and the successful state is
   `(3, -1)/sqrt(10)`; the relative sign matters. If demonstrating the RHS edit,
   use `[1, 0] → [0, 1] → [1, 0]`, rerunning that cell and **all following code
   cells** each time. Keep the matrix fixed.

Use the printed guide for the cell IDs, narration and detailed expected
results. Point to optional Grover/Shor without adding a new required lesson.
For guide links, use **Open With → Markdown Preview** if Markdown source opens.
Show the v0.3 troubleshooting page and explain the support contact and what
diagnostic information to include, omitting private tokens/account details.

## 7. Recover from a mistake during the take

Pause OBS at a clean boundary. Correct the intended parameter and execute it
before dependent cells. For confused state, save the intended values,
**Kernel → Restart Kernel**, then **Run → Run All Cells**. Remember that this
displays Bell section 7 too. Confirm current titles/counts, then resume at a
clear explanation boundary. Do not narrate stale figures as new results.

To begin a lesson completely afresh, restore its defaults, choose **Restart
Kernel and Clear…**, and save. For an exact whole-notebook restore use section 2
with the course server shut down. Neither action requires changing the ZIP or
rerunning installation. Do not improvise package upgrades while recording.

## 8. Finish and check the saved file

Show **Ctrl+S**, explain where **File → Shut Down** is, and remind students that
there is nothing to submit. End the narration, then click **Stop Recording**
and wait for OBS to finish writing. Shut down Jupyter off camera afterward.
Closing only a browser tab does not stop its kernel.

In OBS use **File → Show Recordings**, then open the intended finished MP4 in
VLC. Watch the actual saved file from beginning to end: opening/ending intact,
clear voice, readable code/figures, complete frame, correct current outputs,
clean pause/resume transitions, and no private tabs or token-bearing output.
An OBS preview or moving audio meter alone is not this playback check.

If you used MKV instead, use **File → Remux Recordings** to produce MP4, retain
the original, and play the MP4 too. No repeat short pilot is required solely
for this document update. Correct any actual final-file issue before delivery.

## 9. Prepare the final Canvas delivery set

Use the unchanged sealed ZIP, not a newly zipped working folder with `.venv`,
executed copies, or personal recording files. From the same terminal session:

```bash
export PHYS3810_DELIVERY="$HOME/Desktop/PHYS3810-Final-Delivery-v0.3"
mkdir -p "$PHYS3810_DELIVERY"
cp -n -- "$PHYS3810_ZIP" "$PHYS3810_DELIVERY/"
cp -n -- "$PHYS3810_ZIP.sha256" "$PHYS3810_DELIVERY/"
cp -n -- "$PHYS3810_RUNTIME/teaching/phys3810-fa2026/handouts/recording-v0.3/PHYS3810_Student_Guide_v0.3.pdf" "$PHYS3810_DELIVERY/"
xdg-open "$PHYS3810_DELIVERY"
```

Copy the verified finished video into that folder using Files. If a file with
the same name is already there, compare it rather than overwriting blindly.
Provide Rick the finished video, matching complete kit, and v0.3 student guide
for Canvas through the established delivery route. Clearly supersede the
advance materials for student use. Do not send the audit/coordination packet,
presenter notes, private test footage, or a new approval questionnaire.

## Mechanical verification and references

The reset procedure was checked in a disposable copy: five exact baselines
restored, changed copies backed up, wrong ZIP rejected before overwrite.
The normal environment/kernel route is covered by the exact-kit acceptance.
These checks do not claim the user's future reset, recording, or delivery has
already occurred. No source repository notebook or frozen ZIP is reset by
these instructions.

- [OBS quick start](https://obsproject.com/kb/quick-start-guide)
- [OBS source transforms and recording settings](https://obsproject.com/kb/obs-studio-overview)
- [OBS recording output and remuxing](https://obsproject.com/kb/standard-recording-output-guide)
- [JupyterLab 4.6 commands](https://jupyterlab.readthedocs.io/en/4.6.x/user/commands_list.html)
- [Jupyter authentication](https://jupyter-server.readthedocs.io/en/latest/operators/security.html)
