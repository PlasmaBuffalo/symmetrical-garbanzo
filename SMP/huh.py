import requests
from bs4 import BeautifulSoup
import json

def get_classes(url):
  """Scrapes the website at the given URL and extracts the classes.

  Args:
    url: The URL of the website to scrape.

  Returns:
    A list of classes, where each class is represented by a dictionary containing
    the following keys:
      - name: The name of the class.
      - code: The code of the class.
      - credits: The number of credits for the class.
  """

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  classes = []
  for class_element in soup.find_all('div', class_='course-block'):
    name = class_element.find('h3').text
    code = class_element.find('div', class_='course-code').text
    credits = class_element.find('div', class_='course-credits').text

    classes.append({
      'name': name,
      'code': code,
      'credits': credits
    })

  return classes

# Get the classes from the SMCM website.
classes = get_classes('https://www.smcm.edu/mathcs/academic-offerings/what-you-learn-cs/requirements/#option1')

# Write the classes to a JSON file.
with open('classes.json', 'w') as f:
  json.dump(classes, f, indent=4)