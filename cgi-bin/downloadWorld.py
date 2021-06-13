#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/html")
print()

import cgitb
cgitb.enable()

# Core.
from os import walk
import shutil

def zip_world(world):
    shutil.make_archive(defs.MC_DIR + f"{world}.zip", 'zip', defs.MC_DIR + world)
    link = f"<a href=\"/{defs.MC_DIR + world}.zip\">{world}.zip</a> is ready to be downloaded."
    print(link)

EXCEPTION = ["logs"]

worlds = next(walk(defs.MC_DIR))[1]
for f in EXCEPTION:
    worlds.remove(f)

args = cgi.FieldStorage()

try:
    world = args["level-name"].value
except Exception:
    print("Wrong request.")
    assert False

if '/' in world:
    print("Wrong request.")
    assert False

if world not in worlds:
    print("Wrong request.")
    assert False

zip_world(world)
