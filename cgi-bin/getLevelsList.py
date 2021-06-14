#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

def core(response):
    levels = []
    for l in LEVELS:
        levels.append({"level-name": l})
    response["levels"] = levels
    response["success"] = "true"
    utils.respond_in_json(response)

LEVELS = utils.get_levels()
RESPONSE = dict()
SCRIPT_NAME = "getLevelsList.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
