'''

Write a program that functions as a simple ATM for two accounts:

1. Checking account
1. Savings account

Implement a user interface in a module `main` that lets a user pick each of those actions for a given account and updates
the account. After each action it will print the balance.

Adds some advanced features to the account class.

*   Add a function called `get_standing()` have it return a bool with whether the account has less than $1000 in it.

*   Predatorily charge a transaction fee every time a withdrawal or deposit happens if the account is in bad standing.

*   Save the account balance to a file after each operation.
    Read that balance on startup so the balance persists across program starts.

*   Add to each account class an account ID number.

*   Allow the user to open more than one account.
    Let them perform all of the above operations by account number.'''

class Account:

    account_number = 1

    def __init__(self):
        self.account_number = Account.account_number
        self.__balance = 0
        self.__interest = 0.001

        Account.account_number += 1

    def get_account_number(self):
        '''Returns the account number'''
        return self.account_number

    def get_funds(self):
        '''Returns account balance'''
        return self.__balance

    def deposit(self, amount):
        '''Updates balance by adding amount'''
        self.__balance += amount
        return self.__balance

    def check_withdrawal(self, amount):
        '''Returns True if balance greater than or equal to amount'''
        return True if self.__balance >= amount else False

    def withdraw(self, amount):
        '''Withdraws an allowed amount, ValueError if insufficient balance'''
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            return ValueError(f"Insufficient funds available. Currently ${self.__balance} in account")

    def calc_interest(self):
        '''Calculates and returns total interest on loan balance'''
        return self.__balance * self.__interest

if __name__ == '__main__':
    account1 = Account()
    account1.deposit(500)
    print(account1.get_funds())
    print(account1.check_withdrawal(400))
    print(account1.calc_interest())
    print(account1.withdraw(400))
    print(account1.withdraw(400))
