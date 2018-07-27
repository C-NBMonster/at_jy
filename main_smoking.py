import unittest

from cases.functions.test_baidu import BaiduTest
from cases.sub1.st_youdao import YoudaoTest

#构造测试集
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(BaiduTest))
suite.addTest(unittest.makeSuite(YoudaoTest))

if __name__=='__main__':
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)