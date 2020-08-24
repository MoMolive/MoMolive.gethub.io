#coding=utf8
import unittest
from HTMLTestRunnerCN import HTMLTestRunner
import time

test_dir= r"D:\测试报告\gongzuo\selenium_1\report"
report_dir= r"D:\测试报告"
discover=unittest.defaultTestLoader.discover(test_dir, pattern="test*.py")

if __name__=='__main__':
    now=time.strftime("%Y-%m-%d %H_%M_")
    filename=report_dir+"/"+now+"UI自动化测试报告.html"
    fp=open(filename,'wb')
    runner=HTMLTestRunner(stream=fp,
                          title=u"测试报告",
                          description=u"用例执行情况：")
    runner.run(discover)
    # fp.close()