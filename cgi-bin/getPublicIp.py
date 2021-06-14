#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import miniupnpc
from requests import get
import utils

def core(response):
    ip_address = get('https://api.ipify.org').text
    # Alternativa
    # res = get('https://ident.me').text
    ## Alternativa con dependencia (pip install miniupnpc)
    ## No necesita un servicio externo
    # u = miniupnpc.UPnP()
    # u.discoverdelay = 200
    # u.discover()
    # u.selectigd()
    # ip = u.externalipaddress()
    response["ip-address"] = ip_address
    response["success"] = "true"
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "getPublicIp.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
