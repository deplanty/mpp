import json
import os
import shutil

from src.utils import ask, constants as cst


def setup(args):
    """
    Asks information to the user and setup the environment
    """

    answers = dict()
    answers["name"] = ask.question("What is your project name?", required=True)
    answers["author"] = ask.question("What is your author name?", required=True)
    answers["console"] = ask.question("Do you want to display the console (y/n)?", "n")
    answers["console"] = answers["console"].lower() == "y"
    is_icon = ask.question("Are you using an icon (y/n)?", "y")
    if is_icon.lower() == "y":
        filename = ask.icon()
        if filename != "":
            answers["icon"] = filename
            print(" -→ Using:", filename)
        else:
            answers["icon"] = None
    else:
        answers["icon"] = None

    # Create folders
    os.makedirs("installer", exist_ok=True)
    os.makedirs("resources/images", exist_ok=True)
    os.makedirs("src", exist_ok=True)

    # Add icon
    if answers["icon"]:
        shutil.copy(answers["icon"], "resources/images/icon.ico")
    else:
        shutil.copy(cst.path_ico_default, "resources/images/icon.ico")
    answers["icon"] = "resources/images/icon.ico"

    # Write the config file
    with open(".mwocfg", "w") as f:
        json.dump(answers, f, indent=4)
    # Write the files
    with open("main.py", "w") as f:
        f.write(cst.pattern_main_py % answers)
