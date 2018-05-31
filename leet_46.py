class Solution:
    def permute(self, nums):
        """Return all permutations for list of ints
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # Make container for holding permutations
        permutations = []
        def make_perm(num, start_ix, stop_ix):
            # If you're through the number list, append it
            if start_ix==stop_ix:
                permutations.append(num[:])
            else:
                for i in range(start_ix,stop_ix+1):
                    # Swap values at current index and starting index
                    num[start_ix], num[i] = num[i], num[start_ix]
                    make_perm(num, start_ix+1, stop_ix)
                    num[start_ix], num[i] = num[i], num[start_ix] # backtrack
        make_perm(nums, 0, len(nums) - 1)
        return permutations

if __name__ == '__main__':
    sol = Solution()
    print(sol.permute([1,2,3]))
