#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import datetime

# Headers
a = 5
print("Content-Type: text/plain")
print()

# Contenido (texto plano, como lo hemos especificado)
print("""Hola mundo!""", datetime.datetime.now())
