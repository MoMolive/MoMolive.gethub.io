# coding=utf-8
import unittest,json
from api.YL_api import CMs_api
class YL_test(unittest.TestCase):
    def setUp(self):
        return '开始执行'
    def tearDown(self):
        return '执行完毕'
    def test01_login(self):
        result=CMs_api().login()
        try:
            if result['token']==None:
                print('登陆成功')
            else:
                print('登陆失败')
        except:
            print('登陆成功')
    def test02_query(self):
        result=CMs_api().query()
        try:
            if result['username']=="该账户不存在":
                print('登陆失败')
            else:
                print('登陆成功')
        except:
            print('登陆失败')
    def test03_mengan(self):
        #这里如果调用一个txt遍历得话要在这里进行循环遍历
        r1 = open(r'D:\py文件夹\keywords.txt', 'r', encoding='UTF-8')
        content_list = r1.readlines()
        for item in range(len(content_list)):
            # 输出当前遍历的内容
            result = CMs_api().mengan(content_list[item])
            try:
                if result['pass']==True:
                    print(content_list[item],'敏感词通过')
                else:
                    print(content_list[item],'敏感词不通过')
            except:
                return


