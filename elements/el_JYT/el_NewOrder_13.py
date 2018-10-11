# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_13.py
@time: 2018/9/28 17:42
@desc: 绑定银行卡，四要素二次短信授权
"""
from common.rewrite import C_selenium_rewrite
from appium.webdriver.common.mobileby import MobileBy


class C_el_NewOrder_13():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder13_bankInfo(self, driver):
        """银行卡信息"""
        els = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_right")
        return els

    def el_NewOrder13_SendBtn(self, driver):
        """发送按钮"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_sendCode")
        return el

    def el_NewOrder13_Code(self, driver):
        """发送按钮"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "et_code")
        return el

    def el_NewOrder13_Submit(self, driver):
        """发送按钮"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "et_next")
        return el