import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
PATH="C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)

driver.get("https://www.python.org")
assert "Python" in driver.title
elem = driver.find_element(By.NAME,"q")
elem.clear()
elem.send_keys("@122344")
elem.send_keys(Keys.RETURN)
assert "Not found." not in driver.page_source
# driver.close()
