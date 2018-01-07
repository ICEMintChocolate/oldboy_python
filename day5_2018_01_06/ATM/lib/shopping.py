# -*- coding:utf-8 -*-
# User:fucong
# Time：
import sys
from conf import settings


def shops():
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
    #print(len(shoplist))
    for itme,key in enumerate(shoplist):
        print(itme,key)
    while True:
        user_chicoe = input('请您输入您要选择的商品编号:')
        if user_chicoe == 'q':
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
                        cunkuan = l[i][6]
                        yue = float(cunkuan)-float(zongjia)
                        print('付款：%s,余额：%s' %(zongjia,yue))
                        l[i][6] = str(yue)
                        f = open(settings.DB_PATH, 'r+', encoding='utf-8')
                        for i in range(0, len(l)):
                            lines = l[i]
                            new_lines = ",".join(lines)
                            f.write(new_lines)
                        f.flush()
                        f.close()
            sys.exit()
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

