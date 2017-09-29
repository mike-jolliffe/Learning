'''
Adds some advanced features to the account class.

*   Save the account balance to a file after each operation.
    Read that balance on startup so the balance persists across program starts.

*   Allow the user to open more than one account.
    Let them perform all of the above operations by account number.'''

class Account:

    account_number = 1

    def __init__(self):
        self.account_number = Account.account_number
        self.__balance = 0
        self.__interest = 0.001
        self.fee = 0

        Account.account_number += 1

    def get_account_number(self):
        '''Returns the account number'''
        return self.account_number

    def get_funds(self):
        '''Returns account balance'''
        return self.__balance

    def deposit(self, amount):
        '''Updates balance by adding amount minus fee'''
        self.fee_charge()
        self.__balance += (amount - self.fee)
        return self.__balance

    def check_withdrawal(self, amount):
        '''Returns True if balance greater than or equal to amount plus any fee'''
        self.fee_charge()
        return True if self.__balance >= (amount + self.fee) else False

    def withdraw(self, amount):
        '''Withdraws an allowed amount, ValueError if insufficient balance'''
        self.fee_charge()
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            return ValueError(f"Insufficient funds available. Currently ${self.__balance} in account")

    def calc_interest(self):
        '''Calculates and returns total interest on loan balance'''
        return self.__balance * self.__interest

    def get_standing(self):
        '''Returns True if account balance is below $1000'''
        return True if self.__balance < 1000 else False

    def fee_charge(self):
        '''Creates a fee charge if get standing returned True'''
        if self.get_standing():
            self.fee = 10
        else:
            self.fee = 0




if __name__ == '__main__':
    account1 = Account()
    account1.deposit(500)
    print(account1.get_funds())
    print(account1.check_withdrawal(400))
    print(account1.calc_interest())
    print(account1.withdraw(400))
    print(account1.withdraw(400))
