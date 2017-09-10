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

        self.start_city = None
        self.num_hops = None

    def get_input(self):
        '''Gets starting city and number of hops from user, stores them as instance attributes'''
        for key in CityHopper.city_dict:
            print(f"- {key}")
        self.start_city = input(f"Please enter your starting city: ")
        self.num_hops = int(input(f"How many hops can you take? "))

    def can_hop(self):
        '''Given a starting city and number of hops, returns all cities that can be reached, within that
        number of hops'''



    def min_time(self, city_list):
        '''Calculates minimum travel time to each city that falls within the number of hops'''
        pass

if __name__ == '__main__':
    hopper = CityHopper()
    hopper.get_input()
    city_list = hopper.can_hop()
    best_times = hopper.min_time(city_list)

