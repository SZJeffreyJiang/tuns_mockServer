#usr/bin/python
# -*- coding: utf-8 -*-
# Filename:idMaker.py

import cityZoneDB
import idChecker
import re
import random
import time

class idMaker():
    def __init__(self):
        self.db = cityZoneDB.CZDB()
        self.ic = idChecker.idChecker()
        self.now = time.localtime()
        self.startYear = 1900
        # self.startTime = time.mktime(time.strptime(self.startYear,"%Y-%M-%d"))
        self.bigMonthes = (1, 3, 5, 7, 8, 10, 12)
        self.smallMonthes = (4, 6, 9, 11)
        self.weightList = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        self.validationList = (1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2)

    # 获取所有行政区划记录总数
    def setZoneCodeCount(self):
        try:
            sql = "select id from %s order by id desc limit 1" % self.db.newtable
            self.db.connect()
            self.db.cursor.execute(sql)
            res = self.db.cursor.fetchall()
            if len(res) == 1:
                self.zoneCodeCount = int(res[0][0])
                return True
            else:
                print ('获取数量失败')
                return False
            self.db.dbConnection.close()
        except Exception as e:
            print (e.message)
            print ("Error: unable to fecth data")

    # 随机获取一个身份证号码
    def getRandomIdCode(self):
        zoneCodeId = self.getRandomZoneCode()
        birthday = self.getRandomBirthday()
        policeStationCode = self.getRandomPoliceStationCode()
        genderAndSerial = self.getRandomGenderAndSerial()
        elements = zoneCodeId+birthday+policeStationCode+genderAndSerial
        checkCode = self.getCheckCode(elements)
        idNumber = elements+checkCode
        if zoneCodeId and birthday and policeStationCode and genderAndSerial and checkCode:
            print ('已生成随机身份证:%s，即将进行校验' % idNumber)
            self.ic.validation(idNumber)
            return True
        else:
            print ('生成随机身份证失败')
            return False

    # 随机获取一个行政编码
    def getRandomZoneCode(self):
        try:
            id = random.randrange(1, self.zoneCodeCount, 1)
            sql = "select address_id from %s where id=%d" % (self.db.newtable, id)
            self.db.connect()
            self.db.cursor.execute(sql)
            res = self.db.cursor.fetchall()
            if len(res) == 1:
                if self.getZoneName(int(res[0][0])):
                    return str(res[0][0])
            else:
                print ('获取数量失败')
                return False
            self.db.dbConnection.close()
        except Exception as e:
            print (e.message)
            print ("Error: unable to fecth data")

    # 随机生成一个合法的出生日期
    def getRandomBirthday(self):
        nowYear = int(time.strftime("%Y", self.now))-1
        randYear = random.randrange(self.startYear, int(nowYear))
        randMonth = random.randrange(1, 12)
        if self.ic.isLeapYear(randYear) and randMonth == 2:
            randDate = random.randrange(1, 29)
        elif randMonth == 2:
            randDate = random.randrange(1, 28)
        elif randMonth in self.bigMonthes:
            randDate = random.randrange(1, 31)
        elif randMonth in self.smallMonthes:
            randDate = random.randrange(1, 30)
        #格式转换
        randYear = str(randYear)
        randMonth = str(randMonth) if randMonth > 10 else '0'+str(randMonth)
        randDate = str(randDate) if randDate > 10 else '0'+str(randDate)
        birthday = '%s%s%s' % (randYear, randMonth, randDate)

        return birthday

    # 随机生成一个派出所号
    def getRandomPoliceStationCode(self):
        randCode = random.randrange(1, 100)
        return str(randCode) if randCode > 10 else '0'+str(randCode)

    # 随机生成一个性别和序列号
    def getRandomGenderAndSerial(self):
        return str(random.randrange(0, 9))

    # 通过算法生成校验码
    def getCheckCode(self, elements):
        i = sum = 0
        while i < 17:
            sum += int(elements[i]) * self.weightList[i]
            i += 1
        key = sum % 11
        return str(self.validationList[key])

    # 获取行政名称
    def getZoneName(self, zoneCode):
        try:
            cityCode = (int(zoneCode))/100*100
            provinceCode = (int(zoneCode)/10000)*10000
            sql = 'select address_name from %s where address_id in (%d, %d, %d)' % (self.db.newtable, provinceCode, cityCode, int(zoneCode))
            # 执行SQL语句
            self.db.cursor.execute(sql)
            # 获取所有记录列表
            cityNames = self.db.cursor.fetchall()
            if len(cityNames) == 3:
                # print '籍贯:'+cityNames[0][0]+cityNames[1][0]+cityNames[2][0]
                return '籍贯:'+cityNames[0][0]+cityNames[1][0]+cityNames[2][0]
            else:
                print ('城市编号不存在')
                return False
        except Exception as e:
            print (e.message)
            print ("Error: unable to fecth data")

if __name__ == '__main__':

    im = idMaker()
    im.setZoneCodeCount()
    im.getRandomIdCode()