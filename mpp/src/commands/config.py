import json
import os
import shutil
import sys

from mpp.src.utils import ask, constants as cst, files


# TODO: What to do when args is no given?
def config(args=None, parser=None):
    """
    Show or edit configuration parameters

    Args:
        args (argparse args): parameters from parser.parse_args()
    """

    if not any([args.list, args.parameters]):
        parser.print_help()
        sys.exit()

    # Get project config file
    if not os.path.exists(".mpp_config"):
        sys.exit("Please setup your environment by using the 'setup' command")
    with open(".mpp_config") as f:
        mpp_config = json.load(f)

    # If there is no parameter
    if args.list:
        __show_config(mpp_config)
        sys.exit()

    # If there are parameters
    for param in args.parameters:
        if param not in mpp_config:
            valid = [f"'{x}'" for x in mpp_config.keys()]
            valid = ", ".join(valid)
            sys.exit(f"Invalid parameter: '{param}' (choose from {valid})")

    new_config = __process_parameters(args, mpp_config)
    if new_config:
        mpp_config.update(**new_config)
        files.write_mpp_config(mpp_config)
        files.write_installer(mpp_config)


def __show_config(mpp_config):
    """
    Shows the parameters from the configurtion file

    Args:
        mpp_config (dict): project parameters
    """

    values = [f" -→ {k} = {v}" for k, v in mpp_config.items()]
    print(*values, sep="\n")


def __process_parameters(args, mpp_config):
    """
    Processes the given parameters

    Args:
        args (argparse args): parameters from parser.parse_args()
        mpp_config (dict): project parameters

    Returns:
        dict: user's answers
    """

    # Process each parameter
    answers = dict()
    if "name" in args.parameters:
        answers["name"] = ask.question(
            "What is your project name?",
            default=mpp_config["name"],
            required=True
        )
    if "author" in args.parameters:
        answers["author"] = ask.question(
            "What is your author name?",
            default=mpp_config["author"],
            required=True
        )
    if "console" in args.parameters:
        answers["console"] = ask.question(
            "Do you want to display the console (y/n)?",
            default="y" if mpp_config["console"] else "n"
        )
        answers["console"] = answers["console"].lower() == "y"

    # Validate modifications
    print("")
    is_ok = ask.question(
        "Are you sure of your modifications (y/n)?",
        required=True
    ).lower() == "y"

    if not is_ok:
        answers.clear()

    return answers
