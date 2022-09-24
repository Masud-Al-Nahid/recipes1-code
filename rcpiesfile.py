import csv
import requests
from recipe_scrapers import scrape_html
from csv import writer

with open('recipe.csv', 'w', encoding='utf8', newline='') as file:
    thewriter = writer(file)
    header = ['Title', 'Ingredients', 'Instructions', 'Nutrition_Facts', 'image', 'links']
    thewriter.writerow(header)

    with open('data.txt', 'r') as inf:
        for line in inf:
            html = requests.get(line).content
            scraper = scrape_html(html=html, org_url=line)
            thewriter.writerow([scraper.title(), scraper.ingredients(), scraper.instructions(), scraper.nutrients(), scraper.image(), scraper.links()])
