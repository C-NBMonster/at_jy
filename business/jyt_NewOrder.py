"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: jyt_NewOrder.py
@time: 2018/9/7 17:23
@desc: ���б���������ҵ���߼�����
"""
from elements.el_JYT.el_NewOrder import C_el_NewOrder
import unittest
class C_B_NewOrder(unittest.TestCase):

    Cel_NewOrder = C_el_NewOrder()  #ʵ����

    def b_Chose_Shop(self, Driver, shopeName):
        """
        ѡ���ŵ�
        :param Driver:
        :param shopeName:��Ʒ�ŵ�����
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver,1)  #�����Ʒ�ŵ�
        #���ﻹûдѡ���ŵ����

    def b_Chose_GoodsType(self, Driver, GoodsType):
        """
        ѡ����Ʒ����
        :param Driver:
        :param GoodsType: ��Ʒ����
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver, 2)  # �����Ʒ����
        # ���ﻹûдѡ����Ʒ���ʹ���

    def b_Choose_ProductVerson(self, Driver, ProductVerson):
        """
        ѡ���Ʒ�汾
        :param Driver:
        :param ProductVerson: ��Ʒ�汾
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver, 3)  # �����Ʒ�汾
        # ���ﻹûдѡ���Ʒ�汾����

    def b_Choose_ProductType(self, Driver, ProductType):
        """
        ѡ���Ʒ����
        :param Driver:
        :param ProductType: ��Ʒ����
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver, 4)  # �����Ʒ����
        # ���ﻹûдѡ���Ʒ���ʹ���

    def b_Fill_GoodsTotel(self, Driver, GoodsTotel):
        """
        ��д��Ʒ�ܶ�
        :param Driver:
        :param GoodsTotel: ��Ʒ�ܶ�
        :return:
        """
        C_el_NewOrder.el_MoneyTotle(Driver, 1).clear()
        C_el_NewOrder.el_MoneyTotle(Driver, 1).send_keys(GoodsTotel)

    def b_Fill_Downpayment(self, Driver, Downpayment):
        """
        ��д�׸����
        :param Driver:
        :param Downpayment: �׸����
        :return:
        """
        C_el_NewOrder.el_MoneyTotle(Driver, 2).clear()
        C_el_NewOrder.el_MoneyTotle(Driver, 2).send_keys(Downpayment)

    def b_Fill_NewOrder_1(self, Driver, shopeName, GoodsType, ProductVerson, ProductType, GoodsTotel, Downpayment):
        """
        �½���������һ��������дҳ�棬����
        :return:
        """
        self.b_Chose_Shop(Driver, shopeName)
        self.b_Chose_GoodsType(Driver, GoodsType)
        self.b_Choose_ProductVerson(Driver, ProductVerson)
        self.b_Choose_ProductType(Driver, ProductType)
        self.b_Fill_GoodsTotel(Driver, GoodsTotel)
        self.b_Fill_Downpayment(Driver, Downpayment)

    def b_NewOrder_1_submit(self):
        """��һ���ύ"""
        pass



