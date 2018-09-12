"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_login.py
@time: 2018/9/11 17:35
@desc: ��¼ģ��Ԫ�ؿ�
"""
from selenium.webdriver.common.by import By
from common.rewrite import C_selenium_rewrite
class C_el_login():
    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_Login_uName(self, driver):
        """
        �û���
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "et_account"))
        return el

    def el_login_pwd(self, driver):
        """
        �û�����
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "et_pwd"))
        return el

    def el_login_submit(self, driver):
        """
        �ύ
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_login"))
        return el

    # ��¼֮�����������
    def el_main_PopUp_1_OK(self, driver):
        """
        ��һ��������OK��ť
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_ok"))
        return el

    def el_main_PopUp_2_SetPWD(self, driver):
        """
        �ڶ��������������������� ��ť
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_set"))
        return el

    def el_main_PopUp_2_NotSetPWD(self, driver):
        """
        �ڶ����������������������� ��ť
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_not_set"))
        return el

    def el_main_PopUp_3_OK(self, driver):
        """
        ������������OK ��ť
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_right"))
        return el







