import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import unittest
from time import sleep


class testing(unittest.TestCase):
    def test1(self):
        self.driver=webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://www.facebook.com/reg/")
        self.driver.implicitly_wait(10)
        
        # uname=self.driver.find_element(By.NAME,"username").send_keys("kjhguhergh")
        # sleep(5)

        # passw=self.driver.find_element(By.NAME,"password").send_keys("jhdfijhiurgh")
        # sleep(5)

        # log=self.driver.find_element(By.CLASS_NAME,"sqdOP").click()
        # sleep(5)

        search= self.driver.find_element(By.NAME,"firstname")
        search.clear()
        search.send_keys("jhfjghuhru")
        search.send_keys(Keys.RETURN)
        sleep(5)

        lastname=self.driver.find_element(By.NAME,"lastname")
        lastname.send_keys("jfghuhgij")
        lastname.send_keys(Keys.RETURN)
        sleep(2)

        regemail=self.driver.find_element(By.NAME,"reg_email__")
        regemail.send_keys("jrhhyu@#12gmail.com")
        sleep(2)

        newpassword=self.driver.find_element(By.NAME,"reg_passwd__")
        newpassword.send_keys("rfuifuyerruh")
        sleep(2)
        
        
        birth=self.driver.find_element(By.ID,'day')
        drp=self.driver.Select(birth)
        birth.Select_by_index(2)
        


if __name__=="__main__":
    unittest.main()
