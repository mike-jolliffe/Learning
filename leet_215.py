class Solution:
    def findKthLargest(self, nums, k):
        """Returns Kth largest element from unsorted array
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Return value with a place that matches k - 1 (0-indexed) from the sorted, reversed list 
        new=sorted(nums, reverse=True)
        return new[k-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.findKthLargest([1,2,4,7,5,6], 2))  #6
