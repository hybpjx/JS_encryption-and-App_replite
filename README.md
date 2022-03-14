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

# 0. 常见的加密算法

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
    - DES和AES切换只需要修改CryptoJS.AES <=>CryptoJS.DES
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

  1. 在https诞生之前 所有的网站都是使用http协议。 而http协议在数据传输的过程中都是名为呢 所以可能存在数据泄露和篡改
  2. 使用对称密钥进行数据加密
     - 为了防止 数据泄露和篡改，我们对数据进行加密 如：生成一个堆成密码【askdjlasd】 我们将堆成密钥 分别交给浏览器和服务器端，他们之间传输的数据都是用堆成密钥进行加密和解密

- 请求响应流程如下：

  - 客户端使用对称密钥对请求进行加密，并发送给服务端
  - 服务端接收到密文之后，使用对称密钥对密文进行解密，然后处理请求，最后再使用堆成密钥要把返回的内容再次进行加密 然后返回给客户端
  - 客户端接收到密文之后，使用对称密钥进行解密，并获取最终的响应内容

- 如此一来，数据传输都是密文，解决了铭文传输的问题，但是，这么干有bug

  - 浏览器如何获取堆成密钥？

  - 每个客户端的堆成密钥相同，浏览器能拿到对称密钥，那么黑客页可以拿到，所以，数据加密也就没有了意义

    ![https%3A%2F%2Fs3-us-west-2.amazonaws.com%2Fsecure.notion-static.com%2Fc03a32a8-5a0b-44a2-b557-0ffb0ab04e7f%2FUntitled](README.assets/https%253A%252F%252Fs3-us-west-2.amazonaws.com%252Fsecure.notion-static.com%252Fc03a32a8-5a0b-44a2-b557-0ffb0ab04e7f%252FUntitled.png)

  一言蔽之： 证书用于管理公钥。（公钥要公开。如何避免公钥被替换或损毁，引入了证书。）

  私钥在服务器端，公钥一般在证书中

  比方 证书好比身份证（公钥+姓名+数字签名）。

  证书机构（CA）好比公安局，负责管理和分发身份证。

  证书内容 证书实际上是对于非对称加密算法来说的，一般证书包括公钥、姓名、数字签名三个部分。

  CA登记 HASH(公钥+姓名) 标识唯一性，也就是证书里的数字签名。

  甲方 发送数据给 乙方，

  去CA查找乙方的身份证书，上面有乙方的信息，可以保证公钥就是乙方的。

  然后把要加密的信息进行加密 给乙方。


# js逆向 实战

### **微信公众号平台JS算法 逆向**

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
