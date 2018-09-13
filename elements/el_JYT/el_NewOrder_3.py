"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_3.py
@time: 2018/9/13 16:06
@desc: �½�����������ҳ��
"""


from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By


class C_el_NewOrder_3():

    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder3_GoodPrice(self, driver):
        """��Ʒ���"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_goods_sum"))
        return el

    def el_NewOrder3_DownPayment(self, driver):
        """�׸����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_down_payments"))
        return el

    def el_NewOrder3_LoanSum(self, driver):
        """������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_loan_sum"))
        return el

    def el_NewOrder3_InstalmentNum(self, driver):
        """������"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_loan_sum"))
        return el

    def el_NewOrder3_Pay_PerMonth(self, driver):
        """ÿ��Ӧ��"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_installment_price"))
        return el

    def el_NewOrder3_ProductCode(self, driver):
        """��Ʒ����"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_installment_code"))
        return el

    def el_NewOrder3_Add_GoodType(self, driver):
        """�����Ʒ���͡�PS:��Ӷ�һ����Ʒ"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_change_goods"))
        return el

    def el_NewOrder3_Edit_GoodPrice(self, driver):
        """�༭����Ʒ�۸�"""
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_change_goods"))
        return el

    def el_NewOrder3_Edit_GP_DP(self, driver, opt):
        """
        �༭��1��Ʒ�۸��2�׸����
        :param driver:
        :param opt: 0��Ʒ�۸� 1�׸���� 2��Ʒ�ͺ�
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_change_goods"))
        return els[opt]

    def el_NewOrder3_Choose_GoodsInfo_Click(self, driver, opt):
        """
        �������������1��ƷС�� 2��ƷƷ�� 3��Ʒ�ͺ�
        :param driver:
        :param opt: 1��ƷС�� 2��ƷƷ�� 3��Ʒ�ͺ�
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els[opt]

    def el_NewOrder3_Next(self, driver):
        """
        ��һ����PS:����ߵ��Ƿֶ�ʽ�����̣�������ɨ��ͻ���ά��
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_next"))
        return el

    #�����򹫹�
    def el_NewOrder3_PopUp_Common_Title(self, driver):
        """
        ����title
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_title"))
        return el

    def el_NewOrder3_PopUp_Common_Items(self, driver):
        """
        �б���
        :param driver:
        :strTypes:��Ʒ����
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_text"))
        return els

    def el_NewOrder3_PopUp_Brand_SKU(self, driver):
        """
        �б���
        :param driver:
        :strTypes:��ƷƷ�ƣ��ͺ�
        :return:
        """
        els = self.C_sel_Rewrite.find_els(driver, self.timeOut, self.el_error_prompt, (By.ID, "text1"))
        return els




