'''## Advanced
* Let the user enter a city and a number of hops. Print out all cities that could be reached through that number of hops.
* When the user enters a city and a number of hops, print out the shortest travel times to each city.
Paths with fewer hops are not necessarily those with the shorter travel times.'''

#import itertools

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

        # Create final array
        final_array = []
        # Initialize a loop array with starting city and zero miles traveled
        loop_array = [[self.start_city, 0]]
        # Initialize a temporary holder
        loop_holder = []
        hop_count = 1
        while hop_count <= self.num_hops:
            # Grab all the 'from' cities from the last hop
            for from_city in loop_array:
                # Use those from cities in the loop array to look up possible destinations and times this hop
                values = self.city_dict[from_city[-2]]
                # For each potential destination city
                for destination in values:
                    # Grab all prior from cities (i.e., the path of hops so far)
                    path = from_city[:-1]
                    # Append the potential destination to the path
                    path.append(destination)
                    # Append the total travel time across all hops to the path
                    path.append(values[destination] + from_city[-1])
                    # Save the path with its associated cumulative travel time to the final array
                    final_array.append(path)
                    # Save the path to the temporary holder so that loop array so it can be used in the next loop
                    loop_holder.append(path)
            # Reset loop array so that we can start from our last hop on the next hop
            loop_array = loop_holder
            # Empty out the loop array so it's ready for next iteration
            loop_holder = []
            # Update the hop count
            hop_count += 1
        return all_dest, final_array

    def all_times(self, all_destinations, hop_times):
        '''Returns all cities that can be reached and their various travel times via different hops.'''
        # Create a dictionary that will hold cumulative times by destination
        cumulative_times = {}
        # For each final destination city
        for city in all_destinations:
            # Get the distance from the hop time dictionary for all hops with this city as the destination
            time_array = [destination[-1] for destination in hop_times if destination[-2] == city]
            # Add the city and various times to the cumulative times dictionary
            if not city in cumulative_times:
                cumulative_times[city] = time_array
        # Flatten the value lists in the dictionary
        #for key in cumulative_times:
        #    cumulative_times[key] = list(itertools.chain.from_iterable(cumulative_times[key]))

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
    # Get set of hoppable cities given hop number constraint
    city_list = hopper.can_hop(start_city, num_hops)
    # Return all hop times to potential destinations for all possible routes
    all_destinations, hop_times = hopper.hop_times(city_list)
    all_times = hopper.all_times(all_destinations, hop_times)
    print(f"\nStarting from {hopper.start_city} and given {hopper.num_hops} hops, you can travel to:\n")
    # Report the minimum times for each possible destination
    min_times = hopper.min_time(all_times)
    for city in min_times:
        print(f"{city} in {min_times[city]} hours")

