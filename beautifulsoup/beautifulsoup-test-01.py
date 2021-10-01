from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

html = urlopen("http://www.pythonscraping.com/exercises/exercise1.html")
bsObj = BeautifulSoup(html, "html.parser")
print(bsObj.h1)

# Exception handling
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    try:
        bsObj = BeautifulSoup(html, "html.parser")
        title = bsObj.body.h1
        # title = bsObj.noTag.someTag
    except AttributeError as e:
        print('AttributeError : ', e)
        return None
    return title

title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
# title = getTitle("http://www.pythonscraping.com/exercises/exercise001.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
