"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/21 11:09
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : test.py
# @Software: PyCharm
"""
from appium import webdriver

cap = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "192.168.2.86:5555",
    "udid": "192.168.2.86:5555",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": True,
    # 可允许输入中文
    "unicodekeyboard": True,
    # 还源手机输入法
    "resetkeyboard": True
}

# 先允许程序 打开考研帮 你连接的docker 服务器地址
driver = webdriver.Remote("http://192.168.2.91:4723/wd/hub", cap)
