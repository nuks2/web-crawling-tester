from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import string

def cleanInput(input):
    input = re.sub('\n+', " ", input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', " ", input)
    input = bytes(input, "UTF-8")
    input = input.decode("ascii", "ignore")
    cleanInput = []
    input = input.split(' ')
    for item in input:
        print('previous item : ', item)
        item = item.strip(string.punctuation)
        print('after item : ', item)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input)-n+1):
        newNGram = " ".join(input[i:i+n])
        if newNGram in output:
            output[newNGram] += 1
        else:
            output[newNGram] = 1
    return output

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, "html.parser")
content = bsObj.find("div", {"id":"mw-content-text"}).get_text()

ngrams = getNgrams(content, 2)
# print(ngrams)