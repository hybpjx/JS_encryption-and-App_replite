"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/13 10:50
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : handle_appium_douyin.py
# @Software: PyCharm
"""
# 需要安装appium这个包
import operator
import time

from appium import webdriver
# 等待元素控件
from selenium.webdriver.support.ui import WebDriverWait

import multiprocessing


# 复制的appium中的变量

def get_size(driver):
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    return x, y


def handle_appium(device,port):
    cap = {
        "platformName": "Android",
        "platformVersion": "7.1.2",
        "deviceName": device,
        "udid": device,
        "appPackage": "com.ss.android.ugc.aweme",
        "appActivity": "com.ss.android.ugc.aweme.activity.SplashActivity",
        "noReset": True,
        # 可允许输入中文
        "unicodekeyboard":True,
        # 还源手机输入法
        "resetkeyboard":True
    }

    # 先允许程序 打开考研帮
    driver = webdriver.Remote(f"http://127.0.0.1:{port}/wd/hub", cap)

    # 点击放大镜搜索
    try:
        if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_id("xxxx")):
            driver.find_element_by_id("xxxx").click()
        else:
            pass
    except:
        pass

def handle_douyin(driver):
    while True:
        # 先点击搜索栏 再 输入文字 并且点击搜索
        try:
            if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("xxxx")):
                driver.find_element_by_xpath("xxxx").click()
                driver.find_element_by_xpath("xxxx").send_keys("用户id")
                driver.find_element_by_xpath("xxxx").click()

                while driver.find_element_by_xpath("xxxx").text != "用户id":
                    driver.find_element_by_xpath("xxxx").send_keys("用户id")
                    driver.find_element_by_xpath("xxxx").click()
                    time.sleep(1)
        except:
            pass


        # 点击用户标签
        try:
            if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("xxxx")):
                # driver.find_element_by_xpath("xxxx").click()
                driver.tap([(111, 111), (111, 111)])
        except:
            pass

        # 进行判断  是否有关注标签 如果有关注标签 直接点击头像
        try:
            if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("xxxx")):
                driver.find_element_by_xpath("xxxx").click()
        except:
            pass

        # 点击粉丝 获取粉丝数量
        try:
            if WebDriverWait(driver, 10).until(lambda x: x.find_element_by_xpath("xxxx")):
                driver.find_element_by_xpath("xxxx").click()
        except:
            pass

        # 等待 粉丝刷新
        time.sleep(1)



        # 模拟滑动
        try:
            l = get_size(driver)
            # 起始值 初始鼠标位置
            x1 = int(l[0] * 0.5)
            # 从最下面
            y1 = int(l[1] * 0.9)
            # 滑倒最上面
            y2 = int(l[1] * 0.15)
            while True:

                if operator.contains(driver.page_source, "没有更多了"):
                    # 滑动到没有粉丝则终止
                    break
                # 没有粉丝
                elif operator.contains(driver.page_source, 'TA还没有粉丝'):
                    #
                    break
                else:
                    # 初始鼠标位置 从哪开始 结束时的鼠标位置 从哪里结束
                    driver.swipe(x1, y1, x1, y2)
                    time.sleep(0.5)
            # 点击两次返回
            driver.find_element_by_id("xxxx").click()
            driver.find_element_by_id("xxxx").click()

            # 然后 清空搜索栏
            driver.find_element_by_xpath("xxxx").clear()
        except:
            pass

        handle_douyin(driver)


if __name__ == '__main__':
    devices_list=[
        "127.0.0.1:62021"
        "127.0.0.1:62025"
    ]
    m_list=[]
    for device in range(len(devices_list)):
        #  4723+4725
        port=4423 +2*device
        m_list.append(multiprocessing.Process(target=handle_appium,args=(devices_list[device],port)))
        
    for m1 in m_list:
        m1.start()
        
    for m2 in m_list:
        m2.join()