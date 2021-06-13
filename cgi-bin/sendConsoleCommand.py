#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

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
if not "minecraftServer" in getoutput("screen -ls"):
    print("OK")
    exit()

import base64
command = base64.b64decode(commandEncoded).decode('utf-8')

#run(["screen", "-S", "minecraftServer", "-X", "stuff", "{command}\n"])

print(getoutput(f"screen -S minecraftServer -X stuff '{command}\n'"))
print(command)
print("OK")