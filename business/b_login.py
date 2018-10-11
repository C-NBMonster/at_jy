# coding=utf-8
"""
@author: mirrorChen
@license: (C) Copyright 2011-2018, mirror personal Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: b_login.py
@time: 2018/9/11 17:30
@desc: 登录模块代码,日志也在此处理
"""

import unittest, time
from elements.el_JYT.el_login import C_el_login
from common.rewrite import C_selenium_rewrite
from common.log import Log
mylogger = Log(log_module=u'登录测试用例日志')


C_sel_rewrite = C_selenium_rewrite()
Cel_Login = C_el_login()


class C_B_Login(unittest.TestCase):

    def b_login_uName(self, driver, uName):
        """
        登录
        :param uName: 账号
        :return:
        """
        el_Info = Cel_Login.el_Login_uName(driver)
        if el_Info[0] == True:
            C_sel_rewrite.send_key(el_Info[2], uName)
            mylogger.info("填写用户名--成功")
        else:
            mylogger.error(el_Info[1])

    def b_login_pwd(self, driver, pwd):
        """
        密码
        :param driver:
        :param pwd:
        :return:
        """
        el_Info = Cel_Login.el_login_pwd(driver)
        if el_Info[0] == True:
            C_sel_rewrite.send_key(el_Info[2], pwd)
            mylogger.info("填写用密码--成功")
        else:
            mylogger.error(el_Info[1])

    def b_login_submit(self, driver):
        """
        提交
        :param driver:
        :return:
        """
        el_Info = Cel_Login.el_login_submit(driver)
        if el_Info[0] == True:
            el_Info[2].click()
            mylogger.info("登录提交--成功")
        else:
            mylogger.error(el_Info[1])

    def b_login(self, driver, uName, pwd):
        """
        登录逻辑代码汇总
        :param driver:
        :param uName:
        :param pwd:
        :return:
        """
        act_login = "com.giveu.corder.me.activity.LoginActivity"
        driver.wait_activity(act_login, 20, 1)
        self.b_login_uName(driver, uName)
        self.b_login_pwd(driver, pwd)
        self.b_login_submit(driver)
        mylogger.info("jyb登录成功")

    def accept_PopUp(self, driver):
        """
        点击弹窗，然后显示主页面
        :param driver:
        :return:
        """
        #弹窗逻辑目前只是按最简单的模式进行判断，后续需再熟悉规则，进行优化

        try:
            global el1
            el1 = Cel_Login.el_main_PopUp_1_OK(driver)
            if el1[0] == True:
                el1[2].click()
                time.sleep(0.5)
        except:
            mylogger.info("找不到相机授权这个元素,错误如下")
            mylogger.error(el1[1])
        finally:
            try:
                global el2
                el2 = Cel_Login.el_main_PopUp_2_NotSetPWD(driver)
                if el2[0] == True:
                    el2[2].click()
                    time.sleep(0.5)
            except:
                mylogger.info("找不到取消设置密码这个元素,错误如下")
                mylogger.error(el2[1])
            finally:
                try:
                    global el3
                    el3 = Cel_Login.el_main_PopUp_3_OK(driver)
                    if el3[0] == True:
                        el3[2].click()
                except:
                    mylogger.info("找不到接受协议这个元素,错误如下")
                    mylogger.error(el3[1])
                finally:
                    print("找不到元素，不一定正确或者错误，能继续运行不报错即可")


