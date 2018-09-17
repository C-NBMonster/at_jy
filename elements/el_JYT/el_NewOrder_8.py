"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_8.py
@time: 2018/9/17 10:02
@desc: ��д���˻�����Ϣ
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_8():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder8_County_Click(self, driver):
        """��˳���أ������̶ȣ�����״�� ��������"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els

    def el_NewOrder8_Common_Input(self, driver):
        """����򹫹�����"""
        #���ϵ��°�˳����ϸ��ַ�����������룬������֧������ͥ������,qq,��������

        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_edit_view"))
        return els


    def el_NewOrder8_Children_Num(self, driver):
        """��Ů��Ŀ"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_people"))
        return el

    def el_NewOrder8_Subtract(self, driver):
        """��Ů������1"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_people"))
        return el

    def el_NewOrder8_Add(self, driver):
        """��Ů������1"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_add"))
        return el

    def el_NewOrder8_Submit(self, driver):
        """��һ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el


    #����Ԫ��------------------------------
    #��ַ����
    def el_NewOrder8_Choose_Address(self, driver):
        """ѡ��ʡ�������Զ��ж�ip����ʡ"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_address"))
        return els

    def el_NewOrder8_PoUp_Close(self, driver):
        """�رյ���"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_dialog_close"))
        return el

    #�����̶ȵ���
    def el_NewOrder8_EduMar_Title(self, driver):
        """������������������title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder8_EduMar_Items(self, driver):
        """�������������������б���"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "text1"))
        return els








