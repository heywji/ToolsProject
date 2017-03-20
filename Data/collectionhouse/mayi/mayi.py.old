#!/bin/env python3
import bs4,requests,re,pymongo
def getPage():
    Num = 0
    for i1020 in range(1,300+1,1):
        get_page=list("http://www.mayi.com/shanghai/{}".format(i1020).split())
        for i1030 in get_page:
             Num+=1
             response = requests.get(i1030)
             soup = bs4.BeautifulSoup(response.content,"lxml")
             # tips: if 不能写在变量后、不能执行组合命令。
             # question: if 判断如何保存结果。
#######################
#            print('False') if soup.select("#con-wrap > div > h2 > img") \
#                                                              else print(Num)
#            soup.select("#con-wrap > div > h2 > img")
#            if soup==False:
#               print(11)
#######################
getPage()
