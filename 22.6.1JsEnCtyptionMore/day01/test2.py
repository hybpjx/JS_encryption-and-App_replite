"""

湛江市麻章区政府办公室
http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc
"""
import re

import requests

start_url = "http://www.zjmazhang.gov.cn/hdjlpt/published?via=pc"

with requests.session() as session:
    response = session.get(start_url)
cookie = response.cookies
szxx_session = cookie['szxx_session']
csrf_token = cookie['XSRF-TOKEN']

html = response.text

X_CSRF_TOKEN = re.search(r"var _CSRF = '(.*?)';", html).group(1)

"""
经过反复测试  可发现 

一旦去除cookie中的szxx_session
就会失败请求  所以 可以得知 szxx_session 是重要cookie参数

其他cookie值都可以删除

现在 问题来了？ 如何动态拿到cookie

"""
post_url = "http://www.zjmazhang.gov.cn/hdjlpt/letter/pubList"

print(szxx_session)
print(csrf_token)
print(X_CSRF_TOKEN)
headers = {
    'Cookie': f'XSRF-TOKEN={csrf_token}; szxx_session={szxx_session}',
    # 'Cookie': "XSRF-TOKEN=eyJpdiI6Ikl1UE5VQkRqVEM3anI5bDdPM1pJMHc9PSIsInZhbHVlIjoiNzNpZktBbStIbUUxa0RseEI1MDZmbUEzTEFSM1pLVmQxa2pFYmw2YndhVWRsU0Q5U3JGQlozRGZUZHpaNVRQZSIsIm1hYyI6Ijc5ZjcyMTVlNTk2Y2FhNjNkMDQzMjVhYzU0MTA1OGU5N2M0MTkyY2VkYjM4MDg4YmZjMDlmOGI1ZWVmMzgxOWMifQ%3D%3D; szxx_session=eyJpdiI6IlpZcHhEMDRHVXJBU0xNU0UxcmhUN0E9PSIsInZhbHVlIjoiXC9rMDY4TVJSa1c2RE5OZEFwQTJNVmY4ZDZ3WUhOSHRoZWh1ZFdsZEFhaE9hd0ErNTBjRnJLVjE3Vzd0QnMwaUQiLCJtYWMiOiI4Yjk0MDk0OTA3YWU3MGEzOGZkZDg1MjIzMDY1YTk1NDk4N2UzMGYwYjA0NGFlMDZmNTBjY2Y0NjFmYTcxYzQ0In0%3D",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    'X-CSRF-TOKEN': str(X_CSRF_TOKEN),
    # 'X-CSRF-TOKEN': "Cy8r5llgXWmimNPYEOJjqzOnTGPbkRGkwamrylAl",
    # 'X-CSRF-TOKEN': "KikzUbyJhBg35WGmcWZBZq7lIPUz2RU0hKPH4Kop",
}

form_data = {
    "offset": "0",
    "limit": "20",
    "site_id": "759010",
}
response = session.post(post_url, data=form_data, headers=headers)

print(response.status_code)

print(response.text)  # {"errcode":419,"errmessage":"页面已失效，请刷新重试","data":null,"trigger":null}
