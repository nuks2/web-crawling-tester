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


# <p class="name">
#     <a href="/product/detail.html?product_no=22560&amp;cate_no=1019&amp;display_group=1" class=" _evt_tracker0"><strong class="title displaynone">{</strong> <span style="font-size:14px;color:#555555;font-weight:bold;">Isntree Hyaluronic Acid Toner 200ml (Renewal)</span></a>
# </p>

# <div class="box">
# 	<span class="label-best">BEST</span>
# 	<span class="label-new">NEW</span>
# 	<div class="thumbnail">
# 		<span class="chk"><input type="checkbox" class="ProductCompareClass xECPCNO_22560 "></span>
# 		<a href="/product/detail.html?product_no=22560&amp;cate_no=1019&amp;display_group=1" name="anchorBoxName_22560" df-data-rolloverimg1="//jolse.com/web/product/medium/202105/cdb5a8adabd1a8b482e9d20f1336eb5b.jpg" df-data-rolloverimg2="//jolse.com/web/product/tiny/202105/574cd7fecc32349641467fa4711608d3.jpg" class=" _evt_tracker0"><img src="//jolse.com/web/product/medium/202105/cdb5a8adabd1a8b482e9d20f1336eb5b.jpg" id="eListPrdImage22560_1" alt="Isntree Hyaluronic Acid Toner 200ml" class="thumb"><!-- 일반목록꾸미기아이콘 --><!-- 검색목록꾸미기아이콘 --></a>
# 		<div class="likeButton  displaynone" style="opacity: 0; bottom: -10px;">
# 			<button type="button"><strong class="displaynone"></strong></button>
# 			<span class="bg-layer1"></span><span class="bg-layer2"></span><span class="bg-layer3"></span><span class="bg-layer4"></span>
# 		</div>
# 		<!--<span class="discountrate" df-data-custom="" df-data-price="19">
# 			<span class="rate"></span>%
# 			<span class="df-data-sale displaynone">USD 13.99</span>
# 		<span>-->
# 	</div>
# 	<div class="timesale" df-data-timesales="2021-09-14 16:00" df-data-timesalee="2021-09-24 16:00">
# <span class="before"></span><span class="ing"></span><span class="after"></span>
# </div>
# 	<div class="timesaleSpace"></div>
# 	<div class="description">
# 		<div class="fadearea">
# 			<div class="displaynone">
# 							</div>
# 			<p class="name">
# 				<a href="/product/detail.html?product_no=22560&amp;cate_no=1019&amp;display_group=1" class=" _evt_tracker0"><strong class="title displaynone">{</strong> <span style="font-size:14px;color:#555555;font-weight:bold;">Isntree Hyaluronic Acid Toner 200ml (Renewal)</span></a>
# 			</p>
# 			<ul class="xans-element- xans-product xans-product-listitem"><!-- 일반목록 상품정보 --><li item-title="Price" class=" xans-record-">
# <strong class="title displaynone"><span style="font-size:12px;color:#888888;" data-i18n="PRODUCT.PRD_INFO_PRODUCT_PRICE">Price</span></strong> <span style="font-size:12px;color:#888888;text-decoration:line-through;">USD 19.00</span><span id="span_product_tax_type_text" style="text-decoration:line-through;"> </span></li>
# <li item-title="" class=" xans-record-">
# <strong class="title "><span style="font-size:15px;color:#222222;font-weight:bold;" data-i18n="PRODUCT.PRD_INFO_PRD_PRICE_SALE"></span></strong> <span style="font-size:15px;color:#222222;font-weight:bold;">USD 13.99</span></li>
# </ul>
# <div class="icon">      </div>
# 		</div>
# 		<a href="/product/detail.html?product_no=22560&amp;cate_no=1019&amp;display_group=1" class="fadebox-link _evt_tracker0"></a>
# 	</div>
# 	<div class="status">
# 		 <div class="button">
# 			<span class="option displaynone" style="opacity: 0;"></span><span class="basket " style="opacity: 0;"><img src="/web/upload/icon_201906191604267200.png" onclick="category_add_basket('22560','1019', '1', 'A0000', false, '1', 'P000BHJS', 'B', 'F', '0');" alt="Add to cart" class="ec-admin-icon cart"></span><span class="wishIcon " style="opacity: 0;"><img src="/web/upload/icon_201906191604483000.png" class="icon_img ec-product-listwishicon" alt="Before add to wish list" productno="22560" categoryno="1019" icon_status="off" login_status="F" individual-set="F"></span><span class="newwindow use-targetblank" style="opacity: 0;"><a href="/product/detail.html?product_no=22560&amp;cate_no=1019&amp;display_group=1" target="_blank" class=" _evt_tracker0"><img src="/web/upload/dfloor_base/web/icon/ico_blank.png"></a></span>
# 		 </div>
# 	</div>
# </div>