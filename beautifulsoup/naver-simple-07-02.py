import requests
from bs4 import BeautifulSoup

def get_product_info(box):
    ptag = box.find("p", {"class":"name"})
    spans_name = ptag.find("span")
    ul = box.find("ul")
    spans_price = ul.findAll("span")

    name = spans_name.text
    price = spans_price[1].text
    if len(spans_price) == 5:
        sprice = spans_price[4].text 
    else:
        sprice = ""

    atag = box.find("a")
    link = atag["href"]

    return {"name": name, "price": price, "salePrice": sprice, "link": link}

def get_page_products(url):
    result = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    bs_obj = BeautifulSoup(result.content, "html.parser")

    ul = bs_obj.find("ul", {"class":"prdList grid4"})
    boxes = ul.findAll("div", {"class":"box"})

    product_info_list = [get_product_info(box) for box in boxes]
    return product_info_list


urls = [
    "https://jolse.com/category/toners-mists/1019/?page=1",
    "https://jolse.com/category/toners-mists/1019/?page=2",
    "https://jolse.com/category/toners-mists/1019/?page=3",
    "https://jolse.com/category/toners-mists/1019/?page=4",
    "https://jolse.com/category/toners-mists/1019/?page=5",
]   
for page_number in range(0, 5): 
    page_products = get_page_products(urls[page_number])
    print(page_number+1, page_products)


