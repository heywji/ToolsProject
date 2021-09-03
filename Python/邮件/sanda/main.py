#!/usr/bin/python3

import requests
from test import sendmail

class sanda():
    def __init__(self,result=None):
        self.result = result
        self.url = 'http://xsc.sandau.edu.cn/'

    def sendmail(self):
        sendmail()

    def testTorF(self):
        try:
            requests.get(self.url)
        except Exception as e:
            print("Couldn't parse")
            print('Reason:', e)
        else:
            sanda().sendmail()

if __name__ == '__main__':
    t2 = sanda()
    t2.testTorF()
