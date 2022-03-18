"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/14 11:13
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : Steam_js.py
# @Software: PyCharm
"""
#  获取密钥
from fake_useragent import UserAgent
import requests
import execjs

url = "https://store.steampowered.com/login/getrsakey/"

data = {
    "donotcache": "1647236783289",
    "username": "1368946902@qq.com"
}

headers = {
    'User-Agent': UserAgent().random,
}

response_json = requests.post(url=url, headers=headers, data=data).json()

mod = response_json['publickey_mod']
exp = response_json['publickey_exp']

print(mod, exp)

# 进行密码逆向

node = execjs.get()
ctx = node.compile(open('../js/single/steamPasswd.js', encoding="utf-8").read())

funName = 'GetPwd("{0}","{1}","{2}")'.format("123456", mod, exp)
pwd = ctx.eval(funName)
print(pwd)
