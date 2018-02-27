class Solution:
    def twoSum(self, numbers, target):
        """Find the two numbers that sum to target, where first index must be
           less than second index
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """

        for ix_1 in range(len(numbers) - 1):
            for ix_2 in range(ix_1 + 1, len(numbers)):
                if numbers[ix_1] + numbers[ix_2] == target:
                    # Problem called for solution to be one-indexed
                    return [ix_1 + 1, ix_2 + 1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum([2, 7, 11, 15], 9))  # [1,2]
    print(sol.twoSum([0, 0, 1, 2], 0))  # [1,2]
