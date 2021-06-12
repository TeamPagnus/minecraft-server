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

# Core.
from bs4 import BeautifulSoup
import requests as r

MCVERSIONS_URL = "https://mcversions.net/"

res = r.get(MCVERSIONS_URL)
soup = BeautifulSoup(res.content, "html5lib")

versions = []
for version in soup.findAll(True, {"data-version": True}):
    versions.append([version["data-version"], None])

versions = versions[:10] # Truncate versions to improve latency.

for i in range(len(versions)):
    res = r.get(f"{MCVERSIONS_URL}/download/{versions[i][0]}")
    soup = BeautifulSoup(res.content, "html5lib")
    for link in soup.findAll(True, {"download": True}):
        if "server" in link["download"]:
            versions[i][1] = link["href"]

with open(MINECRAFT_DIR + "/available-versions", "w") as f:
    for v in versions:
        f.write(f"{v[0]} {v[1]}\n")

print("Version list updated.")
