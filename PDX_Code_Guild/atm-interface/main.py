from account import Account
from collections import OrderedDict

class ATM:
    def __init__(self, accounts):
        '''Takes an Account object on instantiation'''
        self.accounts = accounts
        self.account = None
        self.actions = OrderedDict([
                        ('Check Balance', self.account.get_funds),
                        ('Deposit Funds', self.account.deposit),
                        ('Withdraw Funds', self.account.withdraw)
        ])

    def get_account(self, account_num):
        '''Sets the account number of user's account'''
        for account in self.accounts:
            if account.account_number == account_num:
                self.account = account

    def menu(self):
        for i, action in enumerate(self.actions):
            print(f"{i+1} -- {action}")

    def act(self, *action):
        if action[0] == 1:
            return self.actions['Check Balance']()
        elif action[0] == 2:
            return self.actions['Deposit Funds'](action[1])
        elif action[0] == 3:
            return self.actions['Withdraw Funds'](action[1])

if __name__=='__main__':
    account1 = Account()
    account2 = Account()
    account3 = Account()
    print(account2.get_account_number())
    exit()
    atm = ATM([account1, account2, account3])

    while True:
        print()
        atm.menu()
        print()
        action = int(input("Pick a number: "))
        if action == 2 or action == 3:
            amount = int(input("How much: "))
            print(atm.act(action, amount))
        else:
            print(atm.act(action))
