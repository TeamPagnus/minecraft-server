#!/usr/bin/env python
# -*- coding: utf-8 -*-

# directories
CGI_DIR = "cgi_bin/"
MC_DIR = "minecraft/"

# file names
MC_OUT_LOG_FILENAME = "out.txt"

# full file paths
MC_LOG_PATH = MC_DIR + MC_OUT_LOG_FILENAME
MC_LEVELLESS_PATH = MC_DIR + "levelless-server.properties"
MC_LEVEL_NAME_PATH = MC_DIR + "level-name.properties"
MC_SERVER_PROPERTIES_PATH = MC_DIR + "server.properties"
MC_SERVER_VERSION_PATH = MC_DIR + "server-version"
MC_AVAILABLE_VERSION_PATH = MC_DIR + "available-versions"
MC_EULA_PATH = MC_DIR + "eula.txt"

# variables
MC_SCREEN_PROCESS_NAME = "minecraftServer"

# Errors
W_FIELD_NOT_FOUND = {"code": 0, "description": "field not found"}
W_INVALID_FIELD_FORMAT = {"code": 1, "description": "invalid field format"}
W_INVALID_VERSION = {"code": 2, "description": "invalid server version"}
W_INVALID_FILE = {"code": 3, "description": "upload failed. invalid file"}
I_LEVEL_NOT_FOUND = {"code": 100, "description": "level not found"}
P_EXCEPTION = {"code": 200, "description": "runtime exception"}
