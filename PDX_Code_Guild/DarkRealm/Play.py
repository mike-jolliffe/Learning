from Creature import *
from Item import *
from Room import *

if __name__ == '__main__':
    room1 = Room((7, 3), "easy")
    mike = Hero(100, "Sword", room1.entrance, "Mithril", {})
    while True:
        room1.build_Room(mike)
        room1.display_Room()
        dir = input("Which direction would you like to move? ")
        if dir == "Q":
            exit()
        mike.move(dir, room1)
        print(mike.location)
