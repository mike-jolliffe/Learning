import random
import Creature

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
        result = random.randint(1, self.strength)
        # If that integer is above the 90%ile of strength
        if result > round(0.9 * self.strength):
            # Weapon breaks
            return True
        else:
            return False

    def weapon_randomizer(self):
        '''Returns a dictionary for selecting random weapons'''
        baddie_weapons = {1: Weapon('fangs', (0,0), 5, 8),
                          2: Weapon('electric shock', (0,0), 2, 2),
                          3: Weapon('clobber', (0,0), 3, 2),
                          4: Weapon('talk-ya-ear-off', (0,0), 4, 2),
                          5: Weapon('the-lazy-eye', (0,0), 1, 2)}

        hero_weapons = {}

        pick = random.randint(1, len(baddie_weapons))
        return baddie_weapons[pick]