from Room import *

class Creature(object):
    '''Used for creating a creature, giving it stats, and making it fight'''

    def __init__(self, health, weapon, location):
        self.health = health
        self.weapon = weapon
        self.location = location

    def move(self, dir, Room):
        '''Given a direction tuple, updates creature object's location on the board'''
        move_dict = {"N": (1,0), "S": (-1, 0), "E": (0, 1), "W": (0, -1)}
        location_check = []
        if dir in move_dict:
            location_check = tuple(x + y for x, y in zip(self.location, move_dict[dir]))
            if location_check[0] in range(Room.size[0]) and location_check[1] in range(Room.size[1]):
                self.location = tuple(x + y for x, y in zip(self.location, move_dict[dir]))
        return self.location

    def attack(self):
        '''Makes creature object attack Hero object'''
        pass

class Hero(Creature):
    '''Player Character that modifies Creature class'''
    def __init__(self, health, weapon, location, armor, inventory):
        Creature.__init__(self, health, weapon, location)
        self.armor = armor
        self.inventory = inventory

