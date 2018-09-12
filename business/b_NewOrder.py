"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_NewOrder.py
@time: 2018/9/7 17:23
@desc: ���б���������ҵ���߼�����
"""
from elements.el_JYT.el_NewOrder import C_el_NewOrder
import unittest
class C_B_NewOrder(unittest.TestCase):

    def __init__(self):
        self.Cel_NewOrder = C_el_NewOrder()  #ʵ����
        self.shopName = u"ѡ����Ʒ�ŵ�"
        self.goodType = u"ѡ����Ʒ����"
        self.productVersion = u"ѡ���Ʒ�汾"
        self.productType = u"ѡ���Ʒ���"
        self.lName = ['42010000200 - �人�н��������ͨѶ���ľ�Ӫ��', '�ֻ�', '�����B', '����']  #��ȡExcel����


    def b_Choose_Shop_Click(self, driver):
        """
        ����ŵ꣬��������
        :param driver:
        :param shopeName:��Ʒ�ŵ�����
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 1)  #�����Ʒ�ŵ�

    def b_Common_Choose(self, driver, tName, strName):
        #����ѡ�����ݹ�������
        #�ĸ����͵ĵ���������һ��list���棬�����β�
        if self.Cel_NewOrder.el_NewOrder_Common_PopUp_Title(driver).getText().strip() == tName:
            self.Cel_NewOrder.el_NewOrder_Common_PopUp_List(driver, strName).click()
        else:
            print("����ѡ�� %s ����" % strName)

    def b_Chose_GoodsType_Click(self, driver):
        """
        �����Ʒ���� ����
        :param driver:
        :param GoodsType: ��Ʒ����
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 2)  # �����Ʒ����

    def b_Choose_ProductVerson_Click(self, driver):
        """
        ѡ���Ʒ�汾
        :param driver:
        :param ProductVerson: ��Ʒ�汾
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 3)  # �����Ʒ�汾
        # ���ﻹûдѡ���Ʒ�汾����

    def b_Choose_ProductType_Click(self, driver):
        """
        ѡ���Ʒ����
        :param driver:
        :param ProductType: ��Ʒ����
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 4)  # �����Ʒ����
        # ���ﻹûдѡ���Ʒ���ʹ���

    def b_Fill_GoodsTotel(self, driver, GoodsTotel):
        """
        ��д��Ʒ�ܶ�
        :param driver:
        :param GoodsTotel: ��Ʒ�ܶ�
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 1).clear()
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 1).send_keys(GoodsTotel)

    def b_Fill_Downpayment(self, driver, Downpayment):
        """
        ��д�׸����
        :param driver:
        :param Downpayment: �׸����
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 2).clear()
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 2).send_keys(Downpayment)


    # -------------------------------------------------------------
    """ҵ�����"""
    # -------------------------------------------------------------
    def b_Fill_NewOrder_1(self, driver, goodsTotel, downpayment):
        """
        �½���������һ��������дҳ�棬����
        :goodsTotel:��Ʒ�ܼ�
        :downpayment:�׸��ܶ�
        :return:
        """
        self.b_Choose_Shop_Click(driver)
        self.b_Common_Choose(driver, self.shopName, self.lName[0])
        self.b_Chose_GoodsType_Click(driver)
        self.b_Common_Choose(driver, self.goodType, self.lName[1])
        self.b_Choose_ProductVerson_Click(driver)
        self.b_Common_Choose(driver, self.productVersion, self.lName[2])
        self.b_Choose_ProductType_Click(driver)
        self.b_Common_Choose(driver, self.productType, self.lName[3])
        self.b_Fill_GoodsTotel(driver, goodsTotel)
        self.b_Fill_Downpayment(driver, downpayment)

    def b_NewOrder_1_submit(self, driver):
        """��һ���ύ"""
        self.Cel_NewOrder.el_NewOrder_submit_1(driver).click()

    def b_Check_LoanSum(self, driver, goodsTotel, downpayment):
        loanSum = int((self.Cel_NewOrder.el_NewOrder1_LoanSum(driver)).strip())
        tt = int(goodsTotel) - int(downpayment)
        if tt == loanSum:
            return True
        else:
            self.assertEquals(int(goodsTotel) - int(downpayment), loanSum, u"errorInfo:��������㲻��ȷ")
            return False





