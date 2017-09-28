from account import Account
from collections import OrderedDict

class ATM:
    def __init__(self, accounts):
        '''Takes an Account object on instantiation'''
        self.accounts = accounts
        self.account = None
        self.actions = ['Check Balance', 'Deposit Funds', 'Withdraw Funds']

    def get_account(self, account_num):
        '''Sets the account number of user's account'''
        for account in self.accounts:
            if account.account_number == account_num:
                self.account = account

    def menu(self):
        for i, action in enumerate(self.actions):
            print(f"{i+1} -- {action}")

    def act(self, *action):
        act_dict = OrderedDict([
            (self.actions[0], self.account.get_funds),
            (self.actions[1], self.account.deposit),
            (self.actions[2], self.account.withdraw)
        ])

        if action[0] == 1:
            return act_dict['Check Balance']()
        elif action[0] == 2:
            return act_dict['Deposit Funds'](action[1])
        elif action[0] == 3:
            return act_dict['Withdraw Funds'](action[1])

if __name__=='__main__':
    account1 = Account()
    account2 = Account()
    account3 = Account()
    atm = ATM([account1, account2, account3])

    while True:
        print()
        account = int(input("Account Number: "))
        atm.get_account(account)
        atm.menu()
        print()
        action = int(input("Pick a number: "))
        if action == 2 or action == 3:
            amount = int(input("How much: "))
            print(atm.act(action, amount))
        else:
            print(atm.act(action))
