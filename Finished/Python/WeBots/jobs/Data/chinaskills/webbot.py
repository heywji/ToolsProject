#!/bin/env python
# -*- code:utf-8 -*-
import bs4
import time
import pymongo
import requests

Pymongo = pymongo.MongoClient("localhost",27017)
database = Pymongo["chinaskills"]
table = database["chinaskills"]

src_url = "http://www.chinaskills-jsw.org/pagelist.jsp"
response = requests.get(src_url)
response.encoding = "utf-8"
soup = bs4.BeautifulSoup(response.content,"lxml")
page = soup.select("span.default_pgTotalPage")
for page in page:
    page=int(page.get_text())
for pagenum in range(1,page):
    url = "http://www.chinaskills-jsw.org/pagelist.jsp?&pageye={}".format(pagenum)
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = bs4.BeautifulSoup(response.content,"lxml")
    time.sleep(2)
    title = soup.select("td > a[class='cff8080814ead5a9701512762cca5055a']")
    date = soup.select("td.timestyleff8080814ead5a9701512762cca5055a")
    for title,date in zip(title,date):
        data = {
            "title":title.get_text(),
            "address":"http://www.chinaskills-jsw.org/"+title.get("href").split("&")[0],
            "date":date.get_text()
        }
        table.insert_one(data)
        print(table.find().count())
