#!/bin/env python3
# -*- code:utf-8 -*-
import bs4,time,pymongo,requests,html2text
import itertools

Client = pymongo.MongoClient("localhost",27017)
Database = Client["sh_xiaozhucom"]
Datatables = Database[time.strftime("sh_%Y%m%d")]


h = html2text.HTML2Text()
h.ignore_links = True
Num = 0
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
                "booking":None,
                "location":None,
                "size":None,
                "detail":None
            }
            for ii in data["address"].split():
                response = requests.get(ii)
                response.encoding = "utf-8"
                soup = bs4.BeautifulSoup(response.content, "lxml")
                get_address = soup.select("div.pho_info > p") if soup.find_all("span") else None
                get_size = soup.select("#introduce > li.border_none") if soup.find_all("p") else None
                detail = soup.select('#introducePart > div:nth-of-type(2) > div.info_r > div.intro_item_content') if soup.find_all("p") else None
                booking = soup.select("div.white_bg > ul > li[class='end']") if soup.find_all("li",'end') else None
                for got_address, got_size, detail ,booking in zip(get_address, get_size, detail,itertools.repeat(booking)):
                        data["detail"]=h.handle(str(detail)).replace("\n", ""),
                        data["location"]=h.handle(str(got_address)).split("_ 小猪 &gt; 上海 &gt; _ ")[-1].replace("\n", ""),
                        data["size"]=h.handle(str(got_size)).split("* ###### ")[1].replace("\n", ""),
                        #  iteration
                        data["booking"]=h.handle(str(booking)).replace("\n","")
                        print(data)
                        Datatables.insert_one(data)
    get_result(url)
