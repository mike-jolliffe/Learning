import random

class Room(object):
    '''Used to generate a room for moving, fighting, exploring'''
    def __init__(self, size, difficulty):
        self.size = size
        self.difficulty = difficulty
        self.entrance = (0, random.randint(0, self.size[1] - 1))
        self.room_exit = (self.size[0]-1, random.randint(0, self.size[1] - 1))
        self.room = {}

    def build_Room(self):
        '''Build a room given instance attributes and Hero/Creature locations'''

        # Build default room tiles
        for tile_x in range(self.size[0]):
            self.room[tile_x] = []
            for tile_y in range(self.size[1]):
                self.room[tile_x].append("   ")

        # Place entrance and exit doors
        self.room[self.entrance[0]][self.entrance[1]] = "___"
        self.room[self.room_exit[0]][self.room_exit[1]] = "___"

        return self.room

    def display_Room(self):
        row_num = self.size[0] - 1
        while row_num >= 0:
            row = []
            print("|",end="")
            for index in range(self.size[1]):
                try:
                    # TODO fix this for placing Hero, Creatures, Items
                    row.append(self.room[row_num][index])
                except:
                    row.append("   ")
            print(' '.join(row),end="")
            print("|")
            row_num -= 1

new_room = Room((9,9), "hard")
new_room.build_Room()
new_room.display_Room()