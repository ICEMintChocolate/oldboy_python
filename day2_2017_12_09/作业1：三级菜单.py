# -*- coding:utf-8 -*-
# User:fucong
# Time：2017-12-10
'''
#作业一: 三级菜单
#要求:
打印省、市、县三级菜单
可返回上一级
可随时退出程序
'''
menu = {
    '北京':{
        '海淀':{
            '五道口':{
                'soho':{},
                '网易':{},
                'google':{}
            },
            '中关村':{
                '爱奇艺':{},
                '汽车之家':{},
                'youku':{},
            },
            '上地':{
                '百度':{},
            },
        },
        '昌平':{
            '沙河':{
                '老男孩':{},
                '北航':{},
            },
            '天通苑':{},
            '回龙观':{},
        },
        '朝阳':{},
        '东城':{},
    },
    '上海':{
        '闵行':{
            "人民广场":{
                '炸鸡店':{}
            }
        },
        '闸北':{
            '火车战':{
                '携程':{}
            }
        },
        '浦东':{},
    },
    '山东':{},
}
# #current_layer = menu
# list = []
# #print(list[0])
# while True:
#     for k in menu:
#         print(k)
#         list.append(k)

#     if user_input in list:

# print(menu['北京'])
#
# print(menu['北京']['海淀'])
# print(menu['北京']['海淀']['五道口'])
while True:
    for k in menu:
        print(k)
    user_input_1 = input("请跟根据提示输入1：")
    if user_input_1 == 'q' :break
    if user_input_1 in menu:
        for i in menu[user_input_1]:
            print(i)
        user_input_2 = input("请跟根据提示输入2：")
        if user_input_2 == 'b':
            continue
        elif user_input_2 == 'q':
            break
        if user_input_2 in menu[user_input_1]:
            for ii in menu[user_input_1][user_input_2]:
                print(ii)
            user_input_3 = input("请跟根据提示输入3：")
            if user_input_2 == 'b':
                continue
            elif user_input_2 == 'q':
                break
            if user_input_3 in menu[user_input_1][user_input_2]:
                for iii in  menu[user_input_1][user_input_2][user_input_3]:
                    print(iii)


