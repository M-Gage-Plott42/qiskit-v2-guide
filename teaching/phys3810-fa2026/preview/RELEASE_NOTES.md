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

Latest correction evidence is from Linux x86_64, CPython 3.12.15. Independent
review reproduced the preceding 45-test snapshot on Linux CPython 3.12.14.
Native Windows/macOS, interactive editor use, hardware/GPU execution, and a
live classroom timing rehearsal remain unvalidated. Required remote repository
checks must pass through the normal PR workflow before publication.
