# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_18.py
@time: 2018/9/29 14:29
@desc: С�ʾ�
"""


from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_18():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder18_Questionnaire_Title(self, driver):
        """�ʾ����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "top_tab_center_title"))
        return el

    def el_NewOrder18_Question_1(self, driver):
        """����1����ǰ�������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_time"))
        return el

    def el_NewOrder18_Question_2(self, driver):
        """����2���������֪���б�"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose"))
        return els

    def el_NewOrder18_Submit(self, driver):
        """�ύ"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_questionnaire_next"))
        return el


