class Solution:
    def twoSum(self, nums, target):
        """Returns from list a sublist of two numbers that sum to target
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                print("i: {}, j: {}, sum: {}".format(i, j, nums[i]+nums[j]))
                # Move end toward start, calculating sum
                if not nums[i] + nums[j] == target:
                    # If sum greater than target, throw out end
                    pass
                # If you hit the sum, return [start, end] values
                else:
                    return [i, j]
        return []

if __name__ == '__main__':
    sol = Solution()
    #print(sol.twoSum([7,2,15,11,30], 22))
    print(sol.twoSum([3,2,4], 6))  # [1,2]
    print(sol.twoSum([3,3], 6))  # [0,1]
