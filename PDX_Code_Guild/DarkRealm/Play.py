from Creature import *
from Item import *
import random
import Room
import subprocess as sp
import time

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
    hero = Hero(name, 100, "Sword", (0,0), "Mithril", {})

    while room_count < 3:
        room1 = Room.Room((random.randint(4,15), random.randint(3,15)), 2)
        room_count += 1
        hero.location = room1.entrance
        baddie_locs = room1.generate_Creature_locs()
        creature_lookup = room1.make_Creatures(baddie_locs)
        item = room1.generate_Item()
        room1.item_placed = False
        while True:
            room1.build_Room(hero, baddie_locs, item)
            room1.display_Room()
            dir = input(f"Which direction would you like {name} to move? (n)orth, (s)outh, (e)ast, or (w)est?\n"
                        f"You may also press (1) for a status check or (q) to quit ")
            if dir == "q":
                exit()
            elif dir == "1":
                sp.call('clear', shell=True)
                [print(item) for item in hero.get_inventory()]
                print()
                print(
                      f"Health: {hero.health}\n"
                      f"Weapons: {hero.weapon}\n"
                      f"Armor: {hero.armor}\n"
                      )
                pause = input("Type the first letter of an item to use it. Press y to leave menu or any other key to quit the game: ")
                if pause == 'y':
                    continue
                elif pause == '+':
                    try:
                        hero.use_item('+1_Potion', room_count)
                    except:
                        print(f"You don't currently have any +1_Potion in your inventory.")
                elif pause == 'B' or pause == 'b':
                    try:
                        hero.use_item('Broadsword', room_count)
                    except:
                        print(f"you don't currently have a Broadsword in your inventory.")
                elif pause == 'J' or pause == 'j':
                    try:
                        sp.call('clear', shell=True)
                        hero.use_item('Journal_Page', room_count)
                        time.sleep(8)
                    except:
                        print(f"you don't have any journal pages in your inventory.")

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
            elif hero.location == room1.item_dict[item].location:
                print(f"You found a {item}!!!")
                if not item in hero.inventory:
                    hero.inventory[room1.item_dict[item].description] = 1
                else:
                    hero.inventory[room1.item_dict[item].description] += 1
                # Remove item from room
                room1.item_dict[item].location = None

    print("You've escaped the Dark Realm!!!")
