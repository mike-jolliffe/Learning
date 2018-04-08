class Solution(object):
    def searchInsert(self, nums, target):
        """Return index of target number in sorted list if exists, or index it
        would become if inserted
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # If number in list, return its index
        if target in nums:
            return nums.index(target)
        # If number not in list, find first number larger than it get its index,
        # then subtract one
        else:
            for num in nums:
                if num > target:
                    return nums.index(num)
            # If greater than all nums
            return len(nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.searchInsert([1,3,5,6], 5))  # 2
    print(sol.searchInsert([1,3,5,6], 0))  # 0
    print(sol.searchInsert([1,3,5,6], 7))  # 4
