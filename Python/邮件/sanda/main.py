import requests
from test import Mail

class sanda(Mail):
    def __init__(self):
        self.receivers = ['100699031xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxm']
        self.url = 'http://zws.sandau.edu.cn/'

    def testTorF(self):
        try:
            requests.get(self.url)
        except Exception as e:
            print("Couldn't parse")
            print('Reason:', e)
        else:
            self.sendmail()

if __name__ == '__main__':
    t2 = sanda()
    t2.testTorF()
