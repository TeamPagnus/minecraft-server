#!/usr/bin/python
# -*- coding: utf-8 -*-

import cgi
import defs

# Headers
print("Content-Type: text/plain")
print()

import cgitb
cgitb.enable()

# Core.
import os
import sys
import zipfile

def save_uploaded_file():
    form = cgi.FieldStorage()
    if "file" not in form.keys():
        print('Not found parameter: file')
        return

    form_file = form['file']
    if not form_file.file:
        print('Not found parameter: file')
        return

    if not form_file.filename:
        print('Not found parameter: file')
        return

    uploaded_file_path = os.path.join(defs.MC_DIR, os.path.basename(form_file.filename))
    with open(uploaded_file_path, 'wb') as fout:
        while True:
            chunk = form_file.file.read(100000)
            if not chunk:
                break
            fout.write (chunk)
    print("File uploaded.")
    return uploaded_file_path

def unzip_file(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(defs.MC_DIR)
    print("World extracted.")

file_path = save_uploaded_file()
unzip_file(file_path)
