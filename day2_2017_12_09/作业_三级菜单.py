#作业一: 三级菜单
#要求:
# 打印省、市、县三级菜单
# 可返回上一级
# 可随时退出程序

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
    }
}
back_flag = True
quit_flag = True

while back_flag and quit_flag:
    for i in menu:
        print(i)
    city = input('请输入要查找的省份(Q,退出):').strip()
    if city in menu:
        while back_flag and quit_flag:
            for i in menu[city]:
                print(i)
            district = input('请输入要查找的区县(b返回，或Ｑ退出:)').strip()
            if district in menu[city]:
                while back_flag and quit_flag:
                    for i in menu[city][district]:
                        print(i)
                    location = input('请输入要查询的地点(b返回，或Ｑ退出:)').strip()
                    if location in menu[city][district]:
                        while back_flag and quit_flag:
                            for i in menu[city][district][location]:
                                print(i)
                            choice = input('这是最后一页(b返回，或Q退出)')
                            if choice == 'b':
                                back_flag = False
                            elif choice == 'Q':
                                quit_flag = False
                            else:
                                print('输入错误')
                        else:
                           back_flag = True
                    elif location == 'b':
                        back_flag = False
                    elif location == 'Q':
                        quit_flag = False
                    else:
                        print('输入错误!')
                else:
                    back_flag = True
            elif district == 'b':
                back_flag = False
            elif district == 'Q':
                quit_flag = False
            else:
                print('输入错误!')
        else:
            back_flag = True
    elif city == 'Q':
        quit_flag = False
    else:
        print('输入错误!')










