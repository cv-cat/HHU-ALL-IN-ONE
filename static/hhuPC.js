const CryptoJS = require('crypto-js');
function _gas(data, key0, iv0) {
    key0 = key0.replace(/(^\s+)|(\s+$)/g, "");
    var key = CryptoJS.enc.Utf8.parse(key0);
    var iv = CryptoJS.enc.Utf8.parse(iv0);
    var encrypted = CryptoJS.AES.encrypt(data, key, {
        iv: iv,
        mode: CryptoJS.mode.CBC,
        padding: CryptoJS.pad.Pkcs7
    });
    return encrypted.toString();
}
function encryptAES(data, _p1) {
    if (!_p1) {
        return data;
    }
    var encrypted = _gas(_rds(64) + data, _p1, _rds(16));
    return encrypted;
}
function _ep(p0, p1) {
    try {
        return encryptAES(p0, p1);
    } catch (e) {}
    return p0;
}
var $_chars = 'ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678';
var _chars_len = $_chars.length;
function _rds(len) {
    var retStr = '';
    for (i = 0; i < len; i++) {
        retStr += $_chars.charAt(Math.floor(Math.random() * _chars_len));
    }
    return retStr;
}
// let data = '11'
// let _p1 = 'WiCPBi4tV2iHaMZi'
// let res = encryptAES(data, _p1)
// console.log(res)