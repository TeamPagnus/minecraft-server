#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

def core(response):
    utils.stop_server()
    response["success"] = "true"
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "stopServer.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
