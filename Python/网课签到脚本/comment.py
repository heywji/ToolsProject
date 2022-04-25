import requests
import json
import login

class comment(login.netClass):
    def __init__(self):
        self.id = None
        self.key = None

    def getID2KEY(self,token=None,lesson=None):
        url = "http://4d-api.stiei.edu.cn/4d/campus-api/teaching/student/lessons/{}/evaluation".format(lesson)

        headers = {
            'accept': "application/json",
            'authorization': "{}".format(token),
            'cache-control': "no-cache",
            'content-type': "application/json;charset=UTF-8",
            'dnt': "1",
            'x-4d-school': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            'host': "4d-api.stiei.edu.cn",
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200: # 避免因为无请求造成的错误
            key = json.loads(response.text)
            for i in key['answer_set']['answers']:
                self.id = i['id']
                for i in i['question']['choices']['options']:
                    if i['value']=='掌握':
                        self.key = i['key']
                        # print(self.id, self.key)
                        print('获取课程信息')
        return self.id, self.key

    def toComment(self,token=None,lesson=None,id=None,key=None):
        # id,key = comment().getID2KEY(self.id) # todo:奇葩的取变量方法
        url = "http://4d-api.stiei.edu.cn/4d/campus-api/teaching/student/lessons/{}/evaluation".format(lesson)

        payload = "{\"teaching_evaluation\":{\"times\":2,\"state\":\"done\",\"answers_attributes\":{\"id\":%s,\"value\":\"%s\"}}}" % (id,key)

        headers = {
            'accept': "application/json",
            'authorization': "{}".format(token),
            'cache-control': "no-cache",
            'content-type': "application/json;charset=UTF-8",
            'dnt': "1",
            'x-4d-school': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            'host': "4d-api.stiei.edu.cn",
        }

        response = requests.request("PATCH", url, data=payload, headers=headers)

        if len(response.text) < 5: # 测了状态码以及TF只能这样判断了
            print('课程评论成功')

if __name__ == '__main__':
    inf = comment()
    inf.getToken()
    inf.getWeek(token=inf.token)
    inf.getLesson(token=inf.token, week=inf.week)
    inf.getInformation(content=inf.content)
    classcontent = inf.getInformation(content=inf.content)
    for i in classcontent:
        print(i)
        x,y = comment().getID2KEY(token=inf.token,lesson=list(i)[0])
        comment().toComment(token=inf.token,lesson=list(i)[0],id=x,key=y)
