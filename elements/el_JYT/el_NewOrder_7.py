"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_7.py
@time: 2018/9/17 9:50
@desc: ������Ϣ �����ŵ�Ϳͻ�����������ע
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_7():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder7_Code_Click(self, driver):
        """��������ڲ����뵯��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_innerCode"))
        return el

    def el_NewOrder7_Is_MoveShop(self, driver):
        """�Ƿ��ƶ��ŵ�"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "is_move"))
        return el

    def el_NewOrder7_Remark(self, driver):
        """��ע"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_remark"))
        return el

    def el_NewOrder7_Submit(self, driver):
        """��һ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el

    def el_NewOrder7_PopUp(self, driver):
        """�����б��1,2,3"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv"))
        return els


