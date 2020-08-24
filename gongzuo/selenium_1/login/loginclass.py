# coding=utf-8
class login_go():
    u'''登录类封装'''
    def __init__(self,driver):
        u'''初始化driver参数'''
        self.driver = driver

    def login(self,username,password):
        u'''输入用户名和密码,点击登录'''
        self.driver.find_element_by_id("liger-textbox-user").clear()
        self.driver.find_element_by_id("liger-textbox-user").send_keys('ABC')
        self.driver.find_element_by_id("liger-textbox-pwd_old").clear()
        self.driver.find_element_by_id("liger-textbox-pwd").clear()
        self.driver.find_element_by_id("liger-textbox-pwd").send_keys('123456')
        self.driver.find_element_by_id("go").click()