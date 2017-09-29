from account import Account
from collections import OrderedDict
import json

class ATM:
    def __init__(self, accounts):
        '''Takes an Account object on instantiation'''
        self.accounts = accounts
        self.account = None
        self.actions = ['Check Balance', 'Deposit Funds', 'Withdraw Funds', 'Exit']
        self.accounts_dict = {}

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
        elif action[0] == 4:
            self.update_accounts()
            self.to_dict()
            with open('accounts.json', 'w') as fp:
                json.dump(self.accounts_dict, fp)
            exit("Have a nice day!")

    def update_accounts(self):
        '''Updates accounts object by modifying user's account to reflect changes'''
        for unmodified in self.accounts:
            if unmodified.account_number == self.account.account_number:
                unmodified = self.account

    def to_dict(self):
        '''Returns a json-serialization-ready dictionary where values are account objects'''
        for i, j in enumerate(self.accounts):
            #TODO implement pickle rather than saving as JSON file
            self.accounts_dict[i] = j.__dict__

if __name__ == '__main__':
    try:
        with open('accounts.json', 'r') as fp:
            accounts = json.load(fp)
        # Grab just the account objects
        atm = ATM([value for key, value in accounts.items()])

    except:
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
