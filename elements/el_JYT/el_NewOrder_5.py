# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_5.py
@time: 2018/9/14 17:52
@desc: 新建订单第五步，添加店员合照
"""

from common.rewrite import C_selenium_rewrite
from appium.webdriver.common.mobileby import MobileBy


class C_el_NewOrder_5():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder5_GroupPhoto_click(self, driver):
        """点击，打开相机"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.XPATH, "//*[@class='android.widget.ImageView']")
        return el

    def el_NewOrder5_Submit(self, driver):
        """点击，打开相机"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_next")
        return el

    def el_NewOrder5_Camera_Cancel(self, driver):
        """取消"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "btn_cancel")
        return el

    def el_NewOrder5_Camera_Done(self, driver):
        """最终选择"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "btn_done")
        return el

    def el_NewOrder5_Camera_Shot(self, driver):
        """拍照"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "shutter_button")
        return el

    def el_NewOrder5_Camera_Reshot(self, driver):
        """最终选择"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "btn_retake")
        return el