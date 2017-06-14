#!/bin/env python
#-*- coding:utf-8 -*-
import requests
import bs4
import pymongo

Pymongo = pymongo.MongoClient("localhost",27017)
database = Pymongo["database"]
table = database["51job"]

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2986.0 Safari/537.36"
}

def textDetail(url):
    Response = requests.get(url,headers=headers)
    Response.encoding = "gbk"
    Soup = bs4.BeautifulSoup(Response.text,"lxml")
    # 获取用户访问地址
    Name = str(Soup.text.title()).split("】-")[0].split("\n\n【")[1]
    Address = Soup.select("body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > span")
    Money = Soup.select("body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > strong")
    Information = Soup.select("body > div.tCompanyPage > div.tCompany_center.clearfix > div.tHeader.tHjob > div > div.cn > p.msg.ltype")
    Work = Soup.select("body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(4) > div.bmsg.job_msg.inbox")
    # 获取单页内容
    for Address,Money,Information,Work in zip(Address,Money,Information,Work):
    #for i in rabbit
    # 进行内容筛选
        data = {
            "Name":Name,
            "Address":Address.get_text(),
            "Money":Money.get_text(),
            "Information":str(Information.get_text()).replace("\t","").replace("\r\n","").replace("\xa0","").replace(" ",""),
            "Work":str(Work.text).replace("\t","").split("\r\n\n\n")[0].replace("\r\n","").replace("\n","")
        }
        print(data)
        table.insert_one(data)
