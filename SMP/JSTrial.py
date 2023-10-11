import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# start by defining the options
options = webdriver.ChromeOptions()
# options.add_argument('--headless')
# should be resolved now, can remove
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')

# we don't need it as the page also populated with the running javascript code.
options.page_load_strategy = 'none'

# this returns the path web driver downloaded
chrome_path = ChromeDriverManager().install()
chrome_service = Service(chrome_path)
# pass the defined options and service objects to initialize the web driver
driver = Chrome(options=options, service=chrome_service)
driver.implicitly_wait(3)

url = "https://catalog.smcm.edu/"

driver.get(url)
driver.maximize_window()

time.sleep(2)

# this is the explicit/absolute xpath to the 'programs' button to get to the page with all majors and minors
driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[2]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/p[1]/a[2]/img[1]").click()

time.sleep(2)

# now click on the 'computer science BS'
driver.find_element(By.LINK_TEXT, "Computer Science, BS").click()

time.sleep(2)

# now on the page needed to gather all info after many clicks
#once I click on the thing, I have access to the information I need to store

# for each rel. css selector such that [aria-expanded='false'], click on the link

# driver.find_element(By.CSS_SELECTOR, "*[aria-expanded='false']").click()
"""
clickables = driver.find_elements(*(By.CSS_SELECTOR, "*[aria-expanded='false']"))

for item in clickables:
    #focus the driver on the item
    print(item.text)
 """
# this clicks on the first required class
driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[2]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[2]/div[2]/ul[1]/li[1]/span[1]/a[1]").click()
# this clicks on the second required class
driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[2]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/table[1]/tbody[1]/tr[2]/td[1]/div[1]/div[2]/div[2]/ul[1]/li[2]/span[1]/a[1]").click()

time.sleep(5)
