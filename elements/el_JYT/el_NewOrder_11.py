# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_11.py
@time: 2018/9/21 17:20
@desc: 绑定银行卡第一步
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_11():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder11_bind_BankCard_Owner(self, driver):
        """持有人"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_owner"))
        return el

    def el_NewOrder11_bind_BankCard_Number(self, driver):
        """银行卡号"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_cardNumber"))
        return el

    def el_NewOrder11_bind_BankCard_Support(self, driver):
        """支持银行卡"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_supported_bank"))
        return el

    def el_NewOrder11_bind_BankCard_Submit(self, driver):
        """支持银行卡"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el


