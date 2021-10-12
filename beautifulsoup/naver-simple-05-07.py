import urllib.request
import bs4

url = "https://news.naver.com/"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")

headline_news_div = bs_obj.find("div", {"class":"hdline_news"})
headline_article_div = bs_obj.find("ul", {"class":"hdline_article_list"})

headline_news = headline_news_div.findAll("p")
headline_article = headline_article_div.findAll("li")
for news in headline_news:
    print(news.text)

for article in headline_article:
    a_tag = article.find("a", {"class":"lnk_hdline_article"})
    print(a_tag.text.strip())

