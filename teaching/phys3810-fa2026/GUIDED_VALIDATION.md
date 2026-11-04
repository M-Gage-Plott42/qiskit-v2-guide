# Guided beginner-route validation

November 2, 2026. This record covers the new beginner teaching layer under
[GUIDED_TEACHING_PLAN.md](GUIDED_TEACHING_PLAN.md), based on reviewed documentation
commit `7600e85c773db53cf0e99c9642dc85b806bd8a29`. The published release remains
`f717aea99c68a25ad1c68597f11d1ca12c45c56a`; it is not replaced by this review kit.
Material development: **Gage Plott**.

The e4fea10 packet below is preserved historical execution evidence. The later
[focused review and corrections](GUIDED_REVIEW_RECONCILIATION.md) record the
required parameter-cell instruction fix and the separately identified v0.2
packet. Do not treat the original wording as corrected merely because its
mathematical and execution checks passed.

## Accessible requirements and scope

The supplied November 2 planning return is accessible text. It reports the
instructor's two/three-class, zero-Python, laptop-follow-along, no-assessment
requirements and conditional offer to teach after a walkthrough. The underlying
email/private calendar were not separately retrieved. Receipt of material is
not detailed approval, nor proof that this new kit has already been sent.

The three new notebooks import canonical implementations and retain bounded
inputs. All existing source, 160 regression tests, eight reference notebooks,
dependency pins, supplied PDF/companion editions, frozen builders, tags, and
release assets are preserved. New work adds 17 teaching/profile regressions and
20 exporter regressions, for **197 tests**. The deferred optional GPU repair and
dependency updates are outside this change.

## Source execution

**Passed:** `python scripts/validate_classroom.py --profile all` in the reused
repository `.venv`, CPython **3.12.15**, Linux x86_64 kernel 7.0.0-42/glibc 2.43.
The run includes pip check, the complete unit suite, and eleven separate fresh
kernels. Actual totals: **197 tests, eleven notebooks, 74 nonempty code cells,
27 PNGs, zero notebook errors**. No fresh dependency install is claimed.

Versions: pip 26.2.2, Qiskit 2.6.1, Aer 0.17.2, JupyterLab 4.6.4,
ipykernel 7.4.0, NumPy 2.5.4, SciPy 1.18.1, Matplotlib 3.11.2,
nbclient 0.11.0, nbformat 5.10.4. Source acceptance set
`PYTHONDONTWRITEBYTECODE=1`, `OMP_NUM_THREADS=2`, `OPENBLAS_NUM_THREADS=2`.

- Python/Qiskit: nine code cells, four figures.
- Grover: six code cells, three figures.
- QFT/QPE: nine code cells, four figures.
- Original reference inventory: fifty code cells, sixteen figures.

The all profile retains the strict environment, error/skip, execution-count,
figure, and partial-output rules. The default profile still selects the original
eight notebooks; both run the current complete test suite. Existing tests can
still override `ROOT` and `NOTEBOOKS` dynamically.

Independent expectations cover all twelve Grover target/iteration edits,
complex QFT amplitudes and inverse recovery for asymmetric inputs, explicit
QPE target preparation and both exact labels, all displayed counts/captions,
fresh-circuit reruns, and imports from an isolated copied runtime path with
spaces. Real-kernel negative controls reject errors even with `raises-exception`,
skip tags, and missing required figures, preserving partial output.

**Also passed:** Ruff 0.15.22, Bash local smoke, and pre-commit 4.7.0 hooks
(Ruff, YAML, Markdown). Hooks were run with an explicit list including new files,
so untracked additions were not silently omitted. Existing application/tool
environments were reused without changing their installed packages.

During checks, delayed support imports required explicit E402 lint annotations;
their executable AST stayed identical. All three guided notebooks were rerun
through the same strict engine afterward. A later QFT prose correction changed
"first two lines" to "first three lines"; its code remained unchanged and that
notebook was rerun before final rendering. The package exporter received a
plain-language reference-header edit and its twenty focused tests passed again.
The full unit suite was not immediately duplicated as a separate discovery run.

The first result-count script noticed a preserved old optional-runtime output
in the shared artifacts directory. Final counts use only the current declared
eleven-notebook inventory; the old file was not executed or counted here.
Optional Runtime/GPU and hardware execution remain deliberately excluded.

## Document correctness, rendering, and OCR

