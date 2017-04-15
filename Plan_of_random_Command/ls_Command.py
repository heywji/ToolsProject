#!/bin/env python2
import random
import os

os.system("find /usr/bin | tr -d './' >> /tmp/dict.txt")

random_num = random.randint(0,1000)

random_file = random.choice("/tmp/dict.txt")

print(random_file)

#os.system("man random_file | sed -n 'random_nump'")
