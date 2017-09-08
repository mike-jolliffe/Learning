from Room import *

class Creature(object):
    '''Used for creating a creature, giving it stats, and making it fight'''

    def __init__(self, name, health, weapon, location):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.location = location

    def move(self, dir, Room):
        '''Given a direction tuple, updates creature object's location on the board'''
        move_dict = {"n": (1,0), "s": (-1, 0), "e": (0, 1), "w": (0, -1)}
        location_check = []
        if dir in move_dict:
            location_check = tuple(x + y for x, y in zip(self.location, move_dict[dir]))
            if location_check[0] in range(Room.size[0]) and location_check[1] in range(Room.size[1]):
                self.location = tuple(x + y for x, y in zip(self.location, move_dict[dir]))
        return self.location


class Hero(Creature):
    '''Player Character that modifies Creature class'''
    def __init__(self, name, health, weapon, location, armor, inventory):
        Creature.__init__(self, name, health, weapon, location)
        self.armor = armor
        self.inventory = inventory

    def attacked(self, creature):
        '''Makes creature object attack Hero object'''
        damage = random.choice([0, 1, 1, 1, 1, 2, 3, 4])
        print(
            f"The {creature.name} attacks {self.name}, causing {damage} damage.")
        self.health -= damage

    def fight(self, creature):
        print(f"You've encountered a {creature.name}!!")
        print(f'''-------- {creature.name.upper()} STATS --------
                Health: {creature.health}
                Weapon: {creature.weapon.description} 
                Damage: {creature.weapon.damage}''')

        while creature.health > 0 and self.health > 0:
            attack = input("1 -- Stab \n"
                           "2 -- Slash \n"
                           "3 -- Run Away ")

            if attack == '3':
                print("You escaped!")
                break
            elif attack == '1':
                points = random.choice([2,2,2,3,3,4])
                creature.health -= points
                print(f"Your attack did {points} damage!")
            elif attack == '2':
                points = random.choice([0,0,0,5,5,8])
                creature.health -= points
                print(f"Your attack did {points} damage!")
            self.attacked(creature)

        if creature.health <= 0:
            print(f"You've defeated the vicious {creature.name}")
            # Defeat is True, so creature will be removed from board
            return True
        elif hero.health <= 0:
            print(f"{self.name} has perished in the Dark Realm!")
            exit()
        else:
            # Defeat is False, creature will remain
            return False
    def get_inventory(self):
        '''Returns the hero's current inventory'''
        print(f"Your Current Inventory:")
        inventory = []
        for item in self.inventory:
            inventory.append(f"{item}: {self.inventory[item]}")
        return inventory