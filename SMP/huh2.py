import requests
from bs4 import BeautifulSoup
import json

def get_class_codes(url):
  """Scrapes the website at the given URL and extracts the class codes.

  Args:
    url: The URL of the website to scrape.

  Returns:
    A list of class codes, where each class code is a string in the format
    `ABCD123`.
  """

  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')

  degree_text = soup.find(class_='entry catalog')

  class_codes = []
  for li_element in soup.find_all('li', class_='entry catalog'):
    code = li_element.text
    class_codes.append(code)

  return class_codes

def create_json_entry(class_code):
  """Creates a JSON entry for a class code.

  Args:
    class_code: The class code, in the format `ABCD123`.

  Returns:
    A JSON entry for the class code, in the following format:
    {
      "code": "ABCD123"
    }
  """

  return {
    "code": class_code
  }

# Get the class codes from the website.
class_codes = get_class_codes('https://www.smcm.edu/mathcs/academic-offerings/what-you-learn-cs/requirements/#option1')

# Create a list of JSON entries for the class codes.
json_entries = []
for class_code in class_codes:
  json_entry = create_json_entry(class_code)
  json_entries.append(json_entry)

# Write the JSON entries to a file.
with open('class_codes.json', 'w') as f:
  json.dump(json_entries, f, indent=4)