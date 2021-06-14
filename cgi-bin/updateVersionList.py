#!/usr/bin/env python
# -*- coding: utf-8 -*-

import utils

def core(response):
    versions = utils.update_downloadable_versions_list()
    response["versions"] = versions
    response["success"] = "true"
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "updateVersionList.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
