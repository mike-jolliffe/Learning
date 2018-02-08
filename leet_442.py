class Solution:
    def findDuplicates(self, nums):
        """Return list of duplicates
        :type nums: List[int]
        :rtype: List[int]
        """

        # Generate reference list
        uniques = list(set(nums))

        dupes = []
        for num in nums:
            # The first time a number occurs, remove it from reference list
            if num in uniques:
                uniques.remove(num)
            # The next time a number occurs, append it as a duplicate
            else:
                dupes.append(num)
        return dupes

if __name__ == '__main__':
    sol = Solution()
    print(sol.findDuplicates([1,2,3,4,2,3]))  # [2,3]
