#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Content
args = cgi.FieldStorage()   # Stores GET and POST storage into a FieldStorage.
                            # It works similar to a dictionary.
for i in args.keys():
    print(i, args[i].value) # args[i] is type MiniFieldStorage. Use value property to access it.
