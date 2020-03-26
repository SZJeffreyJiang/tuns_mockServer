from flask import Flask,request,render_template
import time
import requests,json
from db import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html", testToken =db.queryTestToken(),devToken=db.queryDevToken(),devVerify=db.queryDevVerify(),testVerify=db.queryTestVerify())

# 保险公司回调mock
@app.route('/com/<insurerName>')
def insurer(insurerName):
    IN=insurerName
    no = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return '{"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "%s%s"}}'%(IN,no)

# 获取测试环境短信验证码
@app.route('/getSmsData')
def getSmsData():
    no = time.strftime("%Y%m%d%H%M%S", time.localtime())
    return '{"responseHead": {"resultCode":"0"},"responseBody": {"proposalNo": "%s%s"}}'%(IN,no)

# post
@app.route('/getPost', methods=['POST','GET'])
def Messaging():
    if request.method =='POST':
        return('post')
    elif request.method =='GET':
        return('get')
    else:
        pass

@app.route('/getToken')
def getToken():
    return ("开发环境token:" + db.querryDevToken()+ "<br><br>测试环境token:" + db.querryTestToken())



@app.route('/TestToken', methods=['POST','GET'])
def TestToken():
    if request.method =='POST':
        return('post')
    elif request.method =='GET':
        return('get')
    else:
        pass

@app.route('/getDevToken', methods=['POST','GET'])
def getDevToken():
    headers = {
    "Connection": "keep-alive",
    #     'Content-Length': '71',
    #     'Origin': 'http://192.168.2.22:8090',
    "Content-Type": "application/json;charset=UTF-8",
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3941.4 Safari/537.36',
    #     'Accept': 'application/json, text/plain, */*',
    #     'Referer': 'https://passport.csdn.net/account/login?from=http://www.csdn.net',
    #     'Accept-Encoding': 'gzip, deflate, br',
    #     'Accept-Language': 'zh-CN,zh;q=0.9'
    #
    }
    url = 'http://192.168.2.22:8012/ins/app/cmm/login'
    data = {"body" : {"loginId" : "15673161167","password" : "14e1b600b1fd579f47433b88e8d85291"},"head" : {"system" : "iOS","version" : "2.0.6","deviceId" : "101d855909235466b73","requestId" : "b7da582845cf4bd2857e34c2c3e42bf3"}}
    r = requests.post(url, data)
    print(r)
    print(r.text)
    print(r.content)
    return r.content

if __name__ == '__main__':
    app.run(host = '192.168.2.76' ,port = 5000, debug = 'True')



