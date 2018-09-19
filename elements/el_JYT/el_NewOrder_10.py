"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_10.py
@time: 2018/9/17 11:47
@desc:��д��ϵ��
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_10():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder10_Common_Input(self, driver):
        """"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_edit_view"))
        return els

    def el_NewOrder10_Common_Add(self, driver):
        """"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_change_contacts"))
        return els

    def el_NewOrder10_Common_PopUp_Click(self, driver):
        """���������������"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els

    def el_NewOrder10_Common_PopUp_Title(self, driver):
        """��������title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder10_Common_PopUp_Items(self, driver):
        """��������items"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "text1"))
        return els

    def el_NewOrder10_Submit(self, driver):
        """���������������"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return els

