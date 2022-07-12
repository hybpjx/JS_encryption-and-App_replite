# -*- coding: utf-8 -*-
# @Time    : 2022/6/28 17:18
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : test.py
# @Software: PyCharm
"""
新浪微博：http://my.sina.com.cn/profile/unlogin

找到包为： https://login.sina.com.cn/sso/prelogin.php?entry=account&callback=pluginSSOController.preloginCallBack&su=MTc3NzIyMzEwOTY%3D&rsakt=mod&checkpin=1&client=ssologin.js(v1.4.19)&_=1656409115902

"""
import re
import time

import requests
import binascii
su = binascii.b2a_base64(b"17772231096").decode()
url = "https://login.sina.com.cn/sso/prelogin.php"
params = {
    "entry": "account",
    "callback": "pluginSSOController.preloginCallBack",
    "su": su, # base64 加密
    "rsakt": "mod",
    "checkpin": "1",
    "client": "ssologin.js(v1.4.19)",
    "_": int(time.time()*1000),
}
headers={
  'cache-control': 'no-cache, must-revalidate',
  'content-type': 'application/javascript; charset=utf-8',
  'date': 'Thu, 07 Jul 2022 10:02:51 GMT',
  'dpool_header': 'gz-pub-10-191-8-21',
  'expires': 'Sat, 26 Jul 1997 05:00:00 GMT',
  'server': 'nginx',
  'x-via-ssl': 'ssl.47.sinag1.shx.lb.sinanode.com',
  'accept': '*/*',
  'accept-encoding': 'gzip, deflate, br',
  'accept-language': 'zh-CN,zh;q=0.9',
  'referer': 'http://my.sina.com.cn/',
  'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'script',
  'sec-fetch-mode': 'no-cors',
  'sec-fetch-site': 'cross-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

# resp  = requests.get(url, params=params,headers=headers)
#
# text = re.search(r"(\(.*\))", resp.text).group(1)
#
#
# print(text)


# 搜索 rsakt
import execjs

with open("1.js", encoding="utf-8") as fp:
    js_code = fp.read()
res=execjs.compile(js_code).call("get_result",{"retcode":0,"servertime":1657188468,"pcid":"gz-529181a8a750b461df6eaa54cb549e9d6158","nonce":"4AGMHS","pubkey":"EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443","rsakv":"1330428213","is_openlock":0,"lm":1,"smsurl":"https:\/\/login.sina.com.cn\/sso\/msglogin?entry=account&mobile=17772231096&s=a78aa95837e0d3f3295b1e49734a5aaa","showpin":0,"nopwd":1,"exectime":35})
print(res)
