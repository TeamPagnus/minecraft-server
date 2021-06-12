#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Escribir Scripts de acá para abajo.

JAVA_START = "java -Xmx1024M -Xms1024M -jar"
JAVA_END =  "nogui"
LOG_OUTPUT = "out.txt"
MINECRAFT_DIR = "minecraft/"
VERSION_FILE = "server_version"

import os
from subprocess import getoutput, run

# cambiar workdir a minecraft
os.chdir(MINECRAFT_DIR)

# si esta iniciado el server, salir
if "minecraftServer" in getoutput("screen -ls"):
    exit()

# aceptar eula por defecto
getoutput("echo eula=true > eula.txt")

# iniciar sesion screen
getoutput("screen -dmS minecraftServer")

# generar comando
version = getoutput(f"cat {VERSION_FILE}")
cmd = f"{JAVA_START} minecraft_server.{version}.jar {JAVA_END} >> {LOG_OUTPUT}"

# iniciar servidor de minecraft en la sesion de screen
run(["screen", "-S",  "minecraftServer",  "-X", "stuff", f'{cmd}; exit\n'])

print("Start signal sent")