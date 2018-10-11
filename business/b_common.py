# coding=utf-8

"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_common.py
@time: 2018/10/8 14:04
@desc: 业务公共函数部分
"""

from appium import webdriver
from common.log import Log
mylogger = Log('初始化手机信息并打开APP')
class C_B_Common():

    def init_APP(self):
        self.base_url = 'http://localhost:4723/wd/hub'
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '4.4.2'
        self.desired_caps['deviceName'] = '127.0.0.1:62001'
        # AndroidDebugBridge().call_adb('127.0.0.1:62025')  用于切换模拟器
        self.desired_caps['appPackage'] = 'com.giveu.corder'
        self.desired_caps['appActivity'] = 'com.giveu.corder.index.activity.SplashActivity'
        self.desired_caps['autoLaunch'] = 'true'
        # 支持中文输入
        self.desired_caps['unicodeKeyboard'] = 'true'
        self.desired_caps['resetKeyboard'] = 'true'
        try:
            self.driver = webdriver.Remote(self.base_url, self.desired_caps)
            mylogger.info("成功打开app")
        except:
            mylogger.error("打开app失败！")
            #self.assertEquals("o", "f", u"打开app失败")

        return self.driver