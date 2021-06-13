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
from os import walk

EXCEPTION = ["logs"]

worlds = next(walk(defs.MC_DIR))[1]
for f in EXCEPTION:
    worlds.remove(f)

for w in worlds:
    print(w)
