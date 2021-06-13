#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Escribir Scripts de acá para abajo.
try:
    with open(defs.MC_AVAILABLE_VERSION_PATH, "r") as f:
        print(f.read())

except Exception:
    pass
