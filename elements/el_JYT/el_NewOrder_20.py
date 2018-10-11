# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_20.py
@time: 2018/9/29 17:20
@desc: 提交订单成功页
"""

from common.rewrite import C_selenium_rewrite
from appium.webdriver.common.mobileby import MobileBy


class C_el_NewOrder_20():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 10
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder20_Success_Title(self, driver):
        """成功页Title"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "top_tab_center_title")
        return el

    def el_NewOrder20_Success_JumpTo_Order(self, driver):
        """查看订单"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_finish")
        return el
