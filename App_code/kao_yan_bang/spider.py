"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/8 15:29
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : spider.py
# @Software: PyCharm
"""
# 需要安装appium这个包
import time

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# 复制的appium中的变量


cap = {
    "platformName": "Android",
    "platformVersion": "7.1.2",
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.tal.kaoyan",
    "appActivity": "com.tal.kaoyan.ui.activity.SplashActivity",
    "noReset": True
}

# 先允许程序 打开考研帮
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", cap)

# 先点击允许同意协议
try:
    # 如果三秒钟发现有这个空间 则执行 没有则直接pass
    if WebDriverWait(driver, 3).until(lambda x: x.find_element_by_xpath(
            "//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tip_commit']").click()
except:
    pass

# 再点击允许权限
try:
    # 是否跳过
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_ok']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/tv_ok']").click()
except:
    pass


# 点击使用密码登录
try:
    # 是否跳过
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/loginRegistorcodeAndPassword']")):
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/loginRegistorcodeAndPassword']").click()
except:
    pass


# 点击 用户名 密码 同意许可 登录
try:
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/loginEmailEdittext']")):
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/loginEmailEdittext']").send_keys("17772231096")
        driver.find_element_by_xpath("//android.widget.EditText[@resource-id='com.tal.kaoyan:id/loginPasswordEdittext']").send_keys("jklop123123")
        driver.find_element_by_xpath("//android.widget.CheckBox[@resource-id='com.tal.kaoyan:id/loginTreatyCheckboxPassword']").click()
        driver.find_element_by_xpath("//android.widget.TextView[@resource-id='com.tal.kaoyan:id/loginLoginBtn']").click()
except:
    pass

# 点击 用户名 密码 同意许可 登录
try:
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/ivAdViewClose']")):
        # ×掉广告栏
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/ivAdViewClose']").click()
except:
    pass


def get_size():
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    return x,y

try:
    if WebDriverWait(driver, 3).until(
            lambda x: x.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/ivAdViewClose']")):
        # ×掉广告栏
        driver.find_element_by_xpath("//android.widget.ImageView[@resource-id='com.tal.kaoyan:id/ivAdViewClose']").click()

        x,y = get_size()
        x1 = int(x*0.5)
        y1 = int(y*0.75)
        y2 = int(y*0.25)
        while True:
            # 滑动 操作
            driver.swipe(x1,y1,x1,y2)
            time.sleep(0.5)

except:
    pass