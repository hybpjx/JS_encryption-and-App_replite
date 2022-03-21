[toc]
# 爬虫JS高阶逆向

# js逆向

- 爬虫的js加密处理+js算法改写分析
- 涉及到的相关的内容
    - 线性散列MD5算法
    - 堆成加密DES/AES算法
    - 非对称加密算法RSA
    - base64伪加密
    - https证书加密
- 可以处理的爬虫问题
    - 模拟登录中密码加密和其他请求参数加密处理
    - 动态加载且加密数据的捕获和破解
    - 重点：找寻到js算法加密和解密相关流程的编码于处理套路/技巧，大幅度提升处理相关问题的效率

# 0\. 常见的加密算法

### **js常见的加密方式**

- 加密在前端开发和爬虫中是经常遇见的，掌握了加密算法 且可以将加密的密文 进行解密破解的密文 进行解密破解的，且加密算法的熟练和刨析也是有助于 实现高效的js逆向只把加密算法进行总结 不去深究加密的具体实现方式
- 常见的加密算法 基本分为这几类
    - 线性散列算法 （签名算法）md5
    - 对称加密算法 AES DES
    - 非对称加密算法 RSA

### **Md5 加密**

- MD5 是一种被广泛使用的线性散列算法 ，可以产生出一个128位（16字节） 的散列值(hash value), 用于确保信息传输完整的一致性 且 MD5 加密之后生成的是一个固定长度(32位 或者 16位)的数据
- 解密：
    - 常规讲MD5 是不存在解密的,但是理论上MD5是可以进行反向暴力破解的，暴力破解的大致原理就是用很多不用的数据 进行加密后跟已有的加密数据进行对比 由此来寻找规律。理论上只要数据量足够庞大 MD5 是可以被破解的，但是要注意 破解MD5 是需要考虑时间和成本的（时间和机器性能）。假设破解当前的MD5密码需要 目前计算能力最优秀的计算机工作100年才能破解完成 。 那么当前的MD5就是安全的。
- 增加破解成本的方法（方法很多）
    - 将一段无意义且随机私钥进行MD5加密 会生成一个加密串，我们暂且称之为1
    - 将要加密的数据和 1 拼接 再进行一次MD5 这时会生成 2
    - 将 2 再进行MD5 加密，这时 生成的3 就是我们加密后的数据
- 我们在注册账号时的密码一般都是用的MD5 加密

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script src="../js/md5.js"></script>
    <script type="application/javascript">
        let hashCode = md5("i am lzc")
        alert(hashCode)
    </script>

