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
    def test_use_pre_commit_hooks_rust(self, os_mock, mock_subprocess_run):
        """
        Test a valid path for rust pre-commit
        """
        os_mock.path.isdir.return_value = False
        os_mock.path.exists.return_value = True

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

        run_pre_commit_hooks_centralized.use_pre_commit_hooks_python()

        mock_subprocess_run.assert_called_once_with(
            ['pre-commit', 'run', '--config', ANY, '--files'],
            check=False
        )


if __name__ == '__main__':
    unittest.main()
