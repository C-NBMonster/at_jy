"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_8.py
@time: 2018/9/17 10:02
@desc: 填写个人基本信息
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_8():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder8_County_Click(self, driver):
        """按顺序，县，教育程度，婚姻状况 公共弹窗"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els

    def el_NewOrder8_Common_Input(self, driver):
        """输入框公共函数"""
        #从上到下按顺序：详细地址，个人月收入，个人月支出，家庭总收入,qq,电子邮箱

        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_edit_view"))
        return els


    def el_NewOrder8_Children_Num(self, driver):
        """子女数目"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_people"))
        return el

    def el_NewOrder8_Subtract(self, driver):
        """子女数量减1"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_people"))
        return el

    def el_NewOrder8_Add(self, driver):
        """子女数量加1"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_add"))
        return el

    def el_NewOrder8_Submit(self, driver):
        """下一步"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el


    #弹窗元素------------------------------
    #地址弹窗
    def el_NewOrder8_Choose_Address(self, driver):
        """选择省市区，自动判定ip所在省"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_address"))
        return els

    def el_NewOrder8_PoUp_Close(self, driver):
        """关闭弹窗"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_dialog_close"))
        return el

    #教育程度弹窗
    def el_NewOrder8_EduMar_Title(self, driver):
        """教育、婚姻公共弹窗title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder8_EduMar_Items(self, driver):
        """教育、婚姻公共弹窗列表项"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "text1"))
        return els








