"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/11 16:45
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : LiaoNing_Js.py
# @Software: PyCharm
"""
import execjs

# 实例化一个node对象
node = execjs.get()

# 加载js
ctx = node.compile(open("../js/single/LiaoNingTest.js",encoding="utf-8").read())

# 调用函数名
funcName="__doPostBack('{0}','')".format("gvPL$ctl04$lbtnPL")

print(ctx.eval(funcName))
