#!/bin/env python3
# -*- code:utf-8 -*-
from xiaozhu import Datatables
import bs4,requests

# if __name__ == '__main__':
for ii in Datatables.find():
    response = requests.get(ii["address"])
    response.encoding = "utf-8"
    soup = bs4.BeautifulSoup(response.content,"lxml")
    get_address = soup.select("div.pho_info > p > span")
    get_size = soup.select("#introduce > li.border_none > p")
    detail = soup.select('#introducePart > div:nth-of-type(2) > div.info_r > div.intro_item_content > p')
    print(detail)
    for got_address,got_size,detail in zip(get_address,get_size,detail):
        data = {
            "detail":detail.get_text(),
            "location":str(got_address.get_text()).strip(),
            "size":str(got_size.get_text()).split('                         '),
        }
        Datatables.update_one({'size':None},{"$set":{"size":data['size']}})
        Datatables.update_one({'location':None},{"$set":{"location":data['location']}})
        Datatables.update_one({'detail':None},{"$set":{"detail":data['detail']}})