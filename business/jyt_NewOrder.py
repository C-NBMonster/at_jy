"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: jyt_NewOrder.py
@time: 2018/9/7 17:23
@desc: 即有宝新增订单业务逻辑代码
"""
from elements.el_JYT.el_NewOrder import C_el_NewOrder
import unittest
class C_B_NewOrder(unittest.TestCase):

    Cel_NewOrder = C_el_NewOrder()  #实例化

    def b_Chose_Shop(self, Driver, shopeName):
        """
        选择门店
        :param Driver:
        :param shopeName:商品门店名称
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver,1)  #点击商品门店
        #这里还没写选择门店代码

    def b_Chose_GoodsType(self, Driver, GoodsType):
        """
        选择商品类型
        :param Driver:
        :param GoodsType: 商品类型
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver, 2)  # 点击商品类型
        # 这里还没写选择商品类型代码

    def b_Choose_ProductVerson(self, Driver, ProductVerson):
        """
        选择产品版本
        :param Driver:
        :param ProductVerson: 产品版本
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver, 3)  # 点击产品版本
        # 这里还没写选择产品版本代码

    def b_Choose_ProductType(self, Driver, ProductType):
        """
        选择产品类型
        :param Driver:
        :param ProductType: 产品类型
        :return:
        """
        C_el_NewOrder.el_ChooseBaseInfo(Driver, 4)  # 点击产品类型
        # 这里还没写选择产品类型代码

    def b_Fill_GoodsTotel(self, Driver, GoodsTotel):
        """
        填写商品总额
        :param Driver:
        :param GoodsTotel: 商品总额
        :return:
        """
        C_el_NewOrder.el_MoneyTotle(Driver, 1).clear()
        C_el_NewOrder.el_MoneyTotle(Driver, 1).send_keys(GoodsTotel)

    def b_Fill_Downpayment(self, Driver, Downpayment):
        """
        填写首付金额
        :param Driver:
        :param Downpayment: 首付金额
        :return:
        """
        C_el_NewOrder.el_MoneyTotle(Driver, 2).clear()
        C_el_NewOrder.el_MoneyTotle(Driver, 2).send_keys(Downpayment)

    def b_Fill_NewOrder_1(self, Driver, shopeName, GoodsType, ProductVerson, ProductType, GoodsTotel, Downpayment):
        """
        新建订单，第一个内容填写页面，汇总
        :return:
        """
        self.b_Chose_Shop(Driver, shopeName)
        self.b_Chose_GoodsType(Driver, GoodsType)
        self.b_Choose_ProductVerson(Driver, ProductVerson)
        self.b_Choose_ProductType(Driver, ProductType)
        self.b_Fill_GoodsTotel(Driver, GoodsTotel)
        self.b_Fill_Downpayment(Driver, Downpayment)

    def b_NewOrder_1_submit(self):
        """第一步提交"""
        pass



