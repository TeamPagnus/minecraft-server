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
    print("already exists")

# aceptar eula por defecto
print(getoutput(f"echo eula=true > {defs.MC_EULA_PATH}"))

# generar comando
version = getoutput(f"cat {defs.MC_SERVER_VERSION_PATH}")
cmd = f"{JAVA_START} minecraft_server.{version}.jar {JAVA_END} >> out.txt &>> out.txt"

# iniciar servidor de minecraft en la sesion de screen
os.chdir(defs.MC_DIR)
print(getoutput(f"screen -dmS {defs.MC_SCREEN_PROCESS_NAME}"))
run(["screen", "-S",  defs.MC_SCREEN_PROCESS_NAME,  "-X", "stuff", f'{cmd}; exit\n'])

print("Start signal sent")
