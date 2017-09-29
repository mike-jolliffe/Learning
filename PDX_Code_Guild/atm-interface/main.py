from account import Account
from collections import OrderedDict
import pickle

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
            self.pickler()
            exit("Have a nice day!")

    def update_accounts(self):
        '''Updates accounts object by modifying user's account to reflect changes'''
        for unmodified in self.accounts:
            if unmodified.account_number == self.account.account_number:
                unmodified = self.account

    def pickler(self):
        '''Pickles an object'''
        output = open('accounts_pickle', 'wb')
        pickle.dump(self.accounts, output)
        output.close()

if __name__ == '__main__':
    try:
        with open('accounts_pickle', 'rb') as fp:
            accounts = pickle.load(fp)

        # Grab just the account objects
        atm = ATM(accounts)

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
