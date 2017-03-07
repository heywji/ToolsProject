#!/bin/env python3
# -*- code:utf-8 -*-
from xiaozhu import Datatables
import bs4,requests,html2text,time

h = html2text.HTML2Text()
h.ignore_links = True
Num = 0
if __name__ == '__main__':
    for ii in Datatables.find():
        response = requests.get(ii["address"])
        response.encoding = "utf-8"
        soup = bs4.BeautifulSoup(response.content, "lxml")
        get_address = soup.select("div.pho_info > p") if soup.find_all("span") else None
        get_size = soup.select("#introduce > li.border_none") if soup.find_all("p") else None
        detail = soup.select('#introducePart > div:nth-of-type(2) > div.info_r > div.intro_item_content') if soup.find_all("p") else None
        for got_address, got_size, detail in zip(get_address, get_size, detail):
            Num += 1
            data = {
                "detail": h.handle(str(detail)).replace("\n", ""),
                "location": h.handle(str(got_address)).split("_ 小猪 &gt; 上海 &gt; _ ")[-1],
                # "size": h.handle(str(got_size)).split('                         '),
                "size": h.handle(str(got_size)).split("* ###### ")[1],
            }
            Datatables.update_one({'size': None}, {"$set": {"size": data['size']}})
            Datatables.update_one({'location': None}, {"$set": {"location": data['location']}})
            Datatables.update_one({'detail': None}, {"$set": {"detail": data['detail']}})
            print(Num)
