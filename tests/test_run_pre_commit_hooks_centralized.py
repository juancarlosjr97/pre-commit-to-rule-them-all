# -*- coding: utf-8 -*-
"""
Test module for the pre_commit_to_rule_them_all module
"""
import unittest
from unittest.mock import patch

from pre_commit_to_rule_them_all import run_pre_commit_hooks_centralized


class TestYamlConfigMethods(unittest.TestCase):
    """Tests for each of the functions, whether files exist or not."""

    def test_invalid_file_name(self):
        """
        Test a path the doesn't exist
        """
        self.assertRaises(
            FileNotFoundError, run_pre_commit_hooks_centralized.execute_pre_commit_hooks_centralized, "beans")


    @patch('pre_commit_to_rule_them_all.run_pre_commit_hooks_centralized.os')
    def test_use_linter_yaml(self, os_mock):
        """
        Test a valid path for linter pre-commit
        """
        os_mock.path.isdir.return_value = False

        run_pre_commit_hooks_centralized.use_pre_commit_hooks_rust()

if __name__ == '__main__':
    unittest.main()
