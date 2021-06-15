#!/usr/bin/env python
# -*- coding: utf-8 -*-

import base64
import cgi
import defs
import utils

def core(response):
    if utils.server_is_alive():
        command = base64.b64decode(command_encoded).decode('utf-8')
        utils.send_command(command)
    response["success"] = "true"
    utils.respond_in_json(response)

ARGS = cgi.FieldStorage()
RESPONSE = dict()
SCRIPT_NAME = "sendConsoleCommand.py"

command_encoded = utils.extract_data(ARGS, "command")

if not command_encoded:
    utils.log_error(RESPONSE, SCRIPT_NAME, defs.W_FIELD_NOT_FOUND)
else:
    try:
        core(RESPONSE)
    except Exception as e:
        utils.log_exception(RESPONSE, SCRIPT_NAME, e)
