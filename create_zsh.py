"""
Create a zsh script to run the python script.

Usage:
    >>> poetry run python create_zsh.py
"""
import getpass
from services.alias_service import AliasService

PATH = f"/Users/{getpass.getuser()}/.zshrc"
YAML_PATH = "alias.yaml"


def main():
    alias_list = AliasService().fetch(YAML_PATH)
    # TODO: print
    import pprint

    pprint.pprint([it.to_string() for it in alias_list])


if __name__ == "__main__":
    main()
