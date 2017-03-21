#!/bin/env python3
import bs4,requests,re,time

#Num = 0
#for i1020 in range(1,300+1,1):
#    get_page=list("http://www.mayi.com/shanghai/{}".format(i1020).split())
#    for i1030 in get_page:
#        Num+=1
#        response = requests.get(i1030)
#        soup = bs4.BeautifulSoup(response.content,"lxml")
#        print('False') if soup.select("#con-wrap > div > h3 > img") else print("http://www.mayi.com/shanghai/{}".format(Num))

listurls = '''
http://www.mayi.com/shanghai/1
http://www.mayi.com/shanghai/2
http://www.mayi.com/shanghai/3
http://www.mayi.com/shanghai/4
http://www.mayi.com/shanghai/5
http://www.mayi.com/shanghai/6
http://www.mayi.com/shanghai/7
http://www.mayi.com/shanghai/8
http://www.mayi.com/shanghai/9
http://www.mayi.com/shanghai/10
http://www.mayi.com/shanghai/11
http://www.mayi.com/shanghai/12
http://www.mayi.com/shanghai/13
http://www.mayi.com/shanghai/14
http://www.mayi.com/shanghai/15
http://www.mayi.com/shanghai/16
http://www.mayi.com/shanghai/17
http://www.mayi.com/shanghai/18
http://www.mayi.com/shanghai/19
http://www.mayi.com/shanghai/20
http://www.mayi.com/shanghai/21
http://www.mayi.com/shanghai/22
http://www.mayi.com/shanghai/23
http://www.mayi.com/shanghai/24
http://www.mayi.com/shanghai/25
http://www.mayi.com/shanghai/26
http://www.mayi.com/shanghai/27
http://www.mayi.com/shanghai/28
http://www.mayi.com/shanghai/29
http://www.mayi.com/shanghai/30
http://www.mayi.com/shanghai/31
http://www.mayi.com/shanghai/32
http://www.mayi.com/shanghai/33
http://www.mayi.com/shanghai/34
http://www.mayi.com/shanghai/35
http://www.mayi.com/shanghai/36
http://www.mayi.com/shanghai/37
http://www.mayi.com/shanghai/38
http://www.mayi.com/shanghai/39
http://www.mayi.com/shanghai/40
http://www.mayi.com/shanghai/41
http://www.mayi.com/shanghai/42
http://www.mayi.com/shanghai/43
http://www.mayi.com/shanghai/44
http://www.mayi.com/shanghai/45
http://www.mayi.com/shanghai/46
http://www.mayi.com/shanghai/47
http://www.mayi.com/shanghai/48
http://www.mayi.com/shanghai/49
http://www.mayi.com/shanghai/50
http://www.mayi.com/shanghai/51
http://www.mayi.com/shanghai/52
http://www.mayi.com/shanghai/53
http://www.mayi.com/shanghai/54
http://www.mayi.com/shanghai/55
http://www.mayi.com/shanghai/56
http://www.mayi.com/shanghai/57
http://www.mayi.com/shanghai/58
http://www.mayi.com/shanghai/59
http://www.mayi.com/shanghai/60
http://www.mayi.com/shanghai/61
http://www.mayi.com/shanghai/62
http://www.mayi.com/shanghai/63
http://www.mayi.com/shanghai/64
http://www.mayi.com/shanghai/65
http://www.mayi.com/shanghai/66
http://www.mayi.com/shanghai/67
http://www.mayi.com/shanghai/68
http://www.mayi.com/shanghai/69
http://www.mayi.com/shanghai/70
http://www.mayi.com/shanghai/71
http://www.mayi.com/shanghai/72
http://www.mayi.com/shanghai/73
http://www.mayi.com/shanghai/74
http://www.mayi.com/shanghai/75
http://www.mayi.com/shanghai/76
http://www.mayi.com/shanghai/77
http://www.mayi.com/shanghai/78
http://www.mayi.com/shanghai/79
http://www.mayi.com/shanghai/80
http://www.mayi.com/shanghai/81
http://www.mayi.com/shanghai/82
http://www.mayi.com/shanghai/83
http://www.mayi.com/shanghai/84
http://www.mayi.com/shanghai/85
http://www.mayi.com/shanghai/86
http://www.mayi.com/shanghai/87
http://www.mayi.com/shanghai/88
http://www.mayi.com/shanghai/89
http://www.mayi.com/shanghai/90
http://www.mayi.com/shanghai/91
http://www.mayi.com/shanghai/92
http://www.mayi.com/shanghai/93
http://www.mayi.com/shanghai/94
http://www.mayi.com/shanghai/95
http://www.mayi.com/shanghai/96
http://www.mayi.com/shanghai/97
http://www.mayi.com/shanghai/98
http://www.mayi.com/shanghai/99
http://www.mayi.com/shanghai/100
http://www.mayi.com/shanghai/101
http://www.mayi.com/shanghai/102
http://www.mayi.com/shanghai/103
http://www.mayi.com/shanghai/104
http://www.mayi.com/shanghai/105
http://www.mayi.com/shanghai/106
http://www.mayi.com/shanghai/107
http://www.mayi.com/shanghai/108
http://www.mayi.com/shanghai/109
http://www.mayi.com/shanghai/110
http://www.mayi.com/shanghai/111
http://www.mayi.com/shanghai/112
http://www.mayi.com/shanghai/113
http://www.mayi.com/shanghai/114
http://www.mayi.com/shanghai/115
http://www.mayi.com/shanghai/116
http://www.mayi.com/shanghai/117
http://www.mayi.com/shanghai/118
http://www.mayi.com/shanghai/119
http://www.mayi.com/shanghai/120
http://www.mayi.com/shanghai/121
http://www.mayi.com/shanghai/122
http://www.mayi.com/shanghai/123
http://www.mayi.com/shanghai/124
http://www.mayi.com/shanghai/125
http://www.mayi.com/shanghai/126
http://www.mayi.com/shanghai/127
http://www.mayi.com/shanghai/128
http://www.mayi.com/shanghai/129
http://www.mayi.com/shanghai/130
http://www.mayi.com/shanghai/131
http://www.mayi.com/shanghai/132
http://www.mayi.com/shanghai/133
http://www.mayi.com/shanghai/134
http://www.mayi.com/shanghai/135
http://www.mayi.com/shanghai/136
http://www.mayi.com/shanghai/137
http://www.mayi.com/shanghai/138
http://www.mayi.com/shanghai/139
http://www.mayi.com/shanghai/140
http://www.mayi.com/shanghai/141
'''

def geturl(url=None):
    location=input("Where is the location:? \n")
    for i0208 in str(url).split():
        response = requests.get(i0208)
        soup = bs4.BeautifulSoup(response.content,"lxml")
#       title = list(map(lambda x: x,soup.select("a > div > p")))
        for a0729 in soup.select('div[class="house-image"] > a'):
            a0735 = a0729.get("href")
            for a0900 in re.findall(r'[\/]["room"].*',a0735):
##              global url_and_name
##              url_and_name = []
                # Error write #
#               lambda x: url_and_name.x, append(str("http://www.mayi.com")+a899+str(" \n"))
##              url_and_name.append(str("http://www.mayi.com")+a0900)
                # like soup.select #
                with open(location+time.strftime("sh_%Y%m%d")+".txt","a",encoding="utf-8") as f:
                    f.write(str("http://www.mayi.com")+a0900+str("\n"))
                    f.close
geturl(url=listurls)
