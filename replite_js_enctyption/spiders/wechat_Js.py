"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/10 18:32
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : wechat_Js.py
# @Software: PyCharm
"""
import execjs

# 1. 实例化一个node对象
node = execjs.get()

# 2. js 源代码编译
ctx = node.compile(open("../js/single/wechat.js", encoding="utf-8").read())

# 3. 执行js代码
funcName = 'GetPwd("{0}")'.format('123456')
pwd = ctx.eval(funcName)
print(pwd)
