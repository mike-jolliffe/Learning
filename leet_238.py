from functools import reduce

class Solution:
    def productExceptSelf(self, nums):
        """Returns array where each index value is product of all other vals in
           array except index value
        :type nums: List[int]
        :rtype: List[int]
        """

        # Define a product array for storing results
        prod_array = []

        # Store current index
        for ix in range(len(nums)):
            # Copy nums for popping without changing
            for_pop = nums[:]
            for_pop.pop(ix)
            # Use reduce to generate produce of all nums in remaining array
            prod_array.append(int(reduce(lambda a,b: a*b, for_pop)))

        return prod_array

if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1,2,3,4]))  # [24, 12, 8, 6]
