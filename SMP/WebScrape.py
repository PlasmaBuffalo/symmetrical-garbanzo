#Schedule maker web scraper version 1: hardcoded to the right website
# needs to create a JSON or something with all classes required for the major provided


from bs4 import BeautifulSoup as bs
import requests


# this is the page containing all smcm majors and minors
# base_url = "http://catalog.smcm.edu/"
base_url = "https://catalog.smcm.edu/content.php?catoid=2&navoid=47"

# get page response
response = requests.get(base_url)
text = response.content

tags = ["Major", "Minor", "BA", "BS"]
links = []

#if the
soup_page = bs(text, "html.parser")
for link in soup_page.find_all('a'):
    for kwd in tags:
        if link.text.find(kwd) != -1:
            links.append(link)

for item in links:
    print(item)

"""
print(soup_page.find_all(class_="entry catalog"))
#h1 = "Degree requirements for x major"

textBlocks = soup_page.article.get_text(strip=True, separator='\n').splitlines() # type:ignore
 """