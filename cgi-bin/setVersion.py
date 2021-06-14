#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs
import utils

def core(response):
    if not utils.set_version(version):
        utils.log_error(RESPONSE, SCRIPT_NAME, defs.W_INVALID_VERSION)
        return
    response["version"] = version
    response["success"] = "true"
    utils.respond_in_json(response)

ARGS = cgi.FieldStorage()
RESPONSE = dict()
SCRIPT_NAME = "setVersion.py"

version = utils.extract_data(ARGS, "version")
if not version:
    utils.log_error(RESPONSE, SCRIPT_NAME, defs.W_FIELD_NOT_FOUND)
else:
    try:
        core(RESPONSE)
    except Exception as e:
        utils.log_exception(RESPONSE, SCRIPT_NAME, e)
