class Solution:
    def maxSubArray(self, nums):
        """Returns the maximum summing contiguous subarray of nums
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        subarray_max = nums[0]
        for i in range(len(nums) - 1):
            if nums[i] > subarray_max:
                subarray_max = nums[i]
            for j in range(i + 1, (len(nums))):
                if nums[j] > subarray_max:
                    subarray_max = nums[j]
                if sum(nums[i:j+1]) > subarray_max:
                    subarray_max = sum(nums[i:j+1])
                    #print(nums[i:j])
        return subarray_max

if __name__ == '__main__':
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # 6
    print(sol.maxSubArray([1]))  # 1
    print(sol.maxSubArray([-2,1]))  # 1
    print(sol.maxSubArray([1,2]))  # 3
