# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_13.py
@time: 2018/9/28 17:42
@desc: �����п�����Ҫ�ض��ζ�����Ȩ
"""
from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_13():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder13_bankInfo(self, driver):
        """���п���Ϣ"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_right"))
        return els

    def el_NewOrder13_SendBtn(self, driver):
        """���Ͱ�ť"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_sendCode"))
        return el

    def el_NewOrder13_Code(self, driver):
        """���Ͱ�ť"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_code"))
        return el

    def el_NewOrder13_Submit(self, driver):
        """���Ͱ�ť"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_next"))
        return el