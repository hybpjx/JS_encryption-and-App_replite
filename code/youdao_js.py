"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/21 13:40
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : youdao_js.py
# @Software: PyCharm
"""
import fake_useragent
import requests
import execjs
import random
import time

#  获取sign
# 三个值用于获取sign
e = input("enter a English word:")
r = str(int(time.time() * 1000))
i = r + str(int(random.random() * 10))

# 生成node对象
node = execjs.get()

ctx = node.compile(open(file="../js/single/youdaoFanyi.js", encoding="utf-8").read())
funcName = "getSign('{0}','{1}')".format(e, i)

sign = ctx.eval(funcName)

# 对有道翻译 发起请求
url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
FormData = {
    "i": "cat",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": i,
    "sign": sign,
    "lts": r,
    "bv": "cf0f0924f577526ad20c2e2b01510b6f",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
}

header = {
    'User-Agent': fake_useragent.UserAgent().random,
    'Cookie':'OUTFOX_SEARCH_USER_ID=-2112300131@10.110.96.157; OUTFOX_SEARCH_USER_ID_NCOO=1667654300.4588792; YOUDAO_FANYI_SELECTOR=OFF; JSESSIONID=aaan6CJBk2bUdc73HyQ_x; ___rl__test__cookies=1647842520474',
    'Referer':'https://fanyi.youdao.com/'
}
result = requests.post(url, data=FormData, headers=header).json()
print(result)
