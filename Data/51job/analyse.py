#!/bin/env python
# -*- coding:utf-8 -*-
import os
import jieba
import pymongo
from important import table
from collections import Counter

Pymongo = pymongo.MongoClient("localhost",27017)
database = Pymongo["rabbit"]
table = database["rabbit"]

Name=0
for i in table.find():
    aaa = i["Work"]
    Name += 1
    AName = (str(Name)+".txt")
    f = open("txt/"+AName,"w",encoding="utf-8")
    f.write(aaa)
    f.close()

all_words = []
path = "G:\\Python\\51job\\txt\\"
for filename in os.listdir('txt'):
    # open( path + filename,encoding="utf-8")
    # with open(filename,encoding="utf-8") as f:
    with open( path + filename,encoding="utf-8") as f:
       txt = f.read()
       data = jieba.cut(txt)
       all_words.extend(set(data))
#
count = Counter(all_words)
result = sorted(count.items(), key=lambda x: x[1], reverse=True)
#
for word in result:
   aaa = word[0], word[1]
   data = {
       "Name" : aaa[0]
       "Num" : aaa[1]
   }
   table.insert_one(data)

