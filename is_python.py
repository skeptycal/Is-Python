#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
import sys
import text_colors
from typing import Dict, List  # pylint: disable=unused-import

""" ╔═════ DOCBLOCK ═════╦════ CODE SUMMARY ════╗
    ║                    ║                      ║
    ║   => TEST INFO:    ║    is_python.py      ║
    ║   ProductName:     ║    Mac OS X          ║
    ║   ProductVersion:  ║    10.14.3           ║
    ║   BuildVersion:    ║    18D109            ║
    ║   Date:            ║    02-13-2019        ║
    ║                    ║                      ║
    ╚═══ LICENSE: MIT ═══╩═════ @skeptycal ═════╝

    ╔═════════ Module is_python.py ════════════════════════════════════════════╗
    ║                                                                          ║
    ║     author      ║    Michael Treanor  <skeptycal@gmail.com>              ║
    ║     copyright   ║    (c) 2019 Michael Treanor                            ║
    ║     license     ║    MIT <https://opensource.org/licenses/MIT>           ║
    ║     link        ║    http://www.github.com/skeptycal                     ║
    ║                                                                          ║
    ╚══════════════════════════════════════════════════════════════════════════╝
        Determine and return python shell environment and version information.

        References are at the end of the file.
        """


""" ╔═════════ Parameters : ═══════════════════════════════════════════════════╗

    requires no input parameters

    python_shell() returns
    'shell' (started python on command line using "python")
    'ipython' (started ipython on command line using "ipython")
    'ipython-notebook' (e.g., running in Spyder or started
        with "ipython qtconsole")
    'Jupyter Notebook' (running in a Jupyter notebook)

    bonus utility:
        sets PY3 (bool) to True or False for python version >= 3.0
    """

# Initialization Section - only run once during initial import or CLI run


def py3():
    """ Returns boolean: Is python version >= 3? """

    import sys
    return sys.version_info[0] >= 3

def py_vers():
    """ Returns float: python version <major>.<minor> """

    import sys
    PY_VER = sys.version_info
    return float(str(PY_VER[0]) + '.' + str(PY_VER[1]))

def is_nb():
    """ Returns boolean: Is python running in a Jupyter notebook? """
    import os

    if "jupyter-notebook" in os.path.basename(os.environ['_']):
        return True
    else:
        return False

def py_shell():
    """ Returns string: Current python shell name. """
    import os
    try:
        import platform
    except ImportError:
        IM_PLAT = False
    else:
        IM_PLAT = True

    PY_ENV = os.environ
    PY_BASE = os.path.basename(PY_ENV['_'])

    if "JPY_PARENT_PID" in PY_ENV:
        shell = "ipython-notebook"
    elif "jupyter-notebook" in PY_BASE:
        shell = "jupyter notebook"
    elif "ipython" in PY_BASE:
        shell = "ipython"
    elif IM_PLAT:
        shell = platform.python_implementation()
    else:
        shell = "shell"
    print("pyshell() output: ", shell.strip())
    return shell.strip()

BG_COLOR = 
PURPLE = FG_DICT['PURPLE']
BLUE = FG_DICT['COOL']+


BG_COLOR = '\u001b[48;5;230m'
HEADER = '\u001b[38;5;18m' + BG_COLOR
BLUE = '\u001b[38;5;27m' + BG_COLOR
PURPLE = '\u001b[38;5;92m'
RESET = '\u001b[0m'

if __name__ == "__main__":
    # ? TEST to use if script is run from the command line
    print(BLUE)
    print("Test output for is_python module:")
    print("MIT license  |  copyright (c) 2018 Michael Treanor")
    print("<https://www.github.com/skeptycal>")
    print()
    print("The type of python shell you are using is: ", HEADER,
          py_shell(), BLUE, ".", sep='')
    print(BLUE)
    for x in sys.version_info:
        print("Python version part is: ", HEADER, x, BLUE, sep='')

    print("Python reports version is: ", HEADER, sys.version_info, BLUE, sep='')
    print("Python reports <major.minor> version is: ", HEADER, py_vers(), BLUE, sep='')
    print("PY3 says python version is >= 3? ", HEADER, py3(), BLUE, sep='')
    print("is_nb() reports jupyter notebook? ", HEADER, is_nb(), BLUE, sep='')
    print(RESET)


""" ╔═════════ Testing complete 2/14/19: ══════════════════════════════════════╗

        macOS Mojave       10.14.3
        jupyter --version    4.4.0
        ipython --version    7.2.0
        spyder(anaconda)     3.3.2
        python --version     3.7.2
        PyPy3 --version      6.0.0
    """

""" ╔═════════ Resources: ═════════════════════════════════════════════════════╗

        * https://stackoverflow.com/a/53436734/9878098
          Quote: "The following captures the cases of
            https://stackoverflow.com/a/50234148/1491619
            without needing to parse the output of ps"
          -- Bob Weigel (https://stackoverflow.com/users/1491619/bob-weigel)
        * See also https://stackoverflow.com/a/37661854
    """
