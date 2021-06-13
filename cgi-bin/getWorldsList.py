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

EXCEPTION = ["logs"]

try:
    worlds = next(walk(MINECRAFT_DIR))[1]
    for f in EXCEPTION:
        worlds.remove(f)

    for w in worlds:
        print(w)
except Exception:
    pass
