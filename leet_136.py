class Solution:
    def singleNumber(self, nums):
        """Return the single number that is unique in the list
        :type nums: List[int]
        :rtype: int
        """
        # Push all nums into frequency dict
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        # Return num where frequency is 1
        return [key for key, value in frequency.items() if value == 1][0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([1,1,2,2,3,4,4,5,5]))  # 3
