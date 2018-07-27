# coding=utf-8
import unittest
import HTMLTestRunner
import time,os
import logging.config
from common.common_func import CCommon_Function
#logging.config.fileConfig("logger.conf")

def creatsuite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = 'D:\\projects\\python\\Projects\\AT_Demo\\cases'
    # 定义 discover 方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit


alltestnames = creatsuite()

if __name__ == '__main__':

    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    filename = r'D:\projects\python\Projects\AT_Demo\report\/' + now + '_func_result.txt'
    fp = open(filename, 'a')

    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例的执行情况')

    runner.run(alltestnames)
    fp.close()

    #发送邮件

    HEmail = CCommon_Function()
    #发送测试报告
    HEmail.send_report()
