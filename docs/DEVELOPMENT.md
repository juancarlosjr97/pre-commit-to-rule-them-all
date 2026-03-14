# Development

## Setup

Install the package locally so the console-script entrypoints are available:

```bash
python -m pip install -e .
```

If you are using the checked-in virtual environment, the validated commands are:

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
pytest tests/test_run_pre_commit_hooks_centralized.py
```

Run a single test:

```bash
pytest tests/test_run_pre_commit_hooks_centralized.py -k test_use_pre_commit_hooks_python
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

## Repository Notes

- `pre_commit_to_rule_them_all/run_pre_commit_hooks_centralized.py` contains the wrapper logic for both published console scripts.
- `tests/test_run_pre_commit_hooks_centralized.py` verifies path resolution and subprocess invocation with mocks rather than executing real hooks.
- Release automation updates `CHANGELOG.md` and the package version automatically, so those files should not be edited manually during normal maintenance work.
