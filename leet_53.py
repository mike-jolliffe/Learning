class Solution:
    def maxSubArray(self, nums):
        """Returns the maximum summing contiguous subarray of nums
        :type nums: List[int]
        :rtype: int
        """

        subarray_max = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, (len(nums) - 1)):
                if sum(nums[i:j+1]) > subarray_max:
                    subarray_max = sum(nums[i:j+1])
                    #print(nums[i:j+1])
        return subarray_max

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
