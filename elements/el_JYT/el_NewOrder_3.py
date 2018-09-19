"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_3.py
@time: 2018/9/13 16:06
@desc: 新建订单第三个页面
"""


from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_3():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "找不到页面元素，请检查元素是否已被加载，或是否可见"

    def el_NewOrder3_GoodPrice(self, driver):
        """商品金额"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_goods_sum"))
        return el

    def el_NewOrder3_DownPayment(self, driver):
        """首付金额"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_down_payments"))
        return el

    def el_NewOrder3_LoanSum(self, driver):
        """贷款金额"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_loan_sum"))
        return el

    def el_NewOrder3_InstalmentNum(self, driver):
        """分期数"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_loan_sum"))
        return el

    def el_NewOrder3_Pay_PerMonth(self, driver):
        """每月应还"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_installment_price"))
        return el

    def el_NewOrder3_ProductCode(self, driver):
        """产品代码"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_installment_code"))
        return el

    def el_NewOrder3_Add_GoodType(self, driver):
        """添加商品类型。PS:添加多一个商品"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_change_goods"))
        return el

    def el_NewOrder3_Edit_GoodPrice(self, driver):
        """编辑框：商品价格"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_change_goods"))
        return el

    def el_NewOrder3_Edit_GP_DP(self, driver, opt):
        """
        编辑框：1商品价格和2首付金额
        :param driver:
        :param opt: 0商品价格 1首付金额 2商品型号
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_change_goods"))
        return els[opt]

    def el_NewOrder3_Choose_GoodsInfo_Click(self, driver, opt):
        """
        点击弹出下拉框：1商品小类 2商品品牌 3商品型号
        :param driver:
        :param opt: 1商品小类 2商品品牌 3商品型号
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els[opt]

    def el_NewOrder3_Next(self, driver):
        """
        下一步。PS:如果走的是分段式的流程，这里是扫码客户二维码
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el

    #下拉框公共
    def el_NewOrder3_PopUp_Common_Title(self, driver):
        """
        弹窗title
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder3_PopUp_Common_Items(self, driver):
        """
        列表项
        :param driver:
        :strTypes:商品类型
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_text"))
        return els

    def el_NewOrder3_PopUp_Brand_SKU(self, driver):
        """
        列表项
        :param driver:
        :strTypes:商品品牌，型号
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "text1"))
        return els




