# -*- coding: utf-8 -*-
"""
Module that executes the pre-commit hook centralized configuration
"""
import os


def use_pre_commit_hooks_rust():
    """Method that executes the pre-commit hook with the javascript linter"""
    execute_pre_commit_hooks_centralized('pre-commit-hooks-rust.yaml')

def execute_pre_commit_hooks_centralized(config_yaml):
    """Method that executes the specified centralized pre-commit hook configuration"""

    root_dir = os.path.dirname(__file__)

    pre_commit_configuration_path = os.path.join(
        root_dir, config_yaml)

    if os.path.exists(pre_commit_configuration_path):
        cmd = ['pre-commit', 'run', '--config',
               pre_commit_configuration_path, '--files']
        os.execvp(cmd[0], cmd)
    else:
        raise FileNotFoundError("File not found!")