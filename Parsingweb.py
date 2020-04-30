#Assignment 2 Parsing a website

from bs4 import BeautifulSoup
import requests
import urllib

page = requests.get('http://www.python.org/downloads')

soup = bs4.BeautifulSoup(page.text, 'html.parser')

download = soup.find_all("a", "release-number")

samples[0]

class_="release-number" href="http://python.org/downloads/release/python-247

data = {}

print("Begin Download")

urllib.urlretrieve("https://www.python.org/downloads/release/python-274/", Marc-Python-247)

print("Completed")


