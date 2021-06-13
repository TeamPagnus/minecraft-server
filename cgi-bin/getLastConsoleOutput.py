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
from subprocess import getoutput

print(getoutput(f"tail -n40 {defs.MC_LOG_PATH}"))
