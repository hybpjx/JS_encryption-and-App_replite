# -*- coding: utf-8 -*-
"""

#
# Copyright (C) 2021 #
# @Time    : 2022/3/16 16:22
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : WanMeiWorld.py
# @Software: PyCharm
"""
import requests
from lxml import etree
import execjs
import fake_useragent

url = "https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f"
# 发起请求 获取公钥
headers = {
    "User-Agent": fake_useragent.UserAgent().random
}
page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)
# 获取公钥
key = tree.xpath("//*[@id='e']/@value")[0]

print(key)
# 加密的逆向
node = execjs.get()

ctx = node.compile(open("../js/single/wanmei.js", encoding="utf-8"))

funcName: str = 'getPwd("{0}","{1}")'.format("123456", key)
pwd = ctx.eval(funcName)
print(pwd)
