"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_NewOrder.py
@time: 2018/9/7 17:23
@desc: 即有宝新增订单业务逻辑代码
"""
from elements.el_JYT.el_NewOrder import C_el_NewOrder
import unittest
class C_B_NewOrder(unittest.TestCase):

    def __init__(self):
        self.Cel_NewOrder = C_el_NewOrder()  #实例化
        self.shopName = u"选择商品门店"
        self.goodType = u"选择商品类型"
        self.productVersion = u"选择产品版本"
        self.productType = u"选择产品类别"
        self.lName = ['42010000200 - 武汉市江夏区多多通讯器材经营部', '手机', '即享贷B', '常规']  #读取Excel数据


    def b_Choose_Shop_Click(self, driver):
        """
        点击门店，弹出弹窗
        :param driver:
        :param shopeName:商品门店名称
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 1)  #点击商品门店

    def b_Common_Choose(self, driver, tName, strName):
        #弹窗选择内容公共函数
        #四个类型的弹窗，放在一个list里面，减少形参
        if self.Cel_NewOrder.el_NewOrder_Common_PopUp_Title(driver).getText().strip() == tName:
            self.Cel_NewOrder.el_NewOrder_Common_PopUp_List(driver, strName).click()
        else:
            print("不是选择 %s 弹窗" % strName)

    def b_Chose_GoodsType_Click(self, driver):
        """
        点击商品类型 弹窗
        :param driver:
        :param GoodsType: 商品类型
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 2)  # 点击商品类型

    def b_Choose_ProductVerson_Click(self, driver):
        """
        选择产品版本
        :param driver:
        :param ProductVerson: 产品版本
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 3)  # 点击产品版本
        # 这里还没写选择产品版本代码

    def b_Choose_ProductType_Click(self, driver):
        """
        选择产品类型
        :param driver:
        :param ProductType: 产品类型
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 4)  # 点击产品类型
        # 这里还没写选择产品类型代码

    def b_Fill_GoodsTotel(self, driver, GoodsTotel):
        """
        填写商品总额
        :param driver:
        :param GoodsTotel: 商品总额
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 1).clear()
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 1).send_keys(GoodsTotel)

    def b_Fill_Downpayment(self, driver, Downpayment):
        """
        填写首付金额
        :param driver:
        :param Downpayment: 首付金额
        :return:
        """
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 2).clear()
        self.Cel_NewOrder.el_NewOrder1_MoneyTotle(driver, 2).send_keys(Downpayment)


    # -------------------------------------------------------------
    """业务组合"""
    # -------------------------------------------------------------
    def b_Fill_NewOrder_1(self, driver, goodsTotel, downpayment):
        """
        新建订单，第一个内容填写页面，汇总
        :goodsTotel:商品总价
        :downpayment:首付总额
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
        """第一步提交"""
        self.Cel_NewOrder.el_NewOrder_submit_1(driver).click()

    def b_Check_LoanSum(self, driver, goodsTotel, downpayment):
        loanSum = int((self.Cel_NewOrder.el_NewOrder1_LoanSum(driver)).strip())
        tt = int(goodsTotel) - int(downpayment)
        if tt == loanSum:
            return True
        else:
            self.assertEquals(int(goodsTotel) - int(downpayment), loanSum, u"errorInfo:贷款金额计算不正确")
            return False





