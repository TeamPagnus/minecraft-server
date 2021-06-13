#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

server_properties = ""
with open(defs.MC_SERVER_PROPERTIES_PATH, 'r') as f:
    for l in f:
        server_properties += l

print(server_properties)
