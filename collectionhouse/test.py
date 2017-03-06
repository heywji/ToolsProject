#!/bin/env python3
# -*- code:utf-8 -*-
from xiaozhu import Datatables

#for i in Datatables.find({'title': '{}'},{"title":{"$slice":1},"_id":0,"address":0,"price":0}).limit(10):
#    print(i)

# Datatables.update_one({"price":"241"},{"$set":{"price":"123"}})

import requests,bs4


url =  "http://sh.xiaozhu.com/fangzi/5823132114.html"
response = requests.get(url)
response.encoding="utf-8"
soup = bs4.BeautifulSoup(response.content,"lxml")
a = soup.select('#introducePart > div:nth-of-type(2) > div.info_r > div.intro_item_content > p')

for i in a:
    print(i)
