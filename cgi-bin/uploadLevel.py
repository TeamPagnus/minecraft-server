#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils
import defs
import cgi

def core(response):
    file_path = utils.save_uploaded_file(ARGS, defs.MC_DIR)
    if not file_path:
        utils.log_error(RESPONSE, SCRIPT_NAME, defs.W_INVALID_FILE)
        return
    utils.unzip_file(file_path)
    response["success"] = "true"
    utils.respond_in_json(response)

ARGS = cgi.FieldStorage()
RESPONSE = dict()
SCRIPT_NAME = "uploadLevel.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
