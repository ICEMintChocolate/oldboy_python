# -*- coding:utf-8 -*-
# User:fucong
# Time：2017-12-03
'''
基础需求：

让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序
'''
user = 'seven'
password = '123'
#计数器
count = 0
while count < 3:
    user_input = input('请输入用户名：')
    pass_input = input('请输入密码：')
    if user_input == user and pass_input == password:
        print('登录成功')
    else:
        count +=1
        print('登录失败')