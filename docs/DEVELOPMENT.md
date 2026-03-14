# Development

## Setup

Install the package locally so the console-script entrypoints are available:

```bash
python -m pip install -e .
```

This installs three local entrypoints:

- `centralized-pre-commit-hooks-common`
- `centralized-pre-commit-hooks-python`
- `centralized-pre-commit-hooks-rust`

If you create a local virtual environment at `./venv` (for example, with `python -m venv venv`), you can run the validated commands as:

```bash
./venv/bin/pytest -q
./venv/bin/pylint .
```

## Test Commands

Run the full test suite:

```bash
pytest
```

Run the main test file:

```bash
pytest tests/test_run_pre_commit_hooks_centralized_test.py
```

Run a single test:

```bash
pytest tests/test_run_pre_commit_hooks_centralized_test.py -k test_use_pre_commit_hooks_python
```

## Lint and Formatting

Run linting:

```bash
pylint .
```

Run formatting:

```bash
autopep8 --in-place --aggressive ./pre_commit_to_rule_them_all/*.py ./tests/*.py
```

Run repository hooks manually:

```bash
pre-commit run --all-files
```

Run only the shared repository checks profile:

```bash
pre-commit run centralized-pre-commit-hooks-common --all-files
```

## Repository Notes

- `pre_commit_to_rule_them_all/run_pre_commit_hooks_centralized.py` contains the wrapper logic for the published console scripts.
- `tests/test_run_pre_commit_hooks_centralized_test.py` verifies path resolution and subprocess invocation with mocks rather than executing real hooks.
- Release automation updates `CHANGELOG.md` and the package version automatically, so those files should not be edited manually during normal maintenance work.
