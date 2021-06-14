#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import utils

def core(response):
    server_properties = utils.extract_all_data(ARGS)
    utils.set_server_properties(server_properties)
    response["server_properties"] = server_properties
    response["success"] = "true"
    utils.respond_in_json(response)

ARGS = cgi.FieldStorage(keep_blank_values = True)
RESPONSE = dict()
SCRIPT_NAME = "setServerProperties.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
