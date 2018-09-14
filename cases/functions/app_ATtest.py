# coding=utf-8

#from selenium import webdriver
from AT_Demo.common.logger import Logger
from common.log import Log
import unittest, time,os,sys,string
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
#my_logger = Logger(logger='BaiduTests').getlog()
from common.rewrite import C_selenium_rewrite
from business.b_login import C_B_Login
from business.b_NewOrder import C_B_NewOrder


class NewOrder_Process_Tests(unittest.TestCase):

    #adb shell dumpsys window w |findstr \/ |findstr name=     用于查看当前activity。建议用这个


    def setUp(self):
        self.log = Log("app demo test")
        self.base_url = 'http://localhost:4723/wd/hub'
        self.desired_caps = {}
        self.desired_caps['platformName']    = 'Android'
        self.desired_caps['platformVersion'] = '4.4.2'
        self.desired_caps['deviceName']  = '127.0.0.1:62001'
        #AndroidDebugBridge().call_adb('127.0.0.1:62025')  用于切换模拟器
        self.desired_caps['appPackage']  = 'com.giveu.corder'
        self.desired_caps['appActivity'] = 'com.giveu.corder.index.activity.SplashActivity'
        self.desired_caps['autoLaunch']  = 'true'
        #支持中文输入
        self.desired_caps['unicodeKeyboard'] = 'true'
        self.desired_caps['resetKeyboard'] = 'true'
        #self.desired_caps['appActivity'] = 'com.giveu.corder.index.activity.WelcomeActivity'
        #.me.activity.LoginActivity}
        #print(os.path.dirname(os.getcwd()))
        self.driver = webdriver.Remote(self.base_url, self.desired_caps)
        self.C_sel_Rewrite = C_selenium_rewrite()
        self.C_B_login = C_B_Login()
        self.C_B_newOrder = C_B_NewOrder()


    def test_jyb_login_demo(self):
        """即有宝登录测试用例"""
        #self.log.info("成功连接appium服务器")
        #ca = self.driver.current_activity()
        #print("当前activity: %s" % sys.stdout.pritn(str(ca)))
        welcome = 'com.giveu.corder.index.activity.WelcomeActivity'
        self.driver.wait_activity(welcome, 20, 1)
        print("info::switch to the welcome activity successfully!!!")

        #滑动欢迎页
        self.C_sel_Rewrite.swipLeft(self.driver, 500, 2)

        #点击进入登录页
        self.C_sel_Rewrite.find_el(self.driver, 20, (By.ID, "tv_into")).click()

        #登录
        act_login = "com.giveu.corder.me.activity.LoginActivity"
        self.driver.wait_activity(act_login,20,1)
        self.C_B_login.b_login(self.driver, 829023, 123456)

        #登录成功验证
        print("current_context:", self.driver.current_context())
        print(self.driver.contexts())

        self.C_B_login.accept_PopUp(self.driver)
        print("login,good!!!")

        #self.log.info("jyb登录成功")

    def test_NewOrder(self):
        """
        新建订单
        :return:
        """
        #新建订单，填写第一页内容
        goodsTotel  = 6000 #从Excel取值
        downPayment = 3000 #从Excel取值
        loanSum     = goodsTotel - downPayment
        instalment  = 12
        cName = "陈真真"
        idNo  = "370126199604209539"
        l_addr= ['广东','深圳', '福田区']
        addrDetail = "华富街道福中一路华润万家"
        startDate  = "2012/09/09"
        endDate    = "2020/09/09"
        phone      = "13410342899"
        self.C_B_newOrder.b_NewOrder_1(self.driver, goodsTotel, downPayment)

        #验证贷款金额是否正确.判断：返回True则是正确的,返回False则整个用例失败
        b = self.C_B_newOrder.b_Check_LoanSum(self.driver, goodsTotel, downPayment)
        if b != True:
            self.assertEquals(b, True, u"贷款金额计算不正常")

        #点击下一步
        self.C_B_newOrder.b_NewOrder_1_submit(self.driver)

        #新建订单第二步
        orderActivity = "com.giveu.corder.ordercreate.activity.InstallmentOrderActivity"
        self.driver.wait_activity(orderActivity, 20, 1)

        #先验证贷款信息是否显示正确，这信息重要，check一下
        self.C_B_newOrder.b_NewOrder_2_Check_LoanSum(self.driver, loanSum)

        #不参加免还大礼包
        #self.C_B_newOrder.b_NewOrder_2_No_TreasureFee(self.driver)

        #选择分期
        self.C_B_newOrder.b_NewOrder_2_ChooseInstalment(self.driver, instalment)

        #提交：点击下一步
        self.C_B_newOrder.b_NewOrder_2_Submit(self.driver)


        #新建订单第三步：
        act_AddGood = "com.giveu.corder.ordercreate.activity.AddGoodsActivity"
        self.driver.wait_activity(act_AddGood, 20, 1)

        #填写商品信息
        subCategory = '苹果手机(iPhone)'
        brand = '苹果'
        sku   = '8(256G)'
        self.C_B_newOrder.b_NewOrder_3_Add_GoodInfo(self.driver, subCategory, brand, sku)

        #提交，下一步
        self.C_B_newOrder.b_NewOrder_3_Submit(self.driver)

        #新建订单第四步：填写客户信息
        act_CustomerInfo = "com.giveu.corder.ordercreate.activity.UploadIdCardActivity"
        self.driver.wait_activity(act_CustomerInfo, 20, 1)
        self.C_B_newOrder.b_NewOrder_4_IDInfo(self.driver, cName, idNo, l_addr,
                                              addrDetail, startDate, endDate, phone)

        #第四步提交
        self.C_B_newOrder.b_NewOrder_4_Submit(self.driver)

        #第五步，上传店员合影
        act_CS = "com.giveu.corder.ordercreate.activity.CustomerStorePhotoActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        #上传店员合照
        self.C_B_newOrder.b_NewOrder_5_Upload_GroupPhoto(self.driver)

        #提交
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder_5_Submit(self.driver)







    def tearDown(self):
        #self.log.info("关闭并退出app。")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
