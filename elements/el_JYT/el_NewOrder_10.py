# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_10.py
@time: 2018/9/17 11:47
@desc:填写联系人
"""

from common.rewrite import C_selenium_rewrite
from appium.webdriver.common.mobileby import MobileBy


class C_el_NewOrder_10():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder10_Common_Input(self, driver):
        """"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "et_edit_view")
        return els

    def el_NewOrder10_Common_Add(self, driver):
        """"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "iv_change_contacts")
        return els

    def el_NewOrder10_Common_PopUp_Click(self, driver):
        """公共点击弹出弹窗"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "tv_choose_right")
        return els

    def el_NewOrder10_Common_PopUp_Title(self, driver):
        """公共弹窗title"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_choose_title")
        return el

    def el_NewOrder10_Common_PopUp_Items(self, driver):
        """公共弹窗items"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "text1")
        return els

    def el_NewOrder10_Submit(self, driver):
        """公共点击弹出弹窗"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_next")
        return els

