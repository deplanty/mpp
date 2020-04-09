import json
import os
import shutil
import sys

from src.utils import download

def installer(args):
    # PyInstaller exists
    if not shutil.which("makensis"):
        sys.exit("It seems that NSIS is not installed or in the PATH.")

    # os.chdir("installer")
    # os.system("pyinstaller installer.spec")
    print("This doesn't do anything yet")

    download.shell_exec_as_user()
