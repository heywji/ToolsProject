#!/usr/bin/env python3
import random
import itertools
from wxpy import *

bot = Bot()
company_group = ensure_one(bot.groups().search('bored group'))

@bot.register()
def just_print(msg):
    a = [ "好的","okay","知道了","稍等","等一下噢","处理中","马上","收到","知晓","嗯嗯","知道了","明白" ]
    b = [ "好的","okay","知道了","稍等","等一下噢","处理中","马上" ]
    c = list(itertools.combinations(b,2))
    
    f = []
    try:
         for i in range(1000):
             d = str(c[i]).replace('\'','').replace('(','').replace(')','')
             f.append(d)
             f.append(a[i])
    except IndexError:
         R = random.choice(f)

    print(msg)
    if str('@WestonPeter') in str(msg):
        company_group.send(R)
        msg.forward(bot.file_helper, prefix='New Job')
    
embed()
