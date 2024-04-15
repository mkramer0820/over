from cx_Freeze import setup, Executable
import os
import sys


base = None
packages=['pandas', 'numpy', 'os', 'datetime', 'time', 'openpyxl']

#includes = ['pandas', 'numpy', 'tia','bnyCompliance',
#           'bloombergBooks', 'os', 'sys', 'win32com', 'file_functions','glob', 'webbrowser']
excludes = ['tkinter','sqlite3', 'tia.rlab.sample', 'tornado','ipython-genutils',
            'decorator', 'traitlets', 'jupyter-core', 'pyzmq', 'jupyter-client',
            'backcall', 'parso', 'jedi', 'simplegeneric', 'pickleshare', 'colorama', 'pygments', 'wcwidth',
            'prompt-toolkit', 'ipykernel', 'pyte']

            
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('test.py', base=base, icon="superman.ico")
]

setup(name='over-under',
      version='1.0',
      description='Sample cx_Freeze wxPython script',
      options = {"build_exe": {#"includes": includes,
                             "excludes": excludes,
                             "packages": packages,
                             }
               },
      executables=executables
      )