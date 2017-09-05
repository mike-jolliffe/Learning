from Creature import *
from Item import *
import random
from Room import *

if __name__ == '__main__':
    while True:
        room1 = Room((random.randint(4,20), random.randint(3,20)), "easy")
        mike = Hero(100, "Sword", room1.entrance, "Mithril", {})
        while True:
            room1.build_Room(mike)
            room1.display_Room()
            dir = input("Which direction would you like to move? ")
            if dir == "Q":
                exit()
            mike.move(dir, room1)
            print(mike.location)
            if mike.location == room1.room_exit:
                break
