# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_7.py
@time: 2018/9/17 9:50
@desc: 其它信息 ，对门店和客户的评定，备注
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_7():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder7_Code_Click(self, driver):
        """点击弹出内部代码弹窗"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_innerCode"))
        return el

    def el_NewOrder7_Is_MoveShop(self, driver):
        """是否移动门店"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "is_move"))
        return el

    def el_NewOrder7_Remark(self, driver):
        """备注"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_remark"))
        return el

    def el_NewOrder7_Submit(self, driver):
        """下一步"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el

    def el_NewOrder7_PopUp(self, driver):
        """弹窗列表项：1,2,3"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv"))
        return els


