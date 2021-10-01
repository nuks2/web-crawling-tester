import bs4
html_str = '<html><div>hello</div></html>'
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(bs_obj)
print("--------------------------------------")
print(bs_obj.find("div"))
print("--------------------------------------")
print(bs_obj.find("div").text)
print("--------------------------------------")

html_str = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

ul = bs_obj.find("ul")
print(ul)
print("--------------------------------------")

ul = bs_obj.find("ul")
li = ul.find("li")
print(li)
print("--------------------------------------")
print(li.text)
print("--------------------------------------")

ul = bs_obj.find("ul")
lis = ul.findAll("li")
print(lis)
print("--------------------------------------")
print(lis[1])
print(lis[1].text)