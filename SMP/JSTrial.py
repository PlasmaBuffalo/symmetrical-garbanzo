import time

import pandas
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# start by defining the options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'
# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(5)

url = "https://catalog.smcm.edu/"

driver.get(url)
time.sleep(3)

driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[2]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/p[1]/a[2]/img[1]").click()

time.sleep(3)

#once I click on the thing, I have access to the information I need to store
