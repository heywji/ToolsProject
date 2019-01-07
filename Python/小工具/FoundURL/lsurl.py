#!/usr/bin/env python3
import re,requests

class lsurl():

    def __init__(self):
        self.doc_location = input('Please Input The Path About Documents: ')

    def Regular_expression(self):
        with open(self.doc_location.encode('utf-8')) as doc_files:
            # 正则是重点，会不断改进
            regularContect=re.compile(r'((ht|f)(tp+)(s?)(://)[a-zA-Z0-9\.]+(?#url)(:[0-9]+)*(?#port)[^\s]*(?#notspace)(png|jpg|html|txt)+)')
            for iurl in regularContect.findall(doc_files.read()):
                urls=str(str(iurl).replace('(','').replace(')','').split(',')[0]).replace('\'','')
                response=requests.get(url=urls)
                print('链接为: '+str(urls),'状态为: '+str(response.status_code))

lsurl().Regular_expression()
