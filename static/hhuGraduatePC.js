const CryptoJS = require('crypto-js');
function getDAesString(encrypted) {
  var key  = CryptoJS.enc.Utf8.parse('southsoft12345!#');
  var decrypted =CryptoJS.AES.decrypt(encrypted,key,{
    mode:CryptoJS.mode.ECB,
    padding:CryptoJS.pad.Pkcs7
  });
  return decrypted.toString(CryptoJS.enc.Utf8);
}
