from lib import logs
from lib import cash_withdrawal
from lib import shopping
from lib import user_repayment
from lib import transfer_users


def shop():
    print('购物')
    shopping.shops()
    logs.logs(shopping.shops())

def ye():
    print('还款')
    user_repayment.repayment()
    logs.logs(user_repayment.repayment())

def transfer_accounts():
    print('转账')
    transfer_users.transfer()
    logs.logs(transfer_accounts())

def cashs():
    print('提取现金')
    cash_withdrawal.cash()
    logs.logs(cash_withdrawal.cash())

def
def run():
    msg = '''
    1 购物
    2 还款
    3 转账
    4 提取现金
    '''
    while True:
        print(msg)
        user_input = input('>>>:').strip()
        if not user_input:continue
        if user_input == '1':
            shop()
        elif user_input == '2':
            ye()
        elif user_input == '3':
            transfer_accounts()
        elif user_input == '4':
            cashs()