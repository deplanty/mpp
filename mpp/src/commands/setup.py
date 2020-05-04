import json
import os
import shutil
import sys

from mpp.src.utils import ask, constants as cst, files


def setup(args=None):
    """
    Asks information to the user and setup the environment

    Args:
        args (argparse args): parameters from parser.parse_args()
    """

    if args.update:
        # Get project config file
        mpp_config = files.get_mpp_config()
        # Update project config
        mpp_config = __update(mpp_config)
        # Write update
        files.write_mpp_config(mpp_config)
        sys.exit("Update done.")

    # Ask questions
    mpp_config = __update(dict())

    # Create folders
    os.makedirs("resources/images", exist_ok=True)
    os.makedirs("src", exist_ok=True)

    # Add icon
    if not os.path.exists(mpp_config["icon"]):
        shutil.copy(cst.path_ico_default, mpp_config["icon"])
    # Write configuration file
    files.write_mpp_config(mpp_config)
    # Write main file
    if not os.path.exists("main.py"):
        with open("main.py", "w") as f:
            f.write(cst.pattern_main_py % mpp_config)

    print("")
    print(f"The project's version is {mpp_config['version']}.")
    print(f"The project's icon can be found here: {mpp_config['icon']}.")
    print("The `main.py` file can now be edited.")
    print("")
    print("Use `mpp --help` to display all possible commands.")
    print("Use `mpp <command> -h` to display the help for a command.")
    print("Use `mpp config --list` to show your project settings.")


def __update(mpp_config):
    """
    Update mpp_config file with current version parameters.

    Args:
        mpp_config (dict): project parameters

    Returns:
        dict: updated project parameters
    """

    with open(cst.path_questions) as f:
        questions = json.load(f)
    new_mpp_config = dict()

    try:
        new_mpp_config["name"] = mpp_config["name"]
    except:
        current_dir = os.path.basename(os.getcwd())
        new_mpp_config["name"] = ask.question(questions["name"], current_dir, required=True)

    try:
        new_mpp_config["author"] = mpp_config["author"]
    except:
        username = os.path.basename(os.path.expanduser("~"))
        new_mpp_config["author"] = ask.question(questions["author"], username, required=True)

    try:
        new_mpp_config["version"] = mpp_config["version"]
    except:
        new_mpp_config["version"] = "0.0.0"

    try:
        new_mpp_config["icon"] = mpp_config["icon"]
    except:
        new_mpp_config["icon"] = "resources/images/icon.ico"

    try:
        new_mpp_config["resources"] = mpp_config["resources"]
    except:
        new_mpp_config["resources"] = ["resources", ".mpp_config"]

    try:
        new_mpp_config["console"] = mpp_config["console"]
    except:
        new_mpp_config["console"] = True

    try:
        new_mpp_config["hidden-imports"] = mpp_config["hidden-imports"]
    except:
        new_mpp_config["hidden-imports"] = list()

    return new_mpp_config
