"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_login.py
@time: 2018/9/11 17:35
@desc: 登录模块元素库
"""
from selenium.webdriver.common.by import By
from common.rewrite import C_selenium_rewrite
class C_el_login():
    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_Login_uName(self, driver):
        """
        用户名
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "et_account"))
        return el

    def el_login_pwd(self, driver):
        """
        用户密码
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "et_pwd"))
        return el

    def el_login_submit(self, driver):
        """
        提交
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_login"))
        return el

    # 登录之后的三个弹窗
    def el_main_PopUp_1_OK(self, driver):
        """
        第一个弹窗，OK按钮
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_ok"))
        return el

    def el_main_PopUp_2_SetPWD(self, driver):
        """
        第二个弹窗，设置手势密码 按钮
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_set"))
        return el

    def el_main_PopUp_2_NotSetPWD(self, driver):
        """
        第二个弹窗，不设置手势密码 按钮
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_not_set"))
        return el

    def el_main_PopUp_3_OK(self, driver):
        """
        第三个弹窗，OK 按钮
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, 1, self.el_error_prompt, (By.ID, "tv_right"))
        return el







