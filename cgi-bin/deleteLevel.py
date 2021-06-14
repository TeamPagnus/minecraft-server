#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs
import utils

def core(response):
    utils.delete_level(level_name)
    response["success"] = "true"
    utils.respond_in_json(response)

ARGS = cgi.FieldStorage()
LEVELS = utils.get_levels()
RESPONSE = dict()
SCRIPT_NAME = "deleteLevel.py"

level_name = utils.extract_data(ARGS, "level-name")

if not level_name:
    utils.log_error(RESPONSE, SCRIPT_NAME, defs.W_FIELD_NOT_FOUND)
elif level_name not in LEVELS:
    utils.log_error(RESPONSE, SCRIPT_NAME, defs.I_LEVEL_NOT_FOUND)
else:
    try:
        core(RESPONSE)
    except Exception as e:
        utils.log_exception(RESPONSE, SCRIPT_NAME, e)
