"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/4/1 17:37
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : save_mongo.py
# @Software: PyCharm
"""
import pymongo
from pymongo.collection import Collection


class ConnectMongo(object):
    def __init__(self):
        # 定义一个链接对象
        self.client=pymongo.MongoClient(host="127.0.0.1",port=27017)
        #  定义数据库的名字
        self.db_data= self.client['dou_guo_mei_shi']

    def insert_mongo(self,item):
        # 前面是数据库的名字 后面是表名
        db_collection  = Collection(self.db_data,"dou_guo_mei_shi")
        # 已经不支持调用了
        # db_collection.insert(item)
        # 用insert_one
        db_collection.insert_one(item)



# 创建一个mongo 实例
mongo_info = ConnectMongo()