# PHYS 3810 · Start here

This provisional full-course preview contains local lessons for Grover search,
QFT, QPE, exact-spectrum HHL, and compiled N=15 Shor order finding. It uses
64-bit CPython 3.12, Qiskit 2.6.1, and Aer 0.17.2. No Git experience, IBM account,
GPU, or quantum hardware is needed for the default lessons.

## Get the full-course preview

1. Download [PHYS3810-Fall2026-v0.2.0-rc1.zip](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/download/phys3810-fa2026-v0.2.0-rc1/PHYS3810-Fall2026-v0.2.0-rc1.zip)
   and extract the complete `phys3810-fa2026` folder. This named asset is available
   from [the published prerelease](https://github.com/M-Gage-Plott42/qiskit-v2-guide/releases/tag/phys3810-fa2026-v0.2.0-rc1);
   use it rather than GitHub's source-only archive.
2. Follow the [current setup instructions](SETUP.md), install the pinned
   environment, and run `python scripts/validate_classroom.py` from the extracted root.
3. Expect 160 tests, eight fresh-kernel notebooks, 50 code cells, and 16 PNGs.
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

## Lessons and limits

- [Grover](notebooks/01_grover.ipynb): phase marking and amplification on 2–5 qubits.
- [QFT](notebooks/02_qft.ipynb): exact 1–6-qubit transforms, phase, sign, and swaps.
- [QPE](notebooks/03_qpe.ipynb): 1–6 counting qubits and one/two target qubits.
- [HHL](notebooks/04_hhl.ipynb): a five-qubit positive-Hermitian 2x2 example with
  exact eigenvalues 1–7, postselection, and explicit resource limitations.
- [Shor](notebooks/05_shor.ipynb): compiled full-domain N=15 multiplication with
  four residue qubits and conservative order/factor recovery.

These are bounded instructional examples, not general scalable implementations
or demonstrations of quantum advantage. The [course plan](COURSE_PLAN.md)
retains 50-minute cores and 75-minute expansions as provisional activity routes
within the now-confirmed 85-minute class period. November 16, 19, and 23 are
provisional requested dates; the final dates, total session count, topic allocation,
delivery arrangements, assessment, and solution distribution remain unconfirmed.

The demonstrated path is Ubuntu/Linux with JupyterLab. Native Windows/macOS,
native editor UI, and human pacing remain untested. This preview is not final
classroom approval. Worked results appear in notebooks, contracts, and tests;
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
