"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_NewOrder.py
@time: 2018/9/7 17:23
@desc: ���б���������ҵ���߼�����
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
        self.Cel_NewOrder_1 = C_el_NewOrder_1()  #ʵ����
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
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 1)  #�����Ʒ�ŵ�

    def b_Common_Choose(self, driver, tName, strName):
        #����ѡ�����ݹ�������
        #�ĸ����͵ĵ���������һ��list���棬�����β�
        if self.Cel_NewOrder_1.el_NewOrder_Common_PopUp_Title(driver).getText().strip() == tName:
            self.Cel_NewOrder_1.el_NewOrder_Common_PopUp_List(driver, strName).click()
        else:
            print("����ѡ�� %s ����" % strName)

    def b_Chose_GoodsType_Click(self, driver):
        """
        �����Ʒ���� ����
        :param driver:
        :param GoodsType: ��Ʒ����
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 2)  # �����Ʒ����

    def b_Choose_ProductVerson_Click(self, driver):
        """
        ѡ���Ʒ�汾
        :param driver:
        :param ProductVerson: ��Ʒ�汾
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 3)  # �����Ʒ�汾
        # ���ﻹûдѡ���Ʒ�汾����

    def b_Choose_ProductType_Click(self, driver):
        """
        ѡ���Ʒ����
        :param driver:
        :param ProductType: ��Ʒ����
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_ChooseBaseInfo_PopUP(driver, 4)  # �����Ʒ����
        # ���ﻹûдѡ���Ʒ���ʹ���

    def b_Fill_GoodsTotel(self, driver, GoodsTotel):
        """
        ��д��Ʒ�ܶ�
        :param driver:
        :param GoodsTotel: ��Ʒ�ܶ�
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 1).clear()
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 1).send_keys(GoodsTotel)

    def b_Fill_Downpayment(self, driver, Downpayment):
        """
        ��д�׸����
        :param driver:
        :param Downpayment: �׸����
        :return:
        """
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 2).clear()
        self.Cel_NewOrder_1.el_NewOrder1_MoneyTotle(driver, 2).send_keys(Downpayment)


    # -------------------------------------------------------------
    """ҵ�����"""
    # -------------------------------------------------------------
    def b_NewOrder_1(self, driver, goodsTotel, downpayment):
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
        self.Cel_NewOrder_1.el_NewOrder_submit_1(driver).click()

    def b_Check_LoanSum(self, driver, goodsTotel, downpayment):
        """
        ��֤�������Ƿ���ȷ
        :param driver:
        :param goodsTotel: ��Ʒ�ܼ�
        :param downpayment:�׸����
        :return:
        """
        loanSum = int((self.Cel_NewOrder_1.el_NewOrder1_LoanSum(driver)).strip())
        tt = int(goodsTotel) - int(downpayment)
        if tt == loanSum:
            return True
        else:
            self.assertEquals(int(goodsTotel) - int(downpayment), loanSum, u"errorInfo:��������㲻��ȷ")
            return False

    #--------------------------------------------------
    #�½������ڶ���ҳ��--------------------------------
    def b_NewOrder_2_Check_LoanSum(self, driver, loanSum):
        """���������Ƿ���ȷ"""
        sText = self.Cel_NewOrder_2.el_NewOrder2_LoanSum(driver).getText().strip()
        if sText != loanSum:
            self.assertEquals(sText, loanSum, u"�½������ڶ���ҳ�棬��������ʾ��������!")
        else:
            #�����־��Ϣ
            print(u"������Ϣ��ʾ��ȷ��")

    def b_NewOrder_2_No_TreasureFee(self, driver):
        """���μ��⻹�����"""
        #ͨ���������ƶ�Ԫ�ء���ͬ�ֱ��ʣ�������bug���Ժ�����취
        driver.flick(1040, 322, 934, 322)

    def b_NewOrder_2_ChooseInstalment(self, driver, instalment):
        """ѡ�����"""
        instal = self.Cel_NewOrder_2.el_NewOrder2_InstalmentItem(driver, instalment)
        l_instals = []
        for el in instal:
            l_instals.append(el.getText().strip())
        index = 0
        if len(l_instals) == 0:
            #�������¼��־��Ϣ
            print("��ѯ������%s - %s - %s - %s : û����������Ʒ���ڣ�������ѡ�ŵ꼰��Ʒ���ͣ���Ʒ�汾���Ƿ���ȷ" % self.shopName, self.goodType, self.productVersion, self.productType)
            return
        else:
            for str in l_instals:
                if str == instalment:
                    index = l_instals.index(str)
            self.Cel_NewOrder_2.el_NewOrder2_InstalmentList(driver)[index].click()

    def b_NewOrder_2_Submit(self, driver):
        """�����һ��"""
        self.Cel_NewOrder_2.el_NewOrder2_Submit(driver).click()

    #-----------------------------------------------------------------------------
    #�½�����������
    #-----------------------------------------------------------------------------
    def b_NewOrder_3_Choose_SubCategory(self, driver, subCategory):
        """ѡ����ƷС��"""
        self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver)[0].click()
        if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"ѡ����ƷС��":
            els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
            for el  in els:
                if el.getText().strip() == subCategory:
                    el.click()
                else:
                    return

    def b_NewOrder_3_Check_SubCategory(self, driver, subCategory):
        """��֤�Ƿ�ɹ�ѡ����ƷС��"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 0).getText().strip()
        if subText == subCategory:
            print("�ɹ�ѡ����ƷС��")
        else:
            print("ѡ����ƷС��ʧ�ܣ�����")

    def b_NewOrder_3_Choose_Brand(self, driver, brand):
        """ѡ����ƷƷ��"""
        self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 1).click()
        if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"ѡ����ƷƷ��":
            els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
            for el  in els:
                if el.getText().strip() == brand:
                    el.click()
                else:
                    return

    def b_NewOrder_3_Check_brand(self, driver, brand):
        """��֤�Ƿ�ɹ�ѡ����ƷƷ��"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 1).getText().strip()
        if subText == brand:
            print("�ɹ�ѡ����ƷƷ��")
        else:
            print("ѡ����ƷƷ��ʧ�ܣ�����")

    def b_NewOrder_3_Choose_SKU(self, driver, sku):
        """
        ѡ����Ʒ�ͺš�PS����ʱ����������ʽ����ʱ���������ʽ��ע�⣡����
        :param driver:
        :param sku:
        :return:
        """
        #����������
        br = self.Cel_NewOrder_3.el_NewOrder3_Edit_GP_DP(driver,2).is_Displayed()
        bh = self.Cel_NewOrder_3.el_NewOrder3_Edit_GP_DP(driver,2)
        if br == True:
            self.C_sel_Rewrite.send_keys(bh, sku)
        else:
            #��������ʽ
            self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 2).click()
            if self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Title(driver).getText().strip() == u"ѡ����Ʒ�ͺ�":
                els = self.Cel_NewOrder_3.el_NewOrder3_PopUp_Common_Items(driver)
                for el in els:
                    if el.getText().strip() == sku:
                        el.click()
                    else:
                        return

    def b_NewOrder_3_Check_SKU(self, driver, sku):
        """��֤�Ƿ�ɹ�ѡ����Ʒ�ͺ�"""
        subText = self.Cel_NewOrder_3.el_NewOrder3_Choose_GoodsInfo_Click(driver, 2).getText().strip()
        if subText == sku:
            print("�ɹ�ѡ����Ʒ�ͺ�")
        else:
            print("ѡ����Ʒ�ͺ�ʧ�ܣ�����")

    #----------------------------------------------------------------------------------
    #�����������Ĳ�����д�ͻ���Ϣ

    def b_NewOrder_4_Upload_IDFront(self, driver):
        """�ϴ����֤����"""
        #����
        self.Cel_NewOrder_4.el_NewOrder4_IDCard_Front(driver).click()
        act_Camera = "com.giveu.corder.ordercreate.activity.CameraActivity"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_4.el_NewOrder4_Camera_Shot(driver).click()
        #��֤����missed

    def b_NewOrder_4_cName(self, driver, cName):
        # ��д�û�����
        hName = self.Cel_NewOrder_4.el_NewOrder4_ID_Name(driver)
        self.C_sel_Rewrite.send_keys(hName, cName)

    def b_NewOrder_4_IDNo(self, driver, idNo):
        #���֤��
        hIDNo = self.Cel_NewOrder_4.el_NewOrder4_ID_No(driver)
        self.C_sel_Rewrite.send_keys(hIDNo, idNo)

    def b_NewOrder_4_parentAddr(self, driver, l_addr):
        """
        ѡ��ʡ����,
        :param driver:
        :param l_addr: ʡ�����б�
        :return:
        """
        self.Cel_NewOrder_4.el_NewOrder4_Address_Click(driver).click()
        hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
        for addr in hAddrs:
            #ѡ��ʡ
            if addr.getText().strip() == l_addr[0]:
                addr.click()
                #ѡ����
                hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
                for addr in hAddrs:
                    if addr.getText().strip() == l_addr[1]:
                        addr.click()
                        #ѡ������
                        hAddrs = self.Cel_NewOrder_4.el_NewOrder4_Choose_Address(driver)
                        for addr in hAddrs:
                            if addr.getText().strip() == l_addr[2]:
                                addr.click()

    def b_NewOrder_4_AddressDetail(self, driver, addrDetail):
        #��д��ϸ��ַ
        hAddr = self.Cel_NewOrder_4.el_NewOrder4_ID_Address(driver)
        self.C_sel_Rewrite.send_keys(hAddr, addrDetail)

    #���֤������Ϣ---------------------------------------
    def b_NewOrder_4_IDCard_Back(self, driver):
        #�������֤����
        self.Cel_NewOrder_4.el_NewOrder4_IDCard_Back(driver).click()
        act_Camera = "com.giveu.corder.ordercreate.activity.CameraActivity"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_4.el_NewOrder4_Camera_Shot(driver).click()

    def  b_NewOrder_4_startDate(self, driver, startDate):
        #��ʼ���ڣ�2011/11/11
        hDate = self.Cel_NewOrder_4.el_NewOrder4_ID_DateStart(driver)
        self.C_sel_Rewrite.send_keys(hDate, startDate)

    def b_NewOrder_4_EndDate(self, driver, endDate):
        # �������ڣ�2016/11/11
        hDate = self.Cel_NewOrder_4.el_NewOrder4_ID_DateEnd(driver)
        self.C_sel_Rewrite.send_keys(hDate, endDate)

    def b_NewOrder_4_Phone(self, driver, phone):
        hPhone = self.Cel_NewOrder_4.el_NewOrder4_Phone(driver)
        self.C_sel_Rewrite.send_keys(hPhone, phone)

    def b_NewOrder_4_Submit(self, driver):
        """�ύ"""
        self.Cel_NewOrder_4.el_NewOrder4_Submit(driver)

    def b_NewOrder_5_Upload_GroupPhoto(self, driver):
        #�ϴ���Ա��Ӱ
        self.Cel_NewOrder_5.el_NewOrder5_GroupPhoto_click(driver).click()
        act_Camera = "com.android.camera.Camera"
        driver.wait_activity(act_Camera, 20, 1)
        self.Cel_NewOrder_5.el_NewOrder5_Camera_Shot(driver).click()
        self.Cel_NewOrder_5.el_NewOrder5_Camera_Done(driver).click()

    def b_NewOrder_5_Submit(self, driver):
        #�ύ
        self.Cel_NewOrder_5.el_NewOrder5_Submit(driver).click()

    def b_NewOrder_6_GetCode(self, driver):
        self.Cel_NewOrder_6.el_NewOrder6_Time(driver).click()
        #�˴�Ҫ����һ�����ݿ�
        sText = self.Cel_NewOrder_6.el_NewOrder6_Phone(driver).getText().strip()
        sql = r"select CODE from  CS_SMS_AUTHORITY  where mobile=" + str(sText) + " order by update_time desc"
        code = self.C_ORCLE.oracle_Search(sql)
        if code == '':
            print("30s��ÿ��3s�����ٴβ�ѯ")
            for i in range(10):
                global timer
                timer = threading.Timer(3,self.b_NewOrder_6_GetCode(driver))
                timer.start()
            timer.cancel()
        else:
            return code

    def b_NewOrder_6_FillCode(self, driver, code):
        #��д��Ȩ��
        loc  = self.Cel_NewOrder_6.el_NewOrder6_ETCode(driver)
        self.C_sel_Rewrite.send_keys(loc, code)

    def b_NewOrder_6_Submit(self, driver):
        #�ύ��֤
        self.Cel_NewOrder_6.el_NewOrder6_Submit(driver).click()


    #���߲� �Կͻ��ŵ����۱�ע
    def b_NewOrder_7_Code_Click(self, driver):
        #�����������
        self.Cel_NewOrder_7.el_NewOrder7_Code_Click(driver).click()

    def b_NewOrder_7_Select_Code(self, driver, item):
        els = self.Cel_NewOrder_7.el_NewOrder7_PopUp(driver)
        for el in els :
            if el.getText().strip()  == item :
                el.click()
                break
            else:
                print("û���ҵ���Ӧ����������Ƿ�����")

    def b_NewOrder_7_IsMove(self, driver):
        #�Ƿ��ƶ��ŵ�:��
        el = self.Cel_NewOrder_7.el_NewOrder7_Is_MoveShop(driver)
        driver.flick(el, 960, 324)

    def b_NewOrder_7_Remark(self, driver, remark):
        #��д��ע
        h = self.Cel_NewOrder_7.el_NewOrder7_Is_MoveShop(driver)
        self.C_sel_Rewrite.send_keys(h, remark)

    def b_NewOrder_7_Submit(self, driver):
        #��һ��
        self.Cel_NewOrder_7.el_NewOrder7_Submit(driver).click()


    #�ڰ˲�����д������Ϣ--------------------------------------------------
    def b_NewOrder_8_County(self, driver, l_addr):
        #ѡ����
        self.Cel_NewOrder_8.el_NewOrder8_Common_PopUp_Click(driver)[0].click()
        hAddrs = self.Cel_NewOrder_8.el_NewOrder8_Choose_Address(driver)
        for addr in hAddrs:
            # ѡ��ʡ
            if addr.getText().strip() == l_addr[0]:
                addr.click()
                # ѡ����
                hAddrs = self.Cel_NewOrder_8.el_NewOrder8_Choose_Address(driver)
                for addr in hAddrs:
                    if addr.getText().strip() == l_addr[1]:
                        addr.click()
                        # ѡ������
                        hAddrs = self.Cel_NewOrder_8.el_NewOrder8_Choose_Address(driver)
                        for addr in hAddrs:
                            if addr.getText().strip() == l_addr[2]:
                                addr.click()

    def b_NewOrder_8_AddressDetail(self, driver, address):
        #��ϸ��ַ
        global hEls
        hEls = self.Cel_NewOrder_8.el_NewOrder8_Common_Input(driver)
        h0 = hEls[0]
        self.C_sel_Rewrite.send_keys(h0, address)

    def b_NewOrder_8_Education(self, driver, educaiton):
        #ѡ������̶�
        self.Cel_NewOrder_8.el_NewOrder8_Common_PopUp_Click(driver)[1].click()
        title = self.Cel_NewOrder_8.el_NewOrder8_EduMar_Title(driver).getText().strip()
        els   = self.Cel_NewOrder_8.el_NewOrder8_EduMar_Items(driver)
        if title == u"ѡ������̶�":
            for el in els:
                if el.getText().strip() == educaiton:
                    el.click()
                    break
                else:
                    print("û���ҵ���Ӧѧ������鿴�����Ƿ���ȷ")
        else:
            print("�ⲻ��ѡ��ѧ���ĵ���")


    def b_NewOrder_8_personIncome(self, pIncome):
        #����������
        self.C_sel_Rewrite.send_keys(hEls[1], pIncome)

    def b_NewOrder_8_Expenditure(self, expenditure):
        # ����֧��
        self.C_sel_Rewrite.send_keys(hEls[2], expenditure)

    def b_NewOrder_8_FamilyIncome(self, fIncome):
        # ����֧��
        self.C_sel_Rewrite.send_keys(hEls[3], fIncome)

    def b_NewOrder_8_QQ(self, qq):
        # QQ
        self.C_sel_Rewrite.send_keys(hEls[4], qq)

    def b_NewOrder_8_Email(self, email):
        # QQ
        self.C_sel_Rewrite.send_keys(hEls[5], email)

    def b_NewOrder_8_Marriage(self, driver, marriage):
        #����״��
        self.Cel_NewOrder_8.el_NewOrder8_Common_PopUp_Click(driver)[2].click()
        title = self.Cel_NewOrder_8.el_NewOrder8_EduMar_Title(driver).getText().strip()
        els = self.Cel_NewOrder_8.el_NewOrder8_EduMar_Items(driver)
        if title == u"ѡ��״��":
            for el in els:
                if el.getText().strip() == marriage:
                    el.click()
                    break
                else:
                    print("û���ҵ���Ӧ����ѡ���鿴�����Ƿ���ȷ")
        else:
            print("�ⲻ��ѡ�����״���ĵ���")

    def b_NewOrder_8_Children(self, driver, cNumber):
        for i in range(int(cNumber)):
            self.Cel_NewOrder_8.el_NewOrder8_Add(driver).click()
            time.sleep(0.3) #ѭ��̫�죬��������ϣ����Լӹ̶�ʱ�䣬ȷ��ÿ�ζ����Ե���
        number = self.Cel_NewOrder_8.el_NewOrder8_Children_Num(driver).getText().strip()
        if number == cNumber:
            print("��Ů������д��ȷ")
        else:
            print("��Ů����û����д��ȷ��")

    def b_NewOrder_8_Submit(self, driver):
        #�ύ
        self.Cel_NewOrder_8.el_NewOrder8_Submit(driver).click()

    def b_NewOrder_9_syncAdress(self, driver, sync):
        #ͬ����ס��ַ
        if sync != "��":
            pass
        else:
            h = self.Cel_NewOrder_9.el_NewOrder9_syncAddress(driver)
            driver.flick(h, 1050, 300)
        #�˴���Ӧ�����ж��Ƿ���ʵͬ���־�ס��ַ���롣�벻��---

    def b_NewOrder9_County(self, driver, sync, l_addr):
        """
        ѡ��ʡ�����ĺ����ɹ���
        :param driver:
        :param sync: �Ƿ�ͬ����ס��ַ���ǣ���
        :param l_addr: ʡ������ַ�б�
        :return:
        """
        if sync == u"��":
            pass
        else:
            self.Cel_NewOrder_9.el_NewOrder9_Common_Click(driver)[0].click()
            hAddrs = self.Cel_NewOrder_9.el_NewOrder9_Address_List(driver)
            for addr in hAddrs:
                # ѡ��ʡ
                if addr.getText().strip() == l_addr[0]:
                    addr.click()
                    # ѡ����
                    hAddrs = self.Cel_NewOrder_9.el_NewOrder9_Address_List(driver)
                    for addr in hAddrs:
                        if addr.getText().strip() == l_addr[1]:
                            addr.click()
                            # ѡ������
                            hAddrs = self.Cel_NewOrder_9.el_NewOrder9_Address_List(driver)
                            for addr in hAddrs:
                                if addr.getText().strip() == l_addr[2]:
                                    addr.click()

    def b_NewOrder9_UnitAddressDetail(self, driver, sync, address):
        """
        ��ϸ��ַ
        :param driver:
        :param sync: �Ƿ�ͬ����ס��ַ���ǣ���
        :param address: ��ϸ��ַ
        :return:
        """
        if sync == u"��":
            pass
        else:
            h = self.Cel_NewOrder_9.el_NewOrder9_Common_Input(driver)[0]
            self.C_sel_Rewrite.send_keys(h, address)

    def b_NewOrder9_CommpanyName(self, driver, comName):
        """
        ��д��˾����
        :param driver:
        :param comName:
        :return:
        """
        h = self.Cel_NewOrder_9.el_NewOrder9_Common_Input(driver)[1]
        self.C_sel_Rewrite.send_keys(h, comName)

    def b_NewOrder9_CommpanyPhone(self, driver, comPhone):
        """
        ��д��˾�绰
        :param driver:
        :param comName:
        :return:
        """
        h = self.Cel_NewOrder_9.el_NewOrder9_Common_Input(driver)[2]
        self.C_sel_Rewrite.send_keys(h, comPhone)

    def b_NewOrder9_PhoneExtension(self, driver, eNumber):
        """
        ��д�̻��ֻ���
        :param driver:
        :param eNumber:
        :return:
        """
        h = self.Cel_NewOrder_9.el_NewOrder9_Common_Input(driver)[3]
        self.C_sel_Rewrite.send_keys(h, eNumber)

    def b_NewOrder9_IndustryGategory(self, driver, iGategory):
        #ѡ����ҵ���
        self.Cel_NewOrder_9.el_NewOrder9_Common_Click(driver)[1].click()
        hEls = self.Cel_NewOrder_9.el_NewOrder9_Common_Items(driver)
        for el in hEls:
            if el.getText().strip() == iGategory:
                el.click()
                break
            else:
                print("û���ҵ�����ҵ���������������")

    def b_NewOrder9_CompanyProperties(self, driver, cProperties):
        #��λ����
        self.Cel_NewOrder_9.el_NewOrder9_Common_Click(driver)[2].click()
        hEls = self.Cel_NewOrder_9.el_NewOrder9_Common_Items(driver)
        for el in hEls:
            if el.getText().strip() == cProperties:
                el.click()
                break
            else:
                print("û���ҵ��õ�λ���ʣ�������������")

    def b_NewOrder9_Position(self, driver, position):
        #ְλ
        self.Cel_NewOrder_9.el_NewOrder9_Common_Click(driver)[3].click()
        hEls = self.Cel_NewOrder_9.el_NewOrder9_Common_Items(driver)
        for el in hEls:
            if el.getText().strip() == position:
                el.click()
                break
            else:
                print("û���ҵ���ְλ��������������")

    def b_NewOrder9_EntryTime(self, driver, etYear, etMonth):
        #��ְʱ��
        self.Cel_NewOrder_9.el_NewOrder9_Common_Click(driver)[3].click()
        text = self.Cel_NewOrder_9.el_NewOrder9_EntryTime_Title(driver).getText().strip()
        if text != u"ѡ��ʱ��":
            print("����ѡ����ְʱ�䵯����������룺Ԫ���±��Ƿ���ȷ")
        else:
            #���ڵ�ǰ�꣬���»�����С�ڵ�ǰ�����ϻ�����=�򲻻���
            year = time.localtime()[0]
            if etYear > year:
                for i in range(etYear-year):
                    self.C_sel_Rewrite.swipeDown(driver, 1, 300, 988, 300, 1156, 500, 2)
                    time.sleep(0.3)
            elif etYear < year:
                for i in range(year - etYear):
                    self.C_sel_Rewrite.swipeUp(driver, 1, 300, 988, 300, 820, 500, 2)
                    time.sleep(0.3)
            else:
                print("��ְ��Ϊ��ǰ�꣬���軬����")
            # ���ڵ�ǰ���£����»�����С�ڵ�ǰ�����ϻ�����=�򲻻���
            month = time.localtime()[1]
            if etMonth > month:
                for i in range(etMonth - month):
                    self.C_sel_Rewrite.swipeDown(driver, 1, 780, 988, 780, 1156, 500, 2)
                    time.sleep(0.3)
            elif etMonth < month:
                for i in range(month - etMonth):
                    self.C_sel_Rewrite.swipeUp(driver, 1, 780, 988, 780, 820, 500, 2)
                    time.sleep(0.3)
            else:
                print("��ְ��Ϊ��ǰ�£����軬����")
            self.Cel_NewOrder_9.el_NewOrder9_EntryTime_Confirm(driver).click()

    def b_NewOrder9_WorkYear(self, driver, wYear):
        #��������
        self.Cel_NewOrder_9.el_NewOrder9_Common_Click(driver)[5].click()
        title = self.Cel_NewOrder_9.el_NewOrder9_Common_Title(driver).getText().strip()
        hEls = self.Cel_NewOrder_9.el_NewOrder9_Common_Items(driver)
        if title != u"ѡ��������":
            print("����ѡ�������޵�����������룺Ԫ���±��Ƿ���ȷ")
        else:
            for el in hEls:
                if el.getText().strip() == wYear:
                    el.click()
                    break
                else:
                    print("û���ҵ��ù������ޣ�������������")

    def b_NewOrder9_Submit(self, driver):
        #�ύ
        self.Cel_NewOrder_9.el_NewOrder9_Submit(driver)

    #----------------------------------------------------------------------
    #ҵ�����
    # ----------------------------------------------------------------------

    def b_NewOrder_3_Add_GoodInfo(self, driver, subCategory, brand, sku):
        #��д��Ʒ��Ϣ
        self.b_NewOrder_3_Choose_SubCategory(driver, subCategory)
        self.b_NewOrder_3_Check_SubCategory(driver, subCategory)
        self.b_NewOrder_3_Choose_Brand(driver, brand)
        self.b_NewOrder_3_Check_brand(driver, brand)
        self.b_NewOrder_3_Choose_SKU(driver, sku)
        self.b_NewOrder_3_Check_SKU(driver, sku)

    def b_NewOrder_3_Submit(self, driver):
        """�ύ����һ��"""
        self.Cel_NewOrder_3.el_NewOrder3_Next(driver).click()

    def b_NewOrder_4_IDInfo(self, driver, cName, idNo, l_addr, addrDetail, startDate, endDate, phone):
        """��дIDInfo"""
        #����
        self.b_NewOrder_4_Upload_IDFront(driver)
        act_CustomerInfo = "com.giveu.corder.ordercreate.activity.UploadIdCardActivity"
        driver.wait_activity(act_CustomerInfo, 20, 1)
        #����
        self.b_NewOrder_4_cName(driver, cName)
        #���֤����
        self.b_NewOrder_4_IDNo(driver, idNo)
        #ѡ��ʡ����
        self.b_NewOrder_4_parentAddr(driver, l_addr)
        #��ϸ��ַ
        self.b_NewOrder_4_AddressDetail(driver, addrDetail)

        #����
        self.b_NewOrder_4_IDCard_Back(driver)
        self.b_NewOrder_4_startDate(driver, startDate)
        self.b_NewOrder_4_EndDate(driver, endDate)
        self.b_NewOrder_4_Phone(driver, phone)

    def b_NewOrder_7_SelectCode(self, driver, item):
        self.b_NewOrder_7_Code_Click(driver)
        self.b_NewOrder_7_Select_Code(driver, item)

    def b_NewOrder_8_Person_BaseInfo(self, driver, l_addr, address, education, pIncome,
                                     expenditure, fIncome, qq, email, marriage, cNumber):
        #��д���˻�����Ϣ
        #ѡ����l_addr:ʡ�����б�
        self.b_NewOrder_8_County(driver, l_addr)
        #��ϸ��ַ
        self.b_NewOrder_8_AddressDetail(driver, address)
        #�����̶�
        self.b_NewOrder_8_Education(driver, education)
        #������������
        self.b_NewOrder_8_personIncome(pIncome)
        #������֧��
        self.b_NewOrder_8_Expenditure(expenditure)
        # ��ͥ��������
        self.b_NewOrder_8_FamilyIncome(fIncome)
        #qq
        self.b_NewOrder_8_QQ(qq)
        #email
        self.b_NewOrder_8_Email(email)
        #����״��
        self.b_NewOrder_8_Marriage(driver, marriage)
        #��Ů����
        if marriage == u"δ��":
            pass
        else:
            self.b_NewOrder_8_Children(driver, cNumber)

    def b_NewOrder_9_CompanyInfo(self, driver, sync, l_addr, address, comName, comPhone, eNumber,
                                 iGategory, cProperties, position, etYear, etMonth, wYear):
        #��˾��Ϣ
        #ͬ���־�ס��ַ
        self.b_NewOrder_9_syncAdress(driver, sync)
        self.b_NewOrder9_County(driver, sync, l_addr)
        self.b_NewOrder9_UnitAddressDetail(driver, sync, address)
        self.b_NewOrder9_CommpanyName(driver, comName)
        self.b_NewOrder9_CommpanyPhone(driver, comPhone)
        self.b_NewOrder9_PhoneExtension(driver, eNumber)
        self.b_NewOrder9_IndustryGategory(driver, iGategory)
        self.b_NewOrder9_CompanyProperties(driver, cProperties)
        self.b_NewOrder9_Position(driver, position)
        self.b_NewOrder9_EntryTime(driver, etYear, etMonth)
        self.b_NewOrder9_WorkYear(driver, wYear)


