class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        # Make the base matrix dictionary
        base_matrix = self.makeMatrix(m, n, 0)

        for op in ops:
            # Make the ops dictionaries
            op_matrix = self.makeMatrix(op[0], op[1], 1)
            # Update base_matrix with the ops
            base_matrix = self.updateMatrix(base_matrix, op_matrix)
        # Get the frequency of max in dictionary
        return self.getMax(base_matrix)

    def makeMatrix(self, rows, cols, val):
        """Return a dictionary of (row, col) keys with values of val
        :type rows: int
        :type cols: int
        :type val: int
        :rtype: dictionary[int]
        """
        base_matrix = {}

        for row in range(rows):
            for col in range(cols):
                base_matrix[(row, col)] = val

        return base_matrix

    def updateMatrix(self, base, new):
        """Update base dictionary with new dictionary values by addition
        :type base: dictionary[int]
        :type new: dictionary[int]
        :rtype: dictionary[int]
        """

        for key in new:
            base[key] += new[key]
        return base

    def getMax(self, dictionary):
        """Returns the frequency of the maximum value in the dictionary
        :type dictionary: dictionary[int]
        :rtype: int
        """
        # Grab last enumerated max from list of maxes
        return [i for i, val in enumerate(dictionary.values()) if val == max(dictionary.values())][-1]


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxCount(3,3,[[2,2],[3,3]]))
