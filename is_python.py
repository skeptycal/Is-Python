#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
"""[module is_python]

Returns:
    py_shell():
        Returns string: Current python shell name. One of:
            ['Ipython', 'Ipython Notebook', 'Jupyter Notebook',
            'CPython', 'IronPython', 'Jython', 'PyPy', 'Shell']

    py3():
        Returns boolean: Is python version >= 3?

    py_vers():
        Returns float: python version <major>.<minor>

    is_nb():
        Returns boolean: Is python running in a Jupyter notebook?
"""

from typing import Dict, List
from sys import version_info


def py3() -> bool:
    """ [function py3]

    Returns
        [boolean] -- [True if python version >= 3 else False] """

    from sys import version_info

    return version_info[0] >= 3


def py_vers() -> float:
    """[function py_vers]

    Returns:
        [float] -- [python version <major>.<minor> ]
    """
    from sys import version_info

    return float(str(version_info[0]) + "." + str(version_info[1]))


def is_nb() -> bool:
    """ [function is_nb]

    Returns
        [boolean] -- [True if python is running in a Jupyter notebook else False] """
    from os import environ, path
    from sys import version_info

    return "jupyter-notebook" in path.basename(environ["_"])


def py_shell():
    """ Returns string: Current python shell name. """
    from os import environ, path

    try:
        import platform
    except ImportError:
        im_plat = False
    else:
        im_plat = True

    py_base = path.basename(environ["_"])

    if "JPY_PARENT_PID" in environ:
        shell = "ipython-notebook"
    elif "jupyter-notebook" in py_base:
        shell = "jupyter notebook"
    elif "ipython" in py_base:
        shell = "ipython"
    elif im_plat:
        shell = platform.python_implementation()
    else:
        shell = "shell"
    print("pyshell() output: ", shell.strip())
    return shell.strip()


# Initialization Section - only run once during initial import or CLI run

BG_COLOR = "[48;5;230m"
HEADER = "[38;5;18m" + BG_COLOR
BLUE = "[38;5;27m" + BG_COLOR
PURPLE = "[38;5;92m" + BG_COLOR
RESET = "[0m"

if __name__ == "__main__":
    # ? TEST to use if script is run from the command line
    from sys import version_info

    print(BLUE)
    print("Test output for is_python module:")
    print("MIT license  |  copyright (c) 2018 Michael Treanor")
    print("<https://www.github.com/skeptycal>")
    print()
    print(
        "The type of python shell you are using is: ",
        HEADER,
        py_shell(),
        BLUE,
        ".",
        sep="",
    )
    print(BLUE)
    for x in version_info:
        print("Python version part is: ", HEADER, x, BLUE, sep="")
    print()

    print("Python reports version is: ", HEADER, version_info, BLUE, sep="")
    print("Python reports <major.minor> version is: ", HEADER, py_vers(), BLUE, sep="")
    print("PY3 says python version is >= 3? ", HEADER, py3(), BLUE, sep="")
    print("is_nb() reports jupyter notebook? ", HEADER, is_nb(), BLUE, sep="")
    print(RESET)
    """
# Module is_python.py

    #  Michael Treanor  <skeptycal@gmail.com>
    #  (c) 2019 Michael Treanor
    #  MIT <https://opensource.org/licenses/MIT
    #  http://www.github.com/skeptycal

    # Determine and return python shell environment and version information.

    # => TEST INFO:    is_python.py
    # ProductName:     Mac OS X
    # ProductVersion:  10.14.19
    # BuildVersion:    18D109
    # Date:            02-13-2019

    """
""" Testing complete 2/14/19:

    macOS Mojave       10.14.3
    jupyter --version    4.4.0
    ipython --version    7.2.0
    spyder(anaconda)     3.3.2
    python --version     3.7.2
    PyPy3 --version      6.0.0
    """
""" Resources:

    * https://stackoverflow.com/a/53436734/9878098
        Quote: "The following captures the cases of without needing to parse
        the output of ps"
    * https://stackoverflow.com/a/50234148/1491619
        -- Bob Weigel (https://stackoverflow.com/users/1491619/bob-weigel)
    * See also https://stackoverflow.com/a/37661854
    """
