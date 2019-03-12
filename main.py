#  necessary to scrape the website
import requests
from bs4 import BeautifulSoup

# hardcoded for now, finds all the medical fundraisers in gofundme
url = 'https://www.gofundme.com/discover/medical-fundraiser'

# gets the html of the provided website
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html.parser')
tiles = soup.select(".js-fund-tile")

for tile in tiles:
  location = str.strip(tile.select_one(".fund-location").get_text())
  title = str.strip(tile.select_one(".fund-title").get_text())
  tile_items = tile.select(".fund-item .show-for-medium")

  # get width for this
  progress_bar = str.strip(tile.select_one(".progress-bar.progress-bar-fill")["style"])

  # hacky way to get raised for now, there's no specific class for the amt
  for tile_item in tile_items:
    if "raised" in tile_item.get_text():
       raised = str.strip(tile_item.get_text())

  print(title,location,raised,progress_bar,"\n\n")
