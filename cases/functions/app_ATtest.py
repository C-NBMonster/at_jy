# coding=utf-8

#from selenium import webdriver
from AT_Demo.common.logger import Logger
from common.log import Log
import unittest, time,os,sys,string
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
#my_logger = Logger(logger='NewOrder_Process_Tests').getlog()
from common.rewrite import C_selenium_rewrite
from business.b_login import C_B_Login
from business.b_NewOrder import C_B_NewOrder


class NewOrder_Process_Tests(unittest.TestCase):

    #adb shell dumpsys window w |findstr \/ |findstr name=     用于查看当前activity。建议用这个


    def setUp(self):
        self.log = Log("jyb automation test")
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
        self.driver.wait_activity(act_login, 20, 1)
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

        #提交
        self.C_B_newOrder.b_NewOrder_4_Submit(self.driver)

        #第五步，上传店员合影
        act_CS = "com.giveu.corder.ordercreate.activity.CustomerStorePhotoActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        #上传店员合照
        self.C_B_newOrder.b_NewOrder_5_Upload_GroupPhoto(self.driver)

        #提交
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder_5_Submit(self.driver)


        #第六步 获取短信授权码
        act_CS = "com.giveu.corder.ordercreate.activity.MessageAuthorizeActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        #获取短信授权码
        code = self.C_B_newOrder.b_NewOrder_6_GetCode(self.driver)
        #输入验证码
        self.C_B_newOrder.b_NewOrder_6_FillCode(self.driver, code)
        #提交验证
        self.C_B_newOrder.b_NewOrder_6_Submit(self.driver)

        #第七步 其它信息 ，对门店和客户的评定，备注
        act_CS = "com.giveu.corder.ordercreate.activity.OtherInfoActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        item = 1
        self.C_B_newOrder.b_NewOrder_7_SelectCode(self.driver, item)
        #是否移动门店:是
        self.C_B_newOrder.b_NewOrder_7_IsMove(self.driver)
        #备注
        self.C_B_newOrder.b_NewOrder_7_Remark(self.driver, remark="123")
        self.C_B_newOrder.b_NewOrder_7_Submit(self.driver)

        #第八步 填写个人基本信息
        act_CS = "com.giveu.corder.ordercreate.activity.InfoEditActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        address = addrDetail
        education = '博士'
        pIncome = '2000'
        expenditure = '800'
        fIncome = '10000'
        qq = '1008611'
        email = 'chen_jz06@126.com'
        marriage = '未婚'
        cNumber  = 3
        self.C_B_newOrder.b_NewOrder_8_Person_BaseInfo(self.driver, l_addr, address, education, pIncome,
                                     expenditure, fIncome, qq, email, marriage, cNumber)

        self.C_B_newOrder.b_NewOrder_8_Submit(self.driver)

        #第九步 单位信息
        act_CS = "com.giveu.corder.ordercreate.activity.CompanyEditActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        sync = "否"
        l_addr = ["广东", "深圳", "福田区"]
        comName = "即有分期"
        comPhone = "13410342891"
        eNumber= "9527"
        iGategory = "军队"
        cProperties = "私企"
        position = "军人"
        etYear = 2016
        etMonth = 12
        wYear = "3年"
        self.C_B_newOrder. b_NewOrder_9_CompanyInfo(self.driver, sync, l_addr, address, comName, comPhone, eNumber,
                                 iGategory, cProperties, position, etYear, etMonth, wYear)
        self.C_B_newOrder.b_NewOrder9_Submit(self.driver)

        #第十步 填写联系人信息
        act_CS = "com.giveu.corder.ordercreate.activity.ContactsEditActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        fContactName = "李大霄"
        fContactPhone = "13410342899"
        fRelationship = "父亲"
        # 家庭联系人信息
        self.C_B_newOrder.b_NewOrder10_Family_ContactName(self.driver, fContactName)
        self.C_B_newOrder.b_NewOrder10_Family_ContactPhone(fContactPhone)
        self.C_B_newOrder.b_NewOrder10_Family_Relationship(self.driver, fRelationship)

        # 其它联系人信息
        oContactName = "黑锅侠"
        oContactPhone = "13410342655"
        oRelationship = "同事-1"
        self.C_B_newOrder.b_NewOrder10_Other_ContactName(self.driver, oContactName)
        self.C_B_newOrder.b_NewOrder10_Other_ContactPhone(oContactPhone)
        self.C_B_newOrder.b_NewOrder10_Other_Relationship(self.driver, oRelationship)

        self.C_B_newOrder.b_NewOrder10_Submit(self.driver)

        #第十一步：绑定银行卡-输入银行卡
        act_CS = "com.giveu.corder.ordercreate.activity.BindingCardActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        bankNo = "6228480136254109277"
        self.C_B_newOrder.b_NewOrder11_Input_BankCardNo(self.driver, bankNo)
        self.C_B_newOrder.b_NewOrder11_Submit(self.driver)

        #第十二步：验证银行卡四要素
        act_CS = "com.giveu.corder.ordercreate.activity.BankCardInfoActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        owner = "吐舌头"
        bankName = "中国农业银行"
        province = "广东"
        city = "深圳"
        #county = "深圳"
        bPhone = "13464631546"
        tdata = (owner, bPhone)
        self.C_B_newOrder.b_NewOrder12_Check_BankInfo(self.driver, owner, bankNo, bankName)
        self.C_B_newOrder.b_NewOrder12_Select_BankAddress(self.driver, province, city)
        self.C_B_newOrder.b_NewOrder12_Input_Phone(self.driver, bPhone)
        self.C_B_newOrder.b_NewOrder12_Submit(self.driver, tdata)

        #第十三步：绑定银行卡， 短信验证
        bankAddress = province + city
        act_CS = "com.giveu.corder.ordercreate.activity.BankCardSecondActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder13_Check_BankInfo(self.driver, owner, bankNo, bankName, bankAddress, bPhone)
        code = self.C_B_newOrder.b_NewOrder13_GetCode(self.driver, bPhone)
        self.C_B_newOrder.b_NewOrder13_FillCode(self.driver, code)
        self.C_B_newOrder.b_NewOrder13_Submit(self.driver)

        #第十四步：其它信息，评定
        act_CS = "com.giveu.corder.ordercreate.activity.OtherInfoActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        code = 2
        isMove = '1'
        remark = "automation test info"
        self.C_B_newOrder.b_NewOrder_14_OtherInfo(self.driver, code, isMove, remark)

        #第十五步：京东授权 --跳过
        act_CS = "com.giveu.corder.ordercreate.activity.JingDongAuthorizeActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder15_JD_Authority(self.driver, Auth=0)

        # 第十六步：富数授权 --跳过
        act_CS = "com.giveu.corder.ordercreate.activity.FushuAuthorizeActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder16_FD_Authority(self.driver, Auth=0)

        # 第十七步：运营商授权 --跳过
        act_CS = "com.giveu.corder.ordercreate.activity.OperatorLicenseAuthorizeActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder17_Operator_Authority(self.driver, Auth=0)

        # 第十八步：小问卷
        act_CS = "com.giveu.corder.index.activity.QuestionnaireActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        #小问卷第一页
        self.C_B_newOrder.b_NewOrder18_Questionnaire(self.driver, time=2, choice=0)

        #第十九步 影像证明
        act_CS = "com.giveu.corder.ordercreate.activity.PhotoCertificateActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder19_ImageProof_BankIMG(self.driver)
        password = "123456"
        self.C_B_newOrder.b_NewOrder19_Submit(self.driver, password)


        #第二十步：成功页校验
        #目前校验文字，后续考虑图片校验
        act_CS = "com.giveu.corder.ordercreate.activity.SuccessActivity"
        self.driver.wait_activity(act_CS, 20, 1)
        self.C_B_newOrder.b_NewOrder20_Success_Check(self.driver)

    def tearDown(self):
        #self.log.info("关闭并退出app。")
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

