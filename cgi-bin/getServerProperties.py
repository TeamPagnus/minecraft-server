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

server_properties = ""
with open(MINECRAFT_DIR + "server.properties", 'r') as f:
    for l in f:
        server_properties += l

print(server_properties)
