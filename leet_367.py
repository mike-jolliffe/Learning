class Solution(object):
    def isPerfectSquare(self, num):
        """Checks if number is perfect square
        :type num: int
        :rtype: bool
        """
        # Establish initial boundary conditions for binary search so they'll
        # capture the corner case of 1 and 2
        upper_end = num + 1
        lower_end = -1

        # Set up a recursive binary search
        def binarySearch(guess, upper_end, lower_end):
            # If bounds get too close together, return False
            if upper_end - lower_end < 0.001:
                return False
            # Success case if int of guess returns the number
            elif int(guess) ** 2 == num:
                return True
            # Guess is too high, set it as the new upper bound
            elif int(guess) ** 2 > num:
                upper_end = guess
            else:
                # Guess is too low, set it as lower bound
                lower_end = guess
            # Make new guess as average of upper and lower bounds
            new_guess = (upper_end + lower_end) / 2
            return binarySearch(new_guess, upper_end, lower_end)

        # Call recursive binary search 
        return binarySearch(num / 2, upper_end, lower_end)


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPerfectSquare(24))  # False
    print(sol.isPerfectSquare(36))  # True
    print(sol.isPerfectSquare(2))  # False
    print(sol.isPerfectSquare(1))  # True
    print(sol.isPerfectSquare(996005996001))  # True
