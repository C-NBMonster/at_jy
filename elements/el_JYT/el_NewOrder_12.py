# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_12.py
@time: 2018/9/21 17:29
@desc:绑定银行卡第二步
"""

from common.rewrite import C_selenium_rewrite
from appium.webdriver.common.mobileby import MobileBy


class C_el_NewOrder_12():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder12_bind_BankCard_Owner(self, driver):
        """持有人"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_owner")
        return el

    def el_NewOrder12_bind_BankCard_Number(self, driver):
        """银行卡号"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_cardNumber")
        return el

    def el_NewOrder12_bind_BankCard_BankName(self, driver):
        """银行名"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_bankName")
        return el

    def el_NewOrder12_bind_BankCard_BankAddr_click(self, driver):
        """银行开户行省市区"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_bankBra")
        return el

    def el_NewOrder12_bind_BankCard_BankAddr_List(self, driver):
        """银行开户行省市区列表"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "tv_address")
        return els

    def el_NewOrder12_bind_BankCard_Phone(self, driver):
        """银行预留手机号"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "et_phone")
        return el

    def el_NewOrder12_bind_BankCard_Submit(self, driver):
        """提交"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_next")
        return el
