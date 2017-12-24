# -*- coding:utf-8 -*-
# User:fucong
# Time：
import os
def filepath(tag):
    while True:
        lujing = yield
        paths = os.walk(lujing)
        for dir,_,filename in paths:
            for fi in filename:
                abc = '%s\%s'%(dir,fi)
                tag.send(abc)
g = filepath()
next(g)
g.send(r'D:\python_oldboby\day4_2017-12-23')

def opener():
    while True:
        abc_path = yield
        print('=======>',abc_path)

