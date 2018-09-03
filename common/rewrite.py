"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: rewrite.py
@time: 2018/9/3 14:14
@desc: ��дselenium�е�Ԫ�ز�������
"""
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time


class C_selenium_rewrite():
    """
    ��װ����API��ʹ�õ�ʱ��ǵð�By���������
    """
    def find_el(self, loc):
        """
        ���ҵ���Ԫ��
        :param loc:Ԫ�ض�λ
        :return:
        :usage:driver.find_el((By.XPATH,"//a"))
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print(u"%s ҳ���г�ʱ%dsδ���ҵ� %s Ԫ��%s" % (self, self.timeout, loc, e))

    def find_els(self, loc):
        """
        ���Ҷ��Ԫ��
        :param loc:Ԫ�ض�λ
        :return:
        :usage:driver.find_els((By.XPATH,"//a"))
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_elements(*loc).is_displayed())
            return self.driver.find_element(*loc)
        except Exception as e:
            print(u"%s ҳ���г�ʱ%dsδ���ҵ� %s Ԫ��%s" % (self, self.timeout, loc, e))

    def click_keys(self, loc):
        """
        ���Ԫ��
        :param loc:Ԫ�ض�λ
        :return:
        :usage:driver.click_keys((By.XPATH,"//a"))
        """
        self.find_el(loc).click()

    def clear_keys(self, loc):
        """
        �������������
        :param loc:Ԫ�ض�λ
        :return:
        :usage:driver.clear_keys((By.XPATH,"//a"))
        """
        self.find_el(loc).clear()

    def send_keys(self, loc, content):
        """
        �������������:
        handle:Ԫ�ؾ��
        content:��Ԫ�ط��͵�����
        Usage:driver.send_keys((By.XPATH,"//a"),'a')
        """
        self.clear_keys(loc).clear()
        self.find_el(loc).send_keys(content)

    def exec_script(self, src):
        """
        ִ���������ԵĽű���JS
        :param src:
        :return:
        Usage:exec_script(src)
        """
        return self.driver.execute_script(src)

    def right_click(self, loc):
        """
        �һ�
        :param loc:
        :return:
        Usage: right_click((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, loc):

        """
        �ƶ���굽Ԫ����
        :param loc:
        :return:
        Usage: move_to_element((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, loc):
        """
        ˫��
        :param loc:
        :return:
        Uage:driver.double_click((By.XPATH,"//a"))
        """
        el = self.find_el(loc)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, loc1, loc2):
        """
        �϶�Ԫ�ص�ָ��λ�ã�PS��ActionChains���϶���û��ô��Ч���������Ҫ������һ��
        :param loc1: ��ʼλ��
        :param loc2: ����λ��
        :return:
        Usage:driver.drag_and_drop((By.XPATH,"//a"),(By.XPATH,"//b"))
        """
        element = self.find_el(loc1)
        target = self.find_el(loc2)
        ActionChains(self.driver).drag_and_drop(element, target).perform()

    def get_display(self, loc):
        """
        �ж�Ԫ���Ƿ���ʾ
        :param loc: Ԫ�ض�λ
        :return:
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(lambda driver: driver.find_element(*loc).is_displayed())
            return True
        except Exception as e:
            print(u"%s ҳ���г�ʱ%dsδ���ҵ� %s Ԫ��%s" % (self, self.timeout, loc, e))
            return False

    def isElement(self, identifyBy, c):
        """
        �ж�Ԫ���Ƿ����
        :param identifyBy:ͨ��ʲô��λ��ʽ��ȡԪ��
        :param c: ��λ��ʽ��ֵ
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
            print("%s ҳ��û���ҵ�ͨ�� %s %s ��λ��Ԫ�ء�%s" % self, identifyBy, c, e)
            flag = False
        finally:
            return flag

    def refresh(self):
        """
        10s�Զ�ˢ��ҳ��
        :return:
        """
        self.driver.implicitly_wait(10)
        self.driver.refresh()

    def get_text(self, loc):
        """
        ��ȡԪ��text����
        :param loc:Ԫ�ض�λ
        :return:
        """
        return self.find_el(loc).text

