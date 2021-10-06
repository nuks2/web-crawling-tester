import os
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup



html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, "html.parser")
# downloadList = bsObj.findAll(src=True)
downloadList = bsObj.findAll({src:True})

for download in downloadList:
    print(download["src"])