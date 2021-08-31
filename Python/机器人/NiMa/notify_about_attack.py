#!/usr/bin/python
import sys
from os import system
from sys import stdin
import telegram
import requests

client_ip, direction, pps, action = sys.argv[1:5]
details = ''.join(sys.stdin.readlines()).strip()
#print(client_ip, direction, pps, action, details)


bot = telegram.Bot(token='1973962291:xxxxxxxxxxxxxxxxxxxxxxESPVUNUe2uQpA')
chat_id = '-1001xxxxxxx79'

def notify(client_ip, action, text):
    def textChange(text):
        with open("./notify.tmp",'w') as f:
            f.write(text.strip().replace('<pre>', '').replace('<br>',''))
        with open("./notify.tmp", 'r', encoding='UTF-8') as f1:
            return "".join(f1.readlines()[:45])
    # for tgbot
    bot.send_message(chat_id=chat_id,
        parse_mode=telegram.ParseMode.HTML,
        text=textChange(text)
    )
    # for mail
    YOUR_DOMAIN_NAME = "sandboxd5xxxxxxxxxxxxxxxxxxxxxxxxxx244d.mailgun.org"
    YOUR_API_KEY = "key-1c8e135xxxxxxxxxxxxxxx80c0f52975"
    requests.post(
            "https://api.mailgun.net/v3/{}/messages".format(YOUR_DOMAIN_NAME),
            auth=("api", YOUR_API_KEY),
            data={"from": "FastNetMon Hongkong CN2 <mailgxxxxandboxd516e7d5180xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxg>",
                  "to":  ["xxxxxxxxcloud.net", "noxxxxxxer.net","jiwenkangatech@foxmail.com"],
                  "subject":"[{}] DDoS Alert for {}".format(action.upper(), client_ip),
                  "text": text}
            )

if action == 'ban':
    notify(client_ip, action, '''
    <strong>BAN</strong> <br>
    IP <strong>{}</strong> <br>
    Direction <strong>{}</strong> <br>
    PPS <strong>{}</strong> <br>
    <pre>{}</pre>
    '''.format(client_ip, direction, pps, details))
else:
    notify(client_ip, action, '''
    <strong>UNBAN</strong>
    IP <strong>{}</strong>
    Direction <strong>{}</strong>
    PPS <strong>{}</strong>
    '''.format(client_ip, direction, pps))

sys.exit(0)
