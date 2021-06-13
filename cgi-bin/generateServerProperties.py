#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generates server.properties by merging worldless-server.properties and
# level-name.properties.

import defs

server_properties = ""

try:
    with open(defs.MC_WORLDLESS_PATH, 'r') as f:
        for l in f:
            server_properties += l
except Exception:
    pass

try:
    with open(defs.MC_LEVEL_NAME_PATH, 'r') as f:
        for l in f:
            server_properties += l
except Exception:
    pass

with open(defs.MC_SERVER_PROPERTIES_PATH, 'w') as f:
    f.write(server_properties)
