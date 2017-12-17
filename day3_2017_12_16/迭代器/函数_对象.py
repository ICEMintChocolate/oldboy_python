# -*- coding:utf-8 -*-
# User:fucong
# Time：
'''
函数是第一类对象：值得是函数可以当做数据传递
1.函数可以被引用

'''
# def func(x,y):
#     print(x,y)
# f = func
# f(3,4)


#2 可以当做函数的参数传入
def foo():
    print('aldkjs')

def bar(fu):
    fu()
bar(foo)


#3 可以当做函数的返回值
def foo():
    print('dadfasd')

def bar():
    return foo

f=bar
f()



前：熊荣琴 ，李树彬
后：赵华田，王罗力
左：陈俊民
