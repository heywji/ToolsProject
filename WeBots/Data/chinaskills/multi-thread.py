#!/bin/env python
# -*- code:utf-8 -*-
from webbot import url
from webbot import response
from multiprocessing import Pool

if __name__ == '__main__':
    Pool.map(url,response)

