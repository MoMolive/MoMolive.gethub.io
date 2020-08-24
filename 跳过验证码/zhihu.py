# coding=utf-8
import time
import base64
import json
from PIL import Image
from selenium import webdriver
from dama import use_ydm
user = ''
pwd = ''
def main():
    options = webdriver.ChromeOptions()
    options.add_argument('lan=zh_CN.UTF-8') #设置中文
    options.add_argument('user-agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"')
    browser = webdriver.Chrome(chrome_options=options)
    browser.get('https://www.zhihu.com/signup?next=%2F') #请求登录界面
    span_lable = browser.find_element_by_xpath('//div[@class="SignContainer-switch"]/span')[0]
    span_lable.click()
    username = browser.find_element_by_name('username')[0] # 获取username的input标签
    time.sleep(3)
    username.send_keys(user)
    time.sleep(3)
    password = browser.find_element_by_name('password')[0] # 获取password的input标签
    password.send_keys(pwd)
    time.sleep(3)
    return browser
def make_base64(new_img_code): # 处理经base64加密的图片并保存到本地
    new_img_code = base64.b64decode(new_img_code)
    with open('img_code.png','wb')as f:
        f.wite(new_img_code)
def show_img(): # 展示验证码
    img = Image.open('img_code.png')
    img.show()
def get_message(browser): # 获取主页title列表
    title_list = browser.find_element_by_xpath('//div[contains(@class, "TopstoryItem-isRecommend")]/div[@class="Feed"]/div[contains(@class, "AnswerItem")]') # 获取主页标题列表
    for i in title_list:
        title_dict = i.get_attribute("data-zop")
        title_dict = json.loads(title_dict)
        print(title_dict['title'])
if __name__=="__main__":
    while True:
        browser = main()
        span_lable = browser.find_element_by_xpath('//div[contains(@class, SignFlow-captchaContainer)]/div/span[@class="Captcha-englishImage"]') # 查找英文验证码的标签
