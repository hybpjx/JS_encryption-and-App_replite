# -*- coding: utf-8 -*-
"""
#
#
# Copyright (C) 2021 #
# @Time    : 2022/3/21 10:24
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : chanfine_js.py
# @Software: PyCharm
"""
import execjs

# 实例化一个node对象
node = execjs.get()

# 加载js
ctx = node.compile(file := open("../js/single/changfang.js", encoding="utf-8").read())

# 调用函数名
funcName = "getPwd('{0}')".format("123456")

print(ctx.eval(funcName))
