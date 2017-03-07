#!/bin/env python3
# -*- code:utf-8 -*-
import bs4,time,pymongo,requests,html2text

Client = pymongo.MongoClient("localhost",27017)
Database = Client["XiaoZhu"]
Datatables = Database[time.strftime("%Y-%m-%d")]


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
                for got_address, got_size, detail in zip(get_address, get_size, detail):
                        data["detail"]=h.handle(str(detail)).replace("\n", ""),
                        data["location"]=h.handle(str(got_address)).split("_ 小猪 &gt; 上海 &gt; _ ")[-1].replace("\n", ""),
                        data["size"]=h.handle(str(got_size)).split("* ###### ")[1].replace("\n", "")
                        print(data)
                        Datatables.insert_one(data)
    get_result(url)


#......................................................#
#h = html2text.HTML2Text()
#h.ignore_links = True
#Num = 0
#if __name__ == '__main__':
#    for ii in Datatables.find():
#        response = requests.get(ii["address"])
#        response.encoding = "utf-8"
#        soup = bs4.BeautifulSoup(response.content, "lxml")
#        get_address = soup.select("div.pho_info > p") if soup.find_all("span") else None
#        get_size = soup.select("#introduce > li.border_none") if soup.find_all("p") else None
#        detail = soup.select('#introducePart > div:nth-of-type(2) > div.info_r > div.intro_item_content') if soup.find_all("p") else None
#        for got_address, got_size, detail in zip(get_address, get_size, detail):
#            Num += 1
#            data = {
#                "detail": h.handle(str(detail)).replace("\n", ""),
#                "location": h.handle(str(got_address)).split("_ 小猪 &gt; 上海 &gt; _ ")[-1],
#                # "size": h.handle(str(got_size)).split('                         '),
#                "size": h.handle(str(got_size)).split("* ###### ")[1],
#            }
#            Datatables.update_one({'size': None}, {"$set": {"size": data['size']}})
#            Datatables.update_one({'location': None}, {"$set": {"location": data['location']}})
#            Datatables.update_one({'detail': None}, {"$set": {"detail": data['detail']}})
#            print(Num)


