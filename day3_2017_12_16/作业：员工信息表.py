# -*- coding:utf-8 -*-
# User:fucong
# Time：2017-12-17
'''
可进行模糊查询，语法至少支持下面3种:
    select name,age from staff_table where age > 22
    select  * from staff_table where dept = "IT"
    select  * from staff_table where enroll_date like "2013"
可修改员工信息，语法如下:
　　UPDATE staff_table SET dept="Market" WHERE where dept = "IT"

用户列表示例
1,Alex Li,22,13651054608,IT,2013-04-01
2,熊荣琴,18,13800000000,IT,2017-12-13
3,李树彬,19,13812344321,TI,2011-10-12
4,赵华田,20,12856788765,IT,2009-10-23
5,王罗力,22,13889000987,IT,2010-10-22
6,陈俊民,24,13876543211,it,2011-11-11
'''
#表名称获取
import os
# name = os.listdir("D:\python_oldboby\day3_2017_12_16\staff_table")
# table = name[0]
# print(table)

#表内信息的获取
def staff_table(staff_table):
    list = []
    with open('staff_table.txt','r+') as table:
        for i in table:
            list.append(i)
        print(list)
#print(staff_table)
staff_table(staff_table)



def select(name,age):



def update():
    pass