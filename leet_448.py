class Solution:
    def findDisappearedNumbers(self, nums):
        """Returns list of all numbers missing from list
        :type nums: List[int]
        :rtype: List[int]
        """

        reference = range(1, len(nums) + 1)
        if len(nums) != 0:
            return list(set(reference) - set(nums))
        return []

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5,6]
