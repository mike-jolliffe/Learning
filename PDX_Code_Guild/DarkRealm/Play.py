from Creature import *
from Item import *
import random
from Room import *
import subprocess as sp

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
            dir = input(f"Which direction would you like {name} to move? (n)orth, (s)outh, (e)ast, or (w)est?\n"
                        f"You may also press (1) for a status check or (q) to quit ")
            if dir == "q":
                exit()
            elif dir == "1":
                sp.call('clear', shell=True)
                print(f"Health: {hero.health}\n"
                      f"Weapons: {hero.weapon}\n"
                      f"Armor: {hero.armor}\n"
                      f"Inventory: {hero.inventory}")
                pause = input("Press y to continue or any other key to exit: ")
                if pause == 'y':
                    continue
                else:
                    exit()
            # Clear screen in terminal so only one room map is showing
            sp.call('clear', shell=True)
            hero.move(dir, room1)
            if hero.location == room1.room_exit:
                break
            elif hero.location in baddies:
                print()
                print("FIGHT!!!")
                # TODO build a fight function (class?) that can be called
                exit()
