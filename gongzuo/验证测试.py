# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class taobao_infos:
    def __init__(self):
        url = 'https://login.taobao.com/member/login/jhtml'
        self.url = url
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs",{"profile.managed_default_settings.images":2})
        options.add_experimental_option('excludeSwitches',['enable-automation'])
        self.browser=webdriver.Chrome(executable_path=chromedriver_path,options=options)
        self.wait = WebDriverWait(self.browser,10)

    def login(self):
        self.browser.get(self.url)
        password_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
        password_login.click()
        weibo_login = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
        weibo_login.click()
        
