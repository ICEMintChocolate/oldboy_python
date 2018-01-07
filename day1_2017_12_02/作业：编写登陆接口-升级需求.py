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
user_list = ['seven','alex','egon']
user_pass = '123'
count = 0
#判断是否有用户存储文件
import pathlib
chenggong_file = pathlib.Path('c:\chenggong.txt')
chenggong_file_status = chenggong_file.is_file()
shibai_file = pathlib.Path('c:\shibai.txt')
shibai_file_status = shibai_file.is_file()
if chenggong_file_status == True and shibai_file_status == True:
    while count < 3:
        f = open('c:\chenggong.txt','r')
        user_chengong = f.readlines()
        f.close()
        f = open('c:\shibai.txt','r')
        user_shibai = f.readlines()
        f.close()
    #第一次正常的循环
        if user_chengong == [] :
            user_input = input('请输入用户：')
            user_pass_input = input('请输入密码：')
            if user_input in user_list  and user_pass_input == user_pass:
                f = open('c:\chenggong.txt','w')
                f.write('%s\n'%user_input)
                f.close()
                print('登录成功')
                count += 1
                continue
            else:
                f = open('c:\shibai.txt','w')
                f.write('%s\n'%user_input)
                f.close()
                print('登录失败')
                count += 1
                continue
        if user_chengong != [] :
                print('%s 登录成功'%user_chengong)
                print('请在 >>> 后开始输入命令，q 为退出')
                tag = True
                while tag:
                    cmd_input = input('>>>')
                    if cmd_input == 'q':
                        print('%s 成功退出'%user_chengong)
                        tag = False
                break
else:
    print('请到 C 盘的根目录创建 "chenggong.txt" 和 "shibai.txt" 再次运行程序')
