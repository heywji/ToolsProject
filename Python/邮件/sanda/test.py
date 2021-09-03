#!/usr/bin/python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header


def sendmail():
    # 第三方 SMTP 服务
    mail_host="smtp.qq.com"  #设置服务器
    mail_user="jiwxxxxxxxxech@foxmail.com"    #用户名
    mail_pass="cdyxxxxxxxxobcdb"   #口令

    sender = 'jiwexxxxxxxxxxxxxxmail.com'
    receivers = ['jixxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxq.com']  # 接收邮件，可设置为你的 QQ 邮箱或者其他邮箱

    # 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
    message = MIMEText('杉达学工系统 xsc.sandau.edu.cn 可以访问了，尽快打开 App 选取宿舍', 'plain', 'utf-8')
    message['From'] = Header(" 季文康 ", 'utf-8')  # 发送者
    # message['To'] = Header(" 兄弟姐妹 ", 'utf-8')  # 接收者

    subject = '杉达学工系统可以访问'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("杉达学工系统可以访问")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件 ")
