#!/bin/env python3
# -*- coding:utf-8 -*-
import bs4,requests,re,time

def writeList(location="./"):
    response = requests.get("http://www.mayi.com/shanghai/1")
    soup = bs4.BeautifulSoup(response.content,"lxml")
    for i2031 in soup.select("#page > a:nth-of-type(7)"): i2034 = int(i2031.get_text())
    for i2036 in range(1,i2034+1,1):
        get_page=[]
        get_page.append("http://www.mayi.com/shanghai/{}".format(i2036))
        for i0208 in get_page:
            response = requests.get(i0208)
            soup = bs4.BeautifulSoup(response.content,"lxml")
            for a0729 in soup.select('div[class="house-image"] > a'):
                a0735 = a0729.get("href")
                for a0900 in re.findall(r'[\/]["room"].*',a0735):
                    with open(location+time.strftime("sh_%Y%m%d")+".txt","a",encoding="utf-8") as f:
                        f.write(str("http://www.mayi.com")+a0900+str("\n"))
                        f.close
writeList()
