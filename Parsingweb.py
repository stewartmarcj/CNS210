#Assignment 2 Parsing a website

from bs4 import BeautifulSoup
import requests
import urllib.request

page = requests.get('http://www.python.org/downloads')

soup = BeautifulSoup(page.text, 'html.parser')

download = soup.find_all("release-date", 'April 6, 2013')


data = {}

print("Begin Download")

urllib.urlretrieve("https://www.python.org/downloads/release/python-274/", "Marc-Python-247")

print("Completed")


