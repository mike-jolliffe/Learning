class ChangeBot():
    '''ChangeBot will keep track of how many coins are on hand, returning the fewest
    coins required to give customer exact change'''

    coins_used_dict = {'quarters': 0, 'dimes': 0, 'nickles': 0, 'pennies': 0}
    coin_count = 0

    def __init__(self, register, change):
        self.register = register
        self.change = int(change)

    def coins_back(self, coinage):
        '''Returns the number of quarters and remainder of change due'''
        self.coinage = coinage
        coins_available = [value[0] for (key, value) in register.items() if key == self.coinage]
        coin_value = [value[1] for (key, value) in register.items() if key == self.coinage]

        while self.change > 0:
            if coins_available[0] > 0 and coin_value[0] <= self.change:
                self.change -= coin_value[0]
                self.coins_used_dict[self.coinage] += 1
                self.coin_count += 1
                coins_available[0] -= 1
                self.register[coinage] = coins_available
            else:
                break

    def run(self):
        self.coins_back("quarters")
        self.coins_back("dimes")
        self.coins_back("nickles")
        self.coins_back("pennies")

        if self.change > 0:
            print ("Can't make exact change")

        return f'''The minimum number of coins to make change is {self.coin_count},
        consisting of {self.coins_used_dict["quarters"]} quarters,
                      {self.coins_used_dict["dimes"]} dimes,
                      {self.coins_used_dict["nickles"]} nickles, and
                      {self.coins_used_dict["pennies"]} pennies.'''

if __name__ == "__main__":
    quarters, dimes, nickles, pennies = input("How many quarters, dimes, nickles, and pennies are in the register? ").split(", ")
    register = {'quarters': [int(quarters), 25], 'dimes': [int(dimes), 10],
                'nickles': [int(nickles), 5], 'pennies': [int(pennies), 1]}
    change = input("How much change in total cents is required? ")
    Change_Bot = ChangeBot(register, change)
    print(Change_Bot.run())
