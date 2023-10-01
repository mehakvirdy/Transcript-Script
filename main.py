# import statements
import json
import urllib
from urllib import request
from bs4 import BeautifulSoup

# variable that stores url of initial document
url = "https://digitalcollections.library.miami.edu/digital/api/collections/asm0341/items/110210/false"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')
site_json = json.loads(soup.text)

parent = site_json['parent']
children = parent['children']

ids = []

for x in children:
    ids.append(x['id'])

file = open("transcript.txt", "x")
file.close()

file = open("transcript.txt", "w")

for x in ids:
    URL = "https://digitalcollections.library.miami.edu/digital/api/collections/asm0341/items/%d/false" %x
    newHTML = request.urlopen(URL).read()
    newSoup = BeautifulSoup(newHTML, 'html.parser')
    site_page = json.loads(newSoup.text)

    file.write(site_page['text'])
    file.write("\n\n----------------------------------------------------------------------------------------\n\n")

file.close()