import time

from bs4 import BeautifulSoup as bs
import os
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

force_scrape = False

# if page.html does not exist or force_scrape == 1, then this method will scrape new data
if (not os.path.exists("SMP/page.html") or force_scrape):
    print("Gathering course data")
    # start by defining the options
    options = webdriver.ChromeOptions()

    # we run this headless normally, but this is available for debugging purposes
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
print("Course data gathering complete")

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
# <table class="td_dark">
# NOT <div class="gateway-toolbar gateway-mini-toolbar clearfix">

# this will keep track of the course codes we have already written
code_list = []

# function to filter out gateway-toolbar class
# def not_gateway_elements(tag):
#     return tag.has_attr('class') and not tag.has_attr('id')

# method function: takes the webpage html ("page.html")
# and outputs class listings into a text file ("classText.html")
with open("SMP/classText.txt", "w", encoding="utf-8") as f:
    # for each list item which fits the description of a course item

    for item in page_as_soup.find_all("li", "acalog-course"):
        bigString:str = ''
        textBlocks: list[str] = item.get_text(strip=True, separator=' ').splitlines()

        # here, we take tne entire course line and remove the share button interactions
        for block in textBlocks:
            # step 1: take the course code matching (ABCD 123)
            course_code = block[0:8]
            # check if the course has already been read in
            # if this is a new course
            if (course_code not in code_list):
                # step 1.5: add the course code to the list of already added courses
                code_list.append(course_code)
                # step 2: find the second occurrence of the course code
                second_code = block.find(course_code, 8)
                # step 3: remove all redundant text before the second course code
                block = block[second_code:]
                # step 4: add the course info to the class list
                bigString += '\n' + block
            # this marks where already added courses get discarded.

        # finally, we remove all unnecessary tabs
        bigString = bigString.replace("\t","")

        # make a space between each course listing for readability
        f.write(bigString)
    f.close()

# next step: create a dict per line organizing course information

# start with proof of concept for our first class

course_list = []

# for each line in classText.txt, check if line is valid and create a dict for it

for line in open("SMP/classText.txt", "r", encoding="utf-8"):
    # if the line is valid (contains a course code)
    if (line[0:8] in code_list):
        # create a dict for the course
        course_dict = {}

        # add the course code to the dict, first 8 characters
        course_dict["code"] = line[0:8]

        # add the course name to the dict, from end of code to "Credit"
        course_dict["name"] = line[9:line.find("Credit") - 1]

        # add the course credits to the dict, from beginning of "Credit" to "Frequency"
        course_dict["credit_hours"] = line[line.find("Credit"):line.find("Frequency")]

        # add the course frequency to the dict, from beginning of "Frequency" to end of "semester"
        course_dict["frequency"] = line[line.find("Frequency") + 11:line.find("semester")+8]

        # using this to bound the course description
        desc_end = -1

        # if course satisfies exists, course description ends at "Course Satisfies"
        if line.find("Course Satisfies") != -1:
            # putting bounds on the description
            desc_end = line.find("Course Satisfies")
            course_dict["satisfies"] = line[line.find("Course Satisfies"):line.find(".",desc_end)]

        # if prerequisites exist, course description ends at "Course Satisfies"
        if line.find("Prerequisite(s):") != -1:
            # check bounds on description again.
            if desc_end != -1:
                desc_end = line.find("Prerequisite(s):")

            # then add the prerequisites to the dict
            course_dict["prerequisites"] = line[line.find("Prerequisite(s):")+17:line.find("Prerequisite(s):")]

        #add the course description to the dict
        course_dict["description"] = line[line.find("semester")+9:desc_end]

        # add the course dict to the course list
        course_list.append(course_dict)

print(course_list[0])