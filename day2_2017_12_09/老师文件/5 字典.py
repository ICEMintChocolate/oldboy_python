#用途：存放多个值，key:value,存取速度快

#定义：key必须是不可变类型（int，float，str，tuple），value可以是任意类型
# info={'name':'egon','age':18,'sex':'male'} #info=dict({'name':'egon','age':18,'sex':'male'})

#了解
# info=dict(age=18,sex='male',name='egon')
# print(info)

# info=dict([('name','egon'),('age',18),('sex','male')])
# info=dict([['name','egon'],['age',18],['sex','male']])
# print(info)

# info={}.fromkeys(['name','age','sex'],None)
# info={}.fromkeys('hello',None)
# print(info)

#优先掌握的操作：
#1、按key存取值：可存可取
# d={'name':'egon'}
# print(d['name'])
#
# d['age']=18
# print(d)

#2、长度len
# info={'name':'egon','age':18,'sex':'male'}
# print(len(info))

#3、成员运算in和not in
# info={'name':'egon','age':18,'sex':'male'}
# print('name' in info)

#4、删除
info={'name':'egon','age':18,'sex':'male'}
# print(info.pop('name'))
# print(info)
# print(info.popitem()) #('sex', 'male')
# print(info)

#5、键keys()，值values()，键值对items() #了解
# print(info.keys())
# print(list(info.keys())[0])

# print(list(info.values()))
print(list(info.items()))

#6、循环
# info={'name':'egon','age':18,'sex':'male'}
# for k in info:
#     print(k,info[k])






