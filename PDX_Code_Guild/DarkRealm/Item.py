import random

class Item(object):
    '''Used to create an item, describe it, and make it do things'''
    def __init__(self, description, location, damage):
        self.description = description
        self.location = location
        self.damage = damage

class Weapon(Item):
    '''Modifies Item to create a weapon and give it specific methods'''
    def __init__(self, description, location, damage, strength):
        Item.__init__(self, description, location, damage)
        self.strength = strength

    def break_weapon(self):
        '''Given strength, tests weapon for breakage after each use'''
        # Generate random integer between 1 and weapon strength
        result = random.randint(self.strength)
        # If that integer is above the 90%ile of strength
        if result > round(0.9 * self.strength):
            # Weapon breaks
            return True
        else:
            return False