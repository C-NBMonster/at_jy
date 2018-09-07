"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder.py
@time: 2018/9/7 17:05
@desc: 即有宝新建订单页面元素
"""


class C_el_NewOrder():

    def el_ChooseBaseInfo(self,driver, opt):
        """
        选择商品门店，商品类型，产品版本，产品类型
        :param driver:
        :param opt: 1：商品门店:2：商品类型，3：产品版本，4：产品类型
        :return:
        """
        els = driver.find_elements_by_id("iv_right")
        els[opt].click()

    def el_MoneyTotle(self, driver, opt):
        """
        商品总额，首付总额
        :param driver:
        :param opt: 1:商品总额，2:首付总额
        :return:
        """
        els=driver.find_elements_by_id("et_edit_view")
        return els

    def el_LoanSum(self, driver):
        el = driver.find_element_by_id("tv_loan_sum")
        return el


