# -*- coding: utf-8 -*-
"""
Module that executes the pre-commit hook centralized configuration
"""
import os
import subprocess


def use_pre_commit_hooks_common():
    """Method that executes the pre-commit hook for shared repository checks"""
    execute_pre_commit_hooks_centralized(
        'configurations/pre-commit-hooks-common.yaml')


def use_pre_commit_hooks_rust():
    """Method that executes the pre-commit hook for Rust"""
    execute_pre_commit_hooks_centralized(
        'configurations/pre-commit-hooks-rust.yaml')


def use_pre_commit_hooks_python():
    """Method that executes the pre-commit hook for Python"""
    execute_pre_commit_hooks_centralized(
        'configurations/pre-commit-hooks-python.yaml')


def execute_pre_commit_hooks_centralized(config_yaml):
    """Method that executes the specified centralized pre-commit hook configuration"""

    root_dir = os.path.dirname(__file__)

    pre_commit_configuration_path = os.path.join(
        root_dir, config_yaml)

    if os.path.exists(pre_commit_configuration_path):
        cmd = ['pre-commit', 'run', '--config',
               pre_commit_configuration_path, '--files']
        completed_process = subprocess.run(cmd, check=False)
        if completed_process.returncode != 0:
            raise SystemExit(completed_process.returncode)
    else:
        raise FileNotFoundError("File not found!")
