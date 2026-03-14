# -*- coding: utf-8 -*-
"""
Test module for the pre_commit_to_rule_them_all module
"""
import unittest
from unittest.mock import ANY, patch

from pre_commit_to_rule_them_all import run_pre_commit_hooks_centralized


class TestYamlConfigMethods(unittest.TestCase):
    """Tests for each of the functions, whether files exist or not."""

    def test_invalid_file_name(self):
        """
        Test a path the doesn't exist
        """
        self.assertRaises(
            FileNotFoundError,
            run_pre_commit_hooks_centralized.execute_pre_commit_hooks_centralized, "beans")

    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.subprocess.run')
    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.os')
    def test_use_pre_commit_hooks_common(self, os_mock, mock_subprocess_run):
        """
        Test a valid path for common pre-commit
        """
        os_mock.path.isdir.return_value = False
        os_mock.path.exists.return_value = True
        mock_subprocess_run.return_value.returncode = 0

        run_pre_commit_hooks_centralized.use_pre_commit_hooks_common()

        mock_subprocess_run.assert_called_once_with(
            ['pre-commit', 'run', '--config', ANY, '--files'],
            check=False
        )

    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.subprocess.run')
    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.os')
    def test_use_pre_commit_hooks_rust(self, os_mock, mock_subprocess_run):
        """
        Test a valid path for rust pre-commit
        """
        os_mock.path.isdir.return_value = False
        os_mock.path.exists.return_value = True
        mock_subprocess_run.return_value.returncode = 0

        run_pre_commit_hooks_centralized.use_pre_commit_hooks_rust()

        mock_subprocess_run.assert_called_once_with(
            ['pre-commit', 'run', '--config', ANY, '--files'],
            check=False
        )

    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.subprocess.run')
    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.os')
    def test_use_pre_commit_hooks_python(self, os_mock, mock_subprocess_run):
        """
        Test a valid path for python pre-commit
        """
        os_mock.path.isdir.return_value = False
        os_mock.path.exists.return_value = True
        mock_subprocess_run.return_value.returncode = 0

        run_pre_commit_hooks_centralized.use_pre_commit_hooks_python()

        mock_subprocess_run.assert_called_once_with(
            ['pre-commit', 'run', '--config', ANY, '--files'],
            check=False
        )

    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.subprocess.run')
    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.os')
    def test_use_pre_commit_hooks_skills_check(self, os_mock, mock_subprocess_run):
        """
        Test a valid path for skills check pre-commit
        """
        os_mock.path.isdir.return_value = False
        os_mock.path.exists.return_value = True

        run_pre_commit_hooks_centralized.use_pre_commit_hooks_skills_check()

        mock_subprocess_run.assert_called_once_with(
            ['pre-commit', 'run', '--config', ANY, '--files'],
            check=False
        )

    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.subprocess.run')
    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.os')
    def test_use_pre_commit_hooks_skills_update(self, os_mock, mock_subprocess_run):
        """
        Test a valid path for skills update pre-commit
        """
        os_mock.path.isdir.return_value = False
        os_mock.path.exists.return_value = True

        run_pre_commit_hooks_centralized.use_pre_commit_hooks_skills_update()

        mock_subprocess_run.assert_called_once_with(
            ['pre-commit', 'run', '--config', ANY, '--files'],
            check=False
        )

    def test_failed_pre_commit_propagates_return_code(self, os_mock, mock_subprocess_run):
        """
        Test a failing delegated pre-commit returns a non-zero exit code
        """
        os_mock.path.isdir.return_value = False
        os_mock.path.exists.return_value = True
        mock_subprocess_run.return_value.returncode = 1

        with self.assertRaises(SystemExit) as context:
            run_pre_commit_hooks_centralized.use_pre_commit_hooks_common()

        self.assertEqual(context.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
