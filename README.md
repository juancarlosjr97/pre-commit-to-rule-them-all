# Pre-Commit to Rule Them All

[![codecov][1]][2]
[![Codacy Grade][3]][4]
[![Codacy Coverage][5]][6]
[![MIT][7]][8]

Centralized pre-commit hook bundles for Python and Rust projects. This repository packages reusable hook profiles as a Python distribution and exposes them through pre-commit hook IDs, so consumers can adopt a curated set of checks without copying large hook configurations into every repository.

> [!NOTE]
> This project releases through automated release-it workflows. `CHANGELOG.md` is generated from commit history and `pyproject.toml` version bumps are handled during release automation.

## How It Works

At runtime, each published hook:

1. Resolves a bundled YAML configuration from the installed Python package
2. Calls `pre-commit run --config <resolved config> --files`
3. Delegates the actual checks to the tools defined in that bundle

The repository currently exposes two hook bundles:

- `centralized-pre-commit-hooks-python` for Python formatting/import cleanup tooling
- `centralized-pre-commit-hooks-rust` for Rust formatting and linting tooling

The package also ships shared configuration under `pre_commit_to_rule_them_all/configurations/`, and the repository uses `.pre-commit-hooks.yaml` plus `.pre-commit-config.yaml` to publish and exercise those hook entrypoints.

## Quick Start

Add this repository to your `.pre-commit-config.yaml` and choose the hook profile you want to consume.

### Python bundle

```yaml
repos:
  - repo: https://github.com/juancarlosjr97/pre-commit-to-rule-them-all
    rev: 0.5.16
    hooks:
      - id: centralized-pre-commit-hooks-python
```

### Rust bundle

```yaml
repos:
  - repo: https://github.com/juancarlosjr97/pre-commit-to-rule-them-all
    rev: 0.5.16
    hooks:
      - id: centralized-pre-commit-hooks-rust
```

After adding a hook, install and run pre-commit as usual:

```bash
pre-commit install
pre-commit run --all-files
```

## Included Tooling

### Python bundle

The Python hook bundle currently includes:

- `isort`
- `pycln`
- `autopep8`

### Rust bundle

The Rust hook bundle currently includes:

- `cargo fmt`
- `cargo-check`
- `clippy`

### Shared repository checks

The repository also maintains shared checks in `pre_commit_to_rule_them_all/configurations/common.yaml`, including:

- `pre-commit-hooks` checks such as merge-conflict detection, TOML/XML validation, whitespace cleanup, JSON formatting, and test naming
- `yamllint`
- `gitleaks`
- `markdownlint`

## Development and Maintenance Docs

- [Development guide](docs/DEVELOPMENT.md)
- [Add a new hook profile](docs/ADD_NEW_PRE_COMMIT.md)

## License

This project is licensed under the MIT License. See [LICENSE][8].

[1]: https://codecov.io/gh/juancarlosjr97/pre-commit-to-rule-them-all/graph/badge.svg?token=P3g2C4nvZm
[2]: https://codecov.io/gh/juancarlosjr97/pre-commit-to-rule-them-all
[3]: https://app.codacy.com/project/badge/Grade/df06b8362cbf4b159d61ad60793f970b
[4]: https://app.codacy.com/gh/juancarlosjr97/pre-commit-to-rule-them-all/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade
[5]: https://app.codacy.com/project/badge/Coverage/df06b8362cbf4b159d61ad60793f970b
[6]: https://app.codacy.com/gh/juancarlosjr97/pre-commit-to-rule-them-all/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage
[7]: https://img.shields.io/badge/License-MIT-brightgreen.svg
[8]: ./LICENSE
