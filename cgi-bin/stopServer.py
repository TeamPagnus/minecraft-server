#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Escribir Scripts de acá para abajo.
import subprocess

## si no esta iniciado el server, salir
if not "minecraftServer" in subprocess.getoutput("screen -ls"):
    exit()

subprocess.run(["screen", "-S", "minecraftServer", "-X", "stuff", "stop\n"])

print("Stop signal sent")