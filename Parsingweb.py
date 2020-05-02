#Assignment 2 Parsing a website

from bs4 import BeautifulSoup
import requests
import urllib

page = requests.get('http://www.python.org/downloads')

soup = BeautifulSoup(page.text, 'html.parser')

all_versions = soup.select('.download-list-widget .list-row-container li')

for version in all_versions:
    print(version)



data = {}

print("Begin Download")

urllib.urlretrieve(" https://www.python.org/ftp/python/274/python-274.amd64.msi", "Marc-Python-247")

print("Completed")


