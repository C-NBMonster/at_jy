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
    def find_el(self, loc):
        """
        查找单个元素
        :param loc:元素定位
        :return:
        :usage:driver.find_el((By.XPATH,"//a"))
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, self.timeout, loc, e))

    def find_els(self, loc):
        """
        查找多个元素
        :param loc:元素定位
        :return:
        :usage:driver.find_els((By.XPATH,"//a"))
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_elements(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, self.timeout, loc, e))

    def click_keys(self, loc):
        """
        点击元素
        :param loc:元素定位
        :return:
        :usage:driver.click_keys((By.XPATH,"//a"))
        """
        self.find_el(loc).click()

    def clear_keys(self, loc):
        """
        清除输入框的内容
        :param loc:元素定位
        :return:
        :usage:driver.clear_keys((By.XPATH,"//a"))
        """
        self.find_el(loc).clear()

    def send_keys(self, loc, content):
        """
        向输入框发送内容:
        handle:元素句柄
        content:向元素发送的内容
        Usage:driver.send_keys((By.XPATH,"//a"),'a')
        """
        self.clear_keys(loc).clear()
        self.find_el(loc).send_keys(content)

    def exec_script(self, src):
        """
        执行其它语言的脚本，JS
        :param src:
        :return:
        Usage:exec_script(src)
        """
        return self.driver.execute_script(src)

    def right_click(self, loc):
        """
        右击
        :param loc:
        :return:
        Usage: right_click((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, loc):

        """
        移动鼠标到元素上
        :param loc:
        :return:
        Usage: move_to_element((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, loc):
        """
        双击
        :param loc:
        :return:
        Uage:driver.double_click((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, loc1, loc2):
        """
        拖动元素到指定位置，PS：ActionChains的拖动并没那么有效果，这个需要再完善一下
        :param loc1: 起始位置
        :param loc2: 结束位置
        :return:
        Usage:driver.drag_and_drop((By.XPATH,"//a"),(By.XPATH,"//b"))
        """
        element = self.find_el(loc1)
        target = self.find_el(loc2)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def get_display(self, loc):
        """
        判断元素是否显示
        :param loc: 元素定位
        :return:
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return True
        except Exception as e:
            print(u"%s 页面中超时%ds未能找到 %s 元素%s" % (self, self.timeout, loc, e))
            return False

    def isElement(self, identifyBy, c):
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
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_id(c)
            elif identifyBy == "xpath":
                # self.driver.implicitly_wait(60)
                self.driver.find_element_by_xpath(c)
            elif identifyBy == "class":
                self.driver.find_element_by_class_name(c)
            elif identifyBy == "link text":
                self.driver.find_element_by_link_text(c)
            elif identifyBy == "partial link text":
                self.driver.find_element_by_partial_link_text(c)
            elif identifyBy == "name":
                self.driver.find_element_by_name(c)
            elif identifyBy == "tag name":
                self.driver.find_element_by_tag_name(c)
            elif identifyBy == "css selector":
                self.driver.find_element_by_css_selector(c)
            flag = True
        except NoSuchElementException as e:
            print("%s 页面没有找到通过 %s %s 定位的元素。%s" % self, identifyBy, c, e)
            flag = False
        finally:
            return flag

    def refresh(self):
        """
        10s自动刷新页面
        :return:
        """
        self.driver.implicitly_wait(10)
        self.driver.refresh()

    def get_text(self, loc):
        """
        获取元素text内容
        :param loc:元素定位
        :return:
        """
        return self.find_el(loc).text

