class Solution:
    def findUnsortedSubarray(self, nums):
        """Return length of shortest subarray that, if sorted, would result in
           entire array being sorted
        :type nums: List[int]
        :rtype: int
        """

        # Create sorted reference
        ref_list = sorted(nums)
        # Compare against reference
        diffs = []
        for i,j in zip(enumerate(nums), ref_list):
            if not i[1] == j:
                diffs.append(i[0])
        return max(diffs) - min(diffs) + 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.findUnsortedSubarray([1,2,4,3,5,7]))  # 2
    print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))  # 5
