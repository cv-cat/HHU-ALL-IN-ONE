const CryptoJS = require("crypto-js");
function encryptCaptcha(t, key) {
    var e = key
      , i = CryptoJS.enc.Utf8.parse(e)
      , s = CryptoJS.enc.Utf8.parse(t)
      , o = CryptoJS.AES.encrypt(s, i, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return o.toString()
}

function decryptCaptcha(t, key) {
    var e = key
      , i = CryptoJS.enc.Utf8.parse(e)
      , s = CryptoJS.AES.decrypt(t, i, {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7
    });
    return s.toString(CryptoJS.enc.Utf8)
}


// const t = `[{"x":59,"y":25},{"x":121,"y":91},{"x":231,"y":83}]`;
// const e = encryptCaptcha(t);
// console.log(e);


// const msg = "3T2551T5kIDUKHrNcYsJB/t0F4G6U/m8pDQllPtJdKHGJ+9LYHNdjirSgxq0nV75yktkHtMT0Tniko4wiWZMEbVLjUqtyrIexVumAV3VTl0GnWi/hai2CM2D+KcLZwoA"
// const key = "hhu_visit_login"
