#!/usr/bin/env python3

"""
Script to create alias scripts for commonly used commands.
"""

import os
import yaml

PROFILE = "$PROFILE" if os.name == "nt" else "~/.bashrc"
LAUNCH_URL = "start" if os.name == "nt" else "xdg-open"
SCRIPT_EXT = ".bat" if os.name == "nt" else ".sh"
COMMENT = "::" if os.name == "nt" else "#"
WARNING = f"{COMMENT} This file is generated by generate_aliases.py. Do not edit.\n"
SCRIPT_TEMPLATE = WARNING + "@echo off\n{command}" if os.name == "nt" else "#!/bin/bash\n{command}"
GENERATED_DIR = "generated"

def fixup_command(command):
    if command.startswith("http"):
        command = f"{LAUNCH_URL} {command}"
    return command

def write_scripts(aliases):
    """Write script files for aliases."""
    os.makedirs(GENERATED_DIR, exist_ok=True)
    for alias, command in aliases.items():
        command = fixup_command(command)
        # Write script file
        script_name = os.path.join(GENERATED_DIR, alias + SCRIPT_EXT)
        print(f"Creating {script_name} for '{alias}' : {command}")
        with open(script_name, "w") as script_file:
            script_file.write(SCRIPT_TEMPLATE.format(command=command))
        # Make script executable on Unix
        if os.name != "nt":
            os.chmod(script_name, 0o755)


def output_aliases(aliases):
    print("\n# Productivity aliases")
    for alias, command in sorted(aliases.items()):
        command = fixup_command(command)
        if os.name == "nt":
            print(f"New-Alias  {alias} {command}")
        else:
            print(f"alias {alias}='{command}'")
    print(f"\nPlease copy above aliases to your {PROFILE}:")
    os.system(f"code {PROFILE}")
    
    
def main():
    """Create executable scripts for aliases."""
    # read aliases from YAML file
    with open("aliases.yml") as f:
        data = yaml.safe_load(f)

    # merge dictionaries
    aliases = data["all"]
    if os.name == "nt":
        aliases.update(data["windows"])
    else:
        aliases.update(data["unix"])
    
    # output aliases
    write_scripts(aliases)
    output_aliases(aliases)


if __name__ == "__main__":
    main()
