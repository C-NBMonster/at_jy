# coding=utf-8
import unittest
import HTMLTestRunner
import time,os


def creatsuite():
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = 'D:\\projects\\python\\Projects\\AT_Demo\\cases'
    # 定义 discover 方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir,
                                                   pattern='test_*.py',
                                                   top_level_dir=None)
    print("dis",discover)
    # discover 方法筛选出来的用例，循环添加到测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


alltestnames = creatsuite()
if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    filename1 = r'D:\Py_Projects\AT_Demo\report\/' + now + '_func_result.html'
    filename2 = r'D:\Py_Projects\AT_Demo\report\/' + now + '_interface_result.html'
    filename3 = r'D:\Py_Projects\AT_Demo\report\/' + now + '_smoking_result.html'
    fp = open(filename1, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'测试报告',
        description=u'用例的执行情况')

    runner.run(alltestnames)
    fp.close()

    #发送邮件
    

