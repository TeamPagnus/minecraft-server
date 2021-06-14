#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs
import utils

def core(response):
    utils.set_level(level_name)
    response["level-name"] = level_name
    response["success"] = "true"
    utils.respond_in_json(response)

ARGS = cgi.FieldStorage()
RESPONSE = dict()
SCRIPT_NAME = "setLevel.py"

level_name = utils.extract_data(ARGS, "level-name")

if not level_name:
    utils.log_error(RESPONSE, SCRIPT_NAME, defs.W_FIELD_NOT_FOUND)
if '/' in level_name:
    utils.log_error(RESPONSE, SCRIPT_NAME, defs.W_INVALID_FIELD_FORMAT)
else:
    try:
        core(RESPONSE)
    except Exception as e:
        utils.log_exception(RESPONSE, SCRIPT_NAME, e)
