import re
import time
import requests
from utils.CommonUtils import generatePCpwdDefaultEncrypt


# HHU官网 APIs
# https://authserver.hhu.edu.cn/authserver/login
class HHUPCApis():
    def __init__(self):
        self.author = 'cv-cat'

    def getPCSession(self, username, password):
        session = requests.Session()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = "https://authserver.hhu.edu.cn/authserver/login"
        params = {
            "service": "https://my.hhu.edu.cn/portal-web/j_spring_cas_security_check"
        }
        response = session.get(url, headers=headers, params=params)
        session.cookies.update({
            'org.springframework.web.servlet.i18n.CookieLocaleResolver.LOCALE': 'zh_CN'
        })
        del headers["Sec-Fetch-User"]
        headers["Referer"] = "https://authserver.hhu.edu.cn/authserver/login?service=https%3A%2F%2Fmy.hhu.edu.cn%2Fportal-web%2Fj_spring_cas_security_check"
        params = {
            "service": "https://my.hhu.edu.cn/portal-web/j_spring_cas_security_check"
        }
        response = session.get(url, headers=headers, params=params)
        res_text = response.text
        lt = re.findall(r'name="lt" value="(.*?)"', res_text)[0]
        pwdDefaultEncryptSalt = re.findall(r'id="pwdDefaultEncryptSalt" value="(.*?)"', res_text)[0]
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded",
            "Origin": "https://authserver.hhu.edu.cn",
            "Pragma": "no-cache",
            "Referer": "https://authserver.hhu.edu.cn/authserver/login?service=https%3A%2F%2Fmy.hhu.edu.cn%2Fportal-web%2Fj_spring_cas_security_check",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-User": "?1",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = "https://authserver.hhu.edu.cn/authserver/login"
        params = {
            "service": "https://my.hhu.edu.cn/portal-web/j_spring_cas_security_check"
        }
        pwdDefaultEncrypt = generatePCpwdDefaultEncrypt(password, pwdDefaultEncryptSalt)
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
        redirectUrl = response.headers["Location"]

        # 1
        headers = {
            "Host": "my.hhu.edu.cn",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Referer": "https://authserver.hhu.edu.cn/",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        response = session.get(redirectUrl, headers=headers, params=params, allow_redirects=False)
        redirectUrl = response.headers["Location"]
        headers = {
            "Host": "my.hhu.edu.cn",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-User": "?1",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        response = session.get(redirectUrl, headers=headers)
        headers = {
            "Host": "my.hhu.edu.cn",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Referer": response.url,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        url = "https://my.hhu.edu.cn/portal-web/guest/hhdx/index.html"
        params = {
            "t": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params)
        refer = response.url
        res_text = response.text
        slide_splice = re.findall(r'data-callback="scanBox-img" data-url="(.*?)"', res_text)[0]
        heyw_rss_splice = re.findall(r'data-callback="heyw-rss-list" data-url="(.*?)"', res_text)[0]
        oa_rss_splice = re.findall(r'data-callback="OA-rss-list" data-url="(.*?)"', res_text)[0]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": refer,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = f"https://my.hhu.edu.cn{slide_splice}"
        params = {
            "t": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params)

        headers = {
            "Host": "my.hhu.edu.cn",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": refer,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        url = f"https://my.hhu.edu.cn{heyw_rss_splice}"
        params = {
            "t": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params)

        headers = {
            "Host": "my.hhu.edu.cn",
            "Pragma": "no-cache",
            "Cache-Control": "no-cache",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": refer,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        url = f"https://my.hhu.edu.cn{oa_rss_splice}"
        params = {
            "t": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params)

        headers = {
            "Host": "my.hhu.edu.cn",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Referer": refer,
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        url = "https://my.hhu.edu.cn/portal-web/html/index.html"
        params = {
            "t": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        url = "https://my.hhu.edu.cn/portal-web/html/oauth2client/oauth2login"
        response = session.get(url, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "authserver.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }

        response = session.get(redirectUrl, headers=headers, allow_redirects=False)
        redirectUrl = response.headers["Location"]

        headers = {
            "Host": "my.hhu.edu.cn",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "cross-site",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Dest": "document",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        response = session.get(redirectUrl, headers=headers)
        access_token = response.cookies["access_token"]
        return {
            'session': session,
            'access_token': access_token
        }

    def getUserInfo(self, access_token):
        headers = {
            "Host": "my.hhu.edu.cn",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua-mobile": "?0",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua-platform": "\"Windows\"",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://my.hhu.edu.cn/portal-web/html/index.html?t=1725617081400",
            "Accept-Language": "zh-CN,zh;q=0.9"
        }
        url = "https://my.hhu.edu.cn/portal-web/api/proxy/interface/api/rest/v1/personalInterface/getUserInfo"
        params = {
            "t": str(int(time.time() * 1000)),
            "access_token": access_token
        }
        response = session.get(url, headers=headers, params=params)
        res_json = response.json()
        return res_json

if __name__ == '__main__':
    username = '231607010123'
    password = 'github.com/cv-cat'

    hhuPCApis = HHUPCApis()
    res = hhuPCApis.getPCSession(username, password)
    session, access_token = res['session'], res['access_token']
    res = hhuPCApis.getUserInfo(access_token)
    print(res)

