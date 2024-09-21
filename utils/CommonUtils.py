# coding: utf-8
import subprocess
from functools import partial
subprocess.Popen = partial(subprocess.Popen, encoding="utf-8")
import execjs

try:
    PCJS = execjs.compile(open("../static/hhuPC.js", "r", encoding='utf-8').read())
except:
    PCJS = execjs.compile(open("static/hhuPC.js", "r", encoding='utf-8').read())

try:
    VisitorPCJS = execjs.compile(open("../static/hhuVisitor.js", "r", encoding='utf-8').read())
except:
    VisitorPCJS = execjs.compile(open("static/hhuVisitor.js", "r", encoding='utf-8').read())

try:
    GraduateJS = execjs.compile(open(r'../static/hhuGraduatePC.js', 'r', encoding='utf-8').read())
except:
    GraduateJS = execjs.compile(open(r'static/hhuGraduatePC.js', 'r', encoding='utf-8').read())


def generatePCpwdDefaultEncrypt(password, salt):
    return PCJS.call("encryptAES", password, salt)

def generateVisitpwdDefaultEncrypt(xy, key):
    return VisitorPCJS.call("encryptCaptcha", xy, key)

def generateGraduatepwdDefaultEncrypt(encryStr):
    return GraduateJS.call("getDAesString", encryStr)

