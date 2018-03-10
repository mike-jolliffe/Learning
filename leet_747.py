class Solution(object):
    def dominantIndex(self, nums):
        """Check whether largest value in list is >= 2x second-largest value
        :type nums: List[int]
        :rtype: int
        """
        # Create sorted copy of list
        ordered = sorted(nums)
        # If there are at least two values and largest is 2x second-largest
        if len(ordered) > 1 and ordered[-1] >= 2 * ordered[-2]:
            # Get its index from original list
            return nums.index(ordered[-1])
        # Otherwise, return -1
        else:
            return -1


if __name__ == '__main__':
    sol = Solution()
    print(sol.dominantIndex([1,7,2,3]))  # 1
    print(sol.dominantIndex([1,5,2,3]))  # -1
    print(sol.dominantIndex([5]))  # -1
