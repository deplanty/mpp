import json
import os
import shutil

from src.utils import ask, constants as cst


def setup(args=None):
    """
    Asks information to the user and setup the environment
    """

    current_dir = os.path.basename(os.getcwd())
    username = os.path.basename(os.path.expanduser("~"))

    answers = dict()
    answers["name"] = ask.question("What is your project name?", current_dir, required=True)
    answers["author"] = ask.question("What is your author name?", username, required=True)
    answers["console"] = ask.question("Do you want to display the console (y/n)?", "y")
    answers["console"] = answers["console"].lower() == "y"

    # Create folders
    os.makedirs("installer", exist_ok=True)
    os.makedirs("resources/images", exist_ok=True)
    os.makedirs("src", exist_ok=True)

    # Add icon
    shutil.copy(cst.path_ico_default, "resources/images/icon.ico")
    answers["icon"] = "resources/images/icon.ico"
    print(f"The project's icon is stored in {answers['icon']}")

    # Write the config file
    with open(".mpp_config", "w") as f:
        json.dump(answers, f, indent=4)
    # Write the files
    with open("main.py", "w") as f:
        f.write(cst.pattern_main_py % answers)
    # Write the specs
    with open(f"installer/installer.spec", "w") as f:
        f.write(cst.pattern_spec % answers)
    # Write the nsis file
    with open(f"installer/installer.nsi", "w") as f:
        f.write(cst.pattern_nsis % answers)
