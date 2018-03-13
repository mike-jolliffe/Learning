class Solution(object):
    def __init__(self):
        self.p_trgl = []

    def generate(self, numRows):
        """Generate a given number of rows in a Pascal's triangle
        :type numRows: int
        :rtype: List[List[int]]
        """

        # Until total number of rows is met
        while len(self.p_trgl) < numRows:
            # Build a new row
            self.build_row(len(self.p_trgl))
        # Return the finished triangle
        return self.p_trgl

    def build_row(self, rowNum):
        """Builds a given row number for the triangle
        :type rowNum: int
        :rtype: None
        """
        row_vals = []
        row_length = rowNum + 1
        # In subsequent rows, the value at index i is equal to the values at
        # index i-1 and i, added. Return 1 for all index errors (edges of trgl are 1).
        for i in range(row_length):
            row_vals.append(self.prior_row_vals(i-1, i))
        self.p_trgl.append(row_vals)


    def prior_row_vals(self, index1, index2):
        """Given two index positions, gets their values from the last list object
           in the p_trgl instance variable
           :type index1: int
           :type index2: int
           :rtype: int
           """
        # If first index is negative, return 1 for left edge of triangle
        if index1 < 0:
            return 1
        else:
            try:
                # If both indexes in range, return sum of values at those indexes
                return self.p_trgl[-1][index1] + self.p_trgl[-1][index2]
            # If one index out of range, value must be a 1 for right edge of triangle
            except IndexError:
                return 1


if __name__ == '__main__':
    sol = Solution()
    #print(sol.prior_row_vals(0,1))  # 1
    print(sol.generate(4))  # [[1],[1,1],[1,2,1],[1,3,3,1]]
    #print(sol.generate(200))
