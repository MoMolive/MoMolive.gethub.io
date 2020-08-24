# coding=utf-8

'''
接口自动化框架设计
此模块放所有的接口入参信息
'''
# 定义登录接口的入参信息
login_url='https://learn.longan.link/api/v1/login/'
login_data={
    "login_type": "password",
    "password": "123456",
    "remeber": True,
    "username": "ABC"
}
# 定义查询用户接口入参
query_url='https://learn.longan.link/api/v1/login/'
query_data={
    "login_type": "password",
    "password": "123456",
    "remeber": False,
    "username": "123"
}

#定义关键词验证url
mengan_url = 'https://sensitive.eliteu.cn/check'
