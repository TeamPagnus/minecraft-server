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

lastLog = getoutput(f"tail -n40 {defs.MC_LOG_PATH}")

def getStatus():
    """
    Hay 3 estados posibles:
    Started, Stopped, Waiting
    """

    # Stopped
    if not defs.MC_SCREEN_PROCESS_NAME in getoutput("screen -ls"):
        return "Stopped"

    # Waiting
    if "Stopping the server" in lastLog:
        return "Waiting"

    # Started & Waiting
    if "Preparing spawn area" in lastLog:
        if "Done" in lastLog:
            return "Started"
        else:
            return "Waiting"

    # Default started, the server has a lot of log
    return "Started"

print(getStatus())