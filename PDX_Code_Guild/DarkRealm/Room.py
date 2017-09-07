import random
import Creature


class Room(object):
    '''Used to generate a room for moving, fighting, exploring'''
    def __init__(self, size, difficulty):
        self.size = size
        self.difficulty = difficulty
        self.entrance = (0, random.randint(0, self.size[1] - 1))
        self.room_exit = (self.size[0]-1, random.randint(0, self.size[1] - 1))
        self.room = {}

    def build_Room(self, Hero, creatures):
        '''Build a room given instance attributes and Hero/Creature locations'''

        # Build default room tiles
        for tile_x in range(self.size[0]):
            self.room[tile_x] = []
            for tile_y in range(self.size[1]):
                self.room[tile_x].append("   ")

        # Place entrance and exit doors
        self.room[self.entrance[0]][self.entrance[1]] = "___"
        self.room[self.room_exit[0]][self.room_exit[1]] = "___"
        # Place hero
        try:
            self.room[Hero.location[0]][Hero.location[1]] = " X "
        except:
            print("Hero can't move there.")
        # Place bad guys
        for creature in creatures:
            self.room[creature[0]][creature[1]] = " B "

        return self.room

    def seed_Creatures(self):
        '''Taking a room's difficulty, creates a location array of bad guy locations with number of creatures
        depending on room difficulty'''
        num_creatures = self.difficulty

        # Generate a bunch of random locations within the room for placing creatures
        locations_array = []
        for creature in range(num_creatures):
            location = (random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1))
            if not location in locations_array:
                locations_array.append(location)

        # Generate a bunch of Creature objects for placement
        creature_pick_dict = {1: 'ROUS', 2: 'BabyDragon', 3: 'MadBat', 4: 'Mugwump', 5: 'Jabberwocky', 6: 'JellyBlob', 7: 'WelshCorgie'}
        creature_place_dict = {}
        for i in range(num_creatures):
            pick = random.randint(1,8)
            creature_place_dict[locations_array[i]] = Creature.Creature(creature_pick_dict[pick], random.randint(1,8),
                                                                        'XXX', locations_array[i]) #TODO fix weapon

        return creature_place_dict

    def display_Room(self):
        '''Print the room to console for user to interact with'''
        row_num = self.size[0] - 1
        while row_num >= 0:
            row = []
            print("|",end="")
            for index in range(self.size[1]):
                try:
                    # TODO add Items
                    row.append(self.room[row_num][index])
                except:
                    row.append("   ")
            print(' '.join(row),end="")
            print("|")
            row_num -= 1
