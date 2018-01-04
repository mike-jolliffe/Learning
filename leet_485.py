class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """Returns the maximum number of consecutive ones in a list
        :type nums: List[int]
        :rtype: int
        """
        max_ct = 0
        curr_ct = 0

        for num in nums:
            # Count consecutive ones
            if num == 1:
                curr_ct += 1
            else:
                # Compare a finished string to the max
                if curr_ct > max_ct:
                    max_ct = curr_ct
                curr_ct = 0
        if curr_ct > max_ct:
            max_ct = curr_ct

        return max_ct

if __name__ == '__main__':
    sol = Solution()
    print(sol.findMaxConsecutiveOnes([1,1,0,1,1,1]))
