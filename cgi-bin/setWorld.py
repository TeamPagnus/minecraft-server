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
args = cgi.FieldStorage()

try:
    world = args["level-name"].value
except Exception:
    print("Wrong request.")
    assert False

level_name = f"level-name={world}"

with open(MINECRAFT_DIR + "level-name.properties", 'w') as f:
    f.write(level_name)

# Merge worldless-server.properties and level-name.properties into
# server.properties.
import generateServerProperties

print(f"World {world} set.")
