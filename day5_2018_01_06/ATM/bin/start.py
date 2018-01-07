# -*- coding:utf-8 -*-
# User:fucong
# Time：
'''
作业需求：

模拟实现一个ATM + 购物商城程序
4 每月22号出账单，每月10号为还款日，过期未还，按欠款总额 万分之5 每日计
10 提供管理接口，包括添加账户、用户额度，冻结账户等。。。

'''
import sys,os
BAES_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BAES_DIR)

from core import src

if __name__ == '__main__':
    src.run()