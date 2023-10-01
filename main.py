# import statements
import json
import urllib
from urllib import request
from bs4 import BeautifulSoup

# stores url of whole subject
subject_url = ("https://digitalcollections.library.miami.edu/digital/collection/asm0341/search/searchterm/business%20re"
               "cords%20--%20management!pan%20american%20world%20airways%2C%20inc.!Manuals%20(instructional%20materials"
               ")/field/subjec!subjec!genre/mode/exact!exact!exact/conn/and!and!all")
subject_html = request.urlopen(subject_url).json()
subject_json = json.loads(subject_html)

print(subject_json)


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