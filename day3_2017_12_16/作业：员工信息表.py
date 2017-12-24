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
1,AlexLi,22,13651054608,IT,2013-04-01
2,熊荣琴,18,13800000000,IT,2017-12-13
3,李树彬,19,13812344321,TI,2011-10-12
4,赵华田,20,12856788765,IT,2009-10-23
5,王罗力,22,13889000987,IT,2010-10-22
6,陈俊民,24,13876543211,it,2011-11-11
使用前请创建一个 staff_table.txt 文件。
'''
#表名称获取
import os
# name = os.listdir("D:\python_oldboby\day3_2017_12_16\staff_table")
# table = name[0]
# print(table)

#表内信息的获取
def staff_table(staff_table):
    list = []
    with open('staff_table.txt','r',encoding='utf-8') as table:
        for i in table:
            list.append(i)
    return list
#staff_table(staff_table)

#print(staff_table(staff_table)[0])




def select(name,age,phonenum,job,time):
    for i in range(0,(len(staff_table(staff_table)))):
        if name in  (staff_table(staff_table)[i]):
            print(staff_table(staff_table)[i])
        if age in  (staff_table(staff_table)[i]):
            print( (staff_table(staff_table)[i]))
        if phonenum in (staff_table(staff_table)[i]):
            print((staff_table(staff_table)[i]))
        if job in  (staff_table(staff_table)[i]):
            print((staff_table(staff_table)[i]))
        if time in  (staff_table(staff_table)[i]):
            print((staff_table(staff_table)[i]))
    return

select('陈俊民','None','None','None','None')


def updata_name(name,newname):
    #获取新的列表
    new_list = []
    for i in staff_table((staff_table)):
        #print(list(i.split(',')))
        new_list.append(list(i.split(',')))
        #print(new_list)
    for ii in range(0,len(new_list)):
        if name in new_list[ii]:
            #print(new_list[ii])
            new_list[ii][1] = newname
            new_lines = ','.join(new_list[ii])
            print(new_list)
    f = open('staff_table.txt','r+',encoding='utf-8')
    for i in new_list:
        lines = ','.join(i)
        f.write(lines)
    f.close()
    return

def updata_age(age,newage):
    #获取新的列表
    new_list = []
    for i in staff_table((staff_table)):
        #print(list(i.split(',')))
        new_list.append(list(i.split(',')))
        #print(new_list)
    for ii in range(0,len(new_list)):
        if age in new_list[ii]:
            #print(new_list[ii])
            new_list[ii][2] = newage
            new_lines = ','.join(new_list[ii])
            print(new_list)
    f = open('staff_table.txt','r+',encoding='utf-8')
    for i in new_list:
        lines = ','.join(i)
        f.write(lines)
    f.close()
    return

def updata_phonenum(phonenum,newphonenum):
    #获取新的列表
    new_list = []
    for i in staff_table((staff_table)):
        #print(list(i.split(',')))
        new_list.append(list(i.split(',')))
        #print(new_list)
    for ii in range(0,len(new_list)):
        if phonenum in new_list[ii]:
            #print(new_list[ii])
            new_list[ii][1] = newphonenum
            new_lines = ','.join(new_list[ii])
            print(new_list)
    f = open('staff_table.txt','r+',encoding='utf-8')
    for i in new_list:
        lines = ','.join(i)
        f.write(lines)
    f.close()
    return

def updata_job(job,newjob):
    #获取新的列表
    new_list = []
    for i in staff_table((staff_table)):
        #print(list(i.split(',')))
        new_list.append(list(i.split(',')))
        #print(new_list)
    for ii in range(0,len(new_list)):
        if job in new_list[ii]:
            #print(new_list[ii])
            new_list[ii][4] = newjob
            new_lines = ','.join(new_list[ii])
            print(new_list)
    f = open('staff_table.txt','r+',encoding='utf-8')
    for i in new_list:
        lines = ','.join(i)
        f.write(lines)
    f.close()
    return

def updata_time(time,newtime):
    #获取新的列表
    new_list = []
    for i in staff_table((staff_table)):
        #print(list(i.split(',')))
        new_list.append(list(i.split(',')))
        #print(new_list)
    for ii in range(0,len(new_list)):
        if time in new_list[ii]:
            #print(new_list[ii])
            new_list[ii][4] = newtime
            new_lines = ','.join(new_list[ii])
            print(new_list)
    f = open('staff_table.txt','r+',encoding='utf-8')
    for i in new_list:
        lines = ','.join(i)
        f.write(lines)
    f.close()
    return

