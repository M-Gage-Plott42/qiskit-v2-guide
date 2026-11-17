# Troubleshooting cues for the recording

PHYS 3810 | Gage Plott | Presenter insert v0.1 | Use beside the four-page recording guide

The existing recording guide's notebook order, examples, defaults, and results still apply. This page adds the simpler explanations and troubleshooting promised for the final student materials. It is a recording aid, not another pilot or approval step.

## Before the first setup command

**Say:** "The setup shown here uses Ubuntu and Python 3.12. The first two commands check that Python is present and is 64-bit; they do not install Python. If those checks fail, pause here. The troubleshooting page tells you what to send me so we can use the right setup for your machine."

Show the extracted kit's **runtime/** folder and **requirements.txt**. Distinguish the terminal, where setup commands go, from notebook cells, where lesson examples run. Run each command separately. Show the printed Python path and explain that the notebook should use that same environment. Keep authentication tokens off camera when launching Jupyter.

## Make the first notebook easy to follow

**Say:** "A cell is one block of code or text. Shift+Enter runs a code cell. The kernel is the Python session that remembers its results. An asterisk means it is working. Changing a number on screen does not run the code or update an old plot."

Use the established RNG edit and restore: **128 -> 1024 -> 128**, running **section 2 -> section 4 -> section 5** each time. For Bell, rerun section 7 too whenever it has already been displayed. Explain checks as software safeguards; nothing is graded or submitted.

## Show recovery without adding a new lesson

Point out **Kernel > Change Kernel > Python (PHYS 3810 Intro)** and the notebook's **Interpreter:** path. For stale results or out-of-order cells, show where **Kernel > Restart Kernel** and **Run > Run All Cells** are located. Explain that restart forgets stored values and Run All rebuilds them. A Bell Run All displays its optional section 7.

For missing files, return to the extracted runtime folder. For an interrupted package download, retry the same install command after restoring the connection. Stop at repeated errors; do not skip failed cells or improvise package upgrades. If a guide opens as plain Markdown, use **Open With > Markdown Preview**.

## Give students one clear support route

**Say:** "If the matching fix on the last page does not solve it, email me at gage-plott@utc.edu. Include your operating system, Python version, notebook and section, the exact error, and what you tried. A cropped screenshot helps, but leave out private URLs, passwords, and tokens. You can pause and return later; there is nothing to submit."

Keep QFT, QPE and HHL explanations focused on the task, circuit and displayed result. Their helper code and more technical details remain in the notebooks. Close with the optional Grover/Shor pointers, **Ctrl+S**, and **File > Shut Down**. Use the ordinary final playback check for the saved video.

[JupyterLab commands](https://jupyterlab.readthedocs.io/en/4.6.x/user/commands.html)
[Jupyter authentication and tokens](https://jupyter-server.readthedocs.io/en/latest/operators/security.html)
