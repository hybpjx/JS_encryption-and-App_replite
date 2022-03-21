import json
import re
import base64

import fake_useragent
import jsonpath
import requests
from hashlib import md5


class GetPic():

    def get_text(self):
        formdata = {
            "width": "150",
            "height": "40",
            "codeNum": "4",
            "interferenceLine": "4",
            "codeGuid": "",
        }
        page_text = requests.post(
            "http://ggzy.tongliao.gov.cn/EpointWebBuilder_tlsggzy/jyxxInfoAction.action?cmd=getVerificationCode",
            data=formdata).json()
        return page_text

    def get_Code(self):
        #  提取出来 Json中 图片的信息
        code = re.search(r"""\{"imgCode":"(.*)\",\"""", str(self.get_text())).group(1)
        # 还需要提出来uuid
        uuid = re.search(r""",\"verificationCodeGuid":\"(.*)\"\}\'""", str(self.get_text())).group(1)
        # print(code)
        # print("***"*50)
        # print(uuid)

        # 由于前面 某些数据是我们不需要 所以我们切割
        data = code.split(',')[1]
        image_data = base64.b64decode(data)
        with open('code.png', 'wb') as f:
            f.write(image_data)
        return uuid


class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password = password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files,
                          headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()


if __name__ == '__main__':
    uuid = GetPic().get_Code()
    chaojiying = Chaojiying_Client('hybpjx', 'jklop123123', '918259')  # 用户中心>>软件ID 生成一个替换 96001
    im = open('code.png', 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    Code_data = chaojiying.PostPic(im, 8001)  # 1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    pic_str = Code_data["pic_str"]
    print(pic_str)

    print(f"uuid是————————{uuid}——————————")

    url = "http://ggzy.tongliao.gov.cn/EpointWebBuilder_tlsggzy/jyxxInfoAction.action?"

    params = {
        "cmd": "getInfolist",
        "fbdate": "",
        "jyfrom": "",
        "xxtype": "010",
        "jytype": "",
        "title": "",
        "pageSize": "12",
        "pageIndex": "1427",
        "imgguid": str(uuid),
        "yzm": str(pic_str),
    }

    # url=f"http://ggzy.tongliao.gov.cn/EpointWebBuilder_tlsggzy/jyxxInfoAction.action?cmd=getInfolist&fbdate=&jyfrom=&xxtype=010&jytype=&title=&pageSize=12&pageIndex=11&imgguid={uuid}&yzm={pic_str}"

    headers = {
        # 'User-Agent': fake_useragent.UserAgent().random,
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "http://ggzy.tongliao.gov.cn/tlsggzy/jsgc/subpage.html",
        "Host": "ggzy.tongliao.gov.cn",
        "Pragma": "no-cache"
    }

    page_text = requests.get(url=url, headers=headers, params=params).json()
    code = requests.get(url=url, headers=headers, params=params).status_code
    # ensure_ascii 保留中文
    json_dump_text = json.dumps(page_text, ensure_ascii=False)
    print(page_text)
    # 转换为Json
    json_text = json.loads(json_dump_text)
    json_dump_text = json_text["custom"]
    json_text = json.loads(json_dump_text)
    # 根据json提取 其中的值
    title_url_list = jsonpath.jsonpath(json_text, "$..infourl")
    title_name_list = jsonpath.jsonpath(json_text, "$..realtitle")
    title_date_list = jsonpath.jsonpath(json_text, "$..infodate")

    for url, name, date in zip(title_url_list, title_name_list, title_date_list):
        print(url)
        print(name)
        print(date)
