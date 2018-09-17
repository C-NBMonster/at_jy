"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_NewOrder.py
@time: 2018/9/7 17:23
@desc: 即有宝新增订单业务逻辑代码
"""
from elements.el_JYT.el_NewOrder_1 import C_el_NewOrder_1
from elements.el_JYT.el_NewOrder_2 import C_el_NewOrder_2
from elements.el_JYT.el_NewOrder_3 import C_el_NewOrder_3
from elements.el_JYT.el_NewOrder_4 import C_el_NewOrder_4
from elements.el_JYT.el_NewOrder_5 import C_el_NewOrder_5
from elements.el_JYT.el_NewOrder_6 import C_el_NewOrder_6
from elements.el_JYT.el_NewOrder_7 import C_el_NewOrder_7
from elements.el_JYT.el_NewOrder_8 import C_el_NewOrder_8
from elements.el_JYT.el_NewOrder_9 import C_el_NewOrder_9
from elements.el_JYT.el_NewOrder_10 import C_el_NewOrder_10
from common.rewrite import C_selenium_rewrite
from common.conn_oracle import C_oracle
import unittest
import time
import threading
import cx_Oracle
from selenium.webdriver.common.touch_actions import TouchActions
class C_B_NewOrder(unittest.TestCase):

    def setUp(self):
        self.Cel_NewOrder_1 = C_el_NewOrder_1()  #实例化
        self.Cel_NewOrder_2 = C_el_NewOrder_2()
        self.Cel_NewOrder_3 = C_el_NewOrder_3()
        self.Cel_NewOrder_4 = C_el_NewOrder_4()
        self.Cel_NewOrder_5 = C_el_NewOrder_5()
        self.Cel_NewOrder_6 = C_el_NewOrder_6()
        self.Cel_NewOrder_7 = C_el_NewOrder_7()
        self.Cel_NewOrder_8 = C_el_NewOrder_8()
        self.Cel_NewOrder_9 = C_el_NewOrder_9()
        self.Cel_NewOrder_10 = C_el_NewOrder_10()
        self.C_sel_Rewrite  = C_selenium_rewrite()
        self.C_ORCLE = C_oracle()
        #self.TouchAct = TouchActions(driver)
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
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 1)  #点击商品门店

    def b_Common_Choose(self, driver, tName, strName):
        #弹窗选择内容公共函数
        #四个类型的弹窗，放在一个list里面，减少形参
        if self.Cel_NewOrder_1.el_NewOrder_Common_PopUp_Title(driver).getText().strip() == tName:
            self.Cel_NewOrder_1.el_NewOrder_Common_PopUp_List(driver, strName).click()
        else:
            print("不是选择 %s 弹窗" % strName)

    def b_Chose_GoodsType_Click(self, driver):
        """
        点击商品类型 弹窗
        :param driver:
        :param GoodsType: 商品类型
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 2)  # 点击商品类型

    def b_Choose_ProductVerson_Click(self, driver):
        """
        选择产品版本
        :param driver:
        :param ProductVerson: 产品版本
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 3)  # 点击产品版本
        # 这里还没写选择产品版本代码

    def b_Choose_ProductType_Click(self, driver):
        """
        选择产品类型
        :param driver:
        :param ProductType: 产品类型
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 4)  # 点击产品类型
        # 这里还没写选择产品类型代码

    def b_Fill_GoodsTotel(self, driver, GoodsTotel):
        """
        填写商品总额
        :param driver:
        :param GoodsTotel: 商品总额
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 1).clear()
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 1).send_keys(GoodsTotel)

    def b_Fill_Downpayment(self, driver, Downpayment):
        """
        填写首付金额
        :param driver:
        :param Downpayment: 首付金额
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 2).clear()
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 2).send_keys(Downpayment)


    # -------------------------------------------------------------
    """业务组合"""
    # -------------------------------------------------------------
    def b_NewOrder_1(self, driver, goodsTotel, downpayment):
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
        self.Cel_NewOrder_1.el_NewOrder_submit_1(driver).click()

    def b_Check_LoanSum(self, driver, goodsTotel, downpayment):
        """
        验证贷款金额是否正确
        :param driver:
        :param goodsTotel: 商品总价
        :param downpayment:首付金额
        :return:
        """
        loanSum = int((self.Cel_NewOrder_1.el_NewOrder1_LoanSum(driver)).strip())
        tt = int(goodsTotel) - int(downpayment)
        if tt == loanSum:
            return True
        else:
            self.assertEquals(int(goodsTotel) - int(downpayment), loanSum, u"errorInfo:贷款金额计算不正确")
            return False

    #--------------------------------------------------
    #新建订单第二个页面--------------------------------
    def b_NewOrder_2_Check_LoanSum(self, driver, loanSum):
        """检查贷款金额是否正确"""
        sText = self.Cel_NewOrder_2.el_NewOrder2_LoanSum(driver).getText().strip()
        if sText != loanSum:
            self.assertEquals(sText, loanSum, u"新建订单第二个页面，贷款金额显示错误，请检查!")
        else:
            #添加日志信息
            print(u"贷款信息显示正确！")

    def b_NewOrder_2_No_TreasureFee(self, driver):
        """不参加免还大礼包"""
        #通过坐标来移动元素。不同分辨率，则会出现bug，以后再想办法
        driver.flick(1040, 322, 934, 322)

    def b_NewOrder_2_ChooseInstalment(self, driver, instalment):
        """选择分期"""
        instal = self.Cel_NewOrder_2.el_NewOrder2_InstalmentItem(driver, instalment)
        l_instals = []
        for el in instal:
            l_instals.append(el.getText().strip())
        index = 0
        if len(l_instals) == 0:
            #这里仅记录日志信息
            print("查询条件：%s - %s - %s - %s : 没有搜索到商品分期，请检查所选门店及商品类型，产品版本等是否正确" % self.shopName, self.goodType, self.productVersion, self.productType)
            return
        else:
            for str in l_instals:
                if str == instalment:
                    index = l_instals.index(str)
            self.Cel_NewOrder_2.el_NewOrder2_InstalmentList(driver)[index].click()

    def b_NewOrder_2_Submit(self, driver):
        """点击下一步"""
        self.Cel_NewOrder_2.el_NewOrder2_Submit(driver).click()

    #-----------------------------------------------------------------------------
    #新建订单第三步
    #-----------------------------------------------------------------------------
    def b_NewOrder_3_Choose_SubCategory(self, driver, subCategory):
        """选择商品小类"""
        self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver)[0].click()
        if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"选择商品小类":
            els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
            for el  in els:
                if el.getText().strip() == subCategory:
                    el.click()
                else:
                    return

    def b_NewOrder_3_Check_SubCategory(self, driver, subCategory):
        """验证是否成功选择商品小类"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 0).getText().strip()
        if subText == subCategory:
            print("成功选择商品小类")
        else:
            print("选择商品小类失败，请检查")

    def b_NewOrder_3_Choose_Brand(self, driver, brand):
        """选择商品品牌"""
        self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 1).click()
        if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"选择商品品牌":
            els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
            for el  in els:
                if el.getText().strip() == brand:
                    el.click()
                else:
                    return

    def b_NewOrder_3_Check_brand(self, driver, brand):
        """验证是否成功选择商品品牌"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 1).getText().strip()
        if subText == brand:
            print("成功选择商品品牌")
        else:
            print("选择商品品牌失败，请检查")

    def b_NewOrder_3_Choose_SKU(self, driver, sku):
        """
        选择商品型号。PS：有时是下拉框形式，有时是输入框形式。注意！！！
        :param driver:
        :param sku:
        :return:
        """
        #如果是输入框
        br = self.Cel_NewOrder_3.el_NewOrder3_Edit_GP_DP(driver,2).is_Displayed()
        bh = self.Cel_NewOrder_3.el_NewOrder3_Edit_GP_DP(driver,2)
        if br == True:
            self.C_sel_Rewrite.send_keys(bh, sku)
        else:
            #下拉框形式
            self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 2).click()
            if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"选择商品型号":
                els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
                for el in els:
                    if el.getText().strip() == sku:
                        el.click()
                    else:
                        return

    def b_NewOrder_3_Check_SKU(self, driver, sku):
        """验证是否成功选择商品型号"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 2).getText().strip()
        if subText == sku:
            print("成功选择商品型号")
        else:
            print("选择商品型号失败，请检查")

    #----------------------------------------------------------------------------------
    #新增订单第四步：填写客户信息

    def b_NewOrder_4_Upload_IDFront(self, driver):
        """上传身份证正面"""
        #拍照
        self.Cel_NewOrder_4.el_NewOrder4_IDCard_Front(driver).click()
        act_Camera = "com.giveu.corder.ordercreate.activity.CameraActivity"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_4.el_NewOrder4_Camera_Shot(driver).click()
        #验证代码missed

    def b_NewOrder_4_cName(self, driver, cName):
        # 填写用户姓名
        hName = self.Cel_NewOrder_4.el_NewOrder4_ID_Name(driver)
        self.C_sel_Rewrite.send_keys(hName, cName)

    def b_NewOrder_4_IDNo(self, driver, idNo):
        #身份证号
        hIDNo = self.Cel_NewOrder_4.el_NewOrder4_ID_No(driver)
        self.C_sel_Rewrite.send_keys(hIDNo, idNo)

    def b_NewOrder_4_parentAddr(self, driver, l_addr):
        """
        选择省市区,
        :param driver:
        :param l_addr: 省市区列表
        :return:
        """
        self.Cel_NewOrder_4.el_NewOrder4_Address_Click(driver).click()
        hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
        for addr in hAddrs:
            #选择省
            if addr.getText().strip() == l_addr[0]:
                addr.click()
                #选择市
                hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
                for addr in hAddrs:
                    # 选择省
                    if addr.getText().strip() == l_addr[1]:
                        addr.click()
                        #选择区县
                        hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
                        for addr in hAddrs:
                            # 选择省
                            if addr.getText().strip() == l_addr[2]:
                                addr.click()

    def b_NewOrder_4_AddressDetail(self, driver, addrDetail):
        #填写详细地址
        hAddr = self.Cel_NewOrder_4.el_NewOrder4_ID_Address(driver)
        self.C_sel_Rewrite.send_keys(hAddr, addrDetail)

    #身份证背面信息---------------------------------------
    def b_NewOrder_4_IDCard_Back(self, driver):
        #拍照身份证背面
        self.Cel_NewOrder_4.el_NewOrder4_IDCard_Back(driver).click()
        act_Camera = "com.giveu.corder.ordercreate.activity.CameraActivity"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_4.el_NewOrder4_Camera_Shot(driver).click()

    def  b_NewOrder_4_startDate(self, driver, startDate):
        #开始日期：2011/11/11
        hDate = self.Cel_NewOrder_4.el_NewOrder4_ID_DateStart(driver)
        self.C_sel_Rewrite.send_keys(hDate, startDate)

    def b_NewOrder_4_EndDate(self, driver, endDate):
        # 结束日期：2016/11/11
        hDate = self.Cel_NewOrder_4.el_NewOrder4_ID_DateEnd(driver)
        self.C_sel_Rewrite.send_keys(hDate, endDate)

    def b_NewOrder_4_Phone(self, driver, phone):
        hPhone = self.Cel_NewOrder_4.el_NewOrder4_Phone(driver)
        self.C_sel_Rewrite.send_keys(hPhone, phone)

    def b_NewOrder_4_Submit(self, driver):
        """提交"""
        self.Cel_NewOrder_4.el_NewOrder4_Submit(driver)

    def b_NewOrder_5_Upload_GroupPhoto(self, driver):
        #上传店员合影
        self.Cel_NewOrder_5.el_NewOrder5_GroupPhoto_click(driver).click()
        act_Camera = "com.android.camera.Camera"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_5.el_NewOrder5_Camera_Shot(driver).click()
        self.Cel_NewOrder_5.el_NewOrder5_Camera_Done(driver).click()

    def b_NewOrder_5_Submit(self, driver):
        #提交
        self.Cel_NewOrder_5.el_NewOrder5_Submit(driver).click()

    def b_NewOrder_6_GetCode(self, driver):
        self.Cel_NewOrder_6.el_NewOrder6_Time(driver).click()
        #此处要操作一下数据库
        sText = self.Cel_NewOrder_6.el_NewOrder6_Phone(driver).getText().strip()
        sql = r"select CODE from  CS_SMS_AUTHORITY  where mobile=" + str(sText) + " order by update_time desc"
        code = self.C_ORCLE.oracle_Search(sql)
        if code == '':
            print("30s内每隔3s尝试再次查询")
            for i in range(10):
                global timer
                timer = threading.Timer(3,self.b_NewOrder_6_GetCode(driver))
                timer.start()
            timer.cancel()
        else:
            return code

    def b_NewOrder_6_FillCode(self, driver, code):
        #填写授权码
        loc  = self.Cel_NewOrder_6.el_NewOrder6_ETCode(driver)
        self.C_sel_Rewrite.send_keys(loc, code)

    def b_NewOrder_6_Submit(self, driver):
        #提交验证
        self.Cel_NewOrder_6.el_NewOrder6_Submit(driver).click()


    #第七步 对客户门店评价备注
    def b_NewOrder_7_Code_Click(self, driver):
        #点击弹出弹窗
        self.Cel_NewOrder_7.el_NewOrder7_Code_Click(driver).click()

    def b_NewOrder_7_Select_Code(self, driver, item):
        els = self.Cel_NewOrder_7.el_NewOrder7_PopUp(driver)
        for el in els :
            if el.getText().strip()  == item :
                el.click()
                break
            else:
                print("没有找到对应项，请检查输入是否有误")

    def b_NewOrder_7_IsMove(self, driver):
        #是否移动门店:是
        el = self.Cel_NewOrder_7.el_NewOrder7_Is_MoveShop(driver)
        driver.flick(el, 960, 324)

    def b_NewOrder_7_Remark(self, driver, remark):
        #填写备注
        h = self.Cel_NewOrder_7.el_NewOrder7_Is_MoveShop(driver)
        self.C_sel_Rewrite.send_keys(h, remark)

    def b_NewOrder_7_Submit(self, driver):
        #下一步
        self.Cel_NewOrder_7.el_NewOrder7_Submit(driver).click()


    #----------------------------------------------------------------------
    #业务组合
    # ----------------------------------------------------------------------

    def b_NewOrder_3_Add_GoodInfo(self, driver, subCategory, brand, sku):
        #填写商品信息
        self.b_NewOrder_3_Choose_SubCategory(driver, subCategory)
        self.b_NewOrder_3_Check_SubCategory(driver, subCategory)
        self.b_NewOrder_3_Choose_Brand(driver, brand)
        self.b_NewOrder_3_Check_brand(driver, brand)
        self.b_NewOrder_3_Choose_SKU(driver, sku)
        self.b_NewOrder_3_Check_SKU(driver, sku)

    def b_NewOrder_3_Submit(self, driver):
        """提交，下一步"""
        self.Cel_NewOrder_3.el_NewOrder3_Next(driver).click()

    def b_NewOrder_4_IDInfo(self, driver, cName, idNo, l_addr, addrDetail, startDate, endDate, phone):
        """填写IDInfo"""
        #正面
        self.b_NewOrder_4_Upload_IDFront(driver)
        act_CustomerInfo = "com.giveu.corder.ordercreate.activity.UploadIdCardActivity"
        driver.wait_activity(act_CustomerInfo, 20, 1)
        #姓名
        self.b_NewOrder_4_cName(driver, cName)
        #身份证号码
        self.b_NewOrder_4_IDNo(driver, idNo)
        #选择省市区
        self.b_NewOrder_4_parentAddr(driver, l_addr)
        #详细地址
        self.b_NewOrder_4_AddressDetail(driver, addrDetail)

        #背面
        self.b_NewOrder_4_IDCard_Back(driver)
        self.b_NewOrder_4_startDate(driver, startDate)
        self.b_NewOrder_4_EndDate(driver, endDate)
        self.b_NewOrder_4_Phone(driver, phone)

    def b_NewOrder_7_SelectCode(self, driver, item):
        self.b_NewOrder_7_Code_Click(driver)
        self.b_NewOrder_7_Select_Code(driver, item)

