# encoding=utf-8
from selenium import webdriver
import unittest, time
from HTMLTestRunner import HTMLTestRunner
import sys
import testPrime
reload(sys)
sys.setdefaultencoding('utf8')

if __name__ == "__main__":
    
    testunit = unittest.TestSuite()
    testunit.addTest(testPrime.TestAdd("test_add"))

    # 按照一定格式获取当前时间
    now = time.strftime("%Y-%m-%d %H-%M-%S")

    # 定义报告存放路径
    # filename = './report/result.html'
    filename = sys.path[0] + '/report/test primepath-' + now + '-result.html'
    fp = open(filename, 'wb')

    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,                  # 指定测试报告文件
                        title='test PrimePath report',        # 定义测试报告标题 
                        description='detail：')    # 定义测试报告副标题
    runner.run(testunit)    # 运行测试用例
    fp.close()  # 关闭报告文件