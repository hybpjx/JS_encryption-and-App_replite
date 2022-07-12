import requests

target_url="http://zrzyt.hubei.gov.cn/bmdt/ztzl/kczyclylyglxxgs/kczyclpsba/"

"""
无限Debugger 死循环问题解决方案

http://zrzyt.hubei.gov.cn/bmdt/ztzl/kczyclylyglxxgs/kczyclpsba/
"""

with requests.session() as session:
    response=session.get(target_url)


# 获取cookie

dynamic_cookie=response.cookies['FSSBBIl1UgzbN7N80S']
headers={
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Encoding': 'gzip, deflate',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
    "Cookie": f"Secure; FSSBBIl1UgzbN7N80S={dynamic_cookie}; dataHide2=baa5f1e1-c8a3-48b6-b266-d56b8d1db2a5; _trs_uv=l3ayn0hk_3010_kgz0; Hm_lvt_5544783ae3e1427d6972d9e77268f25d=1654069243; Secure; _trs_ua_s_1=l42ke1z3_3010_azqe; FSSBBIl1UgzbN7Nenable=true; FSSBBIl1UgzbN7N80T=47OPJWJnga1cv3hD.fjR0qJ_u7GVzvUiPF4VO5tzxLfMx669JXhIpG_cQs3ayM0lR3z3WeVm7JWQnCwujbc0NXIsCI1LgFXS.wBQIiU0QB66E20QRhOCE1XJIfbl7cLIyB_XjUlgigF0bHDpt_72KvRGOGO6uGKWDxFzMPAtn0FP3e0LiD6ZMG1Xs8H.7a4ARh_1PNLfdscI8dnyccJKlNwEeV1nFm7_qS_OIy69HNp1HIMbtOqgRb030RRlAiXArqzZFVse6J41DF0Ye8rm12SMWULBxAYNb1Q9iZ5coSQrblAZw_OuCLV7yscbfI11xH9qN0ecQCRBgbB3HHXlm_.UInDb15RRnISkkjrejQSiD6bi.ZWFPeAu0w3SLYHBTXeVMgSgjfZWZlWzv4nYGXs6L",
  'Host': 'zrzyt.hubei.gov.cn',
  'Referer': 'http://zrzyt.hubei.gov.cn/bmdt/ztzl/kczyclylyglxxgs/kczyclpsba/',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36'
}


"""
如果 只有单个传参 加密  例如

s：1000
b：kasjdkasjdlsadj

直接搜索 
var s 
var b


js中生成 时间戳的代码

Date.parse(new Date())

"""


print(session.get("http://zrzyt.hubei.gov.cn/bmdt/ztzl/kczyclylyglxxgs/kczyclpsba/index_1.shtml").text)