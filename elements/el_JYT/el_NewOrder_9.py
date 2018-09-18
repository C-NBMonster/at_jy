"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_9.py
@time: 2018/9/17 11:14
@desc: ��д��λ��Ϣ
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_9():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder9_syncAddress(self, driver):
        """ͬ���־�ס��ַ"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "toggleSwitch"))
        return el

    def el_NewOrder9_Common_Click(self, driver):
        """�����������������"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els

    def el_NewOrder9_Common_Input(self, driver):
        """�����������"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_edit_view"))
        return els

    # ����Ԫ��------------------------------
    # ��ַ����

    def el_NewOrder9_Address_List(self, driver):
        """ѡ��ʡ����"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_address"))
        return els

    def el_NewOrder9_PoUp_Close(self, driver):
        """�رյ���"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_dialog_close"))
        return el

        # �����̶ȵ���

    def el_NewOrder9_Common_Title(self, driver):
        """��ҵ��𣬵�λ���ʣ�ְλ���������� ��������title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder9_Common_Items(self, driver):
        """��ҵ��𣬵�λ���ʣ�ְλ���������� ���������б���"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "text1"))
        return els

    def el_NewOrder9_EntryTime_Title(self, driver):
        """��ְʱ��title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_title"))
        return el

    def el_NewOrder9_EntryTime_Year(self, driver):
        """��ְʱ��:��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "wl1"))
        return el

    def el_NewOrder9_EntryTime_Month(self, driver):
        """��ְʱ��:��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "wl2"))
        return el

    def el_NewOrder9_EntryTime_Cancel(self, driver):
        """ȡ�����رյ���"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_left"))
        return el

    def el_NewOrder9_EntryTime_Confirm(self, driver):
        """ȷ�� ѡ��ʱ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_right"))
        return el



