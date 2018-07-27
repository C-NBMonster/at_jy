# coding=utf-8

from selenium import webdriver
#from common.logger import Logger
import unittest, time,logs
from AT_Demo.common.common_func import CCommon_Function
#mylogger = Logger(logger='Func_Log').getlog()

class BaiduTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        #mylogger.info("打开浏览器")
        self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"


    def test_baidu(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        #mylogger.info("打开百度首页")
        driver.maximize_window()
        #mylogger.info("最大化浏览器窗口。")
        print(CCommon_Function.createPhone(self))
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        driver.find_element_by_id("su").click()
        time.sleep(3)
        #mylogger.info("停顿3秒")
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")
    def test_xx(self):
        print("empty test")

    def tearDown(self):
        self.driver.quit()
        #mylogger.info("关闭并退出浏览器。")

if __name__ == "__main__":
    unittest.main()
