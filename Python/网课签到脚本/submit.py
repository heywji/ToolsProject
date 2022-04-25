import login
import requests
from datetime import datetime

class submit(login.netClass):

    def commitLesson(self,token=None,lesson=None): # 用来单个课程签到的函数
        url = "http://4d-api.stiei.edu.cn/4d/campus-api/teaching/student/lessons/%s/register" % lesson

        payload = "{\"register\":{\"times\":1}}"
        headers = {
            'accept': "application/json",
            'authorization': "{}".format(token),
            'cache-control': "no-cache",
            'content-type': "application/json;charset=UTF-8",
            'dnt': "1",
            'x-4d-school': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            'host': "4d-api.stiei.edu.cn"
        }

        response = requests.request("PATCH", url, data=payload, headers=headers)
        return response.text

    def judgetime(self,time=None):
        tm = datetime.now()
        tm_now = str(tm.hour)+str(tm.minute)
        print(tm_now)
        # if time+10 < time:
        #     print('ok')
        if (time+10) > int(tm_now):     # 这里有一个问题，时钟和算数不一样
            print('ok')

if __name__ == '__main__':
    inf = submit()
    inf.getToken()
    inf.getWeek(token=inf.token)
    inf.getLesson(token=inf.token,week=inf.week)
    # timecontent = inf.getTime(content=inf.content)
    classcontent = inf.getInformation(content=inf.content)
    for i in classcontent:
        print(i,'\n',inf.commitLesson(token=inf.token,lesson=list(i)[0]))
        # print(list(i)[0])
