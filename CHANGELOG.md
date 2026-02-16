# Changelog

All notable changes to this repository are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-02-16

### Added

- Initial reproducible Qiskit 2.x smoke-test workflow with local and optional IBM Runtime notebook paths.
- CI automation for local notebook smoke execution, Python lint (`ruff`), Markdown lint, and YAML lint.
- Dependabot configuration for `github-actions` and `pip` dependency updates.
- GitHub governance hardening:
  - repository topics,
  - auto-merge enabled,
  - automatic branch deletion on merge enabled,
  - default code scanning configured for Python and GitHub Actions,
  - default-branch ruleset with required checks and admin bypass preserved.
- Optional local pre-commit hook configuration covering `ruff`, `yamllint`, and `markdownlint`.
- Security policy document for vulnerability reporting.

### Changed

- Notebook examples updated to avoid false-positive `basedpyright` attribute warnings while preserving runtime behavior.
- `pyrightconfig.json` cleaned to remove unsupported `$schema` key for better IDE compatibility.
