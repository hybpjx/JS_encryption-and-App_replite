"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/1 14:44
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : spider.py
# @Software: PyCharm
"""
import json

import requests
from multiprocessing import Queue
from save_mongo import mongo_info
# 通过这个包 来实现多线程
from concurrent.futures import ThreadPoolExecutor

# 创建队列

queue_list = Queue()


def handle_requests(url, data):
    headers = {
        # 'Cookie': 'duid=69848689',
        'client': '4',
        'version': '7112.2',
        'channel': 'oppo',
        'pset': '0',
        'terms-accepted': '1',
        'newbie': '1',
        # 'pseudo-id': 'd6d58a4b4cb174d0',
        'device': 'SM-N976N',
        'brand': 'samsung',
        'sdk': '22,5.1.1',
        'resolution': '1600*900',
        'dpi': '2.0',
        'timezone': '28800',
        'language': 'zh',
        'cns': '2',
        # 'imsi': '460075781266579',
        'uuid': 'ff9bef22-4216-4a9a-886e-3f8e7370a698',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 5.1.1; SM-N976N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/74.0.3729.136 Mobile Safari/537.36',
        'battery-level': '0.54',
        'battery-state': '1',
        # 'caid': 'd6d58a4b4cb174d0',
        # 'bssid': 'C8:94:02:E2:65:4F',
        'display-resolution': '1600*900',
        'scale': '2.0',
        'reach': '1',
        'rom-version': 'd2que-user 5.1.1 QP1A.190711.020 500220224 release-keys',
        'syscmp-time': '1645693949000',
        'countrycode': 'CN',
        'sysmemory': '3651985408',
        'sysdisksize': '117 GB',
        'bootmark': 'd054ffd6-9a7f-4432-b4e1-29ad86768686',
        'updatemark': '1646287772.690000000',
        'is-hmos': 'false',
        'app-state': '0',
        'act-code': '1648781815',
        'act-timestamp': '1648781815',
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
        'Accept-Encoding': 'gzip, deflate',
        'Connection': 'Keep-Alive',
        # 'session-info': 'FfOEh1Tp8k2/CqniDOJc958Dz3/Se6idDJef6Oyugunup1KU7qCMWp8jXJYOVQKGWZS47xTHq2PvSZpY2roPrDP8fr0x6PUPHg17W0U5XeyCQicvbjPgt4GVyTVEg57o',
        'Host': 'api.douguo.net',
        # 'Content-Length': '118'
    }

    response = requests.post(url=url, headers=headers, data=data)
    return response


def handle_index():
    url = "https://api.douguo.net/recipe/flatcatalogs"
    data = {
        'client': '4,',
        # '_session': '1648781811648,',
        # 'v': 'news1648778940,',
        '_vs': '0,',
        # 'sign_ran': 'e12896fef1697ae02542349f035be7f4,',
        # 'code': 'a37acbcd7086ad95,'
    }

    response = handle_requests(url, data)
    page_text = response.text
    print(page_text)
    json_text = json.loads(page_text)
    # 可以用 jsonpath 去提取 也可以遍历去提取
    # name_list=jsonpath.jsonpath(json_text,"$..name")
    # print(name_list)
    # 遍历 reuslt 下的cs
    for json_item in json_text["result"]['cs']:
        for index_item in json_item['cs']:
            for item in index_item['cs']:
                data_2 = {
                    'client': '4',
                    # '_session': '1648781811648',
                    'keyword': item['name'],
                    'order': '0',
                    '_vs': '400',
                    'type': '0',
                    'auto_play_mode': '2',
                    # 'sign_ran': 'aa65936a7abf00cbd4a719487f065076',
                    # 'code': '423f293442588a81'
                }
                # print(data_2)
                # 需求是通过多线程 线程池来进行抓取
                # queue.put 是放
                queue_list.put(data_2)


def handle_menu_list(data):
    print("当前处理的食材为：", data["keyword"])
    menu_list_url = "https://api.douguo.net/recipe/v2/search/0/20"
    menu_list_response = handle_requests(url=menu_list_url, data=data)
    # print(menu_list_response.text)

    menu_json_text = json.loads(menu_list_response.text)
    for item in menu_json_text['result']['list']:
        menu_info = {}

        # 哪道食材
        menu_info["menu"] = data["keyword"]
        if item['type'] == 13:
            # 厨师昵称
            menu_info['cooker_name'] = item['r']['an']
            # 食材id
            menu_info['menu_id'] = item['r']['id']
            # 食材介绍
            menu_info['describe'] = item['r']['cookstory'].replace("\n", '').replace(" ", '')
            # 菜名
            menu_info['menu_name'] = item['r']['n']
            # 佐料
            menu_info['menu_util_list'] = item['r']['major']
            # 还需要 食材 的做法
            # 构造食材的方法
            detail_url = "https://api.douguo.net/recipe/v2/detail/{}".format(menu_info['menu_id'])
            detail_data = {
                'client': '4',
                # '_session': '1648803222365174d0d6d58a4b4cb',
                'author_id': '0',
                '_vs': '11102',
                '_ext': '{"query":{"kw":' + str(
                    menu_info['menu_name']) + ',"src":"11102","idx":"2","type":"13","id":' + str(
                    menu_info['menu_id']) + '}}',
                'is_new_user': '1',
                # 'sign_ran': '0b705139094fb19a6ae7cae50f0249d5',
                # 'code': '469de5e50cefa60a'
            }

            detail_response = handle_requests(url=detail_url, data=detail_data)
            # 解析出 制作方法
            # print(detail_response.text)

            detail_response_json = json.loads(detail_response.text)
            # 制作方法
            menu_info['tips'] = detail_response_json['result']['recipe']['tips']
            # 制作步骤
            menu_info['cook_step'] = detail_response_json['result']['recipe']['cookstep']
            # print(menu_info)
            print("当前入库的菜谱是:", menu_info['menu_name'])
            # 插入mongo
            mongo_info.insert_mongo(menu_info)

        else:
            continue


handle_index()

# 通过多线程 来请求 队列中的数据 # 每秒请求几个 就 写几个 workers
pool = ThreadPoolExecutor(max_workers=20)

# 判断 线程队列的大小数字 是否大于20  大于20 则 执行
while queue_num := queue_list.qsize() >= 20:
    # submit 前面执行的是函数  后面的传入的参数
    pool.submit(handle_menu_list, queue_list.get())




# # get 是取出
# handle_menu_list(queue_list.get())
