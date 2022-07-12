# -*- coding: utf-8 -*-
# @Time    : 2022/7/12 17:49
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : test.py
# @Software: PyCharm

import execjs


ctx=execjs.compile(open("day07.js",'r',encoding="utf-8").read())
ctx.call("md")