from cx_Freeze import setup, Executable
import os
import sys

where = os.path.dirname(sys.executable)


os.environ['TCL_LIBRARY'] = where+"\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = where+"\\tcl\\tk8.6"

build_exe_options = {"include_files": [where+"\\DLLs\\tcl86t.dll", where+"\\DLLs\\tk86t.dll"], "packages":["tkinter"]}  


setup(
    name = "Genius",
    version = "0.1",
    description = "Knowledge library",
    options={"build_exe": build_exe_options},  
    executables = [Executable("UserGUI.py")]
)
