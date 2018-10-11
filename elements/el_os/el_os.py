# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_os.py
@time: 2018/9/29 16:22
@desc: 系统应用公共元素库
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_OS():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    #照相机-----------------------------------------------------------------------------------------------------
    def el_OS_Camera_Shot(self, driver):
        """拍照按钮"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "shutter_button"))
        return el

    def el_OS_Camera_ReShot(self, driver):
        """重拍"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "btn_retake"))
        return el

    def el_OS_Camera_Cancel(self, driver):
        """取消"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "btn_cancel"))
        return el

    def el_OS_Camera_Done(self, driver):
        """确认"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "btn_done"))
        return el