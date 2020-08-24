# coding=utf-8
from testcase.YL_testcase import YL_test
import unittest,os,time
from utils.HTMLTestRunnerCN import HTMLTestRunner
from utils.mail import SendMail
def allcase():
    suite=unittest.TestSuite()
    suite.addTests([YL_test("test01_login"),
                    YL_test("test02_query"),
                    YL_test("test03_mengan")])
    return suite
now=time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime(time.time()))
path=os.path.abspath(os.path.dirname(os.getcwd()))+"\\report\\"
report_path=path+'longan-敏感词返回结果.html'

def run_allcase():
    fp=open(report_path,'wb')
    runner=HTMLTestRunner(stream=fp,title='YL接口自动化')
    runner.run(allcase())
    fp.close()
def send_mail():
    sm=SendMail(send_msg=report_path,attachment=report_path)
    sm.send_mail()
if __name__=='__main__':
    run_allcase()
    send_mail()