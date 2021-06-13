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
import subprocess

## si no esta iniciado el server, salir
if not defs.MC_SCREEN_PROCESS_NAME in subprocess.getoutput("screen -ls"):
    exit()

subprocess.run(["screen", "-S", defs.MC_SCREEN_PROCESS_NAME, "-X", "stuff", "stop\n"])

print("Stop signal sent")