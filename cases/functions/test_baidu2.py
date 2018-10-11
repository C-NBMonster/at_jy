# coding=utf-8

from selenium import webdriver

import unittest, time, datetime
#import os.path
import timeit
from common.common_func import CCommon_Function
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common.log import Log
mylogger = Log(log_module='BaiduTest')
Com_Func = CCommon_Function()

from common.rewrite import C_selenium_rewrite
C_sel_rewrite = C_selenium_rewrite()


class BaiduTest(unittest.TestCase):
    def setUp(self):
        try:
            self.driver = webdriver.Chrome()
            mylogger.info("成功打开浏览器")
        except:
            mylogger.error("打开浏览器失败！")
            self.assertEquals("o","f", u"打开浏览器失败")

       # self.driver.implicitly_wait(30)  # 隐性等待时间为30秒
        self.base_url = "https://www.baidu.com"
        t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        self.sTr = "--" * 20 + t + "--" * 20


    def test_baidu(self):
        Com_Func.func_duration()
        mylogger.info(self.sTr + str(self))
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.maximize_window()
        mylogger.info("最大化浏览器窗口。")
        el_info = C_sel_rewrite.find_el(driver, By.ID, "kw")
        if el_info[0] == True:
            #mylogger.info("成功找到 %s 元素" % str(el_info[2]))
            el = el_info[2]
            C_sel_rewrite.send_key(el, "unittest")
        else:
            mylogger.error(el_info[1])
        driver.find_element_by_id("su").click()
        time.sleep(3)
        mylogger.info("停顿3秒")
        title = driver.title
        self.assertEqual(title, u"unittest_百度搜索")

        # 计算用例执行时间，记录到日志中
        func_name = "test_baidu"
        st = Com_Func.func_duration(func_name)
        mylogger.info("%s 用例执行完毕，共消耗：%0.6f Seconds" % ("test_baidu", st))

    # def test_xx(self):
    #     Com_Func.func_duration()
    #     mylogger.info(self.sTr + str(self))
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     mylogger.info("打开百度首页")
    #     driver.maximize_window()
    #     mylogger.info("最大化浏览器窗口。")
    #     print(driver.find_element_by_id("kw").is_displayed())
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys("xxx")
    #     driver.find_element_by_id("su").click()
    #     time.sleep(3)
    #     mylogger.info("停顿3秒")
    #     title = driver.title
    #     self.assertEqual(title, u"xxx_百度搜索")
    #
    #     st = Com_Func.func_duration("test_xx")
    #     mylogger.info("%s 用例执行完毕，共消耗：%0.6f Seconds" % ("test_xx", st))
    #
    # def test_yy(self):
    #     Com_Func.func_duration()
    #     mylogger.info(self.sTr + str(self))
    #     driver = self.driver
    #     driver.get(self.base_url + "/")
    #     mylogger.info("打开百度首页")
    #     driver.maximize_window()
    #     mylogger.info("最大化浏览器窗口。")
    #     driver.find_element_by_id("kw").clear()
    #     driver.find_element_by_id("kw").send_keys("Taylor swift")
    #     driver.find_element_by_id("su").click()
    #     time.sleep(3)
    #     mylogger.info("停顿3秒")
    #     title = driver.title
    #     self.assertEqual(title, u"Taylor swift_百度搜索")
    #
    #     st = Com_Func.func_duration("test_yy")
    #     mylogger.info("%s 用例执行完毕，共消耗：%0.6f Seconds" % ("test_xx", st))

    def tearDown(self):
        self.driver.quit()
        mylogger.info("关闭并退出浏览器。\n")



if __name__ == "__main__":
    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    mylogger.info(u"开始测试百度搜索测试类用例------------------------------------------------------------------------- %s" % t)
    unittest.main()
