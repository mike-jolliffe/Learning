class Solution:
    def distributeCandies(self, candies):
        """ Split candies evenly across two individuals, maximizing diversity of
            candy type given to one of the individuals, while maintaining equal
            number of candies to each.
        :type candies: List[int]
        :rtype: int
        """

        # Create candy counter
        unique_candies = 0

        counter = 0
        # Calculate half of total candies
        num_candies = len(candies) / 2
        print(num_candies)

        # Get set candies
        unique_set = set(candies)

        # While candy counter less than half all candies
        while counter < num_candies:
            # If unique candy still in set, candy counter += 1
            if len(unique_set) > 0:
                unique_set.pop()
                unique_candies += 1
                counter += 1
            # No more unique candy
            else:
                counter += 1
        return unique_candies

if __name__ == '__main__':
    sol = Solution()
    print(sol.distributeCandies([1,1,2,2,3,3]))
