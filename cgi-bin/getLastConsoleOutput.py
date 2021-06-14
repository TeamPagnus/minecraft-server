#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import getoutput
import defs
import utils

def core(response):
    console_output = getoutput(f"tail -n40 {defs.MC_LOG_PATH}")
    response["success"] = "true"
    response["console-output"] = console_output
    utils.respond_in_json(response)

RESPONSE = dict()
SCRIPT_NAME = "getLastConsoleOutput.py"

try:
    core(RESPONSE)
except Exception as e:
    utils.log_exception(RESPONSE, SCRIPT_NAME, e)
