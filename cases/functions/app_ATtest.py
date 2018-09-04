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


class BaiduTests(unittest.TestCase):
    def setUp(self):
        self.log = Log("app demo test")
        self.base_url = 'http://localhost:4723/wd/hub'
        self.desired_caps = {}
        self.desired_caps['platformName']    = 'Android'
        self.desired_caps['platformVersion'] = '5.1.1'
        self.desired_caps['deviceName']  = '127.0.0.1:62025'
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



    def test_jyb_login_demo(self):
        """即有宝登录测试用例"""
        #self.log.info("成功连接appium服务器")
        #ca = self.driver.current_activity()
        #print("当前activity: %s" % sys.stdout.pritn(str(ca)))
        welcome = 'com.giveu.corder.index.activity.WelcomeActivity'
        self.driver.wait_activity(welcome, 10, 1)
        print("info::switch to the welcome activity successfully!!!")
        #C_selenium_rewrite.swipLeft(self.driver, 500, 2)
        l_winSize = self.driver.get_window_size()
        x1 = l_winSize['width'] * 0.75
        y1 = l_winSize['height'] * 0.5
        x2 = l_winSize['width'] * 0.25
        for i in range(2):
            self.driver.swipe(x1, y1, x2, y1, 500)
            time.sleep(0.5)
        C_selenium_rewrite.find_el(self.driver, By.ID, "com.giveu.corder:id/tv_into")
        time.sleep(5)
        at = self.driver.current_activity()
        print("at:",at)
        # self.driver.find_element_by_accessibility_id("com.giveu.corder:id/et_account") #find_element_by_id("com.giveu.corder:id/et_account").clear()
        # self.driver.find_element_by_id("com.giveu.corder:id/et_account").send_keys("865258")
        # self.driver.find_element_by_id("com.giveu.corder:id/et_pwd").clear()
        # self.driver.find_element_by_id("com.giveu.corder:id/et_pwd").send_keys("123456")
        # self.driver.find_element_by_id("tv_login").click()
        # try:
        #     self.driver.find_element_by_id("top_tab_center_title").is_displayed()
        # except:
        #     self.assertEquals(1, 2, u"登录没有成功！,请查找原因")
        # finally:
        #     tt=self.driver.find_element_by_id("top_tab_center_title").text()
        #     tl = tt.strip()
        #     self.assertEquals(tl,u"新建订单",u"jyb登录成功")
        #self.log.info("jyb登录成功")


    def tearDown(self):
        #self.log.info("关闭并退出app。")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
