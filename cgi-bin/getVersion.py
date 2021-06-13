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

# Escribir Scripts de acá para abajo.
from os import walk

def extract_version(filename):
    return '.'.join(filename.split('.')[1:-1])

def get_installed_versions():
    try:
        files = next(walk(MINECRAFT_DIR))[-1]
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
    with open(MINECRAFT_DIR + "/server-version", "r") as f:
        version = next(f).strip()

except Exception:
    version = "Not set."

else:
    versions = get_installed_versions()
    if version not in versions:
        version = "Not set."

print(version)
