# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_2.py
@time: 2018/9/13 10:33
@desc: 新建订单第二个页面
"""

from common.rewrite import C_selenium_rewrite
from appium.webdriver.common.mobileby import MobileBy


class C_el_NewOrder_2():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder2_LoanSum(self, driver):
        """第二页显示的贷款金额"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_loan_sum")
        return el

    def el_NewOrder2_Insurance_Fee(self, driver):
        """开启或关闭参加免还大礼包"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "switch_insurance")
        return el

    def el_NewOrder2_Treasure_Fee(self, driver):
        """开启或关闭参加免还大礼包"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "switch_treasure")
        return  el

    def el_NewOrder2_CouponPrice(self, driver):
        """商城抵用券"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_coupon_price")
        return el

    def el_NewOrder2_InstalmentItem(self, driver):
        """分期标号，用于判断选择分期"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "tv_str1")
        return els

    def el_NewOrder2_ProductCode(self, driver):
        """产品代码，用处是：如果第三个页面需要验证数据，则需获取这个值"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "tv_str3")
        return els

    def el_NewOrder2_InstalmentList(self, driver):
        """商品的分期方案列表，选择分期"""
        els = self.C_sel_Rewrite.find_els(driver, MobileBy.ID, "ll_background")
        return els

    def el_NewOrder2_Submit(self, driver):
        """下一步"""
        el = self.C_sel_Rewrite.find_el(driver, MobileBy.ID, "tv_installment_next")
        return el
