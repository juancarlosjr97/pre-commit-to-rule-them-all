# Agent Instructions

## Repository Purpose

This repository packages centralized pre-commit hook bundles as a small Python distribution. It publishes three console scripts, `centralized-pre-commit-hooks-common`, `centralized-pre-commit-hooks-python`, and `centralized-pre-commit-hooks-rust`, which resolve bundled YAML configurations and execute `pre-commit` with them.

## Commands

- Install locally so the console scripts are available: `python -m pip install -e .`
- Run tests: `pytest`
- Run the main test file: `pytest tests/test_run_pre_commit_hooks_centralized_test.py`
- Run a single test: `pytest tests/test_run_pre_commit_hooks_centralized_test.py -k test_use_pre_commit_hooks_python`
- Run linting: `pylint .`
- Run formatting: `autopep8 --in-place --aggressive ./pre_commit_to_rule_them_all/*.py ./tests/*.py`
- Run repository hooks manually: `pre-commit run --all-files`

## Critical Rules

- Keep hook profiles in sync across `pyproject.toml`, `pre_commit_to_rule_them_all/run_pre_commit_hooks_centralized.py`, packaged YAML files in `pre_commit_to_rule_them_all/configurations/`, `.pre-commit-hooks.yaml`, and `.pre-commit-config.yaml`.
- Keep hook YAML files inside `pre_commit_to_rule_them_all/` so setuptools includes them as package data and runtime path resolution continues to work.
- Preserve the current subprocess contract unless behavior is intentionally changing: `['pre-commit', 'run', '--config', <path>, '--files']` with `subprocess.run(..., check=False)`.
- Do not edit `CHANGELOG.md` manually; release-it regenerates it from commit history using `.release-it.json`.

## Architecture

- `pyproject.toml` defines the package metadata, console-script entrypoints, and package-data rules.
- `pre_commit_to_rule_them_all/run_pre_commit_hooks_centralized.py` contains the thin wrapper logic that resolves a config path relative to the package and launches `pre-commit`.
- `pre_commit_to_rule_them_all/configurations/` contains the reusable hook bundles. The common bundle wraps shared repository checks, the Python bundle wraps `isort`, `pycln`, and `autopep8`, and the Rust bundle wraps `cargo fmt`, `cargo-check`, and `clippy`.
- `.pre-commit-hooks.yaml` is the published manifest for external consumers. `.pre-commit-config.yaml` mirrors the same hook IDs locally so the repository can dogfood its own packaged hooks.
- Tests in `tests/test_run_pre_commit_hooks_centralized_test.py` mock `os` and `subprocess.run` to verify path resolution, error handling, and the exact subprocess invocation shape.

## Repository Docs

- `docs/DEVELOPMENT.md` is the development guide for local setup, test, lint, formatting, and manual pre-commit commands.
- `docs/ADD_NEW_PRE_COMMIT.md` is the maintenance guide for adding a new hook profile across packaging, wrapper code, manifests, tests, and docs.

## Validation

Validate changes by:

1. Running `./venv/bin/pytest -q` if the checked-in virtual environment is present, or `pytest` in an activated development environment.
2. Running `./venv/bin/pylint .` if the checked-in virtual environment is present, or `pylint .` in an activated development environment.
3. Running `pre-commit run --all-files` when changes affect hook configuration or repository metadata.
4. Confirming hook profile changes are reflected everywhere they are declared.

## Release Automation

- Pushes to `main` trigger `.github/workflows/release.yaml`.
- The workflow delegates tests and release steps to reusable workflows in `juancarlosjr97/github-actions-workflows-to-rule-them-all`.
- Release automation uses `@release-it/conventional-changelog` to regenerate `CHANGELOG.md` and `@release-it/bumper` to update `project.version` in `pyproject.toml`.
