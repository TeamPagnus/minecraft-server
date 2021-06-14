#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from os import walk
from subprocess import getoutput, run
import defs
import json
import os
import requests
import shutil

def respond_in_json(payload):
    print("Content-Type: application/json")
    print()
    print(json.dumps(payload))

def extract_version_from_filename(filename):
    return '.'.join(filename.split('.')[1:-1])

def get_selected_version():
    versions = get_installed_versions()
    try:
        with open(defs.MC_SERVER_VERSION_PATH, "r") as f:
            version = next(f).strip()
    except Exception:
        version = None
    if version not in versions:
        version = None
    return version

def get_downloadable_versions():
    versions = []
    try:
        with open(defs.MC_AVAILABLE_VERSION_PATH, 'r') as f:
            versions_raw = f.read().split('\n')
    except Exception:
        versions = []
    for v in versions_raw:
        try:
            split = v.split(' ')
        except Exception:
            pass
        try:
            versions.append({"version": split[0], "download-url": split[1]})
        except Exception:
            pass
    return versions

def get_installed_versions():
    try:
        files = next(walk(defs.MC_DIR))[-1]
    except Exception:
        return []
    else:
        versions = []
        for f in files:
            if "minecraft_server" not in f:
                continue
            versions.append(extract_version_from_filename(f))
        return versions

def generate_server_properties():
    server_properties = ""
    try:
        with open(defs.MC_LEVELLESS_PATH, 'r') as f:
            for l in f:
                server_properties += l
    except Exception:
        pass

    try:
        with open(defs.MC_LEVEL_NAME_PATH, 'r') as f:
            for l in f:
                server_properties += l
    except Exception:
        pass

    with open(defs.MC_SERVER_PROPERTIES_PATH, 'w') as f:
        f.write(server_properties)

def download_file(url, filename):
    local_filename = filename
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192): 
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                # if chunk: 
                f.write(chunk)
    return local_filename

def fetch_version_url(version):
    with open(defs.MC_AVAILABLE_VERSION_PATH, 'r') as f:
        for l in f:
            data = l.split(' ')
            if data[0] == version:
                return data[1].strip()
    return None

def version_is_installed(version):
    files = next(walk(defs.MC_DIR))[-1]
    if f"minecraft_server.{version}.jar" in files:
        return True
    return False

def save_uploaded_file(args, directory):
    form = args
    if "file" not in form.keys():
        return None

    form_file = form['file']
    if not form_file.file:
        return None

    if not form_file.filename:
        return None

    uploaded_file_path = os.path.join(directory, os.path.basename(form_file.filename))
    with open(uploaded_file_path, 'wb') as fout:
        while True:
            chunk = form_file.file.read(100000)
            if not chunk:
                break
            fout.write (chunk)
    return uploaded_file_path

def server_is_alive():
    return defs.MC_SCREEN_PROCESS_NAME in getoutput("screen -ls")

def get_server_status():
    lastLog = getoutput(f"tail -n40 {defs.MC_LOG_PATH}")
    """
    Hay 3 estados posibles:
    Started, Stopped, Waiting
    """
    # Stopped
    if not defs.MC_SCREEN_PROCESS_NAME in getoutput("screen -ls"):
        return "stopped"

    # Waiting
    if "Stopping the server" in lastLog:
        return "waiting"

    # Started & Waiting
    if "Preparing spawn area" in lastLog:
        if "Done" in lastLog:
            return "started"
        else:
            return "waiting"

    # Default started, the server has a lot of log
    return "started"

def send_command(command):
    getoutput(f"screen -S {defs.MC_SCREEN_PROCESS_NAME} -X stuff '{command}\n'")

def get_current_level():
    try:
        with open(defs.MC_LEVEL_NAME_PATH, 'r') as f:
            level = f.read().strip()
    except Exception:
        level = "level-name=world"
    level = '='.join(level.split('=')[1:])
    return level

def get_levels():
    EXCEPTION = ["logs"]

    try:
        levels = next(walk(defs.MC_DIR))[1]
    except Exception:
        levels = []

    for f in EXCEPTION:
        try:
            levels.remove(f)
        except Exception:
            pass

    return levels

