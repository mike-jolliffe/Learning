class Solution:
    def largeGroupPositions(self, S):
        """Return list of [start, end] index for all same-letter groups > len(2)
        :type S: str
        :rtype: List[List[int]]
        """
        # Make dictionary of form {"letter": [start, stop]}
        groups_dict = {}

        def get_stop(start):
            """Finds the index of the last same letter in sequence
            :type start: int
            :rtype: int
            """
            curr_ix = start
            to_match = S[start]
            for letter in S[start + 1:]:
                if letter != to_match:
                    return curr_ix
                else:
                    curr_ix += 1
            return curr_ix

        # Create the dictionary of letter groups > 2
        start = 0
        for ix, letter in enumerate(S):
            if ix >= start:
                stop = get_stop(ix)
                if stop - ix > 1:
                    groups_dict.setdefault(letter, []).extend([ix, stop])
                    start = stop + 1
        # Return lexicographically sorted list of [start,stop] groups
        if groups_dict:
            return [value for key, value in sorted(groups_dict.items())]
        else:
            return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.largeGroupPositions("cccbbaaaddbbb"))  # [[5,7],[10,12],[0,2]]
    print(sol.largeGroupPositions("abbxxxxzzy"))  # [3,6]
    print(sol.largeGroupPositions("abbxxzzy"))  # []
