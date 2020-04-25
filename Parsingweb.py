#Assignment 2 Parsing a website

from bs4 import BeautifulSoup
import requests
import urllib

page = requests.get('http://www.python.org/downloads')

soup = bs4.BeautifulSoup(page.text, 'html.parser')

soup.select('div.row:nth-child(2) > ol:nth-child(4) > li:nth-child(67) > span:nth-child(1) > a:nth-child(1)')

print("Begin Download")

urllib.urlretrieve("https://www.python.org/downloads/release/python-274/", Marc-Python-247)

print("Completed")


