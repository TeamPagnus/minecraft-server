#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

def core(response):
    server_properties = utils.get_server_properties()
    response["server-properties"] = server_properties
    response["success"] = "true"
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "getServerProperties.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
