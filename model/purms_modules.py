#! /usr/bin/env python
#coding=utf-8

from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from Pro_scripts.Modules.order_modules import COrder_Modules

class CPURMS_Modules():
    def setUp(self):
        self.COrderModules = COrder_Modules()
        (self.consignName,self.addressInfo,self.consignPhone,self.OrderNo_0,self.totalPrice) = self.COrderModules.FPalce_An_Order(self)
        self.OrderNo= self.OrderNo_0
        
    #特别说明，每个函数都有iframe的id形参，主要是因为这个id是动态变化的，
    #如pagetabiframe_0，后面的0会变化，根据打开的iframe数（即页面左侧目录功能模块）的多少来增加。
        
    def PURMS_NewPurchaseOrder(self,SKU_code,employeeCode,purchaseQuantity,unitPrice,taxRate,iframeId): 
        u"""新增采购订单"""
        #手动新增采购单
        #SKU_code:ku编码
        #employeeCode:采购员编码
        #purchaseQuantity:采购数量
        #unitPrice:单价
        #taxRate：税率
        ######################################################################
        """
        输入SKU编码会自动带出商品信息：商品名称 	SKU条形码 	计量单位 	规格型号
        所以，调用该函数前，应当首先调用获取商品信息的函数获取以上信息
        """
        ######################################################################
        driver =self.driver
        driver.switch_to.default_content()
        
        if employeeCode == "":
            employeeCode = "TZH00097"
        driver.find_element_by_link_text(u"采购系统").click()
        driver.find_element_by_name(u"采购订单").click()
        driver.switch_to.frame(iframeId)
        driver.find_element_by_link_text(u"  新增").click()
        driver.find_element_by_id("employeeName").click()
        time.sleep(2)
        driver.switch_to.frame("employee")
        driver.find_element_by_id("code").send_keys(employeeCode)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.2)
        bFlag = driver.find_element_by_xpath(".//*[@id='TreeTable']/tbody/tr/td[1]").is_displayed()
        self.assertEqual(bFlag,True,u"采购员不存在，请检查")
        hdbclick = driver.find_element_by_xpath(".//*[@id='TreeTable']/tbody/tr")
        ActionChains(driver).double_click(hdbclick).perform()
        
        driver.switch_to.default_content()
        driver.switch_to.frame(iframeId)
        #采购，发货，到货日期
        purchaseDate  = time.strftime("%Y-%m-%d")
        deliveryDate  = time.strftime("%Y-%m-%d")
        DexpectedDate = datetime.datetime.now() + datetime.timedelta(days=1)
        SexpectedDate = datetime.datetime.strftime(Dtomorrow_time, '%Y-%m-%d')
        
        js = "document.getElementById('purchaseDate').removeAttribute('readOnly')"
        driver.execute(js)
        driver.find_element_by_id("purchaseDate").send_keys(purchaseDate)
        """
        driver.find_element_by_name("deliveryDate_1").click()
        js = "document.getElementByName('deliveryDate_1').removeAttribute('readOnly')"
        driver.execute(js)
        js = "document.getElementByName('expectedDate_1').removeAttribute('readOnly')"
        driver.execute(js)
        
        driver.find_element_by_id("purchaseDate").send_keys(purchaseDate)
        driver.find_element_by_name("deliveryDate_1").send_keys(deliveryDate)
        driver.find_element_by_name("expectedDate_1").send_keys(SexpectedDate)
        """
        #填写采购商品信息
        driver.find_element_by_name("code_1").send_keys(SKU_code)
        time.sleep(0.2)
        driver.find_element_by_css_selector(".ui-menu-item").click()
        time.sleep(0.2)
        #验证商品信息
        
        driver.find_element_by_name("purchaseQuantity_1").send_keys(purchaseQuantity)
        driver.find_element_by_name("unitPrice_1").send_keys(unitPrice)
        driver.find_element_by_name("taxRate_1").send_keys(taxRate)
        #验证： 	*采购数量 	*单价（元） 	金额（元） 	*税率（%） 	税额（元） 	价税合计（元）
        driver.find_element_by_css_selector("input.btn:nth-child(1)").click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_link_text("×").click()
        

    def PURMS_PurchaseWarn(self,barcode,iframeId):  
        u"""采购预警-生成采购订单"""
        #提交预警订单，通过条形码找到关联订单
        driver = self.driver
        driver.switch_to.default_content()
        
        driver.find_element_by_link_text(u"采购系统").click()
        driver.find_element_by_name(u"采购预警").click()
        driver.switch_to.frame(iframeId)
        driver.find_element_by_id("barcode").send_keys(barcode)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.2)
        driver.find_element_by_id("checkboxAll").click()
        driver.find_element_by_link_text(u"生成采购订单").click()
        #此处只有一个成功提示，需要采购订单中确认是否成功
        purchaseTotal = driver.find_element_by_xpath("html/body/div[1]/div/div/div/div[1]/div[2]/table/tbody/tr[1]/td[19]").text
        time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_link_text("×").click()
        
        return purchaseTotal
        
    def PURMS_Submit_Review(self,OrderNo,iframeId): 
        u"""采购订单审核"""
        u"""提交和审核采购订单,返回采购订单号"""
        #目前只适用于自定义在供应商的商品
        driver = self.driver
        driver.switch_to.default_content()
        
        sShot  = "ERROR_PurchaseOrder_"+time.strftime("%Y%m%d%H%M%S")+".png"
        driver.find_element_by_link_text(u"采购系统").click()
        driver.find_element_by_name(u"采购订单").click()
        driver.switch_to.frame(iframeId)
        driver.find_element_by_id("sourceNumber").send_keys(OrderNo)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.2)
        
        PURMS_PurchaseOrderNo  = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr/td[3]").text
        PURMS_OrderStatu       = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr/td[6]").text
        #如果没提交，则先提交
        if(PURMS_OrderStatu == u'待提交'):
            driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr/td[11]/a[3]").click()
            driver.find_element_by_id("submit").click()
            time.sleep(1)
            PURMS_OrderStatu  = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr[1]/td[6]").text
            self.assertEqual(PURMS_OrderStatu,u"待审核",u"单据状态不对！")
            PURMS_OrderSource = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr[1]/td[10]").text
            self.assertEqual(PURMS_OrderSource,u"手工新增",u"订单来源不对不对！")
        else:
            PURMS_CloseStatu  = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr[1]/td[8]").text
            self.assertEqual(PURMS_CloseStatu,u"未关闭",u"关闭状态不对！")
            PURMS_OrderSource = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr[1]/td[10]").text
            self.assertEqual(PURMS_OrderSource,u"销售订单",u"订单来源不对！")
            driver.find_element_by_link_text(u"审核").click()
            driver.find_element_by_id(qualified).click()
            time.sleep(2)
            PURMS_OrderStatu  = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr[1]/td[6]").text
            self.assertEqual(PURMS_OrderStatu,u"已审核",u"单据状态不对！")
        
        #验证状态
        driver.find_element_by_id("sourceNumber").send_keys(OrderNo)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.2)
        PURMS_OrderStatu  = driver.find_element_by_xpath(".//*[@id='myAccount']/table/tbody/tr/td[6]").text
        if PURMS_OrderStatu== u"已审核":
            print(u"采购订单审核成功！")
        else:
            driver.get_screenshot_as_file("D:/Python/Screen_shots/PURMS/PurchaseOrder/"+sShot)
            self.assertEqual(PURMS_OrderStatu,u"已审核",u"采购订单审核状态不对，请检查是否审核成功")
        time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_link_text("×").click()
        
        return PURMS_PurchaseOrderNo
        
    def PURMS_PurchaseReturn_New(self,empNo,warehouseName,returnType,returnMode,vendorName,SKU_code,returnTotal,remarks,iframeId):  
        u"""手动新增采购退货单"""
        #empNo:采购员编号；warehouseName：仓库名称；
        #returnType：退货类型：2，良品退货；3，不良品退货；4，检验退货
        #returnMode：退货方式：2，退货补货；3，退货扣款
        #vendorName:供应商名称
        #SKU_code:视频ku；returnTotal:退货总数;remarks:备注
        driver = self.driver
        driver.switch_to.default_content()
        
        sShot  = "ERROR_PurchaseOrder_"+time.strftime("%Y%m%d%H%M%S")+".png"
        driver.find_element_by_link_text(u"采购系统").click()
        driver.find_element_by_name(u"采购退货单").click()
        time.sleep(2)
        driver.switch_to.frame(iframeId)
        driver.find_element_by_link_text(u"  新增").click()
        time.sleep(1)
        driver.find_element_by_id("empName").click()
        driver.find_element_by_id("code").send_keys(empNo)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.2)
        hdbclick = driver.find_element_by_xpath("//*[@id='TreeTable']/tbody/tr")
        ActionChains(driver).double_click(hdbclick).perform()
        js = "var hem = document.getElementById('refundDate').removeAttribute('readonly')"
        driver.execute(js)
        returnDate = time.strftime("%Y-%m-%d")
        driver.find_element_by_id("refundDate").send_keys(returnDate)
        driver.find_element_by_id("wareName").click()
        time.sleep(0.5)
        driver.find_element_by_id("name").send_keys(warehouseName)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.3)
        hdbclick = driver.find_element_by_xpath("//*[@id='TreeTable']/tbody/tr")
        ActionChains(driver).double_click(hdbclick).perform()
        #验证仓库地址
        driver.find_element_by_id("refundType").click()
        time.sleep(0.1)
        returnType_path = ".//*[@name = 'refundType']/optionp["+returnType+"]"
        returnMode_path = ".//*[@id = 'refundModeSelect']/optionp["+returnMode+"]"
        driver.find_element_by_xpath(returnType_path).click()
        stockType = ""
        if returnType == 2:
            stockType = u"良品"
        if returnType == 3:
            stockType = u"不良品"
        if returnType == 4:
            stockType = u"检验退货"
        time.sleep(0.2)
        driver.find_element_by_xpath(returnMode_path).click()
        time.sleep(0.2)
        driver.find_element_by_id("vendorName").click()
        time.sleep(1)
        driver.find_element_by_id("name").send_keys(vendorName)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.3)
        hdbclick = driver.find_element_by_xpath("//*[@id='TreeTable']/tbody/tr")
        ActionChains(driver).double_click(hdbclick).perform()
        #验证供应商信息
        driver.find_element_by_name("items[0].commodityCode").send_keys(SKU_code)
        driver.find_element_by_id("ui-id-6").click()
        #验证视频信息
        driver.find_element_by_name("items[0].refundBadQty").send_keys(returnTotal)
        driver.find_element_by_name("items[0].remarks").send_keys(remarks)
        #保存
        driver.find_element_by_xpath(".//*[@id='myform']/div[3]/div[7]/div/input[1]").click()
        time.sleep(0.8)
        
        purchaseRetrunNo = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[3]").text
        driver.find_element_by_id("code").send_keys(purchaseRetrunNo)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.3)
        #数据校验
        #验证两个状态
        time.sleep(2)
        returnStatu = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[7]").text
        self.assertEqual(returnStatu,u"待退货",u"采购退货状态不对")
        submitStatu = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[8]").text
        self.assertEqual(submitStatu,u"待提交",u"采购退货状态不对")
        
        #提交采购退货单
        hfather = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[13]")
        hfather.find_element_by_link_text(u"提交").click()
        time.sleep(1.5)
        driver.find_element_by_xpath(".//*[@id='myform']/div[3]/div[7]/div/input[1]").click()
        #验证两个状态
        time.sleep(2)
        driver.find_element_by_id("code").send_keys(purchaseRetrunNo)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.3)
        returnStatu = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[7]").text
        self.assertEqual(returnStatu,u"待退货",u"采购退货状态不对")
        submitStatu = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[8]").text
        self.assertEqual(submitStatu,u"待审核",u"采购退货状态不对")
        
        #提交采购退货单
        hfather = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[13]")
        hfather.find_element_by_link_text(u"审核").click()
        time.sleep(1.5)
        driver.find_element_by_xpath(".//*[@id='myform']/div[3]/div[7]/div/input[1]").click()
        #验证两个状态
        time.sleep(2)
        driver.find_element_by_id("code").send_keys(purchaseRetrunNo)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(0.3)
        returnStatu = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[7]").text
        self.assertEqual(returnStatu,u"退货中",u"采购退货状态不对")
        submitStatu = driver.find_element_by_xpath(".//*[@id='refundOrderList']/table/tbody/tr[1]/td[8]").text
        self.assertEqual(submitStatu,u"已审核",u"采购退货状态不对")

        time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_link_text("×").click()
        
        return purchaseRetrunNo,stockType
    
