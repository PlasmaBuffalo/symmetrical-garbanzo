#Schedule maker web scraper version 1: hardcoded to the right website
# needs to create a JSON with all classes required for the major provided

# this is the page containing all smcm majors and minors
base_url = "http://catalog.smcm.edu/"

from bs4 import BeautifulSoup as bs
import requests


response = requests.get(base_url)
text = response.content

soup_page = bs(text, "html.parser")

"""
print(soup_page.find_all(class_="entry catalog"))
#h1 = "Degree requirements for x major"

textBlocks = soup_page.article.get_text(strip=True, separator='\n').splitlines() # type:ignore
 """