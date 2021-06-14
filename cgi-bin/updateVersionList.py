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
from bs4 import BeautifulSoup
import requests as r

MCVERSIONS_URL = "https://mcversions.net/"

# res = r.get(MCVERSIONS_URL)
# soup = BeautifulSoup(res.content, "html5lib")

versions = []
versions.append(["1.17","https://launcher.mojang.com/v1/objects/0a269b5f2c5b93b1712d0f5dc43b6182b9ab254e/server.jar"])
versions.append(["1.16.5","https://launcher.mojang.com/v1/objects/1b557e7b033b583cd9f66746b7a9ab1ec1673ced/server.jar"])
versions.append(["1.16.4","https://launcher.mojang.com/v1/objects/35139deedbd5182953cf1caa23835da59ca3d7cd/server.jar"])
versions.append(["1.16.3","https://launcher.mojang.com/v1/objects/f02f4473dbf152c23d7d484952121db0b36698cb/server.jar"])
versions.append(["1.16.2","https://launcher.mojang.com/v1/objects/c5f6fb23c3876461d46ec380421e42b289789530/server.jar"])

# for version in soup.findAll(True, {"data-version": True}):
#     versions.append([version["data-version"], None])

# versions = versions[:10] # Truncate versions to improve latency.

# for i in range(len(versions)):
#     res = r.get(f"{MCVERSIONS_URL}/download/{versions[i][0]}")
#     soup = BeautifulSoup(res.content, "html5lib")
#     for link in soup.findAll(True, {"download": True}):
#         if "server" in link["download"]:
#             versions[i][1] = link["href"]

with open(defs.MC_AVAILABLE_VERSION_PATH, "w") as f:
    for v in versions:
        f.write(f"{v[0]} {v[1]}\n")

print("Version list updated.")
