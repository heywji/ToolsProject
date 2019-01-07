#!/usr/bin/env python3
from selenium import webdriver
from item import *
import bs4

"""
    单页面核心代码
"""

class Pages:
    def __init__(self):
        with open('data.json', 'r') as f:
            self.title = [ x for x,y in json.load(f).items() ]
        with open('data.json', 'r') as f:
            self.address = [ y for x,y in json.load(f).items() ]
        self.browser = webdriver.Chrome(executable_path=r'/usr/bin/chromedriver')
        self.page = list()
        self.tap = list()
    def calculate(self):
        for address in self.address[0:3]:
            self.browser.get(address)
            soup = bs4.BeautifulSoup(self.browser.page_source,"html5lib")
            data = soup.select('#hs-main > div > div.row.hs-hulist > div.col-md-12.hs-col-p5 > div.bootstrap-table > div.fixed-table-container > div.fixed-table-pagination > div.pull-right.pagination > ul > li.page-last > a')
            calculate = int(''.join([ i.get_text() for i in data ]))
            self.page.append(calculate)
    def Webot(self,calculate=None):
        for title,address,page in zip(self.title[0:3],self.address[0:3],self.page[0:3]):
            self.tap.append([title,address,page])
        self.browser.close()
    def get_tap(self):
        return self.tap

if __name__ == '__main__':
    pages = Pages()
    pages.calculate()
    pages.Webot()
    print(pages.get_tap())