def zip_level(level):
    shutil.make_archive(defs.MC_DIR + f"{level}.zip", 'zip', defs.MC_DIR + level)
    url = f"/{defs.MC_DIR + level}.zip"
    return url

def unzip_file(file_path):
    with zipfile.ZipFile(file_path, 'r') as zip_ref:
        zip_ref.extractall(defs.MC_DIR)

def delete_level(level_name):
    shutil.rmtree(defs.MC_DIR + level_name)

def extract_data(args, key):
    try:
        result = args[key].value
    except Exception:
        result = None
    return result

def log_error(response, caller, error):
    response["error"] = error
    response["error"]["caller"] = caller
    respond_in_json(response)

def set_version(version):
    downloadable_versions = get_downloadable_versions()
    valid = False
    for v in downloadable_versions:
        if version == v["version"]:
            valid = True
            break
    if not valid:
        return False
    if not version_is_installed(version):
        download_file(
            fetch_version_url(version),
            defs.MC_DIR + f"minecraft_server.{version}.jar"
        )
    with open(defs.MC_SERVER_VERSION_PATH, 'w') as f:
        f.write(version)
    return True

def log_exception(response, caller, exception):
    response["error"] = defs.P_EXCEPTION
    response["error"]["caller"] = caller
    response["error"]["exception"] = str(exception)
    respond_in_json(response)

def set_level(level_name):
    level_name = f"level-name={level_name}"
    with open(defs.MC_LEVEL_NAME_PATH, 'w') as f:
        f.write(level_name)
    generate_server_properties()

def extract_all_data(args):
    data = {}
    for k in args.keys():
        data[k] = args[k].value
    return data

def set_server_properties(payload):
    server_properties = ""
    for k in payload.keys():
        server_properties += f"{k}={payload[k]}\n"
    with open(defs.MC_LEVELLESS_PATH, 'w') as f:
        f.write(server_properties)
    generate_server_properties()

def get_server_properties():
    server_properties = {}
    with open(defs.MC_SERVER_PROPERTIES_PATH, 'r') as f:
        server_properties_raw = f.read().split('\n')
    for prop in server_properties_raw:
        try:
            split = prop.split("=")
        except Exception:
            pass
        try:
            server_properties[split[0]] = split[1]
        except Exception:
            pass
    return server_properties

def start_server():
    if server_is_alive():
        return
    with open(defs.MC_EULA_PATH, 'w') as f:
        f.write("eula=true")
    version = get_selected_version()
    JAVA_START = "java -Xmx1024M -Xms1024M -jar"
    JAVA_END =  "nogui"
    command = f"{JAVA_START} minecraft_server.{version}.jar {JAVA_END} >> {defs.MC_OUT_LOG_FILENAME} &>> {defs.MC_OUT_LOG_FILENAME}"
    os.chdir(defs.MC_DIR)
    getoutput(f"screen -dmS {defs.MC_SCREEN_PROCESS_NAME}")
    run(["screen", "-S",  defs.MC_SCREEN_PROCESS_NAME,  "-X", "stuff", f'{cmd}; exit\n'])
    return

def stop_server():
    if not server_is_alive():
        return
    run(["screen", "-S", defs.MC_SCREEN_PROCESS_NAME, "-X", "stuff", "stop\n"])

def update_downloadable_versions_list():
    MCVERSIONS_URL = "https://mcversions.net/"

    res = requests.get(MCVERSIONS_URL)
    soup = BeautifulSoup(res.content, "html5lib")

    versions = []
    for version in soup.findAll(True, {"data-version": True}):
        versions.append([version["data-version"], None])

    versions = versions[:10] # Truncate versions to improve latency.

    for i in range(len(versions)):
        res = requests.get(f"{MCVERSIONS_URL}/download/{versions[i][0]}")
        soup = BeautifulSoup(res.content, "html5lib")
        for link in soup.findAll(True, {"download": True}):
            if "server" in link["download"]:
                versions[i][1] = link["href"]

    with open(defs.MC_AVAILABLE_VERSION_PATH, "w") as f:
        for v in versions:
            f.write(f"{v[0]} {v[1]}\n")

    return versions

