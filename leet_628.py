class Solution:
    def __init__(self):
        # Container for extreme positive and negative vals
        self.extremes = []

    def maximumProduct(self, nums):
        """Find the maximum possible product of three values in nums

        :type nums: List[int]
        :rtype: int
        """
        # Solution must be (-,-,+) or (+,+,+), extremes in sorted array
        # Check if negatives exist--if so, build (-,-,+,+,+) to check both the
        # (-,-,+) and (+,+,+) cases
        nums.sort()
        if nums[1] < 0:
            try:
                # Get the (+,+,+)
                self.getIX(nums, -1, 3)
                # Get the (-,-)
                self.getIX(nums, 0, 2)
            except:
                # Length of nums < 5, return should still work
                pass
        else:
            self.getIX(nums, -1, 3)
        self.extremes.sort()
        # Find which scenario is the max
        return max([self.extremes[0] * self.extremes[1] * self.extremes[-1],
                   self.extremes[-1] * self.extremes[-2] * self.extremes[-3]])

    def getIX(self, array, pos, num):
        """Put num numbers from front or back of list into array for product calc

        :type array: List[int]
        :type pos: int
        :type num: int
        :rtype: None
        """
        while num >= 1:
            self.extremes.append(array[pos])
            num -= 1
            array.pop(pos)
        return None


if __name__ == '__main__':
    sol = Solution()
    #print(sol.maximumProduct([1,2,3,4,5])) # 60
    #print(sol.maximumProduct([-6,-5,-1,0,1,2,4,5]))  # 150
    print(sol.maximumProduct([-6,-4,4,5]))  # 120
    #sol.getIX([1,2,3,4,5], -1, 3)  # [3,4,5]
    #sol.getIX([-5,-3,1], 0, 2)  # [-5,-3,3,4,5]
