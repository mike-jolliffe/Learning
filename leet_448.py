class Solution:
    def findDisappearedNumbers(self, nums):
        """Returns list of all numbers missing from list
        :type nums: List[int]
        :rtype: List[int]
        """

        missing = []
        reference = [i for i in range(min(nums), max(nums) + 1)]
        for i in reference:
            if not i in set(nums):
                missing.append(i)
        return missing

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDisappearedNumbers([4,3,2,7,8,2,3,1]))  # [5,6]
