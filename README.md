[![PyPI version](https://badge.fury.io/py/mpp.svg)](https://badge.fury.io/py/mpp)

# My Python Project

## Description

A simple tool to create a project with Python, an executable and an installer.

For now, it's only for Windows, but future versions will make it independent of the operating system.

## Installation

`mpp` can be installed using the pip package manager:

```
$ pip install mpp
```

## Usage

Let's create a project together.

```
$ mkdir mpp_tuto
$ cd mpp_tuto
```

### Setup your project easily

Just answer the questions, where the default value is between square brackets.

```
$ mpp setup
What is your project name? [mpp_tuto] MPP Tuto
What is your author name? [username] Name

The project's version is 0.0.0.
The project's icon can be found here: resources/images/icon.ico.
The `main.py` file can now be edited.

Use `mpp --help` to display all possible commands.
Use `mpp <command> -h` to display the help for a command.
Use `mpp config --list` to show your project settings.
```

#### Environment

After setuping your environment, some folders and files are created:

```
mpp_tuto/
    installer/
    resources/
        images/
            icon.ico
    src/
    target/
    .mpp_config
    main.py
```

- **installer/**: contains the files needed to freeze and create an installer;
- **resources/**: contains your project's files;
- **src/**: contains the sources of your project;
- **target/**: contains the created executable and installer;
- **.mpp_config**: stores yout project's settings;
- **main.py**: main python file.

### Show your configuration

```
$ mpp config --list
 -→ name = MPP Tuto
 -→ author = Name
 -→ version = 0.0.0
 -→ console = True
 -→ icon = resources/images/icon.ico
 -→ hidden-imports = []
```

### Edit your configuration

```
$ mpp config author version
What is your author name? [Name] John
What is the new version? [0.0.0] 0.0.1

Are you sure of your modifications (y/n)? y
```

### Process your project version

Show your project version.

```
$ mpp version
Project 0.0.0
```

Increment the version

```
$ mpp version +
Project 0.0.1

$ mpp version ++
Project 0.1.0

$ mpp version +
Project 0.1.1

$ mpp version +++
Project 1.0.0
```

### Freeze your project with [PyInstaller](https://www.pyinstaller.org/)

If `PyInstaller` is not installed, `mpp` asks if it can do it for you.

```
$ mpp freeze
It seems that PyInstaller is not installed.
Please, consider using `pip install PyInstaller`.
Current pip is path/to/pip.
Do you want to install it now (y/n)? [y]
[pip output]

[PyInstaller outpout]

Executable can be found here: target/Project/Project.exe
```

### Create an installer for your project with [NSIS](https://nsis.sourceforge.io/Main_Page)

If `ShellExecAsUSer.dll` is not in the `installer` folder, `mpp` asks if it can download it for you

```
$ mpp installer
NSIS needs "ShellExecAsUser" in order to create the installer.
Do you want to download it (y/n)? [y]

Downloading... Done
[NSIS output]

Installer can be found here: target/Project_setup.exe
```

## Credits

This project was originally inspired from [fbs](https://github.com/mherrmann/fbs).
