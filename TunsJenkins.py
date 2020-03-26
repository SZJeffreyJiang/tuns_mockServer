# -*- coding: utf-8 -*-
from config import jenkinsConfig as JC
import jenkins
from flask import Flask,request,render_template
import time
import requests,json
from db import db

app = Flask(__name__)

class TestJenkins(object):
    def __new__(cls, *args, **kwargs):
        pass
    def __init__(self):
        #这里的api_token是针对远程执行任务时,jenkins要验证的token的信息
        self.api_token = 'okfine'
        self.jenkinsServer = jenkins.Jenkins('http://192.168.2.20:8180', username='prdadm', password='prdadm0502/()')
    def buildJob(self):

        self.jenkinsServer.build_job(self,"验证码")
        # self.server.build_job('jxInstantQuery2',
        #                 {'param1': 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', 'param2': 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'})

def build(jobName):
    server = jenkins.Jenkins(JC.url, username=JC.userName, password=JC.password)
    server.build_job(jobName)


if __name__ == '__main__':
    # TestJenkins.buildJob("11")
    build("验证码")