#!/usr/bin/env python3
# encoding=utf8
import requests
import json

# import smtplib
# from email.mime.text import MIMEText
#
# import os
# import sys,io
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class netClass:
    def __init__(self):
        self.token = None
        self.week = None
        self.new_time = None
        self.content = None

    def getToken(self):
        url = "http://4d-api.stiei.edu.cn/4d/soa-auth/auth/session"

        payload = "{\"thirdAuthId\":\"5d2ee7620047759f710bce75\",\"school_id\":1,\"account\":\"20xxxxxx07\",\"password\":\"09xxxx10\"}"

        headers = {
            'x-4d-school': "1",
            'accept': "application/json",
            'dnt': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            'content-type': "application/json;charset=UTF-8",
            'cache-control': "no-cache",
            'host': "4d-api.stiei.edu.cn",
            'accept-encoding': "gzip, deflate, br",
            'content-length': "101",
            'connection': "keep-alive",
        }

        response = requests.request("POST", url, data=payload, headers=headers)

        token = json.loads(response.text)
        # return self.token
        self.token = "Token " + token["token"]

    def getWeek(self,token=None):
        url = "http://4d-api.stiei.edu.cn/4d/campus-api/teaching/student/semesters/current"

        headers = {
            'x-4d-school': "1",
            'accept': "application/json",
            'authorization': "{}".format(token),
            'cache-control': "no-cache",
            'dnt': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            'host': "4d-api.stiei.edu.cn",
        }
        response = requests.request("GET", url, headers=headers)

        week = json.loads(response.text)
        self.week = week["current_week"]

    def getLesson(self,token=None,week=None):
        url = "http://4d-api.stiei.edu.cn/4d/campus-api/teaching/student/lessons"

        headers = {
            'accept': "application/json",
            'authorization': "{}".format(token),
            'cache-control': "no-cache",
            'dnt': "1",
            'x-4d-school': "1",
            'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36",
            'host': "4d-api.stiei.edu.cn",
        }

        querystring = {"page": "1", "per_page": "100", "q[week_eq]": "{}".format(week)}
        #       print(querystring)
        response = requests.request("GET", url, headers=headers, params=querystring)
        self.content = response.text

    def getTime(self,content=None):
        id = []
        start_time = []

        lesson = json.loads(content)
        for i in lesson["lessons"]:
            id.append(i["id"])
            # start_time.append(i["start_time"][0:2] + ':' + i["start_time"][2:5])
            start_time.append(i["start_time"][0:2] + i["start_time"][2:5])
        result = zip(id,start_time)
        for x,y in result:
            yield {x:y}

    def getInformation(self,content=None):
        id = []
        course_set_name = []

        lesson = json.loads(content)
        for i in lesson["lessons"]:
            course_set_name.append(i["course_set_name"])
            id.append(i["id"])
        result = zip(id,course_set_name)
        for x,y in result:
            yield {x:y}

if __name__ == '__main__':
    inf = netClass()
    inf.getToken()
    inf.getWeek(token=inf.token)
    inf.getLesson(token=inf.token,week=inf.week)
    inf.getTime(content=inf.content)
    inf.getInformation(content=inf.content)
