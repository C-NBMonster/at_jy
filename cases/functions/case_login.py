# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: case_login.py
@time: 2018/10/8 11:33
@desc: 登录测试用例
"""


from common.common_func import CCommon_Function
import unittest, time
from appium.webdriver.common.touch_action import TouchAction
from common.rewrite import C_selenium_rewrite
from business.b_login import C_B_Login
from business.b_NewOrder import C_B_NewOrder
from elements.el_JYT.el_login import C_el_login
from common.log import Log
from business.b_common import C_B_Common
mylogger = Log(log_module=u'登录测试用例日志')

Com_func = CCommon_Function()
Cel_Login = C_el_login()
C_sel_Rewrite = C_selenium_rewrite()
C_B_login = C_B_Login()
C_B_newOrder = C_B_NewOrder()
t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
sTr = "--" * 20 + t + "--" * 20


class NewOrder_Process_Tests(unittest.TestCase):

    #adb shell dumpsys window w |findstr \/ |findstr name=     用于查看当前activity。建议用这个
    def setUp(self):
        #开始计时
        Com_func.func_duration()

        #初始化手机信息，并开启APP
        self.C_B_common = C_B_Common()
        self.driver = self.C_B_common.init_APP()

        self.TA = TouchAction(self.driver)


        welcome = 'com.giveu.corder.index.activity.WelcomeActivity'
        self.driver.wait_activity(welcome, 20, 1)
        # 滑动欢迎页 并点击进入登录页 用坐标速度比较快，不经常换手机分辨率的话建议用坐标
        C_sel_Rewrite.swipeLeft(self.driver, t=500, n=2)
        #Cel_Login.el_Welcome_EnterLogin(self.driver).click()
        self.TA.tap(x=539, y=1781).perform().release()


    def test_jyb_login(self):
        """即有宝登录测试用例"""
        uName = "829023"
        pwd   = "123456"
        # 登录
        C_B_login.b_login(self.driver, uName, pwd)

        #登录成功验证
        self.driver.implicitly_wait(6)
        C_B_login.accept_PopUp(self.driver)
        mylogger.info("处理弹窗完毕，登录验证成功！")



    def tearDown(self):
        #self.driver.quit()
        mylogger.info("关闭logger")

if __name__ == "__main__":
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    mylogger.info(u"开始测试登录测试类用例------------------------------------------------------------------------- %s" % t)
    unittest.main()
