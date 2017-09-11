'''## Advanced
* Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.
* When the user enters a city and a number of hops, print out the shortest travel times to each city.
Paths with fewer hops are not necessarily those with the shorter travel times.'''

class CityHopper:
    '''Allows user to check shortest routes and potential cities based on a starting city
    and number of connecting hops.'''

    city_dict = {
        'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
        'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
        'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
        'Portland': {'Boston': 3, 'Albany': 7},
        'Philadelphia': {'New York': 9}
    }

    def __init__(self):
        # Holder for starting city
        self.start_city = None
        # Holder for number of hops
        self.num_hops = None
        # Holder for all cities falling within number of hops
        self.hoppable = []

    def get_input(self):
        '''Gets starting city and number of hops from user, stores them as instance attributes'''
        for key in CityHopper.city_dict:
            print(f"- {key}")
        self.start_city = input(f"Please enter your starting city: ")
        self.num_hops = int(input(f"How many hops can you take? "))
        return self.start_city, self.num_hops

    def can_hop(self, start_city, num_hops):
        '''Given a starting city and number of hops, returns hops left, and city-pairs that can be hopped from starting
        city'''
        if num_hops == 0:
            return self.hoppable
        else:
            for city in CityHopper.city_dict[start_city].keys():
                self.hoppable.append((num_hops, start_city, city, CityHopper.city_dict[start_city][city]))
                self.can_hop(city, num_hops-1)
            return self.hoppable

    def hop_times(self, city_list):
        '''Builds dictionary of travel times, with hop number as key. Returns the dict and
        a set of all possible destinations falling within that number of hops'''

        # Build set of all possible destinations
        all_dest = set([city[2] for city in city_list])

        # Build travel times dictionary tied to hop number
        hop_time_dict = {}

        max_hop_num = max([city[0] for city in city_list])
        hop_countdown = max_hop_num
        hop_num = 1

        # Put individual travel time pairs into dictionary
        while hop_num <= max_hop_num:
            for city in city_list:
                if city[0] == hop_countdown and not hop_num in hop_time_dict:
                    hop_time_dict[hop_num] = [[city[1], city[2], city[3]]]
                elif city[0] == hop_countdown:
                    hop_time_dict[hop_num].append([city[1], city[2], city[3]])

            hop_num += 1
            hop_countdown -= 1

        # For all keys > 1 in dictionary, grab the travel time from the previous key and add to current travel time
        key_count = 1
        # For a given hop number key
        for keys in hop_time_dict:
            # For each city pair within the hop number
            for key in hop_time_dict[keys]:
                # The first city in that pair is the from city
                from_city = key[0]
                # If we are not in the first hop
                if not key_count == 1:
                    # Look into the prior hop's cities
                    for city in hop_time_dict[keys-1]:
                        # When a given city (to city) matches the from city
                        if city[1] == from_city:
                        # Modify the higher key's city distance
                            key[2] += city[2]
                else:
                    break
            key_count += 1

        return all_dest, hop_time_dict

    def min_times(self, hop_time_dict):
        '''Returns all cities that can be reached and their minimum travel time.'''
        # For each possible destination in the all destinations set, walk through dictionary and return
        # the minimum time associated with getting to it.

if __name__ == '__main__':
    # Create CityHopper instance
    hopper = CityHopper()
    # Grab starting city and number of hops from user
    start_city, num_hops = hopper.get_input()
    # Get set of hoppable cities
    city_list = hopper.can_hop(start_city, num_hops)
    #print(city_list)
    all_destinations, hop_times = hopper.hop_times(city_list)
    print(all_destinations)
    print(hop_times)
    # TODO run debugger and resolve the 28 hours issue with Philadelphia from Portland. It should be 17 or so
