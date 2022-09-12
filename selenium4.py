import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
from time import sleep
import csv


with open('testdata1.csv','r') as csv_file:
    csv_reader=csv.reader(csv_file)

    for line in csv_reader:
        driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        driver.get("https://www.instagram.com/accounts/login/")
        sleep(1)

        username=driver.find_element(By.NAME,"username")
        username.send_keys(line[0])

        passw=driver.find_element(By.NAME,"password")
        passw.send_keys(line[1])

        login=driver.find_element("xpath",'//*[@id="loginForm"]/div/div[3]')
        login.click()
        sleep(3)
        driver.quit()
