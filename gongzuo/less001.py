# coding=utf8
from selenium import webdriver
from time import sleep
import unittest

class longan(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url='https://learn.longan.link/'
        self.verificationErrors= []
        self.accept_next_alert = True

    def test_4(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_partial_link_text('注册').click()
        sleep(1)
        driver.find_element_by_id('normal_login_username').send_keys('ddb')
        sleep(1)
        driver.find_element_by_id('normal_login_password').send_keys('123456')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="normal_login_repectpassword"]').send_keys('123456')
        sleep(1)
        driver.find_element_by_id('normal_login_phone').send_keys('13512345612')
        sleep(1)
        driver.find_element_by_id('normal_login_agreement').click()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="normal_login"]/div[5]/div/div/div/button').click()
        sleep(1)
        driver.find_element_by_id('normal_login_captcha').send_keys('132465')
        sleep(1)
        driver.find_element_by_xpath('//*[@id="normal_login"]/button').click()
        sleep(5)
        driver.find_element_by_xpath('//*[@id="normal_login"]/div[7]/div/div/div/a/button').click()
        sleep(1)
        driver.find_element_by_id('normal_login_username').send_keys('ABC')
        sleep(1)
        driver.find_element_by_id('normal_login_password').send_keys('123456')
        sleep(1)
        text = driver.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button').click()
        if text == "登陆失败":
            print("不通过")
        else:
            print("通过")
        sleep(3)
        driver.quit()
