
m bs4 import BeautifulSoup
import requests
import urllib

page = requests.get('http://www.python.org/downloads')

soup = BeautifulSoup(page.text, 'html.parser')

all_versions = soup.select('.download-list-widget .list-row-container li')

for version in all_versions:
    #print(version)
    #print(version.select('.release-date').get_text())
    for i in version.select('.release-date'):
       #print(i.get_text())
       if "April 6, 2013" in i.get_text():
          print(version.select('.release-number')[0].get_text().split(" ")[1])



chosen = raw_input("Please select which version you would like: ")
print(chosen)

#urllib.urlretrieve("https://www.python.org/ftp/python/2.7.4/Python-2.7.4.tar.bz2", "Marc-Python-247")
urllib.urlretrieve("https://www.python.org/ftp/python/" + chosen + "/Python-" + chosen + ".tar.bz2", "Marc-Python" + chosen)

print("Completed")

