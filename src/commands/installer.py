import json
import os
import shutil
import sys

from src.utils import ask, download, constants as cst

def installer(args):
    # PyInstaller exists
    if not shutil.which("makensis"):
        sys.exit("It seems that NSIS is not installed or in the PATH.")

    if not os.path.exists(cst.path_dll_shellexecasuser):
        print("NSIS needs \"ShellExecAsUser\" in order to create the installer.")
        answer = ask.question("Do you want to download it (y/n)?", "y")
        if answer == "y":
            print("Downloading...", end=" ")
            file = download.shell_exec_as_user()
            print("Done")
        else:
            print("You can find it at this address: https://nsis.sourceforge.io/ShellExecAsUser_plug-in")

    # os.chdir("installer")
    # os.system("pyinstaller installer.spec")
    else:
        print("Ready to create the installer")

