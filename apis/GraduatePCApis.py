# coding: utf-8
import json
import time
import requests
from utils.CookieUtils import trans_cookies
from utils.CommonUtils import generateGraduatepwdDefaultEncrypt
from utils.PassCaptcha import DetectCaptcha


# 河海大学研究生院
# http://yjss.hhu.edu.cn/home/stulogin
class HHUGraduatePCApis():
    def __init__(self):
        self.author = 'cv-cat'
        self.detectCaptcha = DetectCaptcha()

    def getGraduateSession(self, username, password):
        session = requests.session()
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "http://yjss.hhu.edu.cn/student/default/index",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
        }
        cookies = {
            "ASP.NET_SessionId": "mtano3daf40kdql5nxzhi5eu"
        }
        url = "http://yjss.hhu.edu.cn/home/stulogin"
        response = session.get(url, headers=headers, cookies=cookies, verify=False, allow_redirects=False)
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "http://yjss.hhu.edu.cn/student/default/index",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
        }
        url = "http://yjss.hhu.edu.cn/home/stulogin"
        response = session.get(url, headers=headers, cookies=cookies, verify=False)
        headers = {
            "Accept": "image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "http://yjss.hhu.edu.cn/home/stulogin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
        }
        url = "http://yjss.hhu.edu.cn/home/verificationcode"
        params = {
            "codetype": "stucode"
        }
        response = session.get(url, headers=headers, cookies=cookies, params=params, verify=False)
        imageContent = response.content
        captchaResult = self.detectCaptcha.detectImg(imageContent)
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Origin": "http://yjss.hhu.edu.cn",
            "Pragma": "no-cache",
            "Referer": "http://yjss.hhu.edu.cn/home/stulogin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "X-Requested-With": "XMLHttpRequest"
        }
        url = "http://yjss.hhu.edu.cn/home/stulogin_do"
        data = {
            "json": '{' + f'"UserId":"{username}","Password":"{password}","VeriCode":"{captchaResult}","url":"","city":""' + '}'
        }
        response = session.post(url, headers=headers, cookies=cookies, data=data, verify=False)
        res_text = response.text
        res_text = generateGraduatepwdDefaultEncrypt(res_text)
        return session


    def getAllLesson(self, session):
        headers = {
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://yjss.hhu.edu.cn/student/pygl/xscjcx",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "X-Requested-With": "XMLHttpRequest",
            "sec-ch-ua": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = "http://yjss.hhu.edu.cn/student/pygl/xscjcx_list"
        params = {
            "_": str(int(time.time() * 1000))
        }
        response = session.get(url, headers=headers, params=params, verify=False)
        res_text = response.text
        res_text = generateGraduatepwdDefaultEncrypt(res_text)
        res_json = json.loads(res_text)
        # 保存pdf
        # url = "http://yjss.hhu.edu.cn/student/pygl/dcword_cj"
        # response = requests.post(url, headers=headers, cookies=cookies, verify=False)
        # res_content = response.content
        # with open('score.pdf', 'wb') as f:
        #     f.write(res_content)
        return res_json


if __name__ == '__main__':
    username = '231607010123'
    password = 'github.com/cv-cat'
    hhuGraduatePCApis = HHUGraduatePCApis()
    session = hhuGraduatePCApis.getGraduateSession(username, password)
    res_json = hhuGraduatePCApis.getAllLesson(session)
    for i in res_json['xwklist']:
        print(i)
    for i in res_json['fxwklist']:
        print(i)
