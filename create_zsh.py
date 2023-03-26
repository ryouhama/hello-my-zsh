"""
Create a zsh script to run the python script.

Usage:
    >>> poetry run python create_zsh.py
"""
import getpass
from loader import YamlLoader
from models import Alias

PATH = f"/Users/{getpass.getuser()}/.zshrc"
YAML_PATH = "alias.yaml"


def main():
    loaded_alias = YamlLoader(YAML_PATH).load()

    alias_items = [
        Alias(name=key, command=value) for key, value in loaded_alias["alias"].items()
    ]
    import pprint

    pprint.pprint([item.to_string() for item in alias_items])


if __name__ == "__main__":
    main()
