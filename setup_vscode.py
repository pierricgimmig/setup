#!/usr/bin/env python3

"""
Script to setup VSCode as git diff and merge tools.
"""

import os
import subprocess

GIT_NAME = "Pierric Gimmig"
GIT_EMAIL = "pierric.gimmig@gmail.com"

def run_command(command: str):
    print(command)
    subprocess.run(command, capture_output=True, text=True, shell=True)

    
def main():
    """Setup VSCode."""
    
    # Git diff and merge tools.
    run_command(f'git config --global user.email "{GIT_EMAIL}"')
    run_command(f'git config --global user.name "{GIT_NAME}"')
    run_command("git config --global diff.tool vscode")
    run_command("git config --global difftool.vscode.cmd 'code --wait --diff $LOCAL $REMOTE'")
    run_command("git config --global merge.tool vscode")
    run_command("git config --global mergetool.vscode.cmd 'code --wait $MERGED'")
    run_command("git config --global mergetool.vscode.trustExitCode true")
    run_command("git config --global difftool.prompt false")


if __name__ == "__main__":
    main()
