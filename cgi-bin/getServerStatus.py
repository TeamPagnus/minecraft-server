#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import getoutput
import utils

def core(response):
    server_status = utils.get_server_status()
    response["server-status"] = server_status
    response["success"] = "true"
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "getServerStatus.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
