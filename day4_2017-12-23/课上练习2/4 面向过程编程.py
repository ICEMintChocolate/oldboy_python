#grep -rl 'python' /etc
#补充：os.walk
# import os
# g=os.walk(r'D:\video\python20期\day4\a')
# # print(next(g))
# # print(next(g))
# # print(next(g))
# # print(next(g))
# for pardir,_,files in g:
#     for file in files:
#         abs_path=r'%s\\%s' %(pardir,file)
#         print(abs_path)




#分析一：


# #第一步：拿到一个文件夹下所有的文件的绝对路径
# import os
#
# def search(target): #r'D:\video\python20期\day4\a'
#     while True:
#         filepath=yield #fllepath=yield=r'D:\video\python20期\day4\a'
#         g=os.walk(filepath)
#         for pardir, _, files in g:
#             for file in files:
#                 abs_path = r'%s\%s' % (pardir, file)
#                 # print(abs_path)
#                 target.send(abs_path)
#
# # search(r'D:\video\python20期\day4\a')
# # search(r'D:\video\python20期\day4')
#
#
# #第二步：打开文件拿到文件对象f
# def opener():
#     while True:
#         abs_path=yield
#         print('opener func--->',abs_path)
#
#
# target=opener()
# next(target) #target.send('xxxx')
#
# g=search(target)
# next(g)
# g.send(r'D:\video\python20期\day4\a')




#分析二：
# 第一步：拿到一个文件夹下所有的文件的绝对路径
import os
def init(func):
    def inner(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return inner


@init
def search(target):  # r'D:\video\python20期\day4\a'
    while True:
        filepath = yield
        g = os.walk(filepath)
        for pardir, _, files in g:
            for file in files:
                abs_path = r'%s\%s' % (pardir, file)
                #把abs_path传给下一个阶段
                target.send(abs_path)

# 第二步：打开文件拿到文件对象f
@init
def opener(target):
    while True:
        abs_path = yield
        with open(abs_path,'rb') as f:
            #把(abs_path,f)传给下一个阶段
            target.send((abs_path,f))

#第三步：读取f的每一行内容
@init
def cat(target):
    while True:
        abs_path,f=yield
        for line in f:
            #把(abs_path,line)传给下一个阶段
            target.send((abs_path,line))

#第四步：判断'python' in line
@init
def grep(target,pattern):
    pattern = pattern.encode('utf-8')
    while True:
        abs_path,line=yield
        if pattern in line:
            #把abs_path传给下一个阶段
            target.send(abs_path)

#第五步：打印文件路径
@init
def printer():
    while True:
        abs_path=yield
        print('<%s>' %abs_path)

g=search(opener(cat(grep(printer(),'python')))) #'python' in b'xxxxx'
g.send(r'D:\video\python20期\day4\a')


















