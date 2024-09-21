import time
import json
import base64
import requests
from io import BytesIO
from PIL import Image
from uuid import uuid4
from utils.PassCaptcha import DetectCaptcha
from utils.CommonUtils import generateVisitpwdDefaultEncrypt

# HHU访客系统 APIs
# https://visit.hhu.edu.cn/login
class HHUVisitorApis():
    def __init__(self):
        self.author = 'cv-cat'
        self.detectCaptcha = DetectCaptcha()
    def getClickCaptcha(self):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://visit.hhu.edu.cn",
            "Pragma": "no-cache",
            "Referer": "https://visit.hhu.edu.cn/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = "https://visit.hhu.edu.cn/prod-api/captcha/get"
        data = {
            "captchaType": "clickWord",
            "clientUid": f"point-{uuid4()}",
            "ts": int(time.time() * 1000)
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        res_json = response.json()
        return res_json

    def checkClickCaptcha(self, pointJson, token):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://visit.hhu.edu.cn",
            "Pragma": "no-cache",
            "Referer": "https://visit.hhu.edu.cn/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = "https://visit.hhu.edu.cn/prod-api/captcha/check"
        data = {
            "captchaType": "clickWord",
            "pointJson": pointJson,
            "token": token
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        res_json = response.json()
        return res_json

    def sendSmsCode(self, phone, code):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://visit.hhu.edu.cn",
            "Pragma": "no-cache",
            "Referer": "https://visit.hhu.edu.cn/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "isToken": "false",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = "https://visit.hhu.edu.cn/prod-api/captchaSms"
        data = {
            "username": str(phone),
            "code": code
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        res_json = response.json()
        return res_json


    def loginByPhone(self, phone, code):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Content-Type": "application/json;charset=UTF-8",
            "Origin": "https://visit.hhu.edu.cn",
            "Pragma": "no-cache",
            "Referer": "https://visit.hhu.edu.cn/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "isToken": "false",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        url = "https://visit.hhu.edu.cn/prod-api/loginBySmsCode"
        data = {
            "username": phone,
            "code": code
        }
        data = json.dumps(data, separators=(',', ':'))
        response = requests.post(url, headers=headers, data=data)
        res_json = response.json()
        return res_json


    def getSelfInfo(self, token):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Authorization": f"Bearer {token}",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://visit.hhu.edu.cn/login",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        cookies = {
            "hehai-visit-Token": token
        }
        url = "https://visit.hhu.edu.cn/prod-api/getInfo"
        response = requests.get(url, headers=headers, cookies=cookies)
        res_json = response.json()
        return res_json

    def catSubmitAppointment(self, token, pageNum='1', status='0'):
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
            "Authorization": f"Bearer {token}",
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "Pragma": "no-cache",
            "Referer": "https://visit.hhu.edu.cn/applyRecord",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
            "sec-ch-ua": "\"Chromium\";v=\"128\", \"Not;A=Brand\";v=\"24\", \"Microsoft Edge\";v=\"128\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\""
        }
        cookies = {
            "hehai-visit-Token": token
        }
        url = "https://visit.hhu.edu.cn/prod-api/apply/list"
        params = {
            "pageNum": pageNum,
            "pageSize": "4",
            "status": status
        }
        response = requests.get(url, headers=headers, cookies=cookies, params=params)
        res_json = response.json()
        return res_json


    def main(self):
        imageDict = {}
        pointJson = []
        while True:
            try:
                print(1)
                res_json = self.getClickCaptcha()
                token = res_json['repData']['token']
                secretKey = res_json['repData']['secretKey']
                wordList = res_json['repData']['wordList']
                originalImageBase64 = res_json['repData']['originalImageBase64']
                image_data = base64.b64decode(originalImageBase64)
                # resize image to 300x200
                img = Image.open(BytesIO(image_data))
                img_resized = img.resize((300, 200))
                output_buffer = BytesIO()
                img_resized.save(output_buffer, format='JPEG')
                image_data = output_buffer.getvalue()
                # detect image
                imageDictTemp = self.detectCaptcha.detectClickImg(image_data)
                for k, v in imageDictTemp.items():
                    if len(k) == 1:
                        imageDict[k] = v
                    elif len(k) > 1:
                        imageDict[k[0]] = v
                for word in wordList:
                    pointJson.append({
                        "x": imageDict[word][0],
                        "y": imageDict[word][1]
                    })
                break
            except Exception as e:
                continue
        pointJson = json.dumps(pointJson, separators=(',', ':'))
        print(pointJson)
        postCode = f"{token}---{pointJson}"
        pointJson = generateVisitpwdDefaultEncrypt(pointJson, secretKey)
        postCode = generateVisitpwdDefaultEncrypt(postCode, secretKey)
        res_json = self.checkClickCaptcha(pointJson, token)
        print(res_json)

        phone = "15751076989"
        res_json = self.sendSmsCode(phone, postCode)
        print(res_json)

        code = input("请输入验证码：")
        res_json = self.loginByPhone(phone, code)
        print(res_json)

        token = res_json['token']
        res_json = self.getSelfInfo(token)
        print(res_json)


if __name__ == '__main__':
    hhuVisitorApis = HHUVisitorApis()
    hhuVisitorApis.main()