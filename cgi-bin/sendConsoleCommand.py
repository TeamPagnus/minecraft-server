#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()
import cgitb
cgitb.enable()

# Content
args = cgi.FieldStorage()

try:
    commandEncoded = args["command"].value
except Exception:
    print("Wrong request.")
    assert False

from subprocess import run, getoutput

## si no esta iniciado el server, salir
if not defs.MC_SCREEN_PROCESS_NAME in getoutput("screen -ls"):
    print("OK")
    exit()

import base64
command = base64.b64decode(commandEncoded).decode('utf-8')

print(getoutput(f"screen -S {defs.MC_SCREEN_PROCESS_NAME} -X stuff '{command}\n'"))
print(command)
print("OK")