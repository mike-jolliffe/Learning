'''## Advanced
* Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.
* When the user enters a city and a number of hops, print out the shortest travel times to each city.
Paths with fewer hops are not necessarily those with the shorter travel times.'''

import itertools

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
                self.hoppable.append([num_hops, start_city, city, CityHopper.city_dict[start_city][city]])
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

        for cities in city_list:
            cities[0] = abs(cities[0] - (max_hop_num + 1))

        # Put individual travel time pairs into dictionary
        while hop_num <= max_hop_num:
            for city in city_list:
                if city[0] == hop_num and not hop_num in hop_time_dict:
                    hop_time_dict[hop_num] = [[city[1], city[2], city[3]]]
                elif city[0] == hop_num:
                    hop_time_dict[hop_num].append([city[1], city[2], city[3]])
                else:
                    pass
            hop_num += 1

        # TODO resolve the bug in this part of the code that makes the 3-hop total too high
        # For all keys > 1 in dictionary, grab the travel time from the previous key and add to current travel time
        key_count = sorted([key for key in hop_time_dict.keys()])
        # For a given hop number
        for hop in key_count:
            # For each city pair within the hop number
            for final_cities in hop_time_dict[hop]:
                # The first city in that pair is the from city
                from_city = final_cities[0]
                # If we are not in the first hop
                if not hop == 1:
                    # Look into the prior hop's cities
                    for interim_cities in hop_time_dict[hop-1]: # TODO resolve whether I need a loop here, maybe not
                        # When a prior hop's to city matches current from city
                        if interim_cities[1] == from_city:
                            print(f"Departure city: {interim_cities[1]}, time so far: {interim_cities[2]}, "
                                  f"{from_city}, new distance: {final_cities[2]}")
                        # Modify the higher key's city distance
                            final_cities[2] += interim_cities[2]
                            print(f" New total dist: {final_cities[2]}")
                else:
                    break

            hop += 1

        # Clean up the dictionary by removing the from city, leaving only destination and cumulative distance
        for keys in hop_time_dict:
            for key in hop_time_dict[keys]:
                del key[0]

        return all_dest, hop_time_dict


    def all_times(self, all_destinations, hop_time_dict):
        '''Returns all cities that can be reached and their various travel times via different hops.'''
        # Create a dictionary that will hold cumulative times by destination
        cumulative_times = {}
        # For each final destination city
        for city in all_destinations:
            # Get the distance from the hop time dictionary for all hops with this city as the destination
            time_array = [[destination[1] for destination in value if destination[0] == city] for key, value in hop_time_dict.items()]
            # Add the city and various times to the cumulative times dictionary
            if not city in cumulative_times:
                cumulative_times[city] = time_array
        # Flatten the values in the dictionary
        for key in cumulative_times:
            cumulative_times[key] = list(itertools.chain.from_iterable(cumulative_times[key]))

        return cumulative_times

    def min_time(self, cumulative_times):
        '''Returns all available destination cities, and their minimum travel times'''
        min_times_dict = {}
        for city in cumulative_times:
            travel_min = min(cumulative_times[city])
            min_times_dict[city] = travel_min

        return min_times_dict


if __name__ == '__main__':
    # Create CityHopper instance
    hopper = CityHopper()
    # Grab starting city and number of hops from user
    start_city, num_hops = hopper.get_input()
    # Get set of hoppable cities
    city_list = hopper.can_hop(start_city, num_hops)
    all_destinations, hop_times = hopper.hop_times(city_list)
    all_times = hopper.all_times(all_destinations, hop_times)
    print(f"\nStarting from {hopper.start_city} and given {hopper.num_hops} hops, you can travel to:\n")
    min_times = hopper.min_time(all_times)
    for city in min_times:
        print(f"{city} in {min_times[city]} hours")

