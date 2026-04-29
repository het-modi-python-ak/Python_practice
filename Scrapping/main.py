import requests

from bs4 import BeautifulSoup

# Send a GET request to the URL

response = requests.get('https://www.hostinger.com/tutorials/how-to-run-a-python-script-in-linux')
# print(response.text)

# Parse the HTML content using BeautifulSoup

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# Find all elements with a specific tag (e.g. all h2 headings)

titles = soup.find_all('h2')

# Extract text content from each H2 element

all_links = soup.find_all('a')

print('All <a> tag hrefs:')

for link in all_links:

    print(link.get('href'))
    
    
from fastapi import FastAPI

