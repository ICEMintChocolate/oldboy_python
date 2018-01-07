# -*- coding:utf-8 -*-
# User:fucong
# Time：

from conf import settings
from lib import logs



def cash():
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
                print('账户名：%s,存款总数：%s'%(user_input,l[i][6]))
                zongjine = l[i][6]
                tixian = input('请您输入要提取的金额:')
                yue = float(zongjine)-(float(tixian)+float(tixian)*0.05)
                print('您已经成功提取：%s,账户余额 %.2f' %(tixian,yue))
                l[i][6] = str(yue)
                f = open(settings.DB_PATH,'r+',encoding='utf-8')
                for i in range(0,len(l)):
                    lines = l[i]
                    new_lines = ",".join(lines)
                    f.write(new_lines)
                f.flush()
                f.close()
                msg_cash = '您已经成功提取：%s,账户余额 %.2f' %(tixian,yue)
                logs.logs(msg_cash)
