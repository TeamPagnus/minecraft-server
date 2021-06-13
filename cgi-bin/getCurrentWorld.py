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
try:
    with open(def.MC_LEVEL_NAME_PATH, 'r') as f:
        print(f.read())
except Exception:
    print("level-name=world")
