#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generates server.properties by merging worldless-server.properties and
# level-name.properties.

CGI_DIR = "cgi_bin/"
MINECRAFT_DIR = "minecraft/"

server_properties = ""

try:
    with open(MINECRAFT_DIR + "worldless-server.properties", 'r') as f:
        for l in f:
            server_properties += l
except Exception:
    pass

try:
    with open(MINECRAFT_DIR + "level-name.properties", 'r') as f:
        for l in f:
            server_properties += l
except Exception:
    pass

with open(MINECRAFT_DIR + "server.properties", 'w') as f:
    f.write(server_properties)
