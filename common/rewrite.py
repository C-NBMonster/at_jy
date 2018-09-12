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

import time


class C_selenium_rewrite():
    """
    封装部分API，使用的时候记得把By给导入进来
    """
    def find_el(self, Driver, timeOut, frequency=1, ignored_exceptions=u"找不到该元素", *loc):
        """
        查找单个元素
        :param loc:元素定位
        :timeOut:超时时间
        :frequency:频率，即在超时时间内每隔多少秒去查找一次元素
        :ignored_exceptions:发生异常时的提示信息
        :return:
        :usage:Driver.find_el((By.XPATH,"//a"))
        """
        try:
            WebDriverWait(Driver, timeOut, frequency, ignored_exceptions).until(lambda Driver: Driver.find_element(*loc).is_displayed())
            return Driver.find_element(*loc)
        except NoSuchElementException as msg:
            print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, timeOut, loc, msg))

    def find_els(self, Driver, timeOut, frequency=1, ignored_exceptions=u"找不到该元素", *loc):
        """
        查找多个元素
        :param loc:元素定位
        :return:
        :usage:Driver.find_els((By.XPATH,"//a"))
        """
        try:
            WebDriverWait(Driver, timeOut, frequency,  ignored_exceptions).until(lambda Driver: Driver.find_elements(*loc).is_displayed())
            return Driver.find_elements(*loc)
        except NoSuchElementException as e:
            print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, timeOut, loc, e))

    def click_keys(self, loc):
        """
        点击元素
        :param loc:元素定位
        :return:
        :usage:Driver.click_keys((By.XPATH,"//a"))
        """
        self.find_el(loc).click()

    def clear_keys(self, loc):
        """
        清除输入框的内容
        :param loc:元素定位
        :return:
        :usage:Driver.clear_keys((By.XPATH,"//a"))
        """
        self.find_el(loc).clear()

    def send_keys(self, loc, content):
        """
        向输入框发送内容:
        handle:元素句柄
        content:向元素发送的内容
        Usage:Driver.send_keys((By.XPATH,"//a"),'a')
        """
        self.clear_keys(loc).clear()
        self.find_el(loc).send_keys(content)

    def exec_script(self, Driver, src):
        """
        执行其它语言的脚本，JS
        :param src:
        :return:
        Usage:exec_script(src)
        """
        return Driver.execute_script(src)

    def right_click(self, Driver, loc):
        """
        右击
        :param loc:
        :return:
        Usage: right_click((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(Driver).context_click(el).perform()

    def move_to_element(self, Driver, loc):

        """
        移动鼠标到元素上
        :param loc:
        :return:
        Usage: move_to_element((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(Driver).move_to_element(el).perform()

    def double_click(self, Driver, loc):
        """
        双击
        :param loc:
        :return:
        Uage:Driver.double_click((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(Driver).double_click(el).perform()

    def drag_and_drop(self, Driver, loc1, loc2):
        """
        拖动元素到指定位置，PS：ActionChains的拖动并没那么有效果，这个需要再完善一下
        :param loc1: 起始位置
        :param loc2: 结束位置
        :return:
        Usage:Driver.drag_and_drop((By.XPATH,"//a"),(By.XPATH,"//b"))
        """
        element = self.find_el(loc1)
        target = self.find_el(loc2)
        ActionChains(Driver).drag_and_drop(element, target).perform()

    def get_display(self, Driver, timeOut, loc):
        """
        判断元素是否显示
        :param loc: 元素定位
        :return:
        """
        try:
            WebDriverWait(Driver, timeOut).until(lambda Driver: Driver.find_element(*loc).is_displayed())
            return True
        except Exception as e:
            print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, timeOut, loc, e))
            return False

    def isElement(self, Driver, identifyBy, c):
        """
        判断元素是否存在
        :param identifyBy:通过什么定位方式获取元素
        :param c: 定位方式的值
        :return:
        """
        time.sleep(1)
        flag = None
        try:
            if identifyBy == "id":
                # Driver.implicitly_wait(60)
                Driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # Driver.implicitly_wait(60)
                Driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                Driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                Driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                Driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                Driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                Driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                Driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException as e:
            print("%s 页面没有找到通过 %s %s 定位的元素。%s" % self, identifyBy, c, e)
            flag = False
        finally:
            return flag

    def refresh(self, Driver):
        """
        10s自动刷新页面
        :return:
        """
        Driver.implicitly_wait(10)
        Driver.refresh()

    def get_text(self, loc):
        """
        获取元素text内容
        :param loc:元素定位
        :return:
        """
        return self.find_el(loc).text



    #封装滑动方法

    def swipeUp(self, Driver, t=500, n=1):
        """
        向上滑动屏幕
        :param t: 滑动持续时间
        :param n: 滑动的次数
        :return:
        """
        l_winSize = Driver.get_window_size()
        x1 = l_winSize['width'] * 0.5  # x坐标
        y1 = l_winSize['height'] * 0.75  # 起始y坐标
        y2 = l_winSize['height'] * 0.25  # 终点y坐标
        for i in range(n):
            Driver.swipe(x1, y1, x1, y2, t)

    def swipeDown(self, Driver, t=500, n=1):
        """
        向下滑动屏幕
        :param t:  滑动持续时间
        :param n: 滑动的次数
        :return:
        """
        l_winSize = Driver.get_window_size()
        x1 = l_winSize['width'] * 0.5  # x坐标
        y1 = l_winSize['height'] * 0.25  # 起始y坐标
        y2 = l_winSize['height'] * 0.75  # 终点y坐标
        for i in range(n):
            Driver.swipe(x1, y1, x1, y2, t)

    def swipLeft(self, Driver, t=500, n=1):
        """
        向左滑动屏幕
        :param t: 滑动持续时间
        :param n: 滑动的次数
        :return:
        """
        l_winSize = Driver.get_window_size()
        x1 = l_winSize['width'] * 0.75
        y1 = l_winSize['height'] * 0.5
        x2 = l_winSize['width'] * 0.25
        for i in range(n):
            Driver.swipe(x1, y1, x2, y1, t)
            time.sleep(0.5)

    def swipRight(self, Driver, t=500, n=1):
        """
        向右滑动屏幕
        :param t: 滑动持续时间
        :param n: 滑动的次数
        :return:
        """
        l_winSize = Driver.get_window_size()
        x1 = l_winSize['width'] * 0.25
        y1 = l_winSize['height'] * 0.5
        x2 = l_winSize['width'] * 0.75
        for i in range(n):
            Driver.swipe(x1, y1, x2, y1, t)
