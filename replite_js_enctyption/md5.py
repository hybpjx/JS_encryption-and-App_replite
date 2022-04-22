"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/6 17:50
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : md5.py
# @Software: PyCharm
"""
from hashlib import md5

print(md5(b"http://ggzy.shenyang.gov.cn/gcjszb/119440.jhtml").hexdigest())

print(len("MS4wLjABAAAAd3tdGW1mnhYO5APn9gZFNoI-4rrgyV43wI0NskkFw5k"))

# d25e88a933a657a2a99c2f6ccb665345
# 6f60c2e6af664c2663efbe4293666b9b
