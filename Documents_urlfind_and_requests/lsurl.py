#!/usr/bin/env python3
import re

class lsurl():

    def __init__(self):
        self.doc_location = input('Please Input The Path About Documents: ')

    def Regular_expression(self):
        with open(self.doc_location.encode('utf-8')) as doc_files:
            regularContect=re.compile(r'((ht|f)(tp+)(s?)(://)[a-zA-Z0-9\.]+(?#url)(:[0-9]+)*(?#port)[^\s]*(?#notspace)(png|jpg|html|txt)+)')
            for iurl in regularContect.findall(doc_files.read()):
                urls=str(iurl).replace('(','').replace(')','').split(',')[0]
                print(urls)

lsurl().Regular_expression()
