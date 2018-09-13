"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_2.py
@time: 2018/9/13 10:33
@desc: �½������ڶ���ҳ��
"""

from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_2():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder2_LoanSum(self, driver):
        """�ڶ�ҳ��ʾ�Ĵ�����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_loan_sum"))
        return el

    def el_NewOrder2_Insurance_Fee(self, driver):
        """������رղμ��⻹�����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "switch_insurance"))
        return el

    def el_NewOrder2_Treasure_Fee(self, driver):
        """������رղμ��⻹�����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "switch_treasure"))
        return  el

    def el_NewOrder2_CouponPrice(self, driver):
        """�̳ǵ���ȯ"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_coupon_price"))
        return el

    def el_NewOrder2_InstalmentItem(self, driver):
        """���ڱ�ţ������ж�ѡ�����"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_str1"))
        return els

    def el_NewOrder2_ProductCode(self, driver):
        """��Ʒ���룬�ô��ǣ����������ҳ����Ҫ��֤���ݣ������ȡ���ֵ"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_str3"))
        return els

    def el_NewOrder2_InstalmentList(self, driver):
        """��Ʒ�ķ��ڷ����б�ѡ�����"""
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "ll_background"))
        return els

    def el_NewOrder2_Submit(self, driver):
        """��һ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_installment_next"))
        return el
