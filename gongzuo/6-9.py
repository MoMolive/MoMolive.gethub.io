# coding = utf-8
from selenium import webdriver
from time import sleep
from HTMLTestRunnerCN import HTMLTestRunner
import unittest
driver=webdriver.Chrome()
url='https://learn.test.longan.eliteu.xyz/'
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="header"]/div[2]/a[2]').click()
driver.implicitly_wait(3)
driver.find_element_by_xpath('//*[@id="normal_login_username"]').send_keys('abc')
sleep(2)
driver.find_element_by_id('normal_login_password').send_keys('123456')
sleep(1)
driver.find_element_by_xpath('//*[@class="ant-btn login-form-button ant-btn-primary ant-btn-lg ant-btn-block"]').click()
sleep(2)
driver.find_element_by_xpath('//*[@class="ant-btn ant-btn-primary ant-btn-lg"]').click()
sleep(3)
aa=driver.window_handles
print("order page:", aa)
driver.switch_to.window(aa[0])
sleep(3)
driver.find_element_by_xpath('//*[@class="ant-btn ant-btn-primary ant-btn-lg"]').click()
sleep(3)
bb=driver.window_handles
print("order page:", bb)
driver.switch_to.window(bb[0])
sleep(3)
driver.find_element_by_xpath('').click()
# sleep(5)

# driver.quit()
# driver.close()
#
# //*[@id="home"]/section/div[3]/div[2]/div[3]