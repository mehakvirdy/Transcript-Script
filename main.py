# import statements
import json
import urllib
from urllib import request
from bs4 import BeautifulSoup

subject_url = "https://digitalcollections.library.miami.edu/digital/api/search/collection/asm0341/searchterm/business%20records%20--%20management!pan%20american%20world%20airways%2C%20inc.!Manuals%20(instructional%20materials)/field/subjec!subjec!genre/mode/exact!exact!exact/conn/and!and!all/maxRecords/100"
subject_html = request.urlopen(subject_url).read()
subject_json = json.loads(subject_html)

items = subject_json['items']

pageIDS = []

for x in items:
    pageIDS.append(int(x['itemId']))

ids = []

for x in pageIDS:
    url = "https://digitalcollections.library.miami.edu/digital/api/collections/asm0341/items/%d/false" %x
    html = request.urlopen(url).read()
    site_json = json.loads(html)

    parent = site_json['parent']
    children = parent['children']

    for y in children:
        ids.append(y['id'])

    file = open("transcript.txt", "a")

    for z in ids:
        URL = "https://digitalcollections.library.miami.edu/digital/api/collections/asm0341/items/%d/false" %z
        newHTML= request.urlopen(URL).read()
        site_page = json.loads(newHTML)

        binary = (site_page['text'].encode('ascii', errors='ignore'))
        file.write(binary.decode())
        file.write("\n\n----------------------------------------------------------------------------------------\n\n")

    file.write("\n\n\n ---------------------------------------------DOCUMENT DIVIDER---------------------------------------------\n\n\n")

    ids = []

file.close()