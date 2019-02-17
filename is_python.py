#!/usr/bin/env python3
'''
###############################################################################
   python_shell.py - Python3 returns a string containing the parent shell

###############################################################################
    requires no parameters

    returns
    'shell' (started python on command line using "python")
    'ipython' (started ipython on command line using "ipython")
    'ipython-notebook' (e.g., running in Spyder or started with "ipython qtconsole")
    'Jupyter Notebook' (running in a Jupyter notebook)
    
    Copyright (C) 2019  Michael Treanor <https://www.github.com/skeptycal>
    License GPL3.0

###############################################################################
'''
def python_shell():
    import os
    try:
        import platform
    except ImportError:
        im_plat = False
    else:
        im_plat = True

    env = os.environ
    shell = 'shell'
    program = os.path.basename(env['_'])

    if 'jupyter-notebook' in program:
        shell = 'Jupyter Notebook'
    elif 'JPY_PARENT_PID' in env:
        shell = 'ipython-notebook'
    elif 'ipython' in program:
        shell = "ipython"
    elif im_plat:
        shell = platform.python_implementation()
    return shell

# ! TEST - REMOVE THIS
print("The type of python shell you are using is: ", python_shell(), ".")


'''############################################################################
Testing complete 2/14/19
    macOS Mojave       10.14.3
    jupyter --version    4.4.0
    ipython --version    7.2.0
    spyder(anaconda)     3.3.2
    python --version     3.7.2
    PyPy3 --version      6.0.0
############################################################################'''

'''############################################################################
License: GPL3.0

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
############################################################################'''

'''############################################################################
Modifications: 
    * The logic in the main example was clarified 
      (removed double check for JPY_PARENT_PID in env)
    * "import os" placed outside of the function body since it will always be
       required by this module and highly likely will be required by any program
       that is concerned with which shell called it.

Research sources:
    * https://stackoverflow.com/a/53436734/9878098
      Quote: "The following captures the cases of https://stackoverflow.com/a/50234148/1491619 
      without needing to parse the output of ps" 
      -- Bob Weigel (https://stackoverflow.com/users/1491619/bob-weigel)
    * See also https://stackoverflow.com/a/37661854 
############################################################################'''
