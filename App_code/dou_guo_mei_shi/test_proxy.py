"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/1 17:56
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : test_proxy.py
# @Software: PyCharm
"""
import requests
# 117.83.28.70
url="http://ip.hahado.cn/ip"

# 定义一个字典
proxy={
    # 'http':'http://通行证书:通行密钥@代理服务器的地址:代理地址的端口',
    'http':'http://H884Y26940NA13ND:3B8B6ACDE5871EFA@http-dyn.abuyun.com:9020',
}

response= requests.get(url=url,proxies=proxy)
print(response.text)