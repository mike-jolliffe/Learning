import random
import Creature
import Item


class Room(object):
    '''Used to generate a room for moving, fighting, exploring'''
    def __init__(self, size, difficulty):
        self.size = size
        self.difficulty = difficulty
        self.entrance = (0, random.randint(0, self.size[1] - 1))
        self.room_exit = (self.size[0]-1, random.randint(0, self.size[1] - 1))
        self.room = {}
        self.creature_dict = {'ROUS': Creature.Creature('ROUS', 8, Item.Weapon('fangs', (0,0), 5, 8), (0,0)),
                              'BabyDragon': Creature.Creature('BabyDragon', 6, Item.Weapon('fangs', (0,0), 5, 8), (0,0)),
                              'MadBat': Creature.Creature('MadBat', 3, Item.Weapon('electric shock', (0,0), 2, 2), (0,0)),
                              'Mugwump': Creature.Creature('Mugwump', 4, Item.Weapon('clobber', (0,0), 3, 2), (0,0)),
                              'Jabberwocky': Creature.Creature('Jabberwocky', 6, Item.Weapon('talk-ya-ear-off', (0,0), 4, 2), (0,0)),
                              'JellyBlob': Creature.Creature('JellyBlob', 5, Item.Weapon('wiggles', (0,0), 1, 2), (0,0)),
                              'WelshCorgie': Creature.Creature('WelshCorgie', 12, Item.Weapon('the-lazy-eye', (0,0), 3, 2), (0,0))
                            }

        self.item_dict = {'+1_Potion': Item.Item('+1_Potion', (0,0), -1),
                          'Journal_Page': Item.Item('Journal_Page', (0,0), 0),
                          'Broadsword': Item.Weapon('Broadsword', (0,0), 8, 50)} # TODO, hook up weapon damage to fight()

    def build_Room(self, Hero, creatures, item):
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
            # Don't place bad guys over doorways or heros
            if not (self.room[creature[0]][creature[1]] == "__" or self.room[creature[0]][creature[1]] == " X "):
                self.room[creature[0]][creature[1]] = " B "
        # Place item
        if (self.item_placed == True and self.item_dict[item].location == None): # TODO figure out how to remove an item the hero grabbed
            pass
        elif self.item_placed == True:
            # if the item is already placed within a room, just use its current location
            self.room[self.item_dict[item].location[0]][self.item_dict[item].location[1]] = " ? "
        else:
            # Otherwise, get open locations
            open_locs = []
            for x in self.room:
                for y in range(len(self.room[x])):
                    if self.room[x][y] == '   ':
                        open_locs.append((x, y))
            # Place item at a random open location within the room
            self.item_dict[item].location = random.choice(open_locs)
            item_loc = self.item_dict[item].location
            self.room[item_loc[0]][item_loc[1]] = " ? "
            # Modify item_placed status to True for the room
            self.item_placed = True

        return self.room

    def generate_Creature_locs(self):
        '''Taking a room's difficulty, creates a location array of bad guy locations with number of creatures
        depending on room difficulty'''
        num_creatures = self.difficulty

        # Generate a bunch of random locations within the room for placing creatures
        locations_array = []
        for creature in range(num_creatures):
            location = (random.randint(0, self.size[0] - 1), random.randint(0, self.size[1] - 1))
            if not location in locations_array:
                locations_array.append(location)

        return locations_array


    def make_Creatures(self, locations):
        '''Populates a dictionary of Creature objects with updated location attributes'''
        # Generate a bunch of Creature objects for placement
        creature_pick_dict = {1: 'ROUS', 2: 'BabyDragon', 3: 'MadBat', 4: 'Mugwump', 5: 'Jabberwocky', 6: 'JellyBlob',
                              7: 'WelshCorgie'}
        creature_place_dict = {}
        for i in range(len(locations)):
            pick = random.randint(1, 7)
            # Pick a random creature
            creature_to_place = self.creature_dict[creature_pick_dict[pick]]
            creature_to_place.location = locations[i]

            creature_place_dict[locations[i]] = creature_to_place # TODO fix weapon default location of (0,0)

        return creature_place_dict

    def generate_Item(self):
        '''Randomizes and updates the location of items'''
        item_dict = {1:'+1_Potion', 2: 'Journal_Page', 3:'Broadsword'}
        item = item_dict[random.choice([1,1,1,1,1,1,1,1,2,2,2,2,3])]
        return item

    def display_Room(self):
        '''Print the room to console for user to interact with'''
        row_num = self.size[0] - 1
        while row_num >= 0:
            row = []
            print("|",end="")
            for index in range(self.size[1]):
                try:
                    row.append(self.room[row_num][index])
                except:
                    row.append("   ")
            print(' '.join(row),end="")
            print("|")
            row_num -= 1
