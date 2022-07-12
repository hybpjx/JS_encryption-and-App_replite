from selenium import webdriver

# bro=webdriver.PhantomJS(r"D:\phantomjs-2.1.1-windows\bin\phantomjs.exe")
from selenium.webdriver import DesiredCapabilities

user_agent = "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.3 Safari/537.36"

dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
dcap["phantomjs.page.customHeaders.User-Agent"] = user_agent

SERVICE_ARGS = ['--load-images=false',  # 设置PhantomJS不加载图片
                '--disk-cache=true',  # 开启缓存（可选）
                '--ignore-ssl-errors=true'  # 忽略https错误（可选）
                # '--proxy-type=http',  # 代理类型：http/https
                ]

# --cookies-file=/path/to/cookies.txt       # 指定cookies文件
# --disk-cache=[true|false]                 # 是否应用磁盘缓存
# --ignore-ssl-errors=[true|false]          # 是否忽略ssl证书错误
# --load-images=[true|false]                # 是否加载图片
# --output-encoding=encoding                # 指定输出编码 默认是utf8
# --proxy=address:port                      # 指定代理服务器，格式是--proxy=192.168.1.42:8080
# --proxy-type=[http|socks5|none]           # 指定代理服务器协议类型
# --proxy-auth                              # 代理服务器认证，格式是--proxy-auth=username:password


bro = webdriver.PhantomJS(desired_capabilities=dcap, service_args=SERVICE_ARGS)

bro.get("http://mpnr.chengdu.gov.cn/ghhzrzyj/ckqsp/zwgk_dzkc_list_2.shtml")
print(bro.page_source)

bro.close()
