class Creature(object):
    '''Used for creating a creature, giving it stats, and making it fight'''

    def __init__(self, health, weapon, location):
        self.health = health
        self.weapon = weapon
        self.location = location

    def move(self, dir):
        '''Given a direction tuple, updates creature object's location on the board'''
        pass

    def attack(self):
        '''Makes creature object attack Hero object'''
        pass

class Hero(Creature):
    '''Player Character that modifies Creature class'''
    def __init__(self, health, weapon, location, armor, inventory):
        Creature.__init__(self, health, weapon, location)
        self.armor = armor
        self.inventory = inventory

new_hero = Hero(100, "Sword", (1,1), "Mithril", {})
