# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_9.py
@time: 2018/9/17 11:14
@desc: 填写单位信息
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_9():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder9_syncAddress(self, driver):
        """同步现居住地址"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "toggleSwitch"))
        return el

    def el_NewOrder9_Common_Click(self, driver):
        """公共：点击弹出弹窗"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els

    def el_NewOrder9_Common_Input(self, driver):
        """公共：输入框"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_edit_view"))
        return els

    def el_NewOrder9_Submit(self, driver):
        """提交，下一步"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el

    # 弹窗元素------------------------------
    # 地址弹窗

    def el_NewOrder9_Address_List(self, driver):
        """选择省市区"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_address"))
        return els

    def el_NewOrder9_PoUp_Close(self, driver):
        """关闭弹窗"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_dialog_close"))
        return el

        # 教育程度弹窗

    def el_NewOrder9_Common_Title(self, driver):
        """行业类别，单位性质，职位，工作年限 公共弹窗title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder9_Common_Items(self, driver):
        """行业类别，单位性质，职位，工作年限 公共弹窗列表项"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "text1"))
        return els

    def el_NewOrder9_EntryTime_Title(self, driver):
        """入职时间title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_title"))
        return el

    def el_NewOrder9_EntryTime_Year(self, driver):
        """入职时间:年"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "wl1"))
        return el

    def el_NewOrder9_EntryTime_Month(self, driver):
        """入职时间:月"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "wl2"))
        return el

    def el_NewOrder9_EntryTime_Cancel(self, driver):
        """取消，关闭弹窗"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_left"))
        return el

    def el_NewOrder9_EntryTime_Confirm(self, driver):
        """确认 选择时间"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_right"))
        return el



