class Solution(object):
    def findLHS(self, nums):
        """Find longest harmonious subsequence (where diff btwn max/min is 1)
        :type nums: List[int]
        :rtype: int
        """
        # Get all harmonious pairs
        pairs = self.make_pairs(nums)
        if not pairs:
            return 0
        # Find most frequent pairs
        most_freq = self.get_max_freq(pairs, nums)
        # Return longest subsequence of those pair values
        return len([num for num in nums if num in most_freq])

    def make_pairs(self, nums):
        """Breaks list of numbers into harmonious pairs (diff of 1)
        :type: nums: List[int]
        :rtype: List[tuple(int)]
        """
        pairs = []
        for num1 in nums:
            for num2 in nums:
                # If the difference between two numbers is 1
                if abs(num1 - num2) == 1:
                    # append sorted tuple so can make set
                    pairs.append(tuple(sorted([num1, num2])))
        # Return a list of the set of harmonious pairs
        return list(set(pairs))

    def get_max_freq(self, pairs, nums):
        """Finds the most frequent pair
        :type pairs: List[tuple(int)]
        :type nums: List[int]
        :rtype: List[int]
        """
        max_freq = 0
        max_pair = None
        curr_freq = 0
        # For each harmonious pair
        for pair in pairs:
            # Count frequency of numbers in the pair
            for num in nums:
                if num in pair:
                    curr_freq += 1
            # Store the max frequency and corresponding pair 
            if curr_freq > max_freq:
                max_pair = pair
                max_freq = curr_freq
            curr_freq = 0
        return max_pair

if __name__ == '__main__':
    sol = Solution()
    print(sol.make_pairs([1,2,4,5,7,8]))  # [[1,2], [4,5], [7,8]]
    print(sol.get_max_freq([(1,2),(4,5),(7,8)], [1,2,2,4,5,7,8,11]))  # (1,2)
    print(sol.findLHS([1,3,2,2,5,2,3,7]))  # 5
    print(sol.findLHS([1,1,1,1]))  # 0
