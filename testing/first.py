#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import time
import shutil
import unittest
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ScreenProcess:

    def __init__(self, processName):
        self.processName = processName
        subprocess.run(["screen", "-dmS", f"{self.processName}"])

    def exec(self, command):
        subprocess.run(["screen", "-S", self.processName, "-X", 'stuff', f'{command}\n'])

    def keyboardInterrupt(self):
        subprocess.run(["screen", "-S", self.processName, "-X", 'stuff', '^C'])

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.process = ScreenProcess("testing")
        self.process.exec("cd ../;python -m http.server --cgi 8000")
        try:
            shutil.rmtree("../minecraft")
        except FileNotFoundError:
            pass
        os.mkdir("../minecraft")
        self.driver = webdriver.Firefox()

    def test_happy_path(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        self.assertIn("MinecraftServerManager", driver.title)
        ## wait for update-version-links-button
        e = (By.ID, "update-version-links-button")
        w = WebDriverWait(driver, 10)
        element = w.until(EC.presence_of_element_located(e))
        #press it
        element.click()

        ## wait for version-links tenga algun link adentro
        e = (By.CSS_SELECTOR, "#version-links > a:nth-child(3)")
        element = w.until(EC.presence_of_element_located(e))
        element.click()
        
        # buscar y presionar 1.16.5
        ## wait hasta que cambie de pagina
        e = (By.CSS_SELECTOR, "html body pre") 
        element = w.until(EC.text_to_be_present_in_element(e, "was installed"))
        # volver atras y refrescar
        driver.back()
        driver.refresh()

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        startStopButton = w.until(EC.presence_of_element_located(e))

        ## comprobar que el boton start-stop-button sea "Start"
        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Start"))
        startStopButton.click()

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Waiting"))

        longWait = WebDriverWait(driver, 100)

        e = (By.CSS_SELECTOR, "#console-out") 
        element = longWait.until(EC.text_to_be_present_in_element(e, "Done"))

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Stop"))
        startStopButton.click()

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Waiting"))

        e = (By.CSS_SELECTOR, "button#start-stop-button") 
        element = w.until(EC.text_to_be_present_in_element(e, "Start"))

    def tearDown(self):
        self.driver.close()
        self.process.keyboardInterrupt()
        self.process.exec("exit")

if __name__ == "__main__":
    unittest.main()
