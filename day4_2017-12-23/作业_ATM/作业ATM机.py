# -*- coding:utf-8 -*-
# User:fucong
# Time：2017-12-31
'''
作业需求：

模拟实现一个ATM + 购物商城程序

1 额度 15000或自定义 done
2 实现购物商城，买东西加入 购物车，调用信用卡接口结账 done
3 可以息提现，手续费5% done
4 每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计
5 支持多账户登录 done
6 支持账户间转账
7 记录每月日常消费流水
8 提供还款接口
9 ATM记录操作日志
10 提供管理接口，包括添加账户、用户额度，冻结账户等。。。
11 用户认证用装饰器
'''
import time
#功能1
#1 额度 15000或自定义
#用户表构成方式
#id
#name
#可用金额 amount_available
#剩余金额 surplus_amount
#总金额   total_amount
#存入金额 amount
#id,name,password,amount_available,surplus_amount,amount,total_amount
# 1,AlexLi,123,15000,15000,0,15000,2017-12-31 18:43:10
# 2,fu,123,15000,15000,0,25000,2017-12-31 18:45:10
#功能4
#5 支持多账户登录
#print(round(time.time()))
def times():
    caozuo_time = time.strftime("%Y-%m-%d %H:%M:%S")
    print(caozuo_time)
    return
#times()
def login():
    list_user = []
    with open('user.txt','r',encoding='utf-8') as table:
        for i in table:
            list_user.append(i)
    print(list_user)
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
    return


#功能2
#2 实现购物商城，买东西加入 购物车，调用信用卡接口结账
#商品列表
def shop():
    shoplist = [
        ('Iphone',5888),
        ('MacAir',8000),
        ('XiaoMi',19.9),
        ('coffee',30),
    ]
    user_shangping_jiage = []
    user_shangping_mingcheng = []
    print(enumerate(shoplist))
    print('欢迎来到商城')
    for itme,key in enumerate(shoplist):
        print(itme,key)
    while True:
        user_chicoe = input('请您输入您要选择的商品编号:')
        if user_chicoe == 'q':
            list_user = []
            with open('user.txt','r',encoding='utf-8') as table:
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
                        cunkuan = l[i][6]
                        yue = float(cunkuan)-float(zongjia)
                        print('付款：%s,余额：%s' %(zongjia,yue))
                        l[i][6] = yue
                        f = open('user.txt', 'r+', encoding='utf-8')
                        for i in l:
                            lines = ','.join(i)
                            f.write(lines)
                        f.flush()
                        f.close()
                        times()
            break
        if user_chicoe.isdigit() == False:
            print('您输入的商品编号错误，请您重新输入：')
            continue
        elif user_chicoe.isdigit() == True:
            user_chicoe = int(user_chicoe)
            if user_chicoe >= len(shoplist):
                print("您输入的商品编号错误，请您重新输入：")
                continue
            print(shoplist[user_chicoe])
            shangping_jiage = shoplist[user_chicoe][1]  # 存用户购买的物品价格。
            shangping_mingcheng = shoplist[user_chicoe][0]  # 存用户购买的物品名称
        user_shangping_jiage.append(shangping_jiage)
        user_shangping_mingcheng.append(shangping_mingcheng)
        user_shangping_zongshu = set(user_shangping_mingcheng)
        for ii in user_shangping_zongshu:
            mingzi = ii
            geshu = user_shangping_mingcheng.count(ii)
            zhangdan = []
            zhangdan.append([str(mingzi),str(geshu)])
            print(zhangdan)
        print('您购买的商品名称：%s*%s 总价：' % (mingzi, geshu))
        zongjia = 0
        for i in user_shangping_jiage:
            zongjia += i
        print('您购买的商品总价：%.2f' % zongjia)



    return
# login(),times(),shop()
#功能3
#3 可以提现，手续费5%
def cash():
    list_user = []
    with open('user.txt','r',encoding='utf-8') as table:
        for i in table:
            list_user.append(i)
    print(list_user)
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
                yue = float(zongjine)-(float(tixian)*0.05)
                print('您已经成功提取：%s,账户余额 %.2f' %(tixian,yue))
                l[i][6] = yue
                times()
                f = open('user.txt','r+',encoding='utf-8')
                for i in l:
                    lines = ','.join(i)
                    f.write(lines)
                f.flush()
                f.close()
    return

cash()






#功能5
#9 ATM记录操作日志