# -*- coding:utf-8 -*-
from time import *
import sys
import requests
import json
import random
import datetime

def generator(year,md):
    codelist = []
    with open(r'e:\idno.txt', mode="r", encoding="utf-8") as file:
        codelist = file.readlines()

    id = codelist[random.randint(0, len(codelist) - 1)].split(" ")[0]  # 地区项
    id = id + year # 年份项
    id = id + md
    id = id + str(random.randint(100, 300))  # ，顺序号简单处理

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]  # 权重项
    checkcode ={'0': '1', '1': '0', '2': 'X', '3': '9', '4': '8', '5': '7', '6': '6', '7': '5',
                '8': '5', '9': '3', '10': '2'}  # 校验码映射
    for i in range(0, len(id)):
       count = count + int(id[i]) * weight[i]
    id = id + checkcode[str(count%11)]  # 算出校验码
    print (id)
    return id

def age(xAge,dAge,d,m,y):

    a = gmtime()
    # difference in day
    xd = int(d)
    # difference in month
    xm = int(m)
    # difference in year

    xy = int(y) - int(xAge)
    # checks if difference in day is negative

    dd = int(d)
    # difference in month
    dm = int(m)
    # difference in year
    dy = int(y) + int(dAge) + 1
    # checks if difference in day is negative
    print(u"保险允许的年龄区间：%s--%s,今天是 %s-%s-%s"%(xAge,dAge,y,m,d))
    print(u"允许的出生日期: %d-%s-%s to %d-%s-%s" % (xy, xm, xd, dy, dm, dd))

    dingTalk()

def dingTalk(msg):

    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "msgtype": "text",
        "text": {
            "content": "腾顺--%s"%msg
        },
        "at": {
            "atMobiles": [],
            "isAtAll": "false"
        }
    }

    json_data = json.dumps(data)
    requests.post(
        url='https://oapi.dingtalk.com/robot/send?access_token=0d4a6061efd77b130f6d28d5984ed55a4ac3e7b9357197d32c1001acff7054da',
        data=json_data, headers=headers)


if __name__ == '__main__':
    age(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    dingTalk()



