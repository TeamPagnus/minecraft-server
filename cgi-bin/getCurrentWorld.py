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
with open(MC_SERVER_PROPERTIES_PATH, 'r') as f:
    print(f.read())
