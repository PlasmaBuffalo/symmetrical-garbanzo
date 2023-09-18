#Schedule maker web scraper version 1: hardcoded to the right website
# needs to create a JSON with all classes required for the major provided

# this is the page containing all smcm majors and minors
base_url = "https://www.smcm.edu/academics/majors-minors-concentrations/"

#this link is specifically a hardcoded link to the CS Major requirements page
specific = "https://www.smcm.edu/mathcs/academic-offerings/what-you-learn-cs/requirements/#option1"

from bs4 import BeautifulSoup as bs
import requests


response = requests.get(specific)
text = response.content

soup_page = bs(text, "html.parser")

print(soup_page.find_all(class_="entry catalog"))
#h1 = "Degree requirements for x major"

textBlocks = soup_page.article.get_text(strip=True, separator='\n').splitlines() # type:ignore
