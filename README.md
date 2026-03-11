# Pre-Commit to Rule Them All

[![codecov](https://codecov.io/gh/juancarlosjr97/pre-commit-to-rule-them-all/graph/badge.svg?token=P3g2C4nvZm)](https://codecov.io/gh/juancarlosjr97/pre-commit-to-rule-them-all)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/df06b8362cbf4b159d61ad60793f970b)](https://app.codacy.com/gh/juancarlosjr97/pre-commit-to-rule-them-all/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Codacy Badge](https://app.codacy.com/project/badge/Coverage/df06b8362cbf4b159d61ad60793f970b)](https://app.codacy.com/gh/juancarlosjr97/pre-commit-to-rule-them-all/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_coverage)

## Skills Hooks (skills.sh)

This repository includes pre-commit hooks for [skills.sh](https://skills.sh) to keep agent skills up-to-date and avoid drift.

### Available Hooks

- **`centralized-pre-commit-hooks-skills-check`** – Runs `npx skills check` to verify that agent skills are up-to-date before each commit. The commit is blocked if skills are out-of-date.
- **`centralized-pre-commit-hooks-skills-update`** – Runs `npx skills update` to update and re-lock agent skills. Use this hook manually when you want to update your skill definitions.

Both hooks monitor changes to `.agents/skills/` and `skills.lock.json`.

### Setup

1. Install pre-commit:

   ```bash
   pip install pre-commit
   ```

2. Add the hooks to your `.pre-commit-config.yaml`:

   ```yaml
   repos:
     - repo: https://github.com/juancarlosjr97/pre-commit-to-rule-them-all
       rev: <version>
       hooks:
         - id: centralized-pre-commit-hooks-skills-check
         # Optionally, to also update skills automatically:
         # - id: centralized-pre-commit-hooks-skills-update
   ```

3. Install the hooks:

   ```bash
   pre-commit install
   ```

### Remediation

If the `skills-check` hook fails, it means your agent skills are out-of-date. Run the following command to update them:

```bash
npx skills update
```

Then re-stage and commit your changes.
