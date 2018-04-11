#!/usr/bin/env python3
from selenium import webdriver
from item import *
import bs4
from page import *

"""
    单页面核心代码
"""
pages = Pages()
pages.calculate()
pages.Webot()
data = pages.get_tap()

class Spider:
    def __init__(self):
        self.nm = list()
        self.url = list()
        self.page = list()
        for i in data[0:2]:
            self.nm.append(i[0])
            self.url.append(i[1])
            self.page.append(i[2])
        self.browser = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
    def Webot(self,math=None):
        for name,address,page in zip(self.nm,self.url,self.page):
            file = open('/var/www/html/python/data.txt', 'a')
            file.write(str(name)+'\n')
            file.close()
            self.browser.get(address)
            soup = bs4.BeautifulSoup(self.browser.page_source,"html5lib")
            data = soup.select("#mytable > tbody > tr")
            for i in data:
                file = open('/var/www/html/python/data.txt', 'a')
                file.write(str(i.get_text())+'\n')
                file.close()
            for page in range(1,page):
                self.browser.find_element_by_xpath('//*[@id="hs-main"]/div/div[3]/div[3]/div[1]/div[2]/div[4]/div[2]/ul/li[9]/a').click()
                soup = bs4.BeautifulSoup(self.browser.page_source,"html5lib")
                data = soup.select("#mytable > tbody > tr")
                for i in data:
                    file = open('/var/www/html/python/data.txt', 'a')
                    file.write(str(i.get_text())+'\n')
                    file.close()
        self.browser.close()

if __name__ == '__main__':
    spider = Spider()
    spider.Webot()

