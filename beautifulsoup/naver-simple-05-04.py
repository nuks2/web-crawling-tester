import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")

top_right = bs_obj.find("a", {"class":"link_set"})
print(top_right)
print("--------------------------------------")

print(top_right.text)
print("--------------------------------------")