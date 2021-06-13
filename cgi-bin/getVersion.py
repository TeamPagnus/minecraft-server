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
from os import walk

def extract_version(filename):
    return '.'.join(filename.split('.')[1:-1])

def get_installed_versions():
    try:
        files = next(walk(defs.MC_DIR))[-1]
    except Exception:
        return []
    else:
        versions = []
        for f in files:
            if "minecraft_server" not in f:
                continue
            versions.append(extract_version(f))
        return versions

try:
    with open(defs.MC_SERVER_VERSION_PATH, "r") as f:
        version = next(f).strip()

except Exception:
    version = "Not set."

else:
    versions = get_installed_versions()
    if version not in versions:
        version = "Not set."

print(version)
