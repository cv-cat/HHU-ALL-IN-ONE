import re
import json
import time
import requests
from utils.CommonUtils import generatePCpwdDefaultEncrypt

# HHU小程序智慧河海接口
# 河海大学门禁小程序接口
class HHUWXWisdomHohaiApis():
    def __init__(self):
        self.cookies = {
            "tenantId": "1"
        }

    @staticmethod
    def getCommonHeaders(access_token):
        return {
            "Host": "zhjc.hhu.edu.cn",
            "xweb_xhr": "1",
            "Authorization": f"Bearer {access_token}",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

    def getWXSession(self, username, password):
        session = requests.Session()
        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://authserver.hhu.edu.cn/authserver/login"
        params = {
            "service": "https://zhjc.hhu.edu.cn/wxapp/?state=CAS_MOBILE_WXAPP_ACCESS-LOGIN#/pages/h5ToWxWas/index",
            "t": "1725626381142"
        }
        response = session.get(url, headers=headers, params=params, allow_redirects=False)
        redirectUrl = response.headers['Location']

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        url = "https://authserver.hhu.edu.cn/authserver/weixinQYLogin.do"
        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers['Location']

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": response.url,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://authserver.hhu.edu.cn/authserver/login"
        params = {
            "skip": "skip",
            "service": "https://authserver.hhu.edu.cn/authserver/login?service=https%3A%2F%2Fzhjc.hhu.edu.cn%2Fwxapp%2F%3Fstate%3DCAS_MOBILE_WXAPP_ACCESS-LOGIN%23%2Fpages%2Fh5ToWxWas%2Findex"
        }
        response = session.get(url, headers=headers, params=params)
        session.cookies.update({
            'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE': 'zh_CN',
        })

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Referer": response.url,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://authserver.hhu.edu.cn/authserver/login"
        params = {
            "skip": "skip",
            "service": "https://authserver.hhu.edu.cn/authserver/login?service=https%3A%2F%2Fzhjc.hhu.edu.cn%2Fwxapp%2F%3Fstate%3DCAS_MOBILE_WXAPP_ACCESS-LOGIN%23%2Fpages%2Fh5ToWxWas%2Findex"
        }
        response = session.get(url, headers=headers, params=params)
        res_text = response.text
        lt = re.findall(r'name="lt" value="(.*?)"', res_text)[0]
        pwdDefaultEncryptSalt = re.findall(r'id="pwdDefaultEncryptSalt" value="(.*?)"', res_text)[0]
        pwdDefaultEncrypt = generatePCpwdDefaultEncrypt(password, pwdDefaultEncryptSalt)

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "no-cors",
            "Sec-Fetch-Dest": "image",
            "Referer": "https://authserver.hhu.edu.cn/authserver/login?skip=skip&service=https%3A%2F%2Fauthserver.hhu.edu.cn%2Fauthserver%2Flogin%3Fservice%3Dhttps%253A%252F%252Fzhjc.hhu.edu.cn%252Fwxapp%252F%253Fstate%253DCAS_MOBILE_WXAPP_ACCESS-LOGIN%2523%252Fpages%252Fh5ToWxWas%252Findex",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://authserver.hhu.edu.cn/authserver/captcha.html"
        params = {
            "ts": "685"
        }
        response = session.get(url, headers=headers, params=params)

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Accept": "text/plain, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://authserver.hhu.edu.cn/authserver/login?skip=skip&service=https%3A%2F%2Fauthserver.hhu.edu.cn%2Fauthserver%2Flogin%3Fservice%3Dhttps%253A%252F%252Fzhjc.hhu.edu.cn%252Fwxapp%252F%253Fstate%253DCAS_MOBILE_WXAPP_ACCESS-LOGIN%2523%252Fpages%252Fh5ToWxWas%252Findex",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://authserver.hhu.edu.cn/authserver/needCaptcha.html"
        params = {
            "username": username,
            "pwdEncrypt2": "pwdEncryptSalt",
            "_": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params)

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Accept": "text/plain, */*; q=0.01",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "X-Requested-With": "XMLHttpRequest",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://authserver.hhu.edu.cn/authserver/login?skip=skip&service=https%3A%2F%2Fauthserver.hhu.edu.cn%2Fauthserver%2Flogin%3Fservice%3Dhttps%253A%252F%252Fzhjc.hhu.edu.cn%252Fwxapp%252F%253Fstate%253DCAS_MOBILE_WXAPP_ACCESS-LOGIN%2523%252Fpages%252Fh5ToWxWas%252Findex",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://authserver.hhu.edu.cn/authserver/needCaptcha.html"
        params = {
            "username": username,
            "pwdEncrypt2": "pwdEncryptSalt",
            "_": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params)

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "Origin": "https://authserver.hhu.edu.cn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": response.url,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://authserver.hhu.edu.cn/authserver/login"
        params = {
            "skip": "skip",
            "service": "https://authserver.hhu.edu.cn/authserver/login?service=https%3A%2F%2Fzhjc.hhu.edu.cn%2Fwxapp%2F%3Fstate%3DCAS_MOBILE_WXAPP_ACCESS-LOGIN%23%2Fpages%2Fh5ToWxWas%2Findex"
        }
        data = {
            "username": username,
            "password": pwdDefaultEncrypt,
            "lt": lt,
            "dllt": "userNamePasswordLogin",
            "execution": "e2s1",
            "_eventId": "submit",
            "rmShown": "1"
        }
        response = session.post(url, headers=headers, params=params, data=data, allow_redirects=False)
        redirectUrl = response.headers['Location']

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": response.url,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers['Location']
        res_text = response.text
        ticket = re.findall(r'ticket=(.*?)#/pages/h5ToWxWas/index', redirectUrl)[0]
        headers = {
            "Host": "zhjc.hhu.edu.cn",
            "Cache-Control": "max-age=0",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Referer": "https://authserver.hhu.edu.cn/",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        response = session.get(redirectUrl, headers=headers)

        # headers = {
        #     "Host": "zhjc.hhu.edu.cn",
        #     "Origin": "https://zhjc.hhu.edu.cn",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
        #     "Accept": "*/*",
        #     "Sec-Fetch-Site": "same-origin",
        #     "Sec-Fetch-Mode": "cors",
        #     "Sec-Fetch-Dest": "script",
        #     "Accept-Language": "zh-CN,zh;q=0.9"
        # }
        # url = "https://zhjc.hhu.edu.cn/wxapp/assets/pages-h5ToWxWas-index.e2ad4138.js"
        # response = session.get(url, headers=headers)
        # res_text = response.text
        # Basic = re.findall(r'o="server",n="(.*?)"', res_text)[0]
        # print(Basic)

        headers = {
            "Host": "zhjc.hhu.edu.cn",
            "skipToken": "true",
            "Authorization": f'Basic c29jaWFsOnNvY2lhbA==',
            # "Authorization": Basic,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 MicroMessenger/7.0.20.1781(0x6700143B) NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF WindowsWechat(0x63090b19)XWEB/11253",
            "Tenant-ld": "1",
            "Accept": "*/*",
            "Origin": "https://zhjc.hhu.edu.cn",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": response.url,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://zhjc.hhu.edu.cn/admin/oauth2/token"
        params = {
            "mobile": f"CAS_MOBILE_WXAPP_ACCESS@{ticket}",
            "code": ticket,
            "grant_type": "mobile",
            "scope": "server"
        }
        response = session.post(url, headers=headers, params=params)

        res_json = response.json()
        access_token = res_json['access_token']
        return {
            'session': session,
            'access_token': access_token
        }

    def getWXUserInfo(self, access_token):
        headers = self.getCommonHeaders(access_token)
        url = "https://zhjc.hhu.edu.cn/admin/accessPerson/mobile/loginUserBaseInfo"
        response = requests.get(url, headers=headers, cookies=self.cookies)
        res_json = response.json()
        return res_json

    def getWXUserDetailInfo(self, access_token):
        headers = self.getCommonHeaders(access_token)
        url = "https://zhjc.hhu.edu.cn/admin/user/info"
        response = requests.get(url, headers=headers, cookies=self.cookies)
        res_json = response.json()
        return res_json

    def getAccessQrCode(self, access_token):
        headers = self.getCommonHeaders(access_token)
        url = "https://zhjc.hhu.edu.cn/admin/accessPerson/mobile/freshAccessQrCode"
        data = {}
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, cookies=self.cookies, data=data)
        res_json = response.json()
        return res_json

if __name__ == '__main__':
    # 学号和密码
    username = '231607010123'
    password = 'github.com/cv-cat'
    hhuWXWisdomHohaiApis = HHUWXWisdomHohaiApis()
    res = hhuWXWisdomHohaiApis.getWXSession(username, password)
    access_token = res['access_token']
    print(hhuWXWisdomHohaiApis.getWXUserInfo(access_token))
    print(hhuWXWisdomHohaiApis.getWXUserDetailInfo(access_token))
    print(hhuWXWisdomHohaiApis.getAccessQrCode(access_token))