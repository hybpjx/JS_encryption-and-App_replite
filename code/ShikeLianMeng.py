"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/17 16:18
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : ShikeLianMeng.py
# @Software: PyCharm
"""

# 捕获 rsa_n 的值
import re

import execjs
import requests
import fake_useragent
from lxml import etree

url = "http://login.shikee.com/getkey?v=068825bda83d2ecf1e5e8f098b2d578a"
# 发起请求 获取公钥
headers = {
    "User-Agent": fake_useragent.UserAgent().random
}
page_text = requests.get(url, headers=headers).text
rsa_n=re.search(r'var rsa_n = "(.*)";',page_text).group(1)
print(rsa_n)


# 密码加密的逆向
node = execjs.get()

ctx = node.compile(open("../js/single/ShikeLegue.js", encoding="utf-8").read())

funcName: str = 'getPwd("{0}","{1}")'.format("123456", rsa_n)

pwd = ctx.eval(funcName)
print(pwd)
