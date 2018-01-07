# -*- coding:utf-8 -*-
# User:fucong
# Time：
from conf import settings
from lib import logs
import sys,time
def transfer():
    list_user = []
    with open(settings.DB_PATH,'r',encoding='utf-8') as table:
        for i in table:
            list_user.append(i)
    user_input = input('pls you name:')
    l = []
    for i in list_user:
        l.append(list(i.split(',')))
    for i in range(0,len(l)):
        if user_input == l[i][1]:
            user_passwd = input('pls you password:')
            if user_passwd == l[i][2]:
                print('login seussful')
                user_total_amount = l[i][6]
                TFlist = [
                    ('转账给其他账号'),
                    ('退出')
                ]
                for itme, key in enumerate(TFlist):
                    print(itme, key)
                TF_input = input('请根据提示进行选择：')
                if TF_input == '0':
                    transfer_user_input = input('transfer_user:')
                    for i in range(0, len(l)):
                        if transfer_user_input == l[i][1]:
                            print('账号存在，可以进行转账')
                            transfer_amount_input = input('请输入转账金额：')
                            if transfer_amount_input == 'q':
                                break
                            shengyu = float(user_total_amount) - float(transfer_amount_input)
                            if float(shengyu) >= 0.00:
                                print('转账成功,转账金额：%s' %transfer_amount_input)
                                print('账号余额：%s'%shengyu)
                                msg = '转账成功,转账金额：%s,账号余额：%s' %(transfer_amount_input,shengyu)
                                logs.logs(msg)
                                for ii in range(0,len(l)):
                                    if user_input in l[ii][1]:
                                        l[ii][6] = str(shengyu)
                                        f = open(settings.DB_PATH, 'r+', encoding='utf-8')
                                        for i in range(0, len(l)):
                                            lines = l[i]
                                            new_lines = ",".join(lines)
                                            f.write(new_lines)
                                        f.flush()
                                        f.close()
                                    time.sleep(2)
                                for ii in range(0, len(l)):
                                    if transfer_user_input in l[ii][1]:
                                        transfer_user_total_amount = l[ii][6]
                                        l[ii][6] = str(float(transfer_amount_input)+float(transfer_user_total_amount))
                                        f = open(settings.DB_PATH, 'r+', encoding='utf-8')
                                        for i in range(0, len(l)):
                                            lines = l[i]
                                            new_lines = ",".join(lines)
                                            f.write(new_lines)
                                        f.flush()
                                        f.close()
                            elif float(shengyu) < 0.00:
                                print('转账失败')
                                continue
                elif TF_input == '1':
                    sys.exit()