#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Escribir Scripts de acá para abajo.

JAVA_START = "java -Xmx1024M -Xms1024M -jar"
JAVA_END =  "nogui"

import os
from subprocess import getoutput, run

# si esta iniciado el server, salir
if defs.MC_SCREEN_PROCESS_NAME in getoutput("screen -ls"):
    exit()

# aceptar eula por defecto
getoutput(f"echo eula=true > {defs.MC_EULA_PATH}")

# iniciar sesion screen
getoutput(f"screen -dmS {defs.MC_SCREEN_PROCESS_NAME}")

# generar comando
version = getoutput(f"cat {defs.MC_SERVER_VERSION_PATH}")
cmd = f"{JAVA_START} minecraft_server.{version}.jar {JAVA_END} >> {defs.MC_LOG_PATH}"

# iniciar servidor de minecraft en la sesion de screen
run(["screen", "-S",  defs.MC_SCREEN_PROCESS_NAME,  "-X", "stuff", f'{cmd}; exit\n'])

print("Start signal sent")