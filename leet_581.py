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
        # Enumerate the unsorted array, zip to reference list for pairwise compare
        for i,j in zip(enumerate(nums), ref_list):
            # if the value in nums doesn't match ref list
            if not i[1] == j:
                # Store its index
                diffs.append(i[0])
        # If the list isn't already sorted (i.e., if diffs is non-empty)
        if diffs:
            # Return the length between first and last non-match, inclusive (i.e., +1)
            return max(diffs) - min(diffs) + 1
        else:
            return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.findUnsortedSubarray([1,2,4,3,5,7]))  # 2
    print(sol.findUnsortedSubarray([2,6,4,8,10,9,15]))  # 5