Primary-source research is recorded in the [contract](GUIDED_TEACHING_PLAN.md#primary-source-research-november-2).
The independent local technical check found no new algorithm or strict-profile
blocker. It corrected the presenter QPE positions to cells 12/14/15/17 and made
Day 1 follow 12/14/16/18. The quickstart now identifies Day 1 as the notebook
that prints the interpreter path. These are local checks, not an independent
review of the new teaching layer by the external reviewer.

The four concise Markdown documents and three executed guided notebooks are
rendered to local HTML and PNG, then OCR-checked with Tesseract. All 24 new code
cells are compared with rendered HTML; mathematical correctness is established
by independent tests, not inferred from OCR. Screenshots, OCR text, hashes,
tool versions, and discrepancies are retained in the local evidence directory.
No new PDF is generated, and no earlier PDF bytes are rewritten.

**Passed:** seven documents/notebooks captured in eighteen screenshot tiles,
with all eleven new figures visually inspected. OCR token recall was
97.35–100%; recognition differences in code/math were checked against source
and screenshots. All nine student terminal command lines matched after
whitespace normalization. OCR misread underscores in the instructor validator
command; its source, HTML, and visible rendering were correct. No clipping,
overlap, missing glyphs, or remaining rendering defect was found. The final
phase-prose repair was rendered/OCR-checked again and source hashes verified.

Current audience files use Gage Plott and omit internal model terminology and
coordination notes. The archived Grover PDF/companion pairs retain historical
attribution and are excluded from this packet; they require a corrected supplied
edition before reuse as current handouts. Other historical evidence remains dated.

## Export and delivery gate

The dedicated `scripts/build_guided_review.py` exports one committed snapshot,
four concise entrance files, a complete `runtime/`, `VALIDATION.md`, and a
manifest. The manifest does not hash itself or the enclosing ZIP. It records
exact/adapted/generated origins, source hashes, paths, sizes, and payload hashes.
Source notebooks must be output-free. Frozen release builders remain unchanged.

Final acceptance requires an exact ZIP extraction outside the checkout, in a
path with spaces and no `.git`; the full all-profile validator must pass there,
course imports must resolve inside that extraction, and payload bytes must
remain unchanged. The archive excludes PDFs, prompts, correspondence, policy/
history, environments, caches, credentials, and generated execution outputs.
Its committed source identity and delivered checksum are recorded in the final
delivery receipt below.

## Verified delivery receipt

**Passed:** exact archive extraction at a separate `/tmp` path containing spaces,
without Git metadata, using the same reused CPython 3.12.15 environment.
The extracted all-profile validator passed **197 tests, eleven notebooks,
74 code cells, 27 PNGs, zero errors**. All five course modules resolved inside
the extracted `runtime/`; `PYTHONPATH` was unset. All 54 payload file sizes,
hashes, and modes remained unchanged after execution. Source notebooks are
output-free, 44 package-relative links resolve, and all twelve exported Markdown
files pass lint. Package safety, CRC, exact inventory, exclusions, and the
audience-language/name scan passed.

- ZIP source: `e4fea10e5f280d0d5f79f53739321a1e608e7bec`.
- Name: `PHYS3810-Guided-Review-v0.1-e4fea10e5f28.zip`.
- Size: **167,563 bytes**; 55 files including `MANIFEST.json` and 54 payloads.
- SHA-256: `fac5fff2122ae1da5a21a7df8ff0d7db13f4ae6a77c81b6ffc7af28806f08c6a`.
- The Ubuntu desktop copy matches the verified export byte-for-byte.

The ZIP is an instructor-review artifact and has not been sent to anyone or
published as a release. The subsequent receipt-only commit does not change its
source bytes; the manifest identifies the implementation commit above. The
source and exact-extraction runs are separate checks in one reused environment,
not two fresh installs. The current PR's checks provide remote CI evidence for
its actual head; no CI result is inferred from these local passes.

Local logs and receipts are under ignored `artifacts/guided-review-2026-11-02/`.
Repository `main`, the historical integration worktree, and recovery stash
`2705385616e21718a10b73765946e430597dc4bf` remain preserved. CI is triggered by
a normal PR and must be read at its actual head; a local pass is not a CI pass.
No merge, release, external human message, or hardware job is authorized.

## Remaining limits and next review

Native Windows/macOS, native editor UI, new interactive Jupyter operation,
projector/room readability, learner completion, and human pacing are untested
for this new route. HTML rendering/OCR does not establish those results.
Dates/count, algorithm priorities, assisted setup, prior quantum coverage, and
delivery responsibility remain decisions for the walkthrough. Assessment is
resolved: none is planned.

A focused review of the new beginner explanations, editable cells, strict
profile, and concise documents is recommended once the verified kit is ready.
No broad repeat of the completed five-algorithm review is needed.
