#coding=utf8

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import random
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
import unittest
import time
class longan(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.base_url = 'https://longan.link/'
        self.verificationErrors= []
        self.accept_next_alert = True

    def test_1(self):
        driver = self.driver
        driver.implicitly_wait(20)
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_partial_link_text('关于龙眼').click()
        a = driver.window_handles
        print("order page:", a)
        driver.switch_to.window(a[1])
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="about"]/section[2]/p[2]/video').click()
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="about"]/section[2]/p[2]/video').click()
        time.sleep(2)
        driver.close()
        b = driver.window_handles
        print("order page:", b)
        driver.switch_to.window(b[0])
        driver.find_element_by_partial_link_text('技术文档').click()
        time.sleep(3)
        c = driver.window_handles
        print("order page:", c)
        driver.switch_to.window(c[1])
        driver.close()
        time.sleep(3)
        driver.find_element_by_partial_link_text('魔法视频').click()
        d = driver.window_handles
        print("order page:", d)
        driver.switch_to.window(d[1])
        time.sleep(5)
        driver.close()

        # driver.find_element_by_partial_link_text('我是爱好者').click()
        # a = driver.window_handles
        # print("order page:", a)
        # driver.switch_to.window(a[1])
        # driver.find_element_by_partial_link_text("登录").click()
        # sleep(1)
        # driver.find_element_by_id('normal_login_username').send_keys('ABC')
        # sleep(1)
        # driver.find_element_by_id('normal_login_password').send_keys('123456')
        # sleep(1)
        # driver.find_element_by_xpath('//*[@id="normal_login"]/div[4]/div/div/div/button/span').click()
        # sleep(1)
        # driver.find_element_by_id()




        # time.sleep(5)
        # if text == "登录":
        #     print("通过")
        # else:
        #     print("不通过")
        # driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True