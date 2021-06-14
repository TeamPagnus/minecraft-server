#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
import shutil
import unittest
import ipaddress
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options

class ScreenProcess:

    def __init__(self, processName):
        self.processName = processName
        subprocess.run(["screen", "-dmS", f"{self.processName}"])

    def exec(self, command):
        subprocess.run(["screen", "-S", self.processName, "-X", 'stuff', f'{command}\n'])

    def keyboardInterrupt(self):
        subprocess.run(["screen", "-S", self.processName, "-X", 'stuff', '^C'])

class PythonOrgSearch(unittest.TestCase):
    START_SERVER = True
    HEADLESS_MODE = True

    def setUp(self):
        if self.START_SERVER:
            self.process = ScreenProcess("testing")
            self.process.exec("cd ../;python -m http.server --cgi 8000")
        try:
            shutil.rmtree("../minecraft")
        except FileNotFoundError:
            pass
        os.mkdir("../minecraft")
        options = Options()
        options.headless = self.HEADLESS_MODE
        self.driver = webdriver.Firefox(options=options)

    def test_happy_path(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        self.assertIn("MinecraftServerManager", driver.title)

        w = WebDriverWait(driver, 200)
        e = (By.ID, "public-ip")
        element = w.until(EC.visibility_of_element_located(e))

        # check if it is a valid ip
        ipaddress.ip_address(element.text)

        e = (By.ID, "update-version-links-button")
        element = w.until(EC.presence_of_element_located(e))
        element.click()

        e = (By.CSS_SELECTOR, "#version-links > a:nth-child(3)")
        element = w.until(EC.presence_of_element_located(e))
        element.click()

        e = (By.CSS_SELECTOR, "html body pre") 
        element = w.until(EC.text_to_be_present_in_element(e, "was installed"))

        driver.back()
        driver.refresh()

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        startStopButton = w.until(EC.presence_of_element_located(e))

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Start"))
        startStopButton.click()

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Waiting"))

        e = (By.CSS_SELECTOR, "#console-out") 
        element = w.until(EC.text_to_be_present_in_element(e, "Done"))

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Stop"))
        startStopButton.click()

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Waiting"))

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Start"))

    def tearDown(self):
        self.driver.close()
        if self.START_SERVER:
            self.process.keyboardInterrupt()
            self.process.exec("exit")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        PythonOrgSearch.HEADLESS_MODE = sys.argv.pop() != "false"
    
    if len(sys.argv) > 1:
        PythonOrgSearch.START_SERVER = sys.argv.pop() != "false"
    
    print("START_SERVER", PythonOrgSearch.START_SERVER)
    print("HEADLESS_MODE", PythonOrgSearch.HEADLESS_MODE)
    unittest.main()
