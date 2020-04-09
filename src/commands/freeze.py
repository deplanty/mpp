import json
import os
import shutil
import sys

from src.utils import ask

def freeze(args):
    # PyInstaller exists
    if not shutil.which("pyinstaller"):
        print("It seems that PyInstaller is not installed.")
        print("Please, consider using `pip install PyInstaller`.")
        print(f"Current pip is {shutil.which('pip')}.")
        print("")
        answer = ask.question("Do you want to install it on the go (y/n)?", "n")
        if answer == "y":
            print("")
            print("~$ pip install PyInstaller")
            os.system("pip install PyInstaller")
        else:
            sys.exit()

    os.chdir("installer")
    print("")
    print("~$ pyinstaller installer.spec")
    os.system("pyinstaller installer.spec")
