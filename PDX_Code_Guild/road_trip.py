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
                self.hoppable.append((num_hops, start_city, city))
                self.can_hop(city, num_hops-1)
            return self.hoppable

    def min_time(self, city_list):
        '''Calculates minimum travel time to each city that falls within the number of hops'''
        # Initialize a dictionary for chaining hop times
        two_hop = []

        # Add travel time between pairs to the pair tuple
        for i in range(len(city_list)):
            city_list[i] += (CityHopper.city_dict[city_list[i][1]][city_list[i][2]],)

        first_hop_num = max([city[0] for city in city_list])
        hop_num = first_hop_num
        # while hop_num > 0:
        #     for city in city_list:
        #         if city[0] == hop_num and not city[1] in hop_time_dict:
        #             hop_time_dict[city[1]] = (hop_time_dict[city[1]][city[2]] , city[2])

        for hop_from in city_list:
            if hop_from[0] == first_hop_num:
                for hop_to in city_list:
                    if hop_to[0] == first_hop_num - 1 and hop_to[1] == hop_from[2]:
                        two_hop.append([hop_from[1], hop_from[2], hop_to[2], hop_from[3] + hop_to[3]])


        print (city_list)
        print()
        print(two_hop)
        # Try a data structure with the following form
        #   'Starting_city':
        #       {(travel time, ending city):
        #           {(travel time, ending city):

        # Calculate the sum of time for each different trip from starting city to final ending city
        # Display only the minimum time pairs for all trips


if __name__ == '__main__':
    # Create CityHopper instance
    hopper = CityHopper()
    # Grab starting city and number of hops from user
    start_city, num_hops = hopper.get_input()
    # Get set of hoppable cities
    city_list = hopper.can_hop(start_city, num_hops)
    print(city_list)
    best_times = hopper.min_time(city_list)