</head>
<body>
</body>
</html> 
```

DES/AES加密

- DES全称为Data Encryption Standard，即数据加密标准，是一种使用密钥加密的块算法，该加密算法时一种对称加密算法，其加密运算，解密运算 需要使用同样的密钥（一组字符串）即可。
- 注意
    - 现在用AES这个标准来替代原先的DES
    - AES和DES的区别
        - 加密后密文长度的不同：
            - DES加密后密文长度是8的整数倍
            - AES加密后密文长度是16的整数倍
        - 应用场景不同
            - 企业级开发DES足够安全
            - 如果要求搞使用AES
        - DES和AES切换只需要修改CryptoJS.AES &lt;=&gt;CryptoJS.DES
- 使用DES/AES进行数据交互时要求双发都拥有相同的私钥
- 破解方法：
    - 暴力破解
    - DES如果使用56位的密钥，则可能密钥的数量时2的56次方个。只要计算足够强大时可以被破解的
- DES算法的入口参数有三个：
    - Key，Data，Mode，padding。
        - Key为7个字节共56位，是DES算法的工作密钥；
        - Data为8个字节64位，是要被加密或者是被解密的数据；
        - Mode为DES的工作方式
        - Padding的赋值归档位CryptoJs.pad.Pkcs7即可

```html
 <script src="../js/crypto-js.min.js"></script>

    <script type="application/javascript">
        let aseKey = "123456"
        let message = "i am lzc who are you"

        //    加密 DES/AES 切换 只需要修改CryptoJS.AES<==> CryptoJs.DES
        let encrypt = CryptoJS.DES.encrypt(message, CryptoJS.enc.Utf8.parse(aseKey), {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString();

        alert(encrypt);

        // 解密
        let decrypt = CryptoJS.DES.decrypt(encrypt, CryptoJS.enc.Utf8.parse(aseKey), {
            mode: CryptoJS.mode.ECB,
            padding: CryptoJS.pad.Pkcs7
        }).toString(CryptoJS.enc.Utf8);

        alert(decrypt);
    </script> 
```

### **RSA加密**

- RSA加密
    - RSA加密算法是一种非对称加密算法。在公开密钥加密和电子商务中被广泛使用。
- 非对称加密
    - 非对称加密需要两个密钥
        - 公开密钥
        - 私有密钥
        - 公钥和私钥是一对，如果用公钥对数据进行加密 只有用对应的私钥才能解密，因为加密和解密使用的是两个不同的密钥，所以这种算法 叫做非对称加密算法。
    - 注意
        - 使用时都是使用公钥加密使用私钥解密，公钥可以公开 私钥自己保留
        - 算法强度复杂，安全性依赖于算法于算法于密钥但是由于其算法复杂，而使得加密解密速度没有堆成加密解密的速度快
    - 使用流程和场景介绍
        - 使用公钥加密，使用私钥解密 私钥是通过公钥计算生成的，假设ABC三方之间相互要进行加密通信，大家相互之间使用公钥进行信息加密，信息读取时，使用各自对应的私钥进行信息解密
    - 用户输入的支付密码会通过RSA加密
- 公钥私钥生成方式
    - 公司要可以在线生成
        
        - `http://web.chacuo.net/netrsakeypair`
        
        ```html
         <script src="../js/jsencrypt.min.js"></script>
            <script>
                let PUBLIC_KEY="-----BEGIN PUBLIC KEY-----\\n" +
                    "MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQDBhRaag3TE7qu9pLNQGA/bJ+PU\\n" +
                    "hRiPGC464fAqmkNJwsr2LMZ6awWtxJ8ufpK8WPZptboMayssB8CNnqQX8vCPmArg\\n" +
                    "VNw+ysPtnhbN/KBmIq3R/62+O2IkJd5cPL1PwDNCFAmANTqaiEGKLrJgCklCC51c\\n" +
                    "WJhAzIPZ6/GIVxoSVwIDAQAB\\n" +
                    "-----END PUBLIC KEY-----";
                let PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\\n" +
                    "MIICeAIBADANBgkqhkiG9w0BAQEFAASCAmIwggJeAgEAAoGBAMGFFpqDdMTuq72k\\n" +
                    "s1AYD9sn49SFGI8YLjrh8CqaQ0nCyvYsxnprBa3Eny5+krxY9mm1ugxrKywHwI2e\\n" +
                    "pBfy8I+YCuBU3D7Kw+2eFs38oGYirdH/rb47YiQl3lw8vU/AM0IUCYA1OpqIQYou\\n" +
                    "smAKSUILnVxYmEDMg9nr8YhXGhJXAgMBAAECgYEApG/6bQEWz+Aeft7cn0pS7t5O\\n" +
                    "cd9GpxDc95vU/95lHuAuplAVtyAJi0ZwHInhFbpiaCDLHpJR9PABZlVPCiqczWwH\\n" +
                    "kpbbrBt8vvNRZ8hsRdVmcWntf4Nn1HQeY8tO0wDgCZ9SIrz6FrrwucDQ6QNG6U8h\\n" +
                    "qXR0YHLKra3QM+fcZAECQQDv8tJ86tV+kPnEHKauthGySgP0XDM0TK5An/vW8XRh\\n" +
                    "mElTXlHM0L9i4T1+9WQ84lB9Ozj9qBo3Pht8oMiZNcbBAkEAzncp/BC7KmXNkSiN\\n" +
                    "DljjMnBZ3biMBDfiQdVYATzg2cFazR5a8rUCgqS3/iISxK+9V8HA/Loj+c32Ezy8\\n" +
                    "GcH3FwJBALq8U9lJfMsaEnbwATw4j38cIQW791F9V6MNnpWBpZwKQw5xeeGWl0th\\n" +
                    "lVVHrjG/wvoi69BkUbqqSAPusQ6jDkECQDSoienDLqlqm5p5ODi/jPrRUupM5lEx\\n" +
                    "G6Dk0/RE3ahMO2dzZYjfh8tgTZkggZ7un6EhRqJuqzxMPoW7iNIc+XMCQQCrf82P\\n" +
                    "D0yNHu9c0MfqBH8o2iEuVmYfxjB9DFfAeyb8dErWJO7E8wQMI3WFhCjervhTboxK\\n" +
                    "LpGqIA5WSAlmufwK\\n" +
                    "-----END PRIVATE KEY-----\\n";
                // 实例化一个加密对象
                let encrypt = new JSEncrypt();
                // 设置公钥
                encrypt.setPublicKey(PUBLIC_KEY);
                // 对数据进行加密
                let encrypted = encrypt.encrypt("hello,lzc");
                alert(encrypted);
        
                // 使用私钥解密
                let decrypt = new JSEncrypt();
                // 设置私钥
                decrypt.setPrivateKey(PRIVATE_KEY);
                // 解密
                let uncrypted = decrypt.decrypt(encrypted);
                alert(uncrypted)
        
            </script> 
        ```
        

### **base64 伪加密**

- Base 是一种用64个字符来表示任意二进制数据的方法。 base64是一种编码方式而不是加密算法 只是看上去更像是加密而已
- Base64 使用A-Z，a-z，0-9 ，+，/ 这64个字符实现对数据进行加密。

```html
 <script type="text/javascript">
        window.btoa('china is so nb') // 编码
        window.atob("Y2hpbmEgaXMgc28gbmI=") // 解码
    </script> 
```

## **扩展： https 对称密钥加密**

- https 是基于http 和SSL/TLS实现的一个协议 ，他可以保证网络上传输的数据都是加密的，从来保证数据安全
    
- 解析来我们从http协议开始 提出想法 并逐步进行分析 最终实现https。
    
- http协议是不安全的
    
    1.  在https诞生之前 所有的网站都是使用http协议。 而http协议在数据传输的过程中都是名为呢 所以可能存在数据泄露和篡改
    2.  使用对称密钥进行数据加密
        - 为了防止 数据泄露和篡改，我们对数据进行加密 如：生成一个堆成密码【askdjlasd】 我们将堆成密钥 分别交给浏览器和服务器端，他们之间传输的数据都是用堆成密钥进行加密和解密
- 请求响应流程如下：
    
    - 客户端使用对称密钥对请求进行加密，并发送给服务端
    - 服务端接收到密文之后，使用对称密钥对密文进行解密，然后处理请求，最后再使用堆成密钥要把返回的内容再次进行加密 然后返回给客户端
    - 客户端接收到密文之后，使用对称密钥进行解密，并获取最终的响应内容
- 如此一来，数据传输都是密文，解决了铭文传输的问题，但是，这么干有bug
    
    - 浏览器如何获取堆成密钥？
        
    - 每个客户端的堆成密钥相同，浏览器能拿到对称密钥，那么黑客页可以拿到，所以，数据加密也就没有了意义
        
       ![811fa1ac534a92552deb39af95092d49.png](:/b0ef1f2df7ad42e6b199077965a4a6ac)
        
    
    一言蔽之： 证书用于管理公钥。（公钥要公开。如何避免公钥被替换或损毁，引入了证书。）
    
    私钥在服务器端，公钥一般在证书中
    
    比方 证书好比身份证（公钥+姓名+数字签名）。
    
    证书机构（CA）好比公安局，负责管理和分发身份证。
    
    证书内容 证书实际上是对于非对称加密算法来说的，一般证书包括公钥、姓名、数字签名三个部分。
    
    CA登记 HASH(公钥+姓名) 标识唯一性，也就是证书里的数字签名。
    
    甲方 发送数据给 乙方，
    
    去CA查找乙方的身份证书，上面有乙方的信息，可以保证公钥就是乙方的。
    
    然后把要加密的信息进行加密 给乙方。
    

# **js逆向 实战**
## js 解密 + 混淆 破解

原文博客地址：https://www.cnblogs.com/bobo-zhang/p/11243138.html

- 爬取的网站 https://www.aqistudy.cn/html/city_detail.html
- 分析
	-  1. 通过分析发现，只有在页面中设置了查询的城市名称和时间范围后，然后点击查询按钮，在抓包工具中才会捕获到一个ajax请求的数据包，我们想要爬取的数据也在该数据包中：
	-  2. 分析捕获到的数据包
		-  提取出请求的url:https://www.aqistudy.cn/apinew/aqistudyapi.php
		-  请求方式： post
		-  请求参数：d： 动态变化的一组数据（且加密的）
		-  响应数据：是加密的密文数据
			-  问题： 该数据包请求的是密文数据，为何在前端显示的却是原文数据？
			-  原因：请求请求到密文数据后，前台接收到密文数据后使用指定的解密操作（js 函数）对密文数据进行了系欸，然后将原文数据展示在了前端页面
			-  下一步工作的步骤
				-  首先先处理动态变化的请求参数，动态获取该参数的话，就可以携带该参数进行请求发送，将请求到的密文数据捕获到。
				-  将捕获到的密文数据找到对应的解密函数 对其进行解密即可。
				-  需要找到点击查询后对应的ajax请求代码，从这组代码中就可以破解动态变化的请求参数和加密的响应数据对应的相关操作。
	-  3. 找ajax请求对应的代码，分析代码 和获取参数d的生成，和加密的响应数据的解密操作
		-  基于火狐浏览器定位查询按钮绑定的点击事件  可以查看event 点击时间
			![7801c05032576f09c15e35323a0414fe.png](:/2fc0cbb1d6484fbb8d691f23cfdf782b)
		-  从getData 函数实现中找寻ajax请求对应的代码
			-  在该函数的实现中没有找到ajax代码，但是发现了另外两个函数的调用
				-  getAQIData();getweatherData(); ajax 代码一定存在于两个函数内部的
				-  type == "HOUR"； 查询时间是以小时为单位的
		-  分析这两个函数——> 从而找到 ajax请求代码
			-  没有找到ajax请求代码
			-  发现了另一个函数的调用：getServerData(method,param,func,0.5)
				-  method='GETCITYWEATHER' or 'GETDETAIL'
				-  params= {city,type,startTime,endTime}: 查询条件
		-  分析getServerData， 找寻ajax代码l
			-  基于抓包工具 做全局搜索 
			-  找到的函数实现 被加密了
		-  对getServerData加密的实现进行解密
			-  js混淆： 对核心的js代码  进行加密
			-  js反混淆： 对js加密代码 进行解密
				-  暴力破解：[https://www.dingk.cn/jsConfusion/](https://www.dingk.cn/jsConfusion/)
				-  得到了ajax的代码
				-  结论：
					-  data: 加密的响应数据
						-  decodeData(data)将加密的响应数据进行解密
							-  参数data： 加密的响应数据
					-  param： 动态变化且加密的请求参数
						-  getParam(method,object) 返回动态变化的请求参数
							-  参数method：method='GETCITYWEATHER' or 'GETDETAIL'
							-  参数object：{city,type,startTime,endTime} 查询条件
						
		-  js逆向
			-  现在 只需要 调用两个js函数(decodeData,getParam) 返回结果即可。
			-  js逆向：在python中调用js函数
				-  方式1
					-  手动的将js函数改写为python函数
				-  方式2
					-  使用固定模块 实现自动逆向 PyExecJs
					-  在本机装好nodejs的环境
					-  
		-  Py ExecJs的使用

发起请求

```
import execjs
import requests

node = execjs.get()
 
# Params
method = 'GETCITYWEATHER'
city = '北京'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'
 
# Compile javascript
file = 'jsCode.js'
ctx = node.compile(open(file).read())
 
# Get params
js = 'getPostParamCode("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)

#发起post请求
url = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response_text = requests.post(url, data={'d': params}).text

#对加密的响应数据进行解密
js = 'decodeData("{0}")'.format(response_text)
decrypted_data = ctx.eval(js)
print(decrypted_data)
# 执行会报错 ： 目前 页面中没有数据，解密函数只是针对页面的原始数据
```

js加密
js解密
js混淆
js反混淆
js逆向



## **微信公众号平台JS算法 逆向**

- JS调试工具
    - 发条Js调试工具
- PyExecJs
    - 实现使用python 执行JS代码
    - 环境的安装
        - node.js 开发环境
        - pip install PyExecJs
- js算法改写初探
    - 打断点
    - 在代码调试时 发现相关变量的缺失，一般给其定义为空字典即可。

## steam 密码加密

详见github

**steam python代码**
```python
"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/14 11:13
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : Steam_js.py
# @Software: PyCharm
"""
#  获取密钥
from fake_useragent import UserAgent
import requests
import execjs

url = "https://store.steampowered.com/login/getrsakey/"

data = {
    "donotcache": "1647236783289",
    "username": "1368946902@qq.com"
}

headers = {
    'User-Agent': UserAgent().random,
}

response_json = requests.post(url=url, headers=headers, data=data).json()

mod = response_json['publickey_mod']
exp = response_json['publickey_exp']

print(mod, exp)

# 进行密码逆向

node = execjs.get()
ctx = node.compile(open('../js/single/steamPasswd.js', encoding="utf-8").read())

funName = 'GetPwd("{0}","{1}","{2}")'.format("123456", mod, exp)
pwd = ctx.eval(funName) # eval执行js中的函数
print(pwd)
```

## 凡科网逆向之闭包技巧
 > 注意： 如果需要逆向的js函数的实现是出现在一个闭包中，那么直接及那个闭包的整个代码块拷贝出来进行调试即可
url="https://i.fkw.com/?_ta=3"


python代码
```python
import execjs

# 1.实例化一个node对象
node = execjs.get()

# 2.js 源代码编译
ctx = node.compile(open("../js/single/FanKe_JS.js",encoding="utf-8").read())

# 3. 执行js代码

funcName='md5("{0}")'.format("123456")
pwd = ctx.eval(funcName)
print(pwd)
```

## 完美世界RSA逆向

有public key 和privacy key 非对称密钥加密
```python
import requests
from lxml import etree
import execjs
import fake_useragent

url = "https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f"
# 发起请求 获取公钥
headers = {
    "User-Agent": fake_useragent.UserAgent().random
}
page_text = requests.get(url, headers=headers).text
tree = etree.HTML(page_text)
# 获取公钥
key = tree.xpath("//*[@id='e']/@value")[0]

print(key)
# 加密的逆向
node = execjs.get()

ctx = node.compile(open("../js/single/wanmei.js", encoding="utf-8").read().replace("\xa0", ''))

funcName: str = 'getPwd("{0}","{1}")'.format("123456", key)

pwd = ctx.eval(funcName)
print(pwd)
```

js源码 详见github


## 试客联盟 逆向分析
- url ="http://login.shikee.com/"
- serializeArray(): js 函数的作用是用来实现序列化 （对登录页的表达中的值进行序列化从而形成一个数组，数组元素就是表单中的数据）【数据就是用户名和密码】
- key表示的是公钥 ，公钥的生成需要用到 rsa_n,ras_n 是什么 目前还不知道，后续再对其进行处理
	- 基于抓包工具对rsa_n 进行全局搜索


```python
# 捕获 rsa_n 的值
import re

import execjs
import requests
import fake_useragent
from lxml import etree

url = "http://login.shikee.com/getkey?v=068825bda83d2ecf1e5e8f098b2d578a"
# 发起请求 获取公钥
headers = {
    "User-Agent": fake_useragent.UserAgent().random
}
page_text = requests.get(url, headers=headers).text
rsa_n=re.search(r'var rsa_n = "(.*)";',page_text).group(1)
print(rsa_n)


# 密码加密的逆向
node = execjs.get()

ctx = node.compile(open("../js/single/ShikeLegue.js", encoding="utf-8").read())

funcName: str = 'getPwd("{0}","{1}")'.format("123456", rsa_n)

pwd = ctx.eval(funcName)
print(pwd)

```



## 空中网逆向分析
一定不是md5 加密  **要不是16位的 要不是32位的** 位数不够32位 即使是16进制的数值

- js 混淆
	- 将js核心的相关代码 进行变相的加密，加密后的数据就是js混淆之后的结果。
- js反混淆
	- 反混淆的线上工具（不理想）
	- 浏览器自带的反混淆工具设置（推荐）
		- ==开发者工具的Source——>settings——>Search in anonymous and content scripts==
		- 在进行关键字的全局搜索—> VMxx (就是反混淆后的代码)


- 发现了一个data\["dc"] 不知道是什么 后续来处理
	- 全局搜索 直接搜索 data 结果太多 不方便定位

python代码
```python
import re
import time
import fake_useragent
import requests
import execjs

# 捕获dc
headers = {
    "User-Agent": fake_useragent.UserAgent().random,
    "Referer": "https://passport.kongzhong.com/"
}
# 伪装时间戳
url = "https://sso.kongzhong.com/ajaxLogin?j=j&jsonp=j&service=https://passport.kongzhong.com/&_={}".format(
    int(time.time() * 1000))

response = requests.get(url, headers=headers)

source_page = response.text

dc = re.search(r'"dc":"(.*?)"', source_page).group(1)

print(dc)

# 生成一个node对象
node = execjs.get()

# 加载js代码
ctx = node.compile(open("../js/single/sky_web.js", encoding="utf-8").read())

# 传值到函数里
funcName = "getPwd('{0}','{1}')".format("12345", dc)

# 执行 js中的函数 拿到返回值
pwd = ctx.eval(funcName)

print(pwd)

```


## 长房网逆向解析

䐵匠䴵dGEHf432eXNUGFbxer8ExQ== 
密码加密 不一样~！！

https://eip.chanfine.com/login.jsp
- session id 一般存放在cookie中

```python
# -*- coding: utf-8 -*-
"""
#
#
# Copyright (C) 2021 #
# @Time    : 2022/3/21 10:24
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : chanfine_js.py
# @Software: PyCharm
"""
import execjs

# 实例化一个node对象
node = execjs.get()

# 加载js
ctx = node.compile(open("../js/single/changfang.js", encoding="utf-8").read())

# 调用函数名
funcName = "getPwd('{0}')".format("123456")

print(ctx.eval(funcName))

```


##  有道翻译 逆向解析
url="https://fanyi.youdao.com/"


- 通过抓包工具 抓取 发现只有三个参数在变化
	- salt 时间戳
	- its 时间戳
	- sign 加密
		- sign 的值 是经过md5 加密获得的，加密的时候使用了两个变量
		- e 是 翻译的单词
		- i 是 字符串形式的js 时间戳 + 1位数的随机整数 **i 是一个字符串的数据**
			- 备注： python 的时间戳 *1000 = js的时间戳
> i: dog
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 16478310967888
**sign: f49c5977d72a54a6130b2278ff637be8
lts: 1647831096788
bv: cf0f0924f577526ad20c2e2b01510b6f**
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION


> i: cat
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
**salt: 16478312531884**
**sign: 909768a0d162fdb1a6b5d816dcd3c6c5**
**lts: 1647831253188**
bv: cf0f0924f577526ad20c2e2b01510b6f
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_CLICKBUTTION


```python
"""
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2022/3/21 13:40
# @Author  : zicliang
# @Email   : hybpjx@163.com
# @File    : youdao_js.py
# @Software: PyCharm
"""
import fake_useragent
import requests
import execjs
import random
import time

#  获取sign
# 三个值用于获取sign
e = input("enter a English word:")
r = str(int(time.time() * 1000))
i = r + str(int(random.random() * 10))

# 生成node对象
node = execjs.get()

ctx = node.compile(open(file="../js/single/youdaoFanyi.js", encoding="utf-8").read())
funcName = "getSign('{0}','{1}')".format(e, i)

sign = ctx.eval(funcName)

# 对有道翻译 发起请求
url = "https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
FormData = {
    "i": "cat",
    "from": "AUTO",
    "to": "AUTO",
    "smartresult": "dict",
    "client": "fanyideskweb",
    "salt": i,
    "sign": sign,
    "lts": r,
    "bv": "cf0f0924f577526ad20c2e2b01510b6f",
    "doctype": "json",
    "version": "2.1",
    "keyfrom": "fanyi.web",
    "action": "FY_BY_CLICKBUTTION",
}

header = {
    'User-Agent': fake_useragent.UserAgent().random,
    'Cookie':'OUTFOX_SEARCH_USER_ID=-2112300131@10.110.96.157; OUTFOX_SEARCH_USER_ID_NCOO=1667654300.4588792; YOUDAO_FANYI_SELECTOR=OFF; JSESSIONID=aaan6CJBk2bUdc73HyQ_x; ___rl__test__cookies=1647842520474',
    'Referer':'https://fanyi.youdao.com/'
}
result = requests.post(url, data=FormData, headers=header).json()
print(result)
```


