class Solution:
    def containsDuplicate(self, nums):
        """Return True if list contains duplicates
        :type nums: List[int]
        :rtype: bool
        """
        # If the set of numbers is the same as numbers, no unique, so return True
        return not (list(set(nums)) == nums)


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,2,3,4,5]))  # False
    print(sol.containsDuplicate([1,2,3,4,4,5]))  # True
    print(sol.containsDuplicate([1,3]))  # False
