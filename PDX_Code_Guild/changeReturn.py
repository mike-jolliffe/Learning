class ChangeBot():
    '''ChangeBot will keep track of how many coins are on hand, returning the fewest
    coins required to give customer exact change'''

    coins_used = 0

    def __init__(self, register, change):
        self.register = register
        self.change = int(change)

    def coins_back(self, coinage):
        '''Returns the number of quarters and remainder of change due'''
        self.coinage = coinage
        coins_available = [value[0] for (key, value) in register.items() if key == self.coinage]
        coin_value = [value[1] for (key, value) in register.items() if key == self.coinage]

        while self.change > 0:
            if coins_available[0] > 0:
                self.change -= coin_value[0]
                self.coins_used += 1
                self.register[coinage] = coins_available
            else:
                break

    def run(self):
        self.coins_back("quarters")
        self.coins_back("dimes")
        self.coins_back("nickles")
        self.coins_back("pennies")
        return self.coins_used

if __name__ == "__main__":
    quarters, dimes, nickles, pennies = input("How many quarters, dimes, nickles, and pennies are in the register? ").split(", ")
    register = {'quarters': [int(quarters), 25], 'dimes': [int(dimes), 10],
                'nickles': [int(nickles), 5], 'pennies': [int(pennies), 1]}
    change = input("How much change in total cents is required? ")
    Change_Bot = ChangeBot(register, change)
    print(Change_Bot.run())


# Write a python script that figures out how to divvy up an amount of change into
# the _fewest_ quarters, dimes, nickels, and pennies.
#
#
# *   Calculate the number of quarters necessary first.
#
# *   Then calculate the number of dimes, nickels, and pennies.
#     If you do it in that order, you will minimize the number of coins.
#
# This is easiest done by updating a _running total_ of number of cents left to be put into coins.
#
# Also remember that the `//` operator divides and removes any remainder.
#
# * Expand this problem to work on an amount of cents greater than 100 and include bills.
# * Print out the total number of coins and bills dispensed.
#
# * Store how many of each coin is in the cash register, then allow the change
# algorithm to deal with when you don't have enough coins to optimally give change.
