# -*- coding:utf-8 -*-
# User:fucong
# Time：
from conf import settings
from lib import logs
import sys
def repayment():
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
                total_amount = l[i][6]
                if  float(total_amount) < 0.00:
                    print('账户名：%s,还款金额：%s'%(user_input,l[i][6]))
                    print('是否还款，请进行选择：')
                    TFlist = [
                        ('是'),
                        ('否')
                    ]
                    print(enumerate(TFlist))
                    for itme, key in enumerate(TFlist):
                        print(itme, key)
                    TF_input = input('请根据提示进行选择：')
                    if TF_input == '0':
                        while True :
                            repayment_amount_input = input('请您输入要还款的金额：')
                            huankuang = float(repayment_amount_input)+float(total_amount)
                            l[i][6] = huankuang
                            total_amount = l[i][6]

                            if float(huankuang) >= 0.00:
                                print('还款成功')
                                print('您的账号总金额：%s' %total_amount)
                                msg = '还款成功，您的账号总金额：%s' %total_amount
                                logs.logs(msg)
                                l[i][6] = str(total_amount)
                                f = open(settings.DB_PATH, 'r+', encoding='utf-8')
                                for i in range(0, len(l)):
                                    lines = l[i]
                                    new_lines = ",".join(lines)
                                    f.write(new_lines)
                                f.flush()
                                f.close()
                                break
                            elif float(huankuang) < 0.00:
                                print('还款失败，您还需要还款： %s'%huankuang)
                                continue
                    elif TF_input == '1':
                        print('由于欠款未还清，账号被冻结')
                        f = open(settings.FEDB_PATH, 'r+', encoding='utf-8')
                        for i in range(0,len(l)):
                            lines = l[i]
                            if user_input in lines :
                                    new_lines = ",".join(lines)
                                    f.write(new_lines)
                        f.flush()
                        f.close()
                elif float(total_amount) > 0.00:
                    print('账户名：%s,存款总数：%s,本月无需还款'%(user_input,l[i][6]))
                    sys.exit()