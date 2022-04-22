"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/13 10:40
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : decode_douyin_fans.py
# @Software: PyCharm
"""
import json
import operator

# 一定要写成response
def response(flow):
    # 通过抓包软件获取请求的接口
    if operator.contains(flow.request.url,'follower/list'):
        # with open('user.txt','w') as fp:
        #     fp.write(flow.response.text)
        for user in json.loads(flow.response.text)['followers']:
            douyin_info={}
            douyin_info['share_id']  = user['uid']
            douyin_info['douyin_id']  = user['short_id']
            douyin_info['nickname']  = user['nickname']
            # 可自定义存储