"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder.py
@time: 2018/9/7 17:05
@desc: ���б��½�����ҳ��Ԫ��
"""


class C_el_NewOrder():

    def el_ChooseBaseInfo(self,driver, opt):
        """
        ѡ����Ʒ�ŵ꣬��Ʒ���ͣ���Ʒ�汾����Ʒ����
        :param driver:
        :param opt: 1����Ʒ�ŵ�:2����Ʒ���ͣ�3����Ʒ�汾��4����Ʒ����
        :return:
        """
        els = driver.find_elements_by_id("iv_right")
        els[opt].click()

    def el_MoneyTotle(self, driver, opt):
        """
        ��Ʒ�ܶ�׸��ܶ�
        :param driver:
        :param opt: 1:��Ʒ�ܶ2:�׸��ܶ�
        :return:
        """
        els=driver.find_elements_by_id("et_edit_view")
        return els

    def el_LoanSum(self, driver):
        el = driver.find_element_by_id("tv_loan_sum")
        return el


