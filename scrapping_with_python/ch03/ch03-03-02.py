from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks = []
    #Finds all links that begin with a "/"
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None and link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    for link in bsObj.findAll("a", href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None and link.attrs['href'] not in externalLinks:
            externalLinks.append(link.attrs['href'])
    return externalLinks

def getRandomExternalLink(startingPage):
    print('>> getRandomExternalLink : ', startingPage)
    try:
        html = urlopen(startingPage)
        bsObj = BeautifulSoup(html, "html.parser")
        externalLinks = getExternalLinks(bsObj, urlparse(startingPage).netloc)
        if len(externalLinks) == 0:
            print("No external links, looking around the site for one")
            domain = urlparse(startingPage).scheme+"://"+urlparse(startingPage).netloc
            internalLinks = getInternalLinks(bsObj, domain)
            return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
        else:
            return externalLinks[random.randint(0, len(externalLinks)-1)]
    except HTTPError as e:
        print(e)
        return externalLinks[random.randint(0, len(externalLinks)-1)]
    except Exception as e:
        print(e)    
        

def followExternalOnly(startingSite):
    print('>> followExternalOnly : ', startingSite)
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: "+externalLink)
    followExternalOnly(externalLink)

allExtLinks = set()
allIntLinks = set()
def getAllExternalLinks(siteUrl):
    try:
        print('siteUrl : ', siteUrl)
        html = urlopen(siteUrl)
        domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
        bsObj = BeautifulSoup(html, "html.parser")
        internalLinks = getInternalLinks(bsObj,domain)
        externalLinks = getExternalLinks(bsObj,domain)

        for link in externalLinks:
            if link not in allExtLinks:
                allExtLinks.add(link)
                print('external : ', link)
        for link in internalLinks:
            if link not in allIntLinks:
                allIntLinks.add(link)
                print('internal : ', link)
                getAllExternalLinks(link)

    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

getAllExternalLinks("http://oreilly.com")