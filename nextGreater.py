class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        The Next Greater Number of a number x in nums1 is the first greater
        number to its right in nums2. If it does not exist,
        output -1 for this number.
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        # Store next greater
        nextGreater = []

        # For each element in nums1
        for num1 in nums1:
            # Find the corresponding value in nums2
            ix = nums2.index(num1)
            hasGreater = False
            # If any number right of that value in nums2 is larger
            for j in range(ix, len(nums2)):
                # If nums2 > nums1
                if nums2[j] > num1:
                    # Put that value in a list
                    nextGreater.append(nums2[j])
                    hasGreater = True
                    break
            # Otherwise put -1 in a list
            if hasGreater == False:
                nextGreater.append(-1)
        return nextGreater

if __name__ == '__main__':
    sol = Solution()
    print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))  # [-1, 3, -1]
    print(sol.nextGreaterElement([2,4], [1,2,3,4]))  # [3, -1]
