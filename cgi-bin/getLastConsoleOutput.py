#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Escribir Scripts de acá para abajo.
from subprocess import getoutput

print(getoutput("tail -n40 minecraft/out.txt"))