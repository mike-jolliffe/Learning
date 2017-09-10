'''## Advanced
* Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.
* When the user enters a city and a number of hops, print out the shortest travel times to each city.
Paths with fewer hops are not necessarily those with the shorter travel times.'''

class CityHopper:
    '''Allows user to check shortest routes and potential cities based on a starting city
    and number of connecting hops.'''

    def __init__(self, start_city, num_hops):
        self.city_dict = {
          'Boston': {'New York': 4, 'Albany': 6, 'Portland': 3},
          'New York': {'Boston': 4, 'Albany': 5, 'Philadelphia': 9},
          'Albany': {'Boston': 6, 'New York': 5, 'Portland': 7},
          'Portland': {'Boston': 3, 'Albany': 7},
          'Philadelphia': {'New York': 9}
        }

        self.start_city = start_city
        self.num_hops = num_hops
    def can_hop(self):
        '''Given a starting city and number of hops, returns all cities that can be reached, within that
        number of hops'''
        pass

    def min_time(self, city_list):
        '''Calculates minimum travel time to each city that falls within the number of hops'''
        pass

if __name__ == '__main__':
    start_city = input(f"Please enter your starting city: ")
    num_hops = int(input(f"How many hops can you take? "))
    hopper = CityHopper(start_city, num_hops)
    city_list = hopper.can_hop()
    best_times = hopper.min_time(city_list)

