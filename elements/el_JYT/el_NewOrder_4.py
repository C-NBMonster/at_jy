"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_4.py
@time: 2018/9/14 10:29
@desc: ��ӿͻ���Ϣ���ϴ����֤����ס��ַ
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_4():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder4_IDCard_Front(self, driver):
        """���֤����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "iv_loading_front"))
        return el

    def el_NewOrder4_IDCard_Back(self, driver):
        """���֤����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "iv_loading_back"))
        return el

    def el_NewOrder4_Phone(self, driver):
        """�ֻ�����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "et_edit_view"))
        return el

    def el_NewOrder4_Submit(self, driver):
        """�ύ����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "tv_order"))
        return el

    def el_NewOrder4_Camera_Shot(self, driver):
        """����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "imbtn_takepic"))
        return el

    def el_NewOrder4_Camera_ReShot(self, driver):
        """����,0,�������� 1,���ı��� PS:�����涼�������Ԫ��ʱ��Ҫ�±ꡣ������Ҫ"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_remark_back"))
        return els

    def el_NewOrder4_Camera_Cancel(self, driver):
        """ȡ��������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "imbtn_camera_back"))
        return el

    def el_NewOrder4_ID_Name(self, driver):
        """����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "tv_name_front"))
        return el

    def el_NewOrder4_ID_No(self, driver):
        """���֤����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "et_idcard_front"))
        return el

    def el_NewOrder4_ID_Address(self, driver):
        """����ʡ����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "et_address_front"))
        return el

    def el_NewOrder4_Address_Click(self, driver):
        """����ѡ��ʡ��������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "tv_choose_address"))
        return el

    def el_NewOrder4_Choose_Address(self, driver):
        """ѡ��ʡ����"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_address"))
        return els

    def el_NewOrder4_Dialog_Close(self, driver):
        """�رյ�ַ�Ի���"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "iv_dialog_close"))
        return els

    def el_NewOrder4_ID_DateStart(self, driver):
        """���֤��Ч��ʼ����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "rl_date_start"))
        return el

    def el_NewOrder4_ID_DateEnd(self, driver):
        """���֤��Ч��������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "rl_date_end"))
        return el









