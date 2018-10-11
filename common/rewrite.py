#coding:utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: rewrite.py
@time: 2018/9/3 14:14
@desc: 重写selenium中的元素操作方法
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from appium.webdriver.common.mobileby import MobileBy
import time


class C_selenium_rewrite():
    """
    封装部分API，使用的时候记得把By给导入进来
    """
    def find_el(self, driver,  pattern, loc, timeOut=10):
        """
        只能查找元素
        :param driver:
        :param: timeOut:超时
        :param loc: 定位(方式+值）
        :return:
        ：usage: waitSmart(driver,10,(By.ID,"id"))
        """
        driver.implicitly_wait(timeOut)
        log_msg = ''
        t = False
        try:
            if driver.find_element(pattern, loc).is_displayed() == True:
                t = True
        except NoSuchElementException as msg:
            log_msg = msg
        finally:
            if t == True:
                return t, log_msg, driver.find_element(pattern, loc)
            else:
                return t, log_msg

    def find_els(self, driver, pattern, loc, timeOut=10):
        """
        只能查找元素
        :param driver:
        :param: timeOut:超时
        :param loc: 定位(方式+值）
        :return:
        ：usage: waitSmart(driver,10,(By.ID,"id"))
        """
        driver.implicitly_wait(timeOut)
        log_msg = ''
        t = False
        try:
            if driver.find_elements(pattern, loc).is_displayed() == True:
                t = True
        except NoSuchElementException as msg:
            log_msg = msg
        finally:
            if t == True:
                return t, log_msg, driver.find_elements(pattern, loc)
            else:
                return t, log_msg
    # def find_el(self, Driver, timeOut=30, ignored_exceptions=u"找不到该元素", *loc):
    #     """
    #     查找单个元素
    #     :param loc:元素定位
    #     :timeOut:超时时间
    #     :frequency:频率，即在超时时间内每隔多少秒去查找一次元素
    #     :ignored_exceptions:发生异常时的提示信息
    #     :return:
    #     :usage:Driver.find_el((By.XPATH,"//a"))
    #     """
    #     try:
    #         WebDriverWait(Driver, timeOut, ignored_exceptions).until(lambda Driver: Driver.find_element(*loc).is_displayed())
    #         return Driver.find_element(*loc)
    #     except NoSuchElementException as msg:
    #         print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, timeOut, *loc, msg))

    # def find_els(self, Driver, timeOut=30, frequency=1, ignored_exceptions=u"找不到该元素", *loc):
    #     """
    #     查找多个元素
    #     :param loc:元素定位
    #     :return:
    #     :usage:Driver.find_els((By.XPATH,"//a"))
    #     """
    #     try:
    #         WebDriverWait(Driver, timeOut, frequency,  ignored_exceptions).until(lambda Driver: Driver.find_elements(*loc).is_displayed())
    #         return Driver.find_elements(*loc)
    #     except NoSuchElementException as e:
    #         print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, timeOut, loc, e))

    def click_keys(self, driver, pattern, loc):
        """
        点击元素
        :param loc:元素定位
        :return:
        :usage:Driver.click_keys((By.XPATH,"//a"))
        """
        if self.find_el(driver, pattern, loc)[0] == True:
            el = self.find_el(driver, pattern, loc)[2]
            el.click()

    def clear_keys(self, driver, pattern, loc):
        """
        清除输入框的内容
        :param loc:元素定位
        :return:
        :usage:Driver.clear_keys((By.XPATH,"//a"))
        """
        if self.find_el(driver, pattern, loc)[0] == True:
            el = self.find_el(driver, pattern, loc)[2]
            el.clear()

    def send_key(self, el, content):
        """
        向输入框发送内容:
        handle:元素句柄
        content:向元素发送的内容
        Usage:Driver.send_keys((By.XPATH,"//a"),'a')
        """
        el.clear()
        el.send_keys(content)

    def exec_script(self, driver, src):
        """
        执行其它语言的脚本，JS
        :param src:
        :return:
        Usage:exec_script(src)
        """
        return driver.execute_script(src)

    def right_click(self, driver, pattern, loc):
        """
        右击
        :param loc:
        :return:
        Usage: right_click((By.XPATH,"//a"))
        """
        if self.find_el(driver, pattern, loc)[0] == True:
            el = self.find_el(driver, pattern, loc)[2]
            ActionChains(driver).context_click(el).perform()

    def move_to_element(self, driver, pattern, loc):

        """
        移动鼠标到元素上
        :param loc:
        :return:
        Usage: move_to_element((By.XPATH,"//a"))
        """
        if self.find_el(driver, pattern, loc)[0] == True:
            el = self.find_el(driver, pattern, loc)[2]
            ActionChains(driver).move_to_element(el).perform()

    def double_click(self, driver, pattern, loc):
        """
        双击
        :param loc:
        :return:
        Uage:Driver.double_click((By.XPATH,"//a"))
        """
        if self.find_el(driver, pattern, loc)[0] == True:
            el = self.find_el(driver, pattern, loc)[2]
            ActionChains(driver).double_click(el).perform()

    def drag_and_drop(self, driver, *loc1, **loc2):
        """
        拖动元素到指定位置，PS：ActionChains的拖动并没那么有效果，这个需要再完善一下
        :param loc1: 起始位置
        :param loc2: 结束位置
        :return:
        Usage:Driver.drag_and_drop((By.XPATH,"//a"),(By.XPATH,"//b"))
        """
        if self.find_el(driver, *loc1)[0] == True:
            global element
            element = self.find_el(driver, *loc1)[2]
        if self.find_el(driver, *loc2)[0] == True:
            global target
            target = self.find_el(driver, *loc2)[2]
        ActionChains(driver).drag_and_drop(element, target).perform()

    def get_display(self, driver, timeOut, loc):
        """
        判断元素是否显示
        :param loc: 元素定位
        :return:
        """
        try:
            WebDriverWait(driver, timeOut).until(lambda driver: driver.find_element(*loc).is_displayed())
            return True
        except Exception as e:
            print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, timeOut, loc, e))
            return False

    def refresh(self, driver):
        """
        10s自动刷新页面
        :return:
        """
        driver.implicitly_wait(10)
        driver.refresh()

    def get_text(self, driver, pattern, loc):
        """
        获取元素text内容
        :param loc:元素定位
        :return:
        """
        if self.find_el(driver, pattern, loc)[0] == True:
            return self.find_el(driver, pattern, loc)[2].get_Text()

    #封装滑动方法

    def swipeUp(self, Driver, sd=0,  x1=0, y1=0, x2=0, y2=0, t=500, n=1):
        """
        向上滑动屏幕
        :param t: 滑动持续时间
        :param n: 滑动的次数
        :sd:标记为自定义坐标：0表示根据屏幕来算，默认点在中间； 1表示自定义坐标
        :return:
        """
        if sd == 1:
            for i in range(n):
                Driver.swipe(x1, y1, x2, y2, t)
                time.sleep(0.3)
        else:
            l_winSize = Driver.get_window_size()
            x1 = l_winSize['width'] * 0.5  # x坐标
            y1 = l_winSize['height'] * 0.75  # 起始y坐标
            y2 = l_winSize['height'] * 0.25  # 终点y坐标
            for i in range(n):
                Driver.swipe(x1, y1, x1, y2, t)
                time.sleep(0.3)

    def swipeDown(self, Driver, sd=0,  x1=0, y1=0, x2=0, y2=0, t=500, n=1):
        """
        向下滑动屏幕
        :param t:  滑动持续时间
        :param n: 滑动的次数
        :sd:标记为自定义坐标：0表示根据屏幕来算，默认点在中间； 1表示自定义坐标
        :return:
        """
        if sd == 1:
            for i in range(n):
                Driver.swipe(x1, y1, x2, y2, t)
                time.sleep(0.3)
        else:
            l_winSize = Driver.get_window_size()
            x1 = l_winSize['width'] * 0.5  # x坐标
            y1 = l_winSize['height'] * 0.25  # 起始y坐标
            y2 = l_winSize['height'] * 0.75  # 终点y坐标
            for i in range(n):
                Driver.swipe(x1, y1, x1, y2, t)
                time.sleep(0.3)

    def swipeLeft(self, Driver,  sd=0,  x1=0, y1=0, x2=0, y2=0, t=500, n=1):
        """
        向左滑动屏幕
        sd:是否自定义坐标：1是 0否
        :param t: 滑动持续时间
        :param n: 滑动的次数
        :return:
        """
        if sd == 1:
            for i in range(n):
                Driver.swipe(x1, y1, x2, y2, t)
                time.sleep(0.5)
        else:
            l_winSize = Driver.get_window_size()
            x1 = l_winSize['width'] * 0.75
            y1 = l_winSize['height'] * 0.5
            x2 = l_winSize['width'] * 0.25
            for i in range(n):
                Driver.swipe(x1, y1, x2, y1, t)
                time.sleep(0.5)

    def swipeRight(self, Driver, sd=0,  x1=0, y1=0, x2=0, y2=0, t=500, n=1):
        """
        向右滑动屏幕
        :param t: 滑动持续时间
        :param n: 滑动的次数
        :return:
        """
        if sd == 1:
            for i in range(n):
                Driver.swipe(x1, y1, x2, y2, t)
        else:
            l_winSize = Driver.get_window_size()
            x1 = l_winSize['width'] * 0.25
            y1 = l_winSize['height'] * 0.5
            x2 = l_winSize['width'] * 0.75
            for i in range(n):
                Driver.swipe(x1, y1, x2, y1, t)


