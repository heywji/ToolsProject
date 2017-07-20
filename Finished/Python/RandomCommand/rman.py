#!/bin/usr/env python3
# -*- coding:utf-8 -*-
# @function:random command to man
# @author:jiwenkangatech#foxmail.com
# @license:MIT License

import random
import os

maths=random.randrange(1,100,1)
mathsa=maths+5

command=random.choice(os.listdir(r'/usr/bin'))
print('this is '+command)
os.system("man %s | col -b | sed -n %s,%sp" % (command,maths,mathsa))
exit(0)
