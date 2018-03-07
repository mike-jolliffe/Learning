class Solution(object):
    def missingNumber(self, nums):
        """Find number missing from array
        :type nums: List[int]
        :rtype: int
        """
        # Generate a set for reference, from 0 to n
        ref_set = set(range(0, len(nums) + 1))
        # Return the diff of the sets
        return list(ref_set - set(nums))[0]


if __name__ == '__main__':
    sol = Solution()
    print(sol.missingNumber([0,1,2,4,5]))  # 3
    print(sol.missingNumber([0,1]))  # 2
    print(sol.missingNumber([0]))  # 1
    print(sol.missingNumber([1]))  # 0
