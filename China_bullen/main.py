import base64
from statistics import mode
import requests
import pyDes
# ctpstp@custominfo!@#qweASD


# https://ctbpsp.com/#/bulletinList

headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Connection': 'keep-alive',
  'Host': 'custominfo.cebpubservice.com',
  'Origin': 'https://ctbpsp.com',
  'Referer': 'https://ctbpsp.com/',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'cross-site',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36'
}


response = requests.get("https://custominfo.cebpubservice.com/cutominfoapi/recommand/type/5/pagesize/10/currentpage/1",headers=headers,verify=False)



page_text = response.text[1:-1]
data=base64.b64decode(page_text)
key = "ctpstp@custominfo!@#qweASD"[0:8]
des_obj = pyDes.des(key=key,mode=pyDes.ECB,padmode=pyDes.PAD_PKCS5)
text = des_obj.decrypt(data).decode("utf-8")
print(text)
