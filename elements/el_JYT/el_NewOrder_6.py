"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_6.py
@time: 2018/9/17 9:43
@desc:短信征信授权
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_6():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder6_Phone(self, driver):
        """手机号"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_phonenumber"))
        return el

    def el_NewOrder6_Time(self, driver):
        """倒计时"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_code"))
        return el

    def el_NewOrder6_Protocal(self, driver):
        """征信授权协议"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_protocol"))
        return el

    def el_NewOrder6_Submit(self, driver):
        """授权验证"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_authorize"))
        return el
