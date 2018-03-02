class Solution:
    def findShortestSubArray(self, nums):
        """Return shortest subarray created by most frequent elements
        :type nums: List[int]
        :rtype: int
        """

        # Convert array to dict, with number as key, index as value
        nums_dict = self.array_to_Dict(nums)
        # For items in dictionary, get key, value where length of value is longest
        max_val = max([len(value) for value in nums_dict.values()])
        # Grab the index subarrays of the most frequently occurring values
        most_frequent = [value for key, value in nums_dict.items() if len(value) == max_val]
        print(most_frequent)
        # Find the shortest possible subarray of the same degree
        return min([subarray[-1] - subarray[0] + 1 for subarray in most_frequent])

    def array_to_Dict(self, nums):
        """Converts list to dictionary, number is key, index is value
        :type nums: List[int]
        :rtype: dictionary
        """

        nums_dict = {}
        for number_ix in range(len(nums)):
            # Number is key, its index is in list of values
            nums_dict.setdefault(nums[number_ix], []).append(number_ix)

        return nums_dict


if __name__ == '__main__':
    sol = Solution()
    print(sol.findShortestSubArray([1,2,3,3,4,5]))  # 2
    print(sol.findShortestSubArray([1,2,2,3,1,4,2]))  # 6
    print(sol.findShortestSubArray([1,2,2,3,1]))  # 2
    print(sol.findShortestSubArray([1,2,2,1,2,1,1,1,1,2,2,2]))  # 9
