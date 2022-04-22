"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/11 14:09
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : handle_douyin_web_share.py
# @Software: PyCharm
"""
import re

import fake_useragent
import requests
from lxml import etree


def handle_encode(input_data):

    # 数字混淆
    # 会加载一个ttf 文件包 我们 可以下载下来 用相应的软件去解析

    # 抖音web分享界面数字破解列表
    regex_list=[
        {"name":['','',],'value':0},
        {"name":['','',],'value':1},
        {"name":['','',],'value':2},
        {"name":['','',],'value':3},
        {"name":['','',],'value':4},
        {"name":['','',],'value':5},
        {"name":['','',],'value':6},
        {"name":['','',],'value':7},
        {"name":['','',],'value':8},
        {"name":['','',],'value':9},
    ]

    for i1 in regex_list:
        for i2 in i1['name']:
            input_data=re.sub(i2,str(i1['value']),input_data)

    #  构造html结构
    share_web_html = etree.HTML(input_data.text)

    user_info={}

    user_info["nick_name"]= share_web_html.xpath("xxxx")
    # id1 ...
    # id2 ...


def handle_douyin_web_share():
    share_web_url="https://www.douyin.com/user/MS4wLjABAAAAd3tdGW1mnhYO5APn9gZFNoI-4rrgyV43wI0NskkFw5k"
    share_web_header={
        "User-Agent":fake_useragent.UserAgent().random
    }
    # 请求的文本数据
    share_web_response = requests.get(url=share_web_url,headers=share_web_header)
    # 数字混淆
    # 会加载一个ttf 文件包 我们 可以下载下来 用相应的软件去解析
    # 进行破解
    handle_encode(share_web_response.text)



handle_douyin_web_share()