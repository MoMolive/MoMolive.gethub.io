# coding = utf - 8

import random
ver = random.randint(1000,9999)
print(u'生成验证码：%d'%ver)
num = (u'请输入数值：')
print(num)
if num == 0:
    print(u'登陆成功')
elif num == 999999:
    print(u'登陆成功')
else:
    print(u'验证码错误')
