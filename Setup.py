# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 01:13:02 2019

@author: prach
"""

import cx_Freeze
import os.path
import sys
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


executables = [cx_Freeze.Executable("BMXCrashLoop.py")]

cx_Freeze.setup(
        name = "BMXCrashLoop",
        options = {"build_exe": {"packages":["pygame"],
                                 "include_files":["racecar.png",
                                                   "fire1.jpg",
                                                   "Game.wav",
                                                   "PressStart2P-Regular.ttf",
                                                   "Smash.wav",
                                                   "Start.wav",
                                                   "stop1.jpg",
                                                   "stop2.jpg",
                                                   "timesbi.ttf",
                                                   "tree1.jpg",
            (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')),
            (os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll')),
         ]}},
        executables = executables
        )