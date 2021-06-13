#!/usr/bin/env python
# -*- coding: utf-8 -*-

CGI_DIR = "cgi_bin/"
MINECRAFT_DIR = "minecraft/"

import cgi

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Core.
from os import walk
import shutil

EXCEPTION = ["logs"]

worlds = next(walk(MINECRAFT_DIR))[1]
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

shutil.rmtree(MINECRAFT_DIR + world)

print(f"World {world} removed.")
