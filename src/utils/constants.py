import os

pp = os.path.dirname
dir_home = pp(pp(pp(__file__)))

path_ico_default = os.path.join(dir_home, "resources", "default.ico")

with open(os.path.join(dir_home, "resources", "main.py.pattern")) as f:
    pattern_main_py = f.read()