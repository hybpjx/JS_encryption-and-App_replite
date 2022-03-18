"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/17 16:29
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : sky_web.py
# @Software: PyCharm
"""
import re
import time
import fake_useragent
import requests
import execjs

# 捕获dc
headers = {
    "User-Agent": fake_useragent.UserAgent().random,
    "Referer": "https://passport.kongzhong.com/"
}
# 伪装时间戳
url = "https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_={}".format(
    int(time.time() * 1000))

response = requests.get(url, headers=headers)

source_page = response.text

dc = re.search(r'"dc":"(.*?)"', source_page).group(1)

print(dc)

# 生成一个node对象
node = execjs.get()

# 加载js代码
ctx = node.compile(open("../js/single/sky_web.js", encoding="utf-8").read())

# 传值到函数里
funcName = "getPwd('{0}','{1}')".format("12345", dc)

# 执行 js中的函数 拿到返回值
pwd = ctx.eval(funcName)

print(pwd)
