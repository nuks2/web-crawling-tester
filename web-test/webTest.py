from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
from urllib.error import HTTPError
import re


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

def getAllLinks(siteUrl):
    try:
        print('siteUrl : ', siteUrl)
        html = urlopen(siteUrl)
        domain = urlparse(siteUrl).scheme+"://"+urlparse(siteUrl).netloc
        bsObj = BeautifulSoup(html, "html.parser")
        internalLinks = getInternalLinks(bsObj,domain)

        for link in internalLinks:
            print('internal : ', link)

    except HTTPError as e:
        print(e)
    except Exception as e:
        print(e)

getAllLinks("https://comic.naver.com/webtoon/weekday")

# url = "https://www.google.com/search?q=%EB%84%A4%EC%9D%B4%EB%B2%84%EC%9B%B9%ED%88%B0&oq=%EB%84%A4%EC%9D%B4%EB%B2%84%EC%9B%B9&aqs=chrome.1.69i57j0i131i433i512j0i512l8.4766j1j4&sourceid=chrome&ie=UTF-8"
# response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
# print(response.text)