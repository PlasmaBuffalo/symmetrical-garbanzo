import time

from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# start by defining the options
options = webdriver.ChromeOptions()
# we run this headless normally, but this is commented out for debugging purposes
# options.add_argument('--headless')

# certificate errors should be resolved now, leaving here just in case
# options.add_argument('--ignore-certificate-errors')
# options.add_argument('--ignore-ssl-errors')

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

# now click on the 'computer science BS' link to go to the major page
driver.find_element(By.LINK_TEXT, "Computer Science, BS").click()

time.sleep(2)

# now we're on the page needed to gather all course info after many clicks
# now we need to click on each course's dropdown to reveal all the information we need to scrape and store

# get all links with the aria-expanded attribute set to false
links = driver.find_elements(By.CSS_SELECTOR, "[aria-expanded='false']")

# iterate over the links and click on them if they are visible
for link in links:
    if link.is_displayed():
        link.click()

# now that everything is dropped down, we can scrape all data from the site


# Get the HTML of the current page
html = driver.page_source

# Print the HTML to the console (Debug)
# print(html)

# this writes the current HTML as a new document we can now work with and parse
with open("page.html", "w") as f:
    f.write(html)



time.sleep(30)
