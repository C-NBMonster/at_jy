# coding=utf-8

from selenium import webdriver
from AT_Demo.common.logger import Logger
from common.log import Log
import unittest, time,os
from appium import webdriver

#my_logger = Logger(logger='BaiduTests').getlog()

class BaiduTests(unittest.TestCase):
    def setUp(self):
        self.log = Log("app demo test")
        self.base_url = 'http://localhost:4723/wd/hub'
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8'
        self.desired_caps['deviceName'] = 'fc323ca3'
        self.desired_caps['appPackage'] = 'com.giveu.corder'
        #self.desired_caps['appActivity'] = '.SplashActivity'
        self.desired_caps['appActivity'] = '.WelcomeActivity'
        #.me.activity.LoginActivity}
        #print(os.path.dirname(os.getcwd()))
        self.driver = webdriver.Remote(self.base_url, self.desired_caps)
        self.driver.implicitly_wait(15)


    def test_jyb_login_demo(self):
        """即有宝登录测试用例"""

        self.log.info("成功连接appium服务器")
        print(self.driver.current_activity())
        self.driver.find_element_by_id("com.giveu.corder:id/et_account").clear()
        self.driver.find_element_by_id("com.giveu.corder:id/et_account").send_keys("865258")
        self.driver.find_element_by_id("com.giveu.corder:id/et_pwd").clear()
        self.driver.find_element_by_id("com.giveu.corder:id/et_pwd").send_keys("123456")
        self.driver.find_element_by_id("tv_login").click()
        try:
            self.driver.find_element_by_id("top_tab_center_title").is_displayed()
        except:
            self.assertEquals(1, 2, u"登录没有成功！,请查找原因")
        finally:
            tt=self.driver.find_element_by_id("top_tab_center_title").text()
            tl = tt.strip()
            self.assertEquals(tl,u"新建订单",u"jyb登录成功")
        self.log.info("jyb登录成功")
        self.driver.quit()

    def tearDown(self):
        self.log.info("关闭并退出app。")

if __name__ == "__main__":
    unittest.main()
