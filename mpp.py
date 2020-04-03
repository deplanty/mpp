import argparse
import sys

from src.commands import setup


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

setup_parser = subparsers.add_parser(
    "setup",
    description="Ask some questions to setup the project",
    help="ask some questions to setup the project"
)
setup_parser.set_defaults(func=setup)

args = parser.parse_args()

if not hasattr(args, "func"):
    parser.print_help()
    sys.exit(0)

args.func(args)
