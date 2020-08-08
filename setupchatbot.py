from cx_Freeze import *
import sys


base = None

if sys.platform == 'win32':
    base = "Win32GUI"

executables = [Executable("tkinterVid28.py", base=base)]

setup(
    name = "Quote Bot",
    options = {"build_exe": {"packages":["tkinter","matplotlib"]}},
    version = "0.01",
    description = "I say quotes to make your day better",
    executables = executables
    )
