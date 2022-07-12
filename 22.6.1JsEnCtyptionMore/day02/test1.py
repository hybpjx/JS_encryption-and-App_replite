# -*- coding: utf-8 -*-
# 百度翻译 https://fanyi.baidu.com/?aldtype=16047#en/zh/dog
import re

import execjs
import requests


class BaiduTranslatePro:
    def __init__(self, query):
        self.query = query
        self.url = "https://fanyi.baidu.com/v2transapi?from=en&to=zh"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36 Edg/102.0.1245.39',
            'Referer': 'https://fanyi.baidu.com/',
            'Cookie': 'BAIDUID=070900C3687ED8D716A622B72D844144:FG=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1636719409; __yjs_duid=1_7b81f444ae26e8c4b848367282b895731636719409492; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1636719410; __yjs_st=2_Y2FlZTAwMjZhYzA3NDVjMDcxNGYwNzdiZjUwZjM0NGFlMzE3YjA3OThhNTAzYjgwMTliNDcxMmQxMGI1MmI0YTJhMGQ2ZTk2ODZhN2ZjNTliYmY3MTdjMzRjYTFmMzkyZDk2ZGUzMWRiZTJlMDA5MjExOTg0YjBkZDE1OTBiMzcxY2UyZGM2NjJmODI2OGU5NWIxNGU3NWY3MDUzY2QwM2M5NWNmMjM0NTE5OGM5OGFmZjQ4NjYxNDI4YWE2MGRkM2U0MWQ1NGQ1ZDE3ZjA3YjE1MTM3OTFhMDVjMjcwNzYwYzA2YTJlZWJmNGY5ZTZkYmIwZTU1MzhkMTVjYWFhZl83XzVhMDQ1YjE3; ab_sr=1.0.1_OWVlYWE5NzE0MDZjYzE5NzVkMTllNTNiNTgyZjVkYWJiMWUyYzcyNGM0ZTQ1ZDY5YjY4OGY1NTMzMmM3YjYwZDE0ZWVlZjQyZTIwMWFjZGJkNjYyM2VkMTdiNDNkZTVlOTEyYjk1OGVmMGIyMTY4YjUzOWRkMjQ0NzM5MzRlMGRjNDI5N2RmMzQ1MmE0NzIyZDFkMjEwYzgxYzQyNjJhZQ=='

        }
        self.payload = {
            "from": "en",
            "to": "zh",
            "query": self.query,
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": "",
            "token": "d693919bc24c526cf4b8229f17f7b543",
            "domain": "common",
        }
        self.token_url = 'https://fanyi.baidu.com/'
        self.session = requests.session()

    # 获取 token
    def get_token(self):
        # 发送请求
        response = self.session.get(self.token_url, headers=self.headers)
        # 返回 token
        return re.findall("token: '(.*?)'", response.content.decode())[0]

    def get_sign(self):
        # 实例化一个node对象
        node = execjs.get()
        # 加载js
        ctx = node.compile(open("1.js", mode="r", encoding="utf-8").read())
        # 调用函数名
        funcName = "e()"

        sign = ctx.eval(funcName)

        self.payload['sign'] = sign
        self.payload['token'] = self.get_token()
        print(self.payload)


    def main(self):
        """
        通过构造的新的表单数据，访问api，获取翻译内容
        :return:
        """
        self.get_sign()
        response = self.session.post(self.url, headers=self.headers, data=self.payload)
        response.encoding = response.apparent_encoding

        json_text = response.json()

        return json_text


if __name__ == '__main__':
    print(BaiduTranslatePro("cat").main())
