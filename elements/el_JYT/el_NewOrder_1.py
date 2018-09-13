"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: el_NewOrder_1.py
@time: 2018/9/7 17:05
@desc: ���б��½�����ҳ��Ԫ��
"""
from common.rewrite import C_selenium_rewrite
from selenium.webdriver.common.by import By
class C_el_NewOrder_1():
    
    def __init__(self):
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.timeOut = 30
        self.el_error_prompt = "�Ҳ���ҳ��Ԫ�أ�����Ԫ���Ƿ��ѱ����أ����Ƿ�ɼ�"

    def el_NewOrder1_ChooseBaseInfo_PopUP(self, driver, opt):
        """
        �����Ʒ�ŵ꣬��Ʒ���ͣ���Ʒ�汾����Ʒ���� -->��������
        :param driver:
        :param opt: 1����Ʒ�ŵ�:2����Ʒ���ͣ�3����Ʒ�汾��4����Ʒ����
        :return:
        """
        #els = driver.find_elements_by_id("iv_right")
        els = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "iv_right"))
        els[opt].click()

    def el_NewOrder1_ChooseRight(self, driver, opt):
        """
        ���Ԫ��������ʾ�û�ѡ�������
        :param driver:
        :param opt: 1����Ʒ�ŵ�:2����Ʒ���ͣ�3����Ʒ�汾��4����Ʒ����
        :return:
        """
        els = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_choose_right"))
        return els[opt]

    def el_NewOrder1_MoneyTotle(self, driver, opt):
        """
        ��Ʒ�ܶ�׸��ܶ�
        :param driver:
        :param opt: 1:��Ʒ�ܶ2:�׸��ܶ�
        :return:
        """
        els = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "et_edit_view"))
        return els[opt]

    def el_NewOrder1_LoanSum(self, driver):
        """
        ������
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_loan_sum"))
        return el

    def el_NewOrder_submit_1(self, driver):
        """
        ��ť����һ��
        :param driver:
        :return:
        """
        el = self.C_sel_Rewrite.find_el(driver, self.timeOut, self.el_error_prompt, (By.ID, "tv_newbuild_next"))
        return el

    #����Ϊ����Ԫ�أ�PS����������ƿ��һ�£���id��һ�£����ԣ��������֣������������ɸ㶨

    def el_NewOrder_Common_PopUp_Title(self, driver):
        """
        ����title
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
                print("û���ҵ���ӦԪ�أ��������������Ƿ�����")
                break











