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

    room_count = 0

    while room_count < 3:
        room1 = Room((random.randint(4,15), random.randint(3,15)), 2)
        room_count += 1
        hero = Hero(name, 100, "Sword", room1.entrance, "Mithril", {})
        baddie_locs = room1.generate_Creature_locs()
        creature_lookup = room1.make_Creatures(baddie_locs)
        while True:
            room1.build_Room(hero, baddie_locs)
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
            elif hero.location in baddie_locs:
                print()
                ("FIGHT!!!")
                result = hero.fight(creature_lookup[hero.location])
                if result:
                    # Eliminate the creature from the room
                    baddie_locs.remove(hero.location)

    print("You've entered the boss room!!!")
    #TODO create a boss room after hero gets through the first x rooms