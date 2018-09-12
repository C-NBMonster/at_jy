"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_login.py
@time: 2018/9/11 17:30
@desc: 登录模块代码
"""

import unittest
from elements.el_JYT.el_login import C_el_login
from common.rewrite import C_selenium_rewrite

class C_B_Login(unittest.TestCase):

    def __init__(self):
        self.C_sel_rewrite = C_selenium_rewrite()
        self.Cel_Login = C_el_login()

    def b_login_uName(self, driver, uName):
        """
        登录
        :param uName: 账号
        :return:
        """
        self.C_sel_rewrite.send_keys(self.Cel_Login.el_Login_uName(driver), uName)

    def b_login_pwd(self, driver, pwd):
        """
        密码
        :param driver:
        :param pwd:
        :return:
        """
        self.C_sel_rewrite.send_keys(self.Cel_Login.el_login_pwd(driver), pwd)

    def b_login_submit(self, driver):
        """
        提交
        :param driver:
        :return:
        """
        self.Cel_Login.el_login_submit(driver).click()

    def b_login(self, driver, uName, pwd):
        """
        登录逻辑代码汇总
        :param driver:
        :param uName:
        :param pwd:
        :return:
        """
        self.b_login_uName(driver, uName)
        self.b_login_pwd(driver, pwd)
        self.b_login_submit(driver)

    def accept_PopUp(self, driver):
        """
        点击弹窗，然后显示主页面
        :param driver:
        :return:
        """
        self.Cel_Login.el_main_PopUp_1_OK(driver).click()
        self.Cel_Login.el_main_PopUp_2_NotSetPWD(driver).click()
        self.Cel_Login.el_main_PopUp_3_OK(driver).click()


