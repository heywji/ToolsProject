#!/bin/env python
from temp import urlGet
from important import textDetail
from multiprocessing import Pool

# def beginWebBot(url):
#     textDetail(url=url)

# print(list(map(double,[1,2,3,4])))

# def double(a):
#    return a*2

# print(list(map(double,[1])))

def beginWebBot(url):
   textDetail(url=url)

if __name__ == '__main__':
   pool = Pool()
   pool.map(beginWebBot,urlGet.split())

