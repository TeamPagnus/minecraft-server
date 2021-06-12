#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Escribir Scripts de acá para abajo.

from requests import get
print(get('https://api.ipify.org').text)

# Alternativa
# from requests import get
# print(get('https://ident.me').text)


## Alternativa con dependencia (pip install miniupnpc)
## No necesita un servicio externo
# import miniupnpc
# u = miniupnpc.UPnP()
# u.discoverdelay = 200
# u.discover()
# u.selectigd()
# print(u.externalipaddress())
