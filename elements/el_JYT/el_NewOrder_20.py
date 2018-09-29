# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_20.py
@time: 2018/9/29 17:20
@desc: �ύ�����ɹ�ҳ
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_20():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder20_Success_Title(self, driver):
        """�ɹ�ҳTitle"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "top_tab_center_title"))
        return el

    def el_NewOrder20_Success_JumpTo_Order(self, driver):
        """�鿴����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_finish"))
        return el
