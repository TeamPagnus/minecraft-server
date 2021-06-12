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

# Escribir Scripts de acá para abajo.
with open(MINECRAFT_DIR + "/server-version", "r") as f:
    print(next(f))
