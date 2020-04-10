import json
import os
import shutil
import sys

from mpp.src.utils import ask, constants as cst


def config(args=None):
    """
    Show or edit configuration parameters

    Args:
        args (argparse args): parameters from parser.parse_args()
    """

    # Get project config file
    if not os.path.exists(".mpp_config"):
        sys.exit("Please setup your environment by using the 'setup' command")
    with open(".mpp_config") as f:
        answers = json.load(f)

    # If there is no parameter
    if not args.parameter:
        values = [f" -→ {k} = {v}" for k, v in answers.items()]
        values = "\n".join(values)
        sys.exit(f"The list of parameters:\n{values}")

    # If there are parameters
    for param in args.parameter:
        if param not in answers:
            valid = [f"'{x}'" for x in answers.keys()]
            valid = ", ".join(valid)
            sys.exit(f"Invalid parameter: '{param}' (choose from {valid})")

    # Process each parameter
    new_answers = dict()
    if "name" in args.parameter:
        new_answers["name"] = ask.question(
            "What is your project name?",
            default=answers["name"],
            required=True
        )
    if "author" in args.parameter:
        new_answers["author"] = ask.question(
            "What is your author name?",
            default=answers["author"],
            required=True
        )
    if "console" in args.parameter:
        new_answers["console"] = ask.question(
            "Do you want to display the console (y/n)?",
            default="y" if answers["console"] else "n"
        )
        new_answers["console"] = new_answers["console"].lower() == "y"

    # Validate modifications
    is_ok = ask.question(
        "\nAre you sure of your modifications (y/n)?",
        required=True
    ).lower() == "y"
    if is_ok:
        answers.update(**new_answers)
        with open(".mpp_config", "w") as f:
            json.dump(answers, f)

    # Rewrite the specs file
    with open(f"installer/installer.spec", "w") as f:
        f.write(cst.pattern_spec % answers)
    # Rewrite the nsis file
    with open(f"installer/installer.nsi", "w") as f:
        f.write(cst.pattern_nsis % answers)
