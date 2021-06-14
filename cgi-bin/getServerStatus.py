#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Escribir Scripts de acá para abajo.
from subprocess import getoutput

#lastLog = getoutput(f"tail -n40 {defs.MC_LOG_PATH}")
doneCount = getoutput(f"cat {defs.MC_LOG_PATH} | grep 'Done' | wc -l")
stopCount = getoutput(f"cat {defs.MC_LOG_PATH} | grep 'Stopping the server' | wc -l")

def getStatus():
    """
    Hay 3 estados posibles:
    Started, Stopped, Waiting
    """

    if not defs.MC_SCREEN_PROCESS_NAME in getoutput("screen -ls"):
        return "Stopped"

    if doneCount > stopCount:
        return "Started"

    return "Waiting"

print(getStatus())