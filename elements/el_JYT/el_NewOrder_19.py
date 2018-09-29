# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_19.py
@time: 2018/9/29 16:10
@desc: ��ʮ�Ų� Ӱ��֤��
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_19():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder19_ImageProof_Title(self, driver):
        """Ӱ��֤��title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "top_tab_center_title"))
        return el

    def el_NewOrder19_ImageProof_IMG_Common(self, driver):
        """ͼƬ��Ԫ�أ��ӵ���������������Ҫ��ô����Ĭ�����ĸ���˳�򣺿ͻ��ŵ���Ƭ�����֤����֤�����֤�����棬���п���
        PS���������һ��ͼƬ����һ�У����ܻᵼ�¶�λ����Ԫ��"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "gv_otherCertificate"))
        return els

    def el_NewOrder19_ImageProof_BankIMG(self, driver):
        """����Ӱ��"""
        hEls = self.el_NewOrder19_ImageProof_IMG_Common(driver)
        el = hEls[3].find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_photo"))
        return el

    def el_NewOrder19_ImageProof_More(self, driver):
        """����Ӱ��֤��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.XPATH, "//*[@text='����֤��']"))
        return el

    def el_NewOrder19_Submit(self, driver):
        """�ύ"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_commit"))
        return el

    def el_NewOrder19_PopUP_PWD(self, driver):
        """���������¼����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_pwd"))
        return el

    def el_NewOrder19_PopUP_Confirm(self, driver):
        """����ȷ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_confirm"))
        return el


