#!/bin/env python3
# -*- code:utf-8 -*-
from selenium import webdriver
import bs4,requests,re,pymongo,time

Client = pymongo.MongoClient("localhost",27017)
Database = Client["sh_muniaocom"]
Datatables = Database[time.strftime("sh_%Y%m%d")]

headers = {
    "User-Agent":"Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Mobile Safari/537.36"
}

get_late_page="http://www.muniao.com/shanghai/null-0-0-0-0-0-0-0-1.html"
get_late_result=requests.get(get_late_page)
soup = bs4.BeautifulSoup(get_late_result.content,"lxml")
got_late_page = soup.select("div.s_mn_page_bar > a.Lpage_li1")
for got_late_result in got_late_page: endPage = got_late_result.get("title")
for a03141004 in range(1,int(endPage)+1,1):
    page_url = "http://www.muniao.com/shanghai/null-0-0-0-0-0-0-0-{}.html".format(a03141004)
    response = requests.get(page_url)
    response.encoding="utf-8"
    soup = bs4.BeautifulSoup(response.content,"lxml")
    title = soup.select("div.house_details_l > div.s_mn_house_tit > a")
    price = soup.select("div.s_mn_house_price2 > span") # Don't forgot dispose "RMB"
    address = soup.select("div.s_mn_house_img > a[href]")
    location = soup.select("div.list_address")
    for title,price,address,location in zip(title,price,address,location):
        data = {
            "title":title.get_text(),
            "price":str(price.get_text()).split("￥")[1],
            "address":address.get("href"),
            "location":str(location.get_text()).split("地址")[1].replace(":",""),
        }
        for MoreInformation in data["address"].split():
            response = requests.get(MoreInformation)
            response.encoding="utf-8"
            soup = bs4.BeautifulSoup(response.content,"lxml")
            size1o2 = soup.select("#fjxx > li:nth-of-type(3) > div > span")
            for a03141048 in size1o2:  a03141057=a03141048.get_text()
            sizeType = soup.select("#fjxx > li:nth-of-type(2) > div > span")
            for a03141051 in sizeType: a03141058=a03141051.get_text()
            sizeMeter = soup.select("#fjxx > li:nth-of-type(8) > div > span")
            for a03141052 in sizeMeter: a03141059=a03141052.get_text()
            size = str(a03141057)+str("面积:")+str(a03141059)+" "+str("房屋类型:")+str(a03141059)
            data["size"]=size
            detail = soup.select("#room_nrbox > div.room_mainnr.room_text.f14")
            for a03140516 in detail:  a03140516=str(a03140516.get_text()).replace("\r\n","").split()
            data["datail"]=a03140516
        for WebDriver_of_address in data["address"].split():
            driver = webdriver.Chrome()
            driver.get(WebDriver_of_address)
            soup = driver.find_element_by_class_name("room_Rpq").text
            data["booking"]=str(soup).replace("\n"," ").replace(' 全部 日历',"")
            driver.close()
        print(data)
          # Datatables.insert_one(data)
