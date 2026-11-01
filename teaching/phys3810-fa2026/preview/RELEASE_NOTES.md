# PHYS 3810 Grover preview v0.1.0-rc1

This prerelease candidate provides the first PHYS 3810 algorithm lab: phase
oracles, amplitude amplification, multiple marked states, and overshooting.
It includes reusable source, independent mathematical tests, a commented
50-minute core with a 75-minute expansion, and a standalone `phys3810-grover`
folder that runs without Git or an IBM account.

The classroom environment pins CPython 3.12-compatible packages, including
Qiskit 2.6.1 and Aer 0.17.2. Run `python scripts/validate_classroom.py` after
installing the included requirements. Local validation passed 50 tests and
four required notebooks, including the corrected editable-target exercises.
The required runner rejects skipped code and tagged errors and preserves
diagnostics on failure.

The setup PDF is a **review draft v0.1**, not a final classroom guarantee.
Use it with this candidate's standalone ZIP. The instructor guide accompanies
the initial feedback cycle. Dates, student preparation, assessment expectations,
and target classroom platforms still need confirmation.

Supported Grover examples use 2–5 qubits, explicit marked states, uniform
preparation, and ideal local execution. They do not establish quantum advantage
or general large-instance search performance. QFT, QPE, HHL, and Shor are not
included in this first preview.

Original correction evidence is from Linux x86_64, CPython 3.12.15. The
additional review received October 30 independently reports the published
50-test/four-notebook snapshot passing on Linux CPython 3.12.14 using a reused
pinned environment. All nine required PR checks and the merged-commit Linux
classroom run passed; successful artifact upload was observed.
Native Windows/macOS, interactive editor use, hardware/GPU execution, and a
live classroom timing rehearsal remain unvalidated. Deliberate remote
failure-path artifact upload remains untested.

## Planned document v0.2 update — not yet published

The received student and instructor guides are document revisions for unchanged
rc1 code. They correct moved-environment recovery, clarify the Windows install
command, and distinguish local/remote evidence. The corrected receipt identifies
the complete delivered files including appended provenance. Both full-file
hashes now match; retain those existing bytes unchanged. The earlier handoff
hashes identified pre-delivery files and are superseded as integration receipts.

A later authorized documentation update should link its committed student PDF
and documentation commit here, then add the two distinct v0.2 PDF asset names.
That commit does not yet exist. Preserve the rc1 tag, original ZIP, and original
PDF assets. The ZIP still embeds its original v0.1 guide; replacing the bundled
guide requires a new candidate version and matching ChatGPT-supplied PDF.
