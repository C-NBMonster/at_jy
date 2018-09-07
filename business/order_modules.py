#! /usr/bin/env python
#coding=utf-8

from selenium import webdriver
import json
import time,unittest
from Pro_scripts.Modules.MySQL import CDB_CONN
class COrder_Modules(unittest.TestCase):
    
    #特别说明，每个函数都有iframe的id形参，主要是因为这个id是动态变化的，
    #如pagetabiframe_0，后面的0会变化，根据打开的iframe数（即页面左侧目录功能模块）的多少来增加。
    null = ''
    def FPalce_An_Order(self,sysType,uid,addressId,buyType,sku_id,count): 
        u"""下单"""
        #sysTyep:1:andriod,2:ios,3:pc
        #uid:用户id,在uc库中表member的id
        #addressId：签收地址,在uc库中表member_address的id
        #buyType:购买类型普通：COMMON_BUY,预售：PRE_SALE,抢购:PANIC_BUY,新手专享：NEWUSER_VIP;批发：WHOLESALEK_MANAGER,普通活动：ORDINARY_ACTIVITY
        #sku_id:商品的sku_id，ims库中表commodity_sku的id
        #count:购买数量
        driver = webdriver.Chrome()
        driver.maximize_window()
        #driver = self.driver
        
        #设置参数的默认值
        if sysType == "":
            sysType = "1"
        if count == "":
            count = "1"
        if buyType == "":
            buyType = "COMMON_BUY"
        ip1 = "120.24.217.16:8086"
        ip2 = "app-client.ffzxnet.com"
        orderURL  ="http://"+ip2+"/app-client-web/order/toBuy.do?params={'sysType':'"+sysType+"','uid':'"+uid+"','isInvoice':'0','addressId':'"+addressId+"','goods':[{'buyType':'"+buyType+"','value':'','id':'"+sku_id+"','count':"+count+",'wholeSaleCount':0}]}"
        try:
            driver.get(orderURL)
        except Exception as e:
            print(e)
            driver.quit()
        
        OrderContent = eval(driver.find_element_by_tag_name("body").text)
        
        consignName  = OrderContent["resultData"]["consignName"]
        addressInfo  = OrderContent["resultData"]["addressInfo"]
        consignPhone = OrderContent["resultData"]["consignPhone"]
        OrderNo      = OrderContent["resultData"]["orderNumber"]
        totalPrice   = OrderContent["resultData"]["totalPrice"]
        returnMsg    = OrderContent["resultMsg"] 
        returnStatu  = OrderContent["resultStatus"]
        
        if returnMsg == "OK" and returnStatu == 100:
            print(u"下单成功")
        else:
            print(u"下单失败")
            driver.close()
        driver.quit()
        return consignName,addressInfo,consignPhone,OrderNo,totalPrice
        
    def Init_PayInfo(self,orderNo,payType):
        global null
        driver = webdriver.Chrome()
        if payType == '':
            payType = "alipay"
        InterURL   = "http://app-client.ffzxnet.com/app-client-web/order/toPay.do?params={orderNumber:'"+str(orderNo)+"',payType:'"+payType+"',value:''}"
        InitContent = ''
        try:
            driver.get(InterURL)
            time.sleep(1)
            #InitContent  = eval(driver.find_element_by_tag_name("body").text)
            InitContent  = str((driver.find_element_by_tag_name("body").text).encode("utf-8"))
        except Exception as e:
            print(e)
        
        successFlag = '"resultMsg":"OK","resultStatus":100'   
        if (successFlag in InitContent) == True:
            print(u"初始化支付信息成功！")
            #driver.close()
        else:
            print(u"初始化支付信息失败，请查看信息")
            #print(InitContent)
            driver.close()
        driver.quit()
       
        
    def OrderPay(self,orderNo):
        global null
        driver = webdriver.Chrome()
        InterURL = "http://order.ffzxnet.com/order-web/webhooks/mtNotify.do?mtNotifyType=PAY&orderNo="+str(orderNo)
        PayedContent = ''
        try:
            
            driver.get(InterURL)
            time.sleep(0.5)
            #PayedContent = str((driver.find_element_by_tag_name("body").text).encode("utf-8"))
            PayedContent = eval(driver.find_element_by_tag_name("body").text)
        except Exception as e:
            print(e)
        
        successFlag = '"resultMsg":"OK","resultStatus":100'
        
        operMsg      = PayedContent["MSG"]
        payStatu     = PayedContent["STATUS"]
        if payStatu == "SUCCESS" and operMsg == u"操作成功" :
            print(u"支付成功！")
            #print(PayedContent) 
        else:
            print(u"支付失败，请查看信息")
            driver.close()
        print(u"下单结束")
        driver.quit()
        
    def Order_search_Stock(self,barcode,iframeId):  
        u"""库存查询"""
        #订单系统-购买管理-库存管理：库存查询
        driver = self.driver
        driver.switch_to.default_content()
        
        driver.find_element_by_link_text(u"订单系统").click()
        time.sleep(0.5)
        driver.find_element_by_link_text(u"购买管理").click()
        time.sleep(0.5)
        driver.find_element_by_name(u"库存管理").click()
        time.sleep(1)
        driver.switch_to.frame(iframeId)
        driver.find_element_by_id("barCode").send_keys(barcode)
        driver.find_element_by_id("find-page-orderby-button").click()
        time.sleep(1)
        try:
            if driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr").is_displayed() == True:
                print("查询有结果！")
            else:
                print("查询结果为空！")
        except e:
            print(e)
            driver.close()
                
        Skus       = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[5]").text
        WStock     = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[10]").text
        StockTotal = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[11]").text
        Occupied   = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[12]").text
        CanBuyNum  = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[13]").text
        if WStock == "0":
            driver.find_element_by_id("barCode").clear()
            driver.find_element_by_id("barCode").send_keys(barcode)
            driver.find_element_by_id("find-page-orderby-button").click()
            time.sleep(1)
            try:
                if driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr").is_displayed() == True:
                    print("订单库存管理查询成功！")
                else:
                    print("查询结果为空！")
            except e:
                print(e)
                driver.close()
                    
        Skus       = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[5]").text
        WStock     = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[10]").text
        StockTotal = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[11]").text
        Occupied   = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[12]").text
        CanBuyNum  = driver.find_element_by_xpath(".//*[@id='brandList']/div[2]/table/tbody/tr/td[13]").text
            
        #time.sleep(2)
        driver.switch_to.default_content()
        driver.find_element_by_link_text("×").click()
        
        return Skus,WStock,StockTotal,Occupied,CanBuyNum
            
if __name__ == '__main__':
    print ('下单开始......')
    cc = COrder_Modules()
    barcode   = 55667781
    sysType   = "1"
    buyType   = "COMMON_BUY"
    count     = "1"
    #测试环境
    #uid       = "3d97a3a87cec4e6390a635244cbd5ba2" #"5daba828e61f4c3994693f98deb010af"
    #addressId = "a43aa16b9b964c6c892d9700b77f7536" #"c7bf8b08caa8430e8971e69fa48ddeb7"
    #sku_id    = "b9d728c9a4174a74b0cb9fbe55d5e384"
    #预生产环境
    uid       = "3d97a3a87cec4e6390a635244cbd5ba2"
    addressId = "b119b5cfb0dc4302a1d3c60346bbbd32"
    sku_id    = "1480c0574c6442f6977653542e07138c"

    
    (consignName,addressInfo,consignPhone,OrderNo,totalPrice) = cc.FPalce_An_Order(sysType,uid,addressId,buyType,sku_id,count)
    print(consignName,addressInfo,consignPhone,OrderNo,totalPrice) 
    