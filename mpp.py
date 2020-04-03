import argparse
import sys

from src.commands import setup, config, freeze


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

setup_parser = subparsers.add_parser(
    "setup",
    description="Ask some questions to setup the project",
    help="ask some questions to setup the project"
)
setup_parser.set_defaults(func=setup)

config_parser = subparsers.add_parser(
    "config",
    description="Show project parameters and edit them",
    help="show project parameters and edit them"
)
config_parser.add_argument("parameter", nargs="*", help="parameters to edit")
config_parser.set_defaults(func=config)

freeze_parser = subparsers.add_parser(
    "freeze",
    description="Create an executable using PyInstaller",
    help="create an executable using PyInstaller"
)
freeze_parser.set_defaults(func=freeze)

args = parser.parse_args()

if not hasattr(args, "func"):
    parser.print_help()
    sys.exit(0)

args.func(args)
