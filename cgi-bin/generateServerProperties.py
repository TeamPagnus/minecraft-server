#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generates server.properties by merging worldless-server.properties and
# level-name.properties.

import defs

server_properties = ""

with open(defs.MC_WORLDLESS_SP, 'r') as f:
    for l in f:
        server_properties += l

with open(defs.MC_LEVEL_NAME_SP, 'r') as f:
    for l in f:
        server_properties += l

with open(defs.MC_SERVER_PROPERTIES_PATH, 'w') as f:
    f.write(server_properties)
