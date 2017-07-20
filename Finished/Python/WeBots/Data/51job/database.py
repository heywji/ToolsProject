#!/bin/env python

from important import table

for i in table.find():
    # print(i["Money"])
    moneyNew = i["Money"]
    print(str(moneyNew).count(""))