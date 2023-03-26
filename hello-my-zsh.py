"""
This is a script to write an alias to your zshrc.
A backup will be created before execution.
It is dangerous because it writes directly.

Usage:
    >>> poetry run python hello-my-zsh.py
"""
import os
import shutil
import getpass
from typing import List
from loader import YamlLoader
from models import Alias


PATH = f"/Users/{getpass.getuser()}/.zshrc"
YAML_PATH = "my-alias.yaml"
ENCORDING = "UTF-8"


def check_file_exist():
    if not os.path.isfile(PATH):
        raise FileNotFoundError(f"File not found: path={PATH}")


def create_backup():
    shutil.copyfile(PATH, f"{PATH}.backup")


def load_yaml():
    yaml_souces = YamlLoader(YAML_PATH).load()
    alias_items = [
        Alias(name=key, command=value) for key, value in yaml_souces["alias"].items()
    ]
    return alias_items


def write_alias_in_zsh(items: List[Alias]):
    with open(PATH, mode="a", encoding=ENCORDING) as zsh_file:
        zsh_file.write("\n")
        for item in items:
            zsh_file.write(f"{item.to_string()}\n")


def main():
    check_file_exist()
    create_backup()
    items = load_yaml()
    write_alias_in_zsh(items)


if __name__ == "__main__":
    main()
