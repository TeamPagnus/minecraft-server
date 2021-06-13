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
try:
    with open(MINECRAFT_DIR + "level-name.properties", 'r') as f:
        print(f.read())
except Exception:
    print("level-name=world")
