# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_17.py
@time: 2018/9/29 14:18
@desc: 运营商授权
"""

from common.rewrite import C_selenium_rewrite
from appium.webdriver.common.mobileby import MobileBy


class C_el_NewOrder_17():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder17_Operator_Authority(self, driver):
        """运营商授权认证"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_authorize")
        return el

    def el_NewOrder17_Skip_Authority(self, driver):
        """跳过授权认证"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_skip")
        return el