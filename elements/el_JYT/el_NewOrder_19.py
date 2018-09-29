# coding = utf-8  
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_19.py
@time: 2018/9/29 16:10
@desc: 第十九步 影像证明
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_19():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder19_ImageProof_Title(self, driver):
        """影像证明title"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "top_tab_center_title"))
        return el

    def el_NewOrder19_ImageProof_IMG_Common(self, driver):
        """图片父元素，坑爹的命名方法导致要这么做，默认有四个，顺序：客户门店照片，身份证人像证，身份证国徽面，银行卡。
        PS：如果任意一种图片超过一行，可能会导致定位不到元素"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "gv_otherCertificate"))
        return els

    def el_NewOrder19_ImageProof_BankIMG(self, driver):
        """银行影像"""
        hEls = self.el_NewOrder19_ImageProof_IMG_Common(driver)
        el = hEls[3].find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_photo"))
        return el

    def el_NewOrder19_ImageProof_More(self, driver):
        """更多影像证明"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.XPATH, "//*[@text='更多证明']"))
        return el

    def el_NewOrder19_Submit(self, driver):
        """提交"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_commit"))
        return el

    def el_NewOrder19_PopUP_PWD(self, driver):
        """弹窗输入登录密码"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_pwd"))
        return el

    def el_NewOrder19_PopUP_Confirm(self, driver):
        """弹窗确认"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_confirm"))
        return el


