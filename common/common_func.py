#! /usr/bin/env python
#coding=utf-8
import sys

from selenium import webdriver
import unittest,sys,time,random,datetime
from random import Random
import HTMLTestRunner
import time,os,datetime
import smtplib
from selenium.webdriver.support.ui import WebDriverWait
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage



class CCommon_Function():
    def setUP(self):
        self.verificationErrors = []
    

        #生成字母随机码，随机码位数由业务（randomlength）规定
    def randomBarcodeS(self,randomlength):
        strs   = ''
        chars  = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            strs+=chars[random.randint(0, length)]
        return strs
        #生成数字随机码，随机码位数由业务（randomlength）规定

    def randomBarcodeN(self,randomlength):
        strN   = ''
        chars  = '0123456789'
        length = len(chars) - 1
        random = Random()
        for i in range(randomlength):
            strN+=chars[random.randint(0, length)]
        return strN
        
    #随机生成手机号码
    def createPhone(self):
        
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","176","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
    #随机生成身份证号码
    def makeIDNo(self):
        ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
        LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
        u''' 随机生成新的18为身份证号码 '''
        t = time.localtime()[0]
        x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                            random.randint(1,99),
                                            random.randint(1,99),
                                            random.randint(t - 80, t - 18),
                                            random.randint(1,12),
                                            random.randint(1,28),
                                            random.randint(1,999))
        y = 0
        for i in range(17):
            y += int(x[i]) * ARR[i]

        return '%s%s' %(x, LAST[y % 11])
    #优惠券名字
    def YHQ_Name(self):
        dt      = datetime.datetime.now()
        dtStr   = str(dt.month) + str(dt.day+1) + str(dt.hour) + str(dt.minute) + str(dt.second)
        YHQName = u"新增YHQ"+dtStr
        return (YHQName)

    #生成测试报告
    def createReports(self,testunit):
        now=time.strftime("%Y-%m-%d %H_%M_%S",time.localtime(time.time()))
        filename = "D:\\Python\\Reports\\Smoking"+"smokingTestReport"+now+".html"
        fp = open(filename, 'wb')
        runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = u'新系统后台自动化综合测试报告',description=u'用例执行情况:')
        runner.run(testunit)

    def AutoSentMail(self,file_new):
        mail_from = 'chen_jz06@126.com'
        mail_to   = '1667809009@qq.com'

        #定义正文
        f = open(file_new,'rb')
        mail_content = f.read()
        f.close()
        msg = MIMEText(mail_content,'html','utf-8')
        msg['Subject'] = u'新系统后台自动化测试综合报告'
        msg['from']    = mail_from
        msg['to']      = mail_to
        #定义发送时间
        msg['date'] = time.strftime('%a,%d %b %y %H:%M:%S %z')
        smtp=smtplib.SMTP()
        smtp.connect('smtp.126.com')
        smtp.login(mail_from,'cjxPNXZX06')
        smtp.sendmail(mail_from,mail_to,msg.as_string())
        smtp.quit()
        print("邮件发送成功!")

    #发送测试报告

    def send_report(self):
        #查找最新文件并发送    
        result_dir = os.path.dirname(os.getcwd()) + '\\AT_Demo\\report\\'
        lists = os.listdir(result_dir)
        lists.sort(key=lambda    fn:    os.path.getmtime(result_dir+"\\"+fn)    if    not    os.path.isdir(result_dir+"\\"+fn)  else  0)
        print ('最新的测试报告文件为： '+lists[-1])
        file_new = os.path.join(result_dir,lists[-1])
        print(file_new)
        CCommon_Function.AutoSentMail(self,file_new)
        
    def is_option_value_present(self,element_id,tag_name,option_text): #遍历select
        driver = self.driver
        select=driver.find_element_by_id(element_id)
        # 注意使用find_elements
        options_list=select.find_elements_by_tag_name(tag_name)
        for option in options_list:
            # print ("Value is: " + option.get_attribute("value"))
            # print ("Text is:" +option.text)
            if option_text in option.text:
                global select_value
                select_value = option.get_attribute("value")
                print("option_textoption_textoption_textValue is: " + select_value)
                break
        return select_value



    def wait_activity(self, activity, timeout, interval=1):
        """Wait for an activity: block until target activity presents
              or time out.

              This is an Android-only method.

              :Agrs:
               - activity - target activity
             - timeout - max wait time, in seconds
             - interval - sleep interval between retries, in seconds
             """

        def wait_activity(self, activity, timeout, interval=1):
            """Wait for an activity: block until target activity presents
            or time out.

            This is an Android-only method.

            :Agrs:
             - activity - target activity
             - timeout - max wait time, in seconds
             - interval - sleep interval between retries, in seconds
            """
            try:
                WebDriverWait(self, timeout, interval).until(
                    lambda d: d.current_activity == activity)
                return True
            except Exception as e:
                return False

