#  necessary to scrape the website
import requests
from bs4 import BeautifulSoup

# hardcoded for now, finds all the medical fundraisers in gofundme
url = 'https://www.gofundme.com/discover/medical-fundraiser'

# gets the html of the provided website
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
print(soup.prettify())

