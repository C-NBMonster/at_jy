# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_4.py
@time: 2018/9/14 10:29
@desc: 添加客户信息：上传身份证，居住地址
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_4():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder4_IDCard_Front(self, driver):
        """身份证正面"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "iv_loading_front"))
        return el

    def el_NewOrder4_IDCard_Back(self, driver):
        """身份证背面"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "iv_loading_back"))
        return el

    def el_NewOrder4_Phone(self, driver):
        """手机号码"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "et_edit_view"))
        return el

    def el_NewOrder4_Submit(self, driver):
        """提交订单"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "tv_order"))
        return el

    def el_NewOrder4_Camera_Shot(self, driver):
        """拍照"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "imbtn_takepic"))
        return el

    def el_NewOrder4_Camera_ReShot(self, driver):
        """重拍,0,重拍正面 1,重拍背面 PS:正反面都出现这个元素时需要下标。否则不需要"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_remark_back"))
        return els

    def el_NewOrder4_Camera_Cancel(self, driver):
        """取消，返回"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "imbtn_camera_back"))
        return el

    def el_NewOrder4_ID_Name(self, driver):
        """姓名"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "tv_name_front"))
        return el

    def el_NewOrder4_ID_No(self, driver):
        """身份证号码"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "et_idcard_front"))
        return el

    def el_NewOrder4_ID_Address(self, driver):
        """所在省市区"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "et_address_front"))
        return el

    def el_NewOrder4_Address_Click(self, driver):
        """弹出选择省市区弹窗"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "tv_choose_address"))
        return el

    def el_NewOrder4_Choose_Address(self, driver):
        """选择省市区"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "tv_address"))
        return els

    def el_NewOrder4_Dialog_Close(self, driver):
        """关闭地址对话框"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, (By.ID, "iv_dialog_close"))
        return els

    def el_NewOrder4_ID_DateStart(self, driver):
        """身份证有效开始日期"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "rl_date_start"))
        return el

    def el_NewOrder4_ID_DateEnd(self, driver):
        """身份证有效结束日期"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, (By.ID, "rl_date_end"))
        return el









