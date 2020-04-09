import json
import os
import shutil
import sys


def freeze(args):
    # PyInstaller exists
    if not shutil.which("pyinstaller"):
        sys.exit("It seems that PyInstaller is not installed.\nPlease, consider using `pip install PyInstaller`.")

    os.chdir("installer")
    os.system("pyinstaller installer.spec")
