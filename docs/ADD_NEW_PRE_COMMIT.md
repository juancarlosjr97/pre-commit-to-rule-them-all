# Add a New Hook Profile

This repository publishes hook profiles as coordinated changes across Python packaging metadata, wrapper functions, and pre-commit manifests. When adding a new hook profile, update every surface that declares it.

## Files to Update

1. `pre_commit_to_rule_them_all/configurations/pre-commit-hooks-<new-profile>.yaml`
2. `pre_commit_to_rule_them_all/run_pre_commit_hooks_centralized.py`
3. `pyproject.toml`
4. `.pre-commit-hooks.yaml`
5. `.pre-commit-config.yaml`
6. `README.md` if the new profile should be documented for users
7. `AGENTS.md` if the architecture or maintenance guidance changes

## Step 1: Add the Bundled YAML Configuration

Create a new YAML file under `pre_commit_to_rule_them_all/configurations/`.

- Keep the file inside the Python package so setuptools includes it as package data.
- Follow the existing filename convention: `pre-commit-hooks-<profile>.yaml`.
- Define only the hooks that belong to the new profile.
- Reuse the same style as the existing Python and Rust profile files.

## Step 2: Add a Wrapper Function

In `pre_commit_to_rule_them_all/run_pre_commit_hooks_centralized.py`, add a small wrapper that delegates to `execute_pre_commit_hooks_centralized(...)`.

Follow the existing pattern:

```python
def use_pre_commit_hooks_example():
    """Method that executes the pre-commit hook for Example"""
    execute_pre_commit_hooks_centralized(
        'configurations/pre-commit-hooks-example.yaml')
```

The wrapper should keep using the existing subprocess contract:

- resolve the path relative to the package directory
- run `pre-commit run --config <resolved path> --files`
- keep `check=False` unless intentionally changing behavior

## Step 3: Register the Console Script

In `pyproject.toml`, add a new entry under `[project.scripts]` that points to the new wrapper function.

Example shape:

```toml
[project.scripts]
centralized-pre-commit-hooks-example = "pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized:use_pre_commit_hooks_example"
```

## Step 4: Publish the Hook ID

Add the new hook entry to `.pre-commit-hooks.yaml`.

- Keep the hook ID, name, description, and entry aligned with the console script you added in `pyproject.toml`.
- Match the existing schema used by the Python and Rust entries.

## Step 5: Mirror It in Local Dogfooding

Add the same hook definition to `.pre-commit-config.yaml` so this repository can exercise the new published hook profile locally.

This repository treats `.pre-commit-hooks.yaml` and `.pre-commit-config.yaml` as synchronized declarations of the same profile set.

## Step 6: Add or Update Tests

Extend `tests/test_run_pre_commit_hooks_centralized_test.py` with a test for the new wrapper.

Follow the existing mocking pattern:

- mock `os.path.exists` to simulate the config file being present
- call the wrapper function
- assert `subprocess.run(...)` received the expected command shape

If you change shared execution behavior, also update the missing-file test coverage.

## Step 7: Validate

Run:

```bash
pytest
pylint .
pre-commit run --all-files
```

If you are using the checked-in virtual environment, the validated commands are:

```bash
./venv/bin/pytest -q
./venv/bin/pylint .
```
