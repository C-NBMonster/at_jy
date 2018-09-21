# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_12.py
@time: 2018/9/21 17:29
@desc:�����п��ڶ���
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_12():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder12_bind_BankCard_Owner(self, driver):
        """������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_owner"))
        return el

    def el_NewOrder12_bind_BankCard_Number(self, driver):
        """���п���"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_cardNumber"))
        return el

    def el_NewOrder12_bind_BankCard_BankName(self, driver):
        """������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_bankName"))
        return el

    def el_NewOrder12_bind_BankCard_BankAddr_click(self, driver):
        """���п�����ʡ����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_bankBra"))
        return el

    def el_NewOrder12_bind_BankCard_BankAddr_List(self, driver):
        """���п�����ʡ�����б�"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_address"))
        return els

    def el_NewOrder12_bind_BankCard_Phone(self, driver):
        """����Ԥ���ֻ���"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_phone"))
        return el

    def el_NewOrder12_bind_BankCard_Submit(self, driver):
        """֧�����п�"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el