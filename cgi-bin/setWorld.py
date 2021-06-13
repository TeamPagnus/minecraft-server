#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Core.
args = cgi.FieldStorage()

try:
    world = args["level-name"].value
except Exception:
    print("Wrong request.")
    assert False

level_name = f"level-name={world}"

with open(defs.MC_LEVEL_NAME_PATH, 'w') as f:
    f.write(level_name)

# Merge worldless-server.properties and level-name.properties into
# server.properties.
import generateServerProperties

print(f"World {world} set.")
