# PHYS 3810 · Start here

The current beginner route is **one prerecorded class by Gage Plott**, with
laptop follow-along and zero assumed Python experience. Start with the
[single-class quickstart](intro/START_HERE.md): Ubuntu/Linux setup, quantum
random-bit generation, then Bell-state preparation. Other algorithms are
optional exploration. Nothing is assigned, graded, evaluated, or submitted.

The classroom environment uses 64-bit CPython 3.12, Qiskit 2.6.1, Aer 0.18.2,
and JupyterLab 4.6.5. No Git experience, IBM account, GPU, or quantum hardware is
needed for the local lessons. The video reserves 15–20 minutes for setup;
installation and student pauses may take longer. The total class window, date,
and video/kit delivery location remain unconfirmed.

## Follow the current class

1. Use the [single-class quickstart](intro/START_HERE.md) and the complete matching
   kit supplied with the video. No new public student download is published yet.
2. Open [Quantum random bits](notebooks/intro/01_quantum_rng.ipynb), check the
   kernel, and run the one-qubit demonstration.
3. Open [Prepare a Bell state](notebooks/intro/02_bell_state.ipynb) in its own
   kernel and run the two-qubit demonstration.

The earlier [guided review entrance](guided/START_HERE.md), three guided
notebooks, and all supplied PDF/Markdown editions retain their original scope.
Their multi-session route is historical. The frozen downloads below do not
contain the two new intro notebooks.

For maintainer validation, `python scripts/validate_classroom.py --profile all`
runs thirteen notebooks: two intro, three guided, and eight reference/validation
notebooks. Run it from the repository root or the matching extracted kit's
`runtime` folder. The default profile still selects the original eight.
[Current evidence](STATUS.md) records measured results; tests are support
material, not the student's video setup checkpoint.

## Historical full-course preview

1. Download [PHYS3810-Fall2026-v0.2.0-rc1.zip](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-v0.2.0-rc1/PHYS3810-Fall2026-v0.2.0-rc1.zip)
   and extract the complete `phys3810-fa2026` folder. This named asset is available
   from [the published prerelease](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-v0.2.0-rc1);
   use it rather than GitHub's source-only archive.
2. Follow the [published-preview setup instructions](SETUP.md), install the pinned
   environment, and run `python scripts/validate_classroom.py` from the extracted root.
3. In this frozen release ZIP, expect 160 tests, eight fresh-kernel notebooks,
   50 code cells, and 16 PNGs.
   Optional Runtime/GPU execution is skipped. A traceback or failed check needs
   attention; do not bypass an unexecuted required cell.
4. Open [preflight](notebooks/00_setup_preflight.ipynb) in JupyterLab, select
   **Python (PHYS 3810)**, restart/run all, and verify its interpreter and figures.

The preserved [student PDF](handouts/PHYS3810_Full_Course_Student_Setup_v0.1_REVIEW_DRAFT.pdf)
and [paired Markdown](handouts/FULL_COURSE_SETUP_DRAFT.md) are prepublication
review drafts. Their old statement that the download is unpublished describes
review-time availability. The current setup page governs this preview; see
[the publication notice](handouts/PUBLICATION_NOTICE.md). No PDF was rewritten.
See the [document index](handouts/README.md) for separately supplied review editions;
they do not replace the files inside the frozen release ZIP.

## Optional algorithms and limits

- [Grover](notebooks/01_grover.ipynb): phase marking and amplification on 2–5 qubits.
- [QFT](notebooks/02_qft.ipynb): exact 1–6-qubit transforms, phase, sign, and swaps.
- [QPE](notebooks/03_qpe.ipynb): 1–6 counting qubits and one/two target qubits.
- [HHL](notebooks/04_hhl.ipynb): a five-qubit positive-Hermitian 2x2 example with
  exact eigenvalues 1–7, postselection, and explicit resource limitations.
- [Shor](notebooks/05_shor.ipynb): compiled full-domain N=15 multiplication with
  four residue qubits and conservative order/factor recovery.

These are bounded instructional examples, not general scalable implementations
or demonstrations of quantum advantage. They are optional after the RNG/Bell
class. The [earlier course plan](COURSE_PLAN.md) preserves the superseded
multi-session proposal and its provisional dates; those dates and durations
are not confirmed constraints for the prerecorded class.

The selected recording path is Ubuntu/Linux with JupyterLab. Native Windows/macOS,
native editor UI, and human pacing remain untested. Worked results appear in notebooks, contracts, and tests;
excluding separate instructor guides from the named ZIP does not make it an
answer-free assessment. The repository source also contains instructor material.

## Earlier Grover-only edition

The [Grover rc1 release](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-grover-v0.1.0-rc1),
its [original standalone ZIP](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-grover-v0.1.0-rc1/PHYS3810-Grover-v0.1.0-rc1.zip),
and its [version-matched guide](preview/SETUP_REVIEW_DRAFT.md) remain unchanged.
That older download intentionally contains only onboarding and Grover.

See [status and evidence](STATUS.md) for the identified validation snapshots,
and the [repository README](../../README.md) for optional workflows outside
classroom defaults.
