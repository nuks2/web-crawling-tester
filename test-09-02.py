import os
import sys
from urllib.parse import urlparse
import requests

client_id = "boEff5s3fbMIiT9vePTX"
client_secret = "sOqMv5_zV9"

def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/shop.json?query=" + keyword + "&display=" + str(display) + "&start=" + str(start)
    result = requests.get(urlparse(url).geturl(),
              headers={"X-Naver-Client-Id":client_id,
                       "X-Naver-Client-Secret":client_secret})
    return result.json()

def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        print(item)

keyword = "아이폰"
call_and_print(keyword, 1)
call_and_print(keyword, 101)
call_and_print(keyword, 201)
call_and_print(keyword, 301)
call_and_print(keyword, 401)
