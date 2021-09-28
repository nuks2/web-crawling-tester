import urllib.request
import bs4

url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
bs_obj = bs4.BeautifulSoup(html, "html.parser")

ul = bs_obj.find("ul", {"class":"list_nav type_fix"})
lis = ul.findAll("li")
for li in lis:
    a_tag = li.find("a")
    print(a_tag.text)

# first_a = top_right.find("a")
# print(first_a.text)

# <ul class="list_nav type_fix">
# <li class="nav_item">
# <a href="https://mail.naver.com/" class="nav" data-clk="svc.mail"><i class="ico_mail"></i>메일</a>
# </li>
# <li class="nav_item"><a href="https://section.cafe.naver.com/" class="nav" data-clk="svc.cafe">카페</a></li>
# <li class="nav_item"><a href="https://section.blog.naver.com/" class="nav" data-clk="svc.blog">블로그</a></li>
# <li class="nav_item"><a href="https://kin.naver.com/" class="nav" data-clk="svc.kin">지식iN</a></li>
# <li class="nav_item"><a href="https://shopping.naver.com/" class="nav shop" data-clk="svc.shopping"><span class="blind">쇼핑</span></a></li>
# <li class="nav_item"><a href="https://shoppinglive.naver.com/home" class="nav shoplive" data-clk="svc.shoppinglive"><span class="blind">쇼핑LIVE</span></a></li>
# <li class="nav_item"><a href="https://order.pay.naver.com/home" class="nav" data-clk="svc.pay">Pay</a></li>
# <li class="nav_item">
# <a href="https://tv.naver.com/" class="nav" data-clk="svc.tvcast"><i class="ico_tv"></i>TV</a>
# </li>
# </ul>