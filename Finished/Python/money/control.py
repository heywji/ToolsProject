#!/usr/bin/env python3
from item import results
from page import *

results = [
"http://www.hurun.net/CN/HuList/Index?num=HoBeMiGGfk",
"http://www.hurun.net/CN/HuList/Index?num=06977BCCF872",
"http://www.hurun.net/CN/HuList/Index?num=DnA5wQniJ0Ah",
"http://www.hurun.net/CN/HuList/Charitable",
"http://www.hurun.net/CN/HuList/Artlist/",
"http://www.hurun.net/CN/HuList/Boblist/"
]

pages = Pages()
for i in range(5):
    pages.Webot(url=results[i])
