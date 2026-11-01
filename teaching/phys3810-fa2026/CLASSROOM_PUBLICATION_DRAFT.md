# Provisional full-course candidate and publication draft

Prepared October 31, 2026 for R5 of the
[readiness plan](RELEASE_READINESS_PLAN.md). **Local planning text only:** no
PR, tag, release, new student archive, PDF, or external message is created by
this document. Classroom delivery and publication gates remain open.

## Candidate identity

- Proposed code version: **v0.2.0-rc1**.
- Proposed release title: **PHYS 3810 Fall 2026 — five-lesson preview v0.2.0-rc1**.
- Proposed tag: `phys3810-fa2026-v0.2.0-rc1`.
- Proposed standalone student asset: `PHYS3810-Fall2026-v0.2.0-rc1.zip`, with
  a `phys3810-fa2026` top-level folder. These names describe a future package;
  neither the archive nor a downloadable URL exists as part of R5.
- Local branch: `candidate/phys3810-fa2026-v0.2.0-rc1`, in the protected
  `artifacts/local-candidate-2026-10-31/worktree` beneath the original repository.
- Accepted source carried into the candidate:
  `0570863f17971473977a65ad6d4623c27aca61c8`. The 13 accepted local commits are
  retained without rewriting. R5's documentation/evidence commit follows them.
  The exact candidate revision is the commit containing this R5 record, as
  reported in the completion receipt; do not substitute the timed R4 snapshot
  or a historical review ZIP for that identity.
- Refreshed `origin/main` remains
  `3894391f2026d4fd9351b346b44b5eda453a17da`; no intervening upstream commits or
  fixes require replay. A read-only exact-tag query on October 31 returned no
  advertised match for the proposed tag. That is not a reservation or an audit
  of GitHub draft releases. Recheck availability immediately before publication.

Keep code and document versions separate. The verified Grover **document-v0.2**
PDFs still describe the published **code-v0.1.0-rc1** preview. Their document
number does not make them the guides for this proposed full-course code version.
Matching full-course student/instructor PDFs have not been supplied. Do not
rename or regenerate the Grover editions to fill that gap.

## Proposed review sequence

Use coherent scoped changes and the repository's solo-maintainer contribution
policy. This grouping is a publication plan, not authority to create PRs:

1. Documentation and exact delivered Grover v0.2 PDF bytes: `b16d235`.
2. QFT/QPE implementations and accepted follow-ups: `f277e21`, `e365d38`,
   `695c425`.
3. HHL/Shor contracts, implementations, and reconciliation: `6ed4d19`,
   `234c608`, `a85a88a`, `ec07359`.
4. Readiness evidence and provisional teaching preparation: `9e73b82`,
   `6b70fbd`, `4c589fd`, `07831f4`, `0570863`, followed by the R5 record.

Later reconciliation documents link to the complete lesson set. Preserve those
dependencies when preparing PR branches; do not publish a link-incomplete
subset or move full-course claims into the original Grover-only preview.
Readiness documentation belongs after the complete implementation chain.

## PR description draft

Proposed title: **Add bounded QFT, QPE, HHL, and compiled N=15 Shor lessons**.

The body below follows the repository
[PR template](../../.github/PULL_REQUEST_TEMPLATE.md). Before opening a PR,
adapt it to the actual scoped branch and exact validation receipt. Unchecked
items are not failures; this draft does not certify future publication actions.

### Summary

The published Grover preview provides the first algorithm lesson. This change
adds reusable QFT, QPE, HHL, and compiled N=15 order-finding implementations,
independent mathematical tests, and teaching notebooks, giving the development
course all five requested bounded lessons. The strict local validator covers
eight notebooks, including preflight and two smoke notebooks, with 50 required
code cells and 16 PNG figures.

QFT supports exact transforms on 1–6 qubits. QPE supports 1–6 counting qubits
and numeric unitaries on one or two target qubits. HHL is a five-qubit 2x2
positive-Hermitian example with exact integer eigenvalues 1–7, explicit
postselection, relative complex phase, and both-branch count cleanup. Shor is
a disclosed compiled full-domain N=15 example using four residue qubits and
4–6 counting qubits; it has its own order-finding builder and leaves QPE's
target-width limit unchanged. No general solver, scalable arithmetic network,
hardware performance, or quantum-advantage claim is made.

The reviewed Grover PDFs retain their exact delivered bytes and corrected
receipts. The published Grover rc1 tag, original ZIP, and release assets stay
unchanged. All notebook sources are output-free, and default execution remains
local and credential-free. Existing workflows, job names, and repository
governance are retained.

### Scope

- [x] Runtime auth/setup/docs — setup and course documentation; no new Runtime
  authentication behavior or hardware path.
- [x] Notebook behavior (`notebooks/*.ipynb`) — course notebooks live under
  `teaching/phys3810-fa2026/notebooks/`; the smoke notebooks remain required.
- [x] Python module updates (`src/*.py`) — canonical modules under
  `src/phys3810/`, with independent tests under `tests/`.
- [ ] CI/workflow or governance updates — not part of this candidate.

### Validation evidence to attach before opening

The [R5 receipt](R5_CANDIDATE_VALIDATION.md) records passed checks using the
retained R1 CPython 3.12.15 environment: `python -m pip check`, standalone
160-test discovery, the strict classroom validator (another 160-test run and
eight fresh-kernel notebooks), Ruff, and `bash scripts/smoke_local.sh`. Saved
outputs were independently counted: 50 executed code cells and 16 PNGs. No new
environment installation was performed. `pre-commit run --all-files` also
passed after the documentation correction recorded in R5's receipt. Use that
receipt and the exact candidate commit before opening a PR.

Reassess this evidence against the actual future PR branch. Preserve the
160-test/eight-notebook/50-cell/16-PNG baseline; do not quote the old 92-/158-test
archive totals as current validation or use present checks to pre-certify a
later changed source revision.

R1 already established a fresh Linux installation of unchanged pins; R2
established actual Linux/Chrome JupyterLab execution. The QFT/QPE and HHL/Shor
independent reviews apply to their identified historical snapshots, followed
by documented local corrections. Native Windows x64, macOS ARM64/Intel, and
native editor UI remain untested. Human pacing remains untested, while R4's
proposed run sheets and machine timings are available. A local check does not
stand in for required remote CI after a future authorized PR is opened.

### Checklist

- [ ] I ran `python -m pip install -r requirements-ci.txt` — keep unchecked
  unless this exact command was actually executed for the PR. R5 reuses the
  validated environment; do not relabel that as an installation. Link R1's
  documented unchanged-pin installation and explain the evidence instead.
- [ ] I ran `bash scripts/smoke_local.sh` — mark only from the final receipt.
- [ ] I ran `pre-commit run --all-files` (or equivalent lint checks) — mark
  only from the final receipt.
- [ ] I updated README/docs/changelog as needed — verify the scoped PR's
  links and keep candidate-versus-published download claims explicit.
- [ ] No credentials, tokens, or `.env` secrets are included — verify the
  actual staged diff and any future packaged payload before opening.

## Release-note draft

Proposed title: **PHYS 3810 Fall 2026 — five-lesson preview v0.2.0-rc1**.

This proposed preview brings together local lessons for Grover search, QFT,
QPE, exact-spectrum HHL, and compiled N=15 Shor order finding. Reusable source,
independent mathematical checks, preflight, and teaching notebooks accompany
the lessons. CPython 3.12, Qiskit 2.6.1, and Aer 0.17.2 remain pinned. After
installation, default validation and demonstrations need no cloud credentials
or quantum hardware.

The algorithms are deliberately small instructional examples. Grover supports
2–5 qubits; QFT supports 1–6; QPE retains one/two target qubits. HHL accepts the
documented exact-spectrum positive 2x2 systems and returns a postselected
solution state. Shor uses compiled 16x16 reversible permutations for N=15,
four residue qubits, conservative order recovery, and explicit failure cases.
These examples make no scalability or quantum-advantage claim.

