# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: case_Order.py
@time: 2018/10/9 11:39
@desc: 新建订单用例
"""
from common.common_func import CCommon_Function
import unittest, time
import unittest
from selenium.webdriver.common.by import By
from common.rewrite import C_selenium_rewrite
from business.b_login import C_B_Login
from business.b_common import C_B_Common
from business.b_NewOrder import C_B_NewOrder
from common.log import Log

mylogger = Log('NewOrder_Process_Tests')
Com_func = CCommon_Function()
C_sel_Rewrite = C_selenium_rewrite()
C_B_login = C_B_Login()
C_B_newOrder = C_B_NewOrder()
t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
sTr = "--" * 20 + t + "--" * 20

class C_TC_Order(unittest.TestCase):
    def setUP(self):
        #初始化手机及打开APP
        self.C_B_common = C_B_Common()
        self.driver = self.C_B_common.init_APP()

        #登录
        #计时开始
        Com_func.func_duration()

        welcome = 'com.giveu.corder.index.activity.WelcomeActivity'
        self.driver.wait_activity(welcome, 30, 1)
        # 滑动欢迎页
        C_sel_Rewrite.swipeLeft(self.driver, t=500, n=2)

        # 点击进入登录页
        C_sel_Rewrite.find_el(self.driver, 20, (By.ID, "tv_into")).click()

        # 登录
        act_login = "com.giveu.corder.me.activity.LoginActivity"
        self.driver.wait_activity(act_login, 20, 1)
        C_B_login.b_login(self.driver, 829023, 123456)

        # 登录成功验证
        print("current_context:", self.driver.current_context())
        print(self.driver.contexts())

    def test_NewOrder(self):
        self.assertEqual(True, False)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
