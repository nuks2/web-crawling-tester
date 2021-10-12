from urllib.request import urlopen

robotsTxt = urlopen("https://www.avdbs.com/robots.txt")
print(robotsTxt.read())