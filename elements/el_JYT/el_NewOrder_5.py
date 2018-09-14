"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_5.py
@time: 2018/9/14 17:52
@desc: �½��������岽����ӵ�Ա����
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_5():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder5_GroupPhoto_click(self, driver):
        """����������"""
        el  = self.C_sel_Rewrite.find_el(driver,self.timeOut,(By.XPATH, "//*[@class='android.widget.ImageView']"))
        return el

    def el_NewOrder5_Submit(self, driver):
        """����������"""
        el  = self.C_sel_Rewrite.find_el(driver,self.timeOut,(By.ID, "tv_next"))
        return el

    def el_NewOrder5_Camera_Cancel(self, driver):
        """ȡ��"""
        el  = self.C_sel_Rewrite.find_el(driver,self.timeOut,(By.ID, "btn_cancel"))
        return el

    def el_NewOrder5_Camera_Shot(self, driver):
        """����"""
        el  = self.C_sel_Rewrite.find_el(driver,self.timeOut,(By.ID, "shutter_button"))
        return el

