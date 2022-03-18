function getPwd(){
var key="";
var iv = "";
var security="\u4435\u5320\u4d35";


 value = CryptoJS.AES.encrypt(value, CryptoJS.enc.Utf8.parse(key), {
                iv: CryptoJS.enc.Utf8.parse(iv)
            }).toString()

return security + value
}