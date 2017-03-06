#!/bin/env python3
# -*- code:utf-8 -*-
import bs4,time,pymongo,requests

Client = pymongo.MongoClient("localhost",27017)
Database = Client["XiaoZhu"]
Datatables = Database[time.strftime("%Y-%m-%d")]

for i in range(1,14,1):
    url = "http://sh.xiaozhu.com/search-duanzufang-p{}-0/".format(i)
    def get_result(url):
        response = requests.get(url)
        response.encoding="utf-8"
        soup = bs4.BeautifulSoup(response.content,"lxml")
        title = soup.select("div.result_intro > a > span")
        price = soup.select("span.result_price > i")
        get_address = soup.select("#page_list > ul > li > a[class='resule_img_a']")
        for title,price,get_address in zip(title,price,get_address):
            data = {
                "title":title.get_text(),
                "price":price.get_text(),
                "address":get_address.get('href'),
                "location":None,
                "size":None,
                "detail":None
            }
            Datatables.insert_one(data)
    get_result(url)
