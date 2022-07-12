# -*- coding: utf-8 -*-
# https://qimingpian.cn/finosda/project/pinvestment
import fake_useragent
import requests
import json

import execjs



target_site = "https://qimingpian.cn/finosda/project/pinvestment"

def request():
    url = "https://vipapi.qimingpian.cn/DataList/productListVip"
    headers={
        "User-Agent":fake_useragent.UserAgent().random
    }
    data = {
        "time_interval":"",
        "tag":"",
        "tag_type":"",
        "province":"",
        "lunci":"",
        "page": "1",
        "num": "20",
        "unionid":"",
    }

    response=requests.post(url,headers=headers,data=data)
    return response.json()['encrypt_data']

    
encrypt_data = request()
# 加载js

with open("../../replite_js_enctyption/js/qimingkeji.js",mode="r",encoding="utf-8") as f:
    jscode=f.read()
results = execjs.compile(jscode).call("s",encrypt_data)
print(json.loads(results))