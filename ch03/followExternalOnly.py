from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
from urllib.error import HTTPError


pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None and link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None and link.attrs['href'] not in externalLinks:
            externalLinks.append(link.attrs['href'])
    return externalLinks    

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    try:
        html = urlopen(startingPage)
        bsObj = BeautifulSoup(html, "html.parser")
        externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
        if len(externalLinks) == 0:
            internalLinks = getInternalLinks(startingPage)
            return getRandomExternalLink(internalLinks[random.randint(0, 
                                    len(internalLinks)-1)])
        else:
            return externalLinks[random.randint(0, len(externalLinks)-1)]
    except HTTPError as e:
        print(e)
        return None

def followExternalOnly(startingSite):
    print("startingSite : "+startingSite)

    externalLink = getRandomExternalLink(startingSite)
    if (externalLink is not None):
        print("Random external link is: "+externalLink)
        followExternalOnly(externalLink)
    else:
        print("Random external link is None ")
    
followExternalOnly("http://oreilly.com")