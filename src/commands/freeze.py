import json
import os
import shutil
import sys


def freeze(args):
    # PyInstaller exists
    if not shutil.which("pyinstaller"):
        sys.exit("PyInstaller seems not to be installed\nConsider using `pip install PyInstaller`")

    os.chdir("installer")
    os.system("pyinstaller installer.spec")
