# -*- coding:utf-8 -*-
# User:fucong
# Time：2017-12-10
'''
#作业二：请闭眼写出购物车程序
#需求:
用户名和密码存放于文件中，格式为：egon|egon123
启动程序后，先登录，登录成功则让用户输入工资,然后打印商品列表，失败则重新登录，超过三次则退出程序
允许用户根据商品编号购买商品
用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
可随时退出，退出时，打印已购买商品和余额

使用的知识点
set() 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。
count() 方法用于统计某个元素在列表中出现的次数。


'''
#获取用户和密码
user_db = {}
with open(r'c:\user.txt','r') as login_file :
    for userinfo in login_file:
        user,passwd = userinfo.split('|')
        user_db[user] = passwd


#商品列表
shoplist = [
    ('Iphone',5888),
    ('MacAir',8000),
    ('XiaoMi',19.9),
    ('coffee',30),
   ]
print(len(shoplist))
print(shoplist[0])
#登录接口
# enumerate()函数可以取索引
user_shangping_jiage = []
user_shangping_mingcheng = []
count = 0
while count > 3:
    user_input = input("请输入用户名：")
    user_pass_inupt = input("请输入用户密码：")
    if user_input in user_db.keys() and user_pass_inupt == user_db[user_input] :
        print("登录成功,请您输入您的工资")
        user_gongzi = input("工资：")
        if user_gongzi.isdigit() == False  :
            print("您输入的工资需要是数字形式。请您检查输入是否正确")
        elif user_gongzi.isdigit() == True:
            print('工资总数：%s' %user_gongzi)
        for index, itme in enumerate(shoplist):
            print(index, itme)
        while True:
            user_chicoe = input('请您输入您要选择的商品编号:')
            if user_chicoe == 'q':
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
                shangping_jiage = shoplist[user_chicoe][1] #存用户购买的物品价格。
                shangping_mingcheng = shoplist[user_chicoe][0] #存用户购买的物品名称
            user_shangping_jiage.append(shangping_jiage)
            user_shangping_mingcheng.append(shangping_mingcheng)
            zongjia = 0
            for i in user_shangping_jiage:
                zongjia += i
            print('您购买的商品总价：%s'%zongjia)
            user_shangping_zongshu = set(user_shangping_mingcheng)
            for ii in user_shangping_zongshu:
                mingzi = ii
                geshu = user_shangping_mingcheng.count(ii)
                print('您购买的商品名称：%s 个数 %s' %(mingzi,geshu))
            user_gongzi = int(user_gongzi)
            yue = user_gongzi -zongjia
            print('您的余额还有：%s' %yue)
            if user_gongzi - zongjia == 0 :
                print('购买完成')
                break
            elif user_gongzi -zongjia < 0:
                print('您的余额不足，无法完成支付')
                break
            elif user_gongzi - zongjia > shoplist[1][1]:
                print('您还可以继续购买 所有商品')
            elif user_gongzi - zongjia < shoplist[2][1]:
                print('您的余额不足，无法购买商品')
                break
    else:
        count +=1
        print("登录失败")




