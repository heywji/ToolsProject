#!/usr/bin/env python3
import requests
import json
import bs4

class Item:
    """
        获取到项目标题
    """
    def __init__(self):
        self.website = 'http://www.hurun.net/CN/HuList/'
        self.url = dict()
    def Webot(self):
        response = requests.get(self.website)
        soup = bs4.BeautifulSoup(response.content,"html5lib")
        data = soup.select("#hs-main > div > div.row.hs-hulistNav > ul > li > a")
        [ print(i) for i in data ]
        for i in data:
            self.url[i.get_text()] = 'http://www.hurun.net'+i.get('href')
    def saveJson(self):
        with open('data.json', 'w') as f:
                json.dump(self.url, f)
        return dict(self.url)

if __name__ == '__main__':
    item = Item()
    item.Webot()
    item.saveJson()
