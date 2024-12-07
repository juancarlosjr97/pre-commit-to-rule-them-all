# Pre-Commit to Rule Them All

[![codecov](https://codecov.io/gh/juancarlosjr97/pre-commit-to-rule-them-all/graph/badge.svg?token=P3g2C4nvZm)](https://codecov.io/gh/juancarlosjr97/pre-commit-to-rule-them-all)

https://github.com/pre-commit/pre-commit/issues/731#issuecomment-376945745

### Linter and Formatting

The project uses pre-commit, which will perform linting and formatting on every commit. For manual execution run:

#### Linter

```bash
pylint .
```

#### Formatting

```bash
autopep8 --in-place --aggressive ./pre_commit_to_rule_them_all/*.py ./tests/*.py
```
