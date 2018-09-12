# coding=utf-8

#from selenium import webdriver
from AT_Demo.common.logger import Logger
from common.log import Log
import unittest, time,os,sys,string
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
#my_logger = Logger(logger='BaiduTests').getlog()
from common.rewrite import C_selenium_rewrite
from business.b_login import C_B_Login


class NewOrder_Process_Tests(unittest.TestCase):

    #adb shell dumpsys window w |findstr \/ |findstr name=     用于查看当前activity。建议用这个


    def setUp(self):
        self.log = Log("app demo test")
        self.base_url = 'http://localhost:4723/wd/hub'
        self.desired_caps = {}
        self.desired_caps['platformName']    = 'Android'
        self.desired_caps['platformVersion'] = '4.4.2'
        self.desired_caps['deviceName']  = '127.0.0.1:62001'
        #AndroidDebugBridge().call_adb('127.0.0.1:62025')  用于切换模拟器
        self.desired_caps['appPackage']  = 'com.giveu.corder'
        self.desired_caps['appActivity'] = 'com.giveu.corder.index.activity.SplashActivity'
        self.desired_caps['autoLaunch']  = 'true'
        #支持中文输入
        self.desired_caps['unicodeKeyboard'] = 'true'
        self.desired_caps['resetKeyboard'] = 'true'
        #self.desired_caps['appActivity'] = 'com.giveu.corder.index.activity.WelcomeActivity'
        #.me.activity.LoginActivity}
        #print(os.path.dirname(os.getcwd()))
        self.driver = webdriver.Remote(self.base_url, self.desired_caps)
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.C_B_login = C_B_Login()


    def test_jyb_login_demo(self):
        """即有宝登录测试用例"""
        #self.log.info("成功连接appium服务器")
        #ca = self.driver.current_activity()
        #print("当前activity: %s" % sys.stdout.pritn(str(ca)))
        welcome = 'com.giveu.corder.index.activity.WelcomeActivity'
        self.driver.wait_activity(welcome, 10, 1)
        print("info::switch to the welcome activity successfully!!!")

        #滑动欢迎页
        self.C_sel_Rewrite.swipLeft(self.driver, 500, 2)

        #点击进入登录页
        self.C_sel_Rewrite.find_el(self.driver, 20, (By.ID, "tv_into")).click()

        #登录
        act_login = "com.giveu.corder.me.activity.LoginActivity"
        self.driver.wait_activity(act_login,20,1)
        self.C_B_login.b_login(self.driver, 300079, 123456)

        #登录成功验证
        print("current_context:", self.driver.current_context())
        print(self.driver.contexts())

        print("login,good!!!")

        #self.log.info("jyb登录成功")


    def tearDown(self):
        #self.log.info("关闭并退出app。")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
