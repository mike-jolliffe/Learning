from collections import defaultdict

class Solution:
    def topKFrequent(self, nums, k):
        """Return the k most frequent numbers
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        # Generate dictionary of frequencies
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1

        k_most = []
        # Grab the k most frequent values, sorted descending
        for val in sorted(frequency.values())[::-1][:k]:
            # Append the associated key to k_most if it isn't already there
            k_most.append([key for key, value in frequency.items() if (value == val and not key in k_most)][0])
        return k_most

if __name__ == '__main__':
    sol = Solution()
    print(sol.topKFrequent([2,2,1,1,1,3,3,3,3], 2))  # [3,1]
    print(sol.topKFrequent([1,2], 2))  # [1,2]