Before using this draft as actual release notes, insert the final merged source
revision, sealed ZIP hash/size, manifest identity, delivered guide editions and
hashes, exact validation receipt, supported-platform decision, and verified
live asset links. No future download URL is presented here as available.

The Grover-only `phys3810-fa2026-grover-v0.1.0-rc1` preview remains available
under its original identity and bytes. Historical review archives remain
review evidence, not substitutes for this new student package. Course dates,
coverage, assessment, and delivery arrangements remain unconfirmed; this draft
does not announce a classroom-ready release or a confirmed teaching schedule.

## Remaining publication inputs and stop conditions

- **R3/R4:** obtain evidence for every platform/UI path actually claimed, or
  agree and clearly state an appropriate classroom alternative. Keep the native
  Windows/macOS/editor gaps explicit. Record instructor teaching decisions and
  a real presenter rehearsal; machine seconds do not establish human pacing.
- **R6:** the [provisional document inputs](R6_DOCUMENT_INPUTS.md) now include
  separate version-matched student and instructor Markdown companions. The
  [literal Ubuntu setup/UI walkthrough](R6_GUIDE_WALKTHROUGH_VALIDATION.md) passed.
  The [provisional document return](R6_DOCUMENT_REVIEW_RECONCILIATION.md) is
  verified and integrated with delivered-byte receipts and synchronized visible
  Markdown. The four-page student and six-page instructor PDFs remain unchanged.
  Final editions still require the relevant teaching/platform/pacing decisions;
  P3-01 belongs in the next authored instructor edition before final distribution.
  Do not rewrite supplied PDF bytes locally.
- **Entry-point adaptation:** the current course `README.md` and `SETUP.md`
  intentionally link the published Grover rc1 asset and distinguish development
  lessons. A full-course student package needs its own version-matched entry
  instructions and folder name. Remove maintainer coordination/review jargon
  from that student flow; do not replace live Grover links with unbuilt URLs.
- **R7:** build a new exact-source standalone package with all required tests,
  helpers, eight notebooks, dependencies, license, guide, and manifest. Use
  current counts rather than old review-builder constants. Verify an extraction
  outside the checkouts, strict execution, output-free sources, local links,
  exclusions, and unchanged payload hashes after execution. A GitHub-generated
  source ZIP is not automatically the verified standalone student package.
- **Answers and exclusions:** assessment and solution distribution are pending.
  Keep instructor guides/run-sheet answers outside a student-only bundle.
  Exclude prompts, policy/chat records, unrelated history, Git metadata,
  environments, credentials, caches, and generated execution outputs. Preserve
  the original reviewed ZIPs rather than rebuilding them under their old names.
- **R8:** obtain applicable publication authorization only after the concrete
  candidate and evidence are ready. Recheck then-current upstream, rules and
  required checks, tag availability, and the final asset/version identity.
  Use the normal PR/CI/merge workflow without changing rulesets. If merging
  changes the source identity, rebuild and revalidate the package and guide
  correspondence before tagging. Download published bytes independently and
  verify hashes, manifest, links, release assets, and tag target afterward.

The provisional R6 Markdown inputs and literal Ubuntu setup/UI walkthrough are
complete. The supplied review-draft PDFs and companion edits are now reconciled
locally, while teaching decisions remain pending. The next step can build and
verify a local R7 preview package with the unchanged student PDF; keep instructor
answer material separate. This does not constitute final classroom approval,
publication, or a changed Grover release.
The completed provisional GPT Pro document/teaching sync is recorded with its
exact outgoing and returned archive identities; final classroom gates remain open.
Neither local file visibility nor this draft implies another chat has received
the files. No new algorithm-review round is required solely for this unchanged
R5 history; substantive technical or scope changes would require reassessment.
