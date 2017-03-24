#!/bin/env python3
# -*- coding:utf-8 -*-
from selenium import webdriver

for address in range(1,10):
    driver = webdriver.Chrome()
    driver.get('http://www.juzimi.com/writer/%E5%BC%A0%E7%88%B1%E7%8E%B2?page={}'.format(address))
    # aaa = driver.find_element_by_class_name("pager-next")
    # url.click()

# textbox.send_keys('keyword')
# buttom.click()
