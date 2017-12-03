# -*- coding:utf-8 -*-
# User:fucong
# Time：2017-12-03
'''
基础需求：

让用户输入用户名密码
认证成功后显示欢迎信息
输错三次后退出程序
升级需求：

可以支持多个用户登录 (提示，通过列表存多个账户信息)
用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示:需把用户锁定的状态存到文件里）
'''
#可以支持多个用户登录 (提示，通过列表存多个账户信息)
# userlist = ['seven','alex','egon']
# password = '123'
# #计数器
# count = 0
# while count < 3:
#     user_input = input('请输入用户名：')
#     pass_input = input('请输入密码：')
#     if user_input in userlist and pass_input == password:
#         print('登录成功')
#     else:
#         count +=1
#         print('登录失败')
