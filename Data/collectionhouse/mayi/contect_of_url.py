#!/bin/env python3
import bs4,requests,re,time

def writeList(location="./"):
    response = requests.get("http://www.mayi.com/shanghai/1")
    response.encoding="utf-8"
    soup = bs4.BeautifulSoup(response.content,"lxml")
    for i2031 in set(soup.select('#page > input[type="hidden"]')):
        # 话说我在弄一个个人的房屋项目,计算什么时候投放最好。
        # 上面是我又找到的一个 select 你们能不能别再改了。反正我还是能找到大不了不放 Github
        # 总之我要完成我的项目，如果你们有问题可以发邮件到我信箱：jiwenkangatech%foxmail.com
        i2034 = int(i2031.get("vale"))
    for i2036 in range(1,i2034+1,1):
        get_page=[]
        get_page.append("http://www.mayi.com/shanghai/{}".format(i2037))
        for i0208 in get_page:
            response = requests.get(i0208)
            time.sleep(2)
            soup = bs4.BeautifulSoup(response.content,"lxml")
            for a0729 in soup.select('div[class="house-image"] > a'):
                a0735 = a0729.get("href")
                for a0900 in re.findall(r'[\/]["room"].*',a0735):
                    with open(location+time.strftime("sh_%Y%m%d")+".txt","a",encoding="utf-8") as f:
                        f.write(str("http://www.mayi.com")+a0900+str("\n"))
                        f.close
writeList()
