#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

def core(response):
    level = utils.get_current_level()
    response["level-name"] = level
    response["success"] = "true"
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "getCurrentLevel.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
