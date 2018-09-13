"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_1.py
@time: 2018/9/7 17:05
@desc: 即有宝新建订单页面元素
"""
from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By
class C_el_NewOrder_1():
    
    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder1_ChooseBaseInfo_PopUP(self, driver, opt):
        """
        点击商品门店，商品类型，产品版本，产品类型 -->弹出弹窗
        :param driver:
        :param opt: 1：商品门店:2：商品类型，3：产品版本，4：产品类型
        :return:
        """
        #els = driver.find_elements_by_id("iv_right")
        els = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_right"))
        els[opt].click()

    def el_NewOrder1_ChooseRight(self, driver, opt):
        """
        这个元素用于显示用户选择的内容
        :param driver:
        :param opt: 1：商品门店:2：商品类型，3：产品版本，4：产品类型
        :return:
        """
        els = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els[opt]

    def el_NewOrder1_MoneyTotle(self, driver, opt):
        """
        商品总额，首付总额
        :param driver:
        :param opt: 1:商品总额，2:首付总额
        :return:
        """
        els = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_edit_view"))
        return els[opt]

    def el_NewOrder1_LoanSum(self, driver):
        """
        贷款金额
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_loan_sum"))
        return el

    def el_NewOrder_submit_1(self, driver):
        """
        按钮：下一步
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_newbuild_next"))
        return el

    #以下为弹窗元素，PS，弹窗的设计框架一致，连id都一致，所以，弹窗部分，两个函数即可搞定

    def el_NewOrder_Common_PopUp_Title(self, driver):
        """
        弹窗title
        :param driver:

        :return:
        """
        #els = driver.find_elements_by_id("iv_right")
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder_Common_PopUp_List(self, driver, strName):
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "test1"))
        for n in els:
            if n.text().strip() == strName.strip():
                return n
            else:
                print("没有找到对应元素，请检查输入内容是否有误")
                break











