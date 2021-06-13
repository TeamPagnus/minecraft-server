#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Core.
from os import walk
import requests

def download_file(url, filename):
    local_filename = filename
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk: 
                f.write(chunk)
    return local_filename

def fetch_version_url(version):
    with open(defs.MC_AVAILABLE_VERSION_PATH, 'r') as f:
        for l in f:
            data = l.split(' ')
            if data[0] == version:
                return data[1].strip()
    return None

def version_is_installed(version):
    files = next(walk(defs.MC_DIR))[-1]
    if f"minecraft_server.{version}.jar" in files:
        return True
    return False

args = cgi.FieldStorage()

try:
    version = args["version"].value
except Exception:
    print("Wrong request.")
    assert False

if not version_is_installed(version):
    download_file(
        fetch_version_url(version),
        defs.MC_DIR + f"minecraft_server.{version}.jar"
    )
    print(f"{version} was installed.")

with open(defs.MC_SERVER_VERSION_PATH, 'w') as f:
    f.write(version)

print(f"Version {version} will be used.")
