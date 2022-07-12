# -*- coding: utf-8 -*-
# @Time    : 2022/6/27 16:03
# @Author  : lzc
# @Email   : hybpjx@163.com
# @File    : test4.py
# @Software: PyCharm
# http://cfx.health.xywy.com/question/1/index.htm
# http://cfx.health.xywy.com
import requests
from lxml import etree


def start_request():
    start_url="http://cfx.health.xywy.com/question/1/index.htm"
    response=requests.get(start_url)
    tree=etree.HTML(response.text)
    print(tree.xpath("//input[@name='_csrf']/@value")[0])

def request():
    headers={
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Encoding': 'gzip, deflate',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Content-Length': '480',
      'Content-Type': 'application/x-www-form-urlencoded',
      'Cookie': 'PHPCFXSESSID=f7qcu5jj72v9r44ap4gopgbus2; Hm_lvt_eaee4f1985af67cf84c51be1767282a2=1656317062; _csrf=c18d16c0252c7b962cf859b2290523aee151ac6e5368091e0bd5495c9c4136e0a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22GqNemzkyrKuSXZzzIdvEE1k0VOnm_K0L%22%3B%7D; f7qcu5jj72v9r44ap4gopgbus2=%7B%220%22%3A9890%2C%222%22%3A9891%7D; Hm_lpvt_eaee4f1985af67cf84c51be1767282a2=1656317184',
      'Host': 'cfx.health.xywy.com',
      'Origin': 'http://cfx.health.xywy.com',
      'Referer': 'http://cfx.health.xywy.com/question/1/index.htm',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    form_data = {'_csrf': 'Q1BySEpkb3QEITwtJx4EDTEbBxsSPhUOCjQEDQ9VBEQVHxwlFS9fOA==',
                'params[age]': '24',
                'params[gender]': '1',
                'params[hbp_his]': '2',
                'params[diab_his]': '2',
                'params[diab_family]': '1',
                'params[smoke_status]': '1',
                'params[vegetable]': '1',
                'params[fru]': '4',
                'params[is_act]': '1',
                'params[act_freq]': '5',
                'params[act_time]': '2',
                'params[act_intensity]': '3',
                'params[waist]': '80.0',
                'params[tg]': '15.00',
                'params[hdl]': '10.00',
                'params[height]': '176.0',
                'params[weight]': '150.00',
                'params[fbg]': '25.00'}


    response = requests.post("http://cfx.health.xywy.com/question/1/index.htm",headers=headers,data=form_data)

    print(response.text)


# request()

start_request()