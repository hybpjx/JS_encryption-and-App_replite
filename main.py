import base64
import binascii
import re
from Crypto.Cipher import AES


class AESCBC:
    def __init__(self):
        self.key = '4b4e31356d6638344c6e61326c3030347361646572364d72'[:24].encode('utf-8')  # 定义key值
        self.mode = AES.MODE_CBC
        self.bs = 16  # block size
        self.PADDING = lambda s: s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    # 加密
    def encrypt(self, text):
        generator = AES.new(key='4b4e31356d6638344c6e61326c3030347361646572364d72'[:24].encode('utf-8'), mode=self.mode, iv="436d396432667338346c3364324e3673"[:16].encode('utf-8'))
        crypt = generator.encrypt(self.PADDING(text).encode('utf-8'))
        crypted_str = base64.b64encode(crypt)  # 输出Base64
        # crypted_str = binascii.b2a_hex(crypt)  # 输出Hex
        result = crypted_str.decode()
        return result

    # 解密
    def decrypt(self, text):
        generator = AES.new(key='4b4e31356d6638344c6e61326c3030347361646572364d72'[:24].encode('utf-8'), mode=self.mode, iv="436d396432667338346c3364324e3673"[:16].encode('utf-8'))
        text += (len(text) % 4) * '='
        # decrpyt_bytes = base64.b64decode(text)  # 输出Base64
        decrpyt_bytes = binascii.a2b_hex(text.encode())  # 输出Hex
        meg = generator.decrypt(decrpyt_bytes)
        # 去除解码后的非法字符
        try:
            result = re.compile('[\\x00-\\x08\\x0b-\\x0c\\x0e-\\x1f\n\r\t]').sub('', meg.decode())
        except Exception:
            result = '解码失败，请重试!'
        return result


if __name__ == '__main__':
    a = AESCBC()
    print(a.encrypt('1'))
    print(a.decrypt(a.encrypt('1')))
