from os import system
from pathlib import Path
from subprocess import PIPE, Popen

from toml import load


def get_project_version() -> str:
    with open(Path("pyproject.toml").absolute(), "r") as f:
        version: str = load(f)["project"]["version"]
    return version


def print_title_and_instuctions() -> None:
    system("clear")
    print(f"Story Lord v{get_project_version()}")
    print('Type "help" for help and "exit" to exit.')
    print()


def print_version() -> None:
    print()
    print(get_project_version())
    print()


def print_help() -> None:
    print(
        """
Options:
    -v, --version   output the version number
    -h, --help      display help
Commands:
    help            display help
    academic        change to academic mode
    normal          change to normal mode
    story           change to story mode
"""
    )


def write_to_clipboard(text: str) -> None:
    process = Popen("pbcopy", env={"LANG": "en_US.UTF-8"}, stdin=PIPE)
    process.communicate(text.encode())
