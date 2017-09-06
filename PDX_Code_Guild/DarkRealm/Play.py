from Creature import *
from Item import *
import random
from Room import *

if __name__ == '__main__':
    print()
    print("YOU'VE ENTERED THE DARK REALM")
    print()
    print(

        f'''        The hero must navigate 
        the Dark Realm's myriad dungeons, 
        battling monsters of every ilk, 
        on a mission to gain the Chalice 
        of Object Oriented Programming wisdom!!''')
    print()

    name = input(("PICK A NAME FOR YOUR HERO: "))

    print(f"Welcome, {name}! Steel thy nerves for you are about to encounter some terrifying monsters!!!")


    while True:
        room1 = Room((random.randint(4,15), random.randint(3,15)), 2)
        hero = Hero(100, "Sword", room1.entrance, "Mithril", {})
        baddies = room1.seed_Creatures()
        while True:
            room1.build_Room(hero, baddies)
            room1.display_Room()
            dir = input(f"Which direction would you like {name} to move? (n)orth, (s)outh, (e)ast, or (w)est? ")
            if dir == "Q":
                exit()
            elif dir == "1":
                print(f"Health: {hero.health}\n"
                      f"Weapons: {hero.weapon}\n"
                      f"Armor: {hero.armor}\n"
                      f"Inventory: {hero.inventory}")
                continue
            hero.move(dir, room1)
            if hero.location == room1.room_exit:
                break
            elif hero.location in baddies:
                print("FIGHT!!!")
                # TODO build a fight function (class?) that can be called
                exit()
