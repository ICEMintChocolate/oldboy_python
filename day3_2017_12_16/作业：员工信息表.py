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


熊荣琴 ，李树彬
赵华田，王罗力
陈俊民

'''
mylist = [1,2,2,2,2,3,3,3,4,4,4,4]
my = set(mylist)
for i in my:
    print(i)
    print(mylist.count(i))