# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_os.py
@time: 2018/9/29 16:22
@desc: ϵͳӦ�ù���Ԫ�ؿ�
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_OS():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    #�����-----------------------------------------------------------------------------------------------------
    def el_OS_Camera_Shot(self, driver):
        """���հ�ť"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "shutter_button"))
        return el

    def el_OS_Camera_ReShot(self, driver):
        """����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "btn_retake"))
        return el

    def el_OS_Camera_Cancel(self, driver):
        """ȡ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "btn_cancel"))
        return el

    def el_OS_Camera_Done(self, driver):
        """ȷ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "btn_done"))
        return el