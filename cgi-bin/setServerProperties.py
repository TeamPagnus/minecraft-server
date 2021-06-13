#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Content
args = cgi.FieldStorage(keep_blank_values = True)

# Extract POST arguments.
server_properties = ""
for i in args.keys():
    server_properties += f"{i}={args[i].value}\n"

with open(defs.MC_WORLDLESS_PATH, 'w') as f:
    f.write(server_properties)

# Merge worldless-server.properties and level-name.properties into
# server.properties.
import generateServerProperties

print("server.properties saved.")
