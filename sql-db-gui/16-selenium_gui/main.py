from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config import *

service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=service)
driver.get(URL)

input("Press Enter to close the browser...")
driver.quit()


