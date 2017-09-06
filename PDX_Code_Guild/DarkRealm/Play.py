from Creature import *
from Item import *
import random
from Room import *

if __name__ == '__main__':
    print("YOU'VE ENTERED THE DARK REALM")
    name = input(("PICK A NAME FOR YOUR HERO: "))
    while True:
        room1 = Room((random.randint(4,20), random.randint(3,20)), 2)
        hero = Hero(100, "Sword", room1.entrance, "Mithril", {})
        baddies = room1.seed_Creatures()
        while True:
            room1.build_Room(hero, baddies)
            room1.display_Room()
            dir = input(f"Which direction would you like {name} to move? (n)orth, (s)outh, (e)ast, or (w)est? ")
            if dir == "Q":
                exit()
            hero.move(dir, room1)
            if hero.location == room1.room_exit:
                break
            elif hero.location in baddies:
                print("FIGHT!!!")
                # TODO build a fight function (class?) that can be called
                exit()
