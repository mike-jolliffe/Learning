class Solution:
    def majorityElement(self, nums):
        """Find the element of an array occurring over half the time
        :type nums: List[int]
        :rtype: int
        """

        # Make function to build frequency dictionary
        def arrayToDict():
            frequency_dict = {}
            for num in nums:
                frequency_dict[num] = frequency_dict.get(num, 1) + 1
            return frequency_dict
        # Invoke the function
        frequency_dict = arrayToDict()

        # Iterate through all values, grab the key associated with the majority
        return [key for key,val in frequency_dict.items() if val > (len(nums) / 2)][0]

if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([1,2,3,4,5,6,7,8,9,8,8,8,8,8,8,8,8]))  # 8
    print(sol.majorityElement([3,2,3]))  # 3
