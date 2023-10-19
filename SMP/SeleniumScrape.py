import time

from bs4 import BeautifulSoup as bs
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

force_scrape = 0

# if page.html does not exist or force_scrape == 1, then this method will scrape new data
if (not os.path.exists("SMP/page.html") or force_scrape == 1):

    # start by defining the options
    options = webdriver.ChromeOptions()

    # we run this headless normally, but this is commented out for debugging purposes
    options.add_argument('--headless')

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
    # just for debugging
    # driver.maximize_window()

    time.sleep(1)

    # this is the explicit/absolute xpath to the 'programs' button to get to the page with all majors and minors
    driver.find_element(By.XPATH, "/html[1]/body[1]/table[1]/tbody[1]/tr[3]/td[2]/table[1]/tbody[1]/tr[2]/td[2]/table[1]/tbody[1]/tr[1]/td[1]/p[1]/a[2]/img[1]").click()

    time.sleep(1)

    # now click on the 'computer science BS' link to go to the major page
    driver.find_element(By.LINK_TEXT, "Computer Science, BS").click()

    time.sleep(1)

    # now we're on the page needed to gather all course info after many clicks
    # now we need to click on each course's dropdown to reveal all the information we need to scrape and store

    # get all links with the aria-expanded attribute set to false
    links = driver.find_elements(By.CSS_SELECTOR, "[aria-expanded='false']")

    # iterate over the links and click on them if they are visible
    for link in links:
        time.sleep(0.1)
        if link.is_displayed():
            link.click()

    # now that everything is dropped down, we can scrape all data from the site
    # Get the HTML of the current page
    html = driver.page_source

    # Print the HTML to the console (Debug)
    # print(html)

    # this writes the current HTML as a new document we can now work with and parse
    with open("SMP/page.html", "w", encoding="utf-8") as f:
        f.write(html)
# end web scrape method

# now we switch over to BeautifulSoup to parse our webpage which contains the info we need

# open the file and create a BS4 object with it
page_as_io = open("SMP/page.html", "r", encoding="utf-8")

# this converts the open file into a single string variable
page_as_str = page_as_io.read()

# turning the downloaded file into a BS4 object, parsed as HTML
page_as_soup = bs(page_as_str, "html.parser")

# now find text specifically from the list items we dropped down with Selenium (all class details)
# pattern matches:
# class="program_description"
# class="acalog-core"
garbage = "Add to Saved Course (opens a new window) Add to My Favorites (opens a new window) Share this Page Facebook this Page (opens a new window) Tweet this Page (opens a new window) Print (opens a new window)"

# writes all the class data neatly into a text file
with open("SMP/classText.html", "w", encoding="utf-8") as f:
    for item in page_as_soup.find_all("li", "acalog-course"):
        bigString:str = ''
        textBlocks: list[str] = item.get_text(strip=True, separator=' ').splitlines()
        for block in textBlocks:
            print(block + "\n\n")
            bigString += ' ' + block
        bigString = bigString.replace("\t","").replace(garbage,"")
        f.write(bigString + "\n")
    f.write("\n\n\n")


        # f.write(item.text.strip().replace("\t",""))
        # f.write("\n\n\n")
# textBlocks = thisArticle.article.get_text(strip=True, separator='\n').splitlines()
# write needed data into a CSV file in this same folder containing organized relevant course data