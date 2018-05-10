class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """

        all_distances = []
        # Get indexes for all lookup chars
        lookup_indexes = [ix for ix, num in enumerate(S) if num == C]

        def get_distance(char_ix):
            """Find the minimum index position distance between given char and lookup"""
            return min([abs(char_ix - lookup_index) for lookup_index in lookup_indexes])

        for ix, char in enumerate(S):
            all_distances.append(get_distance(ix))

        return all_distances

if __name__ == '__main__':
    sol = Solution()
    print(sol.shortestToChar("abcdedede", "e"))
