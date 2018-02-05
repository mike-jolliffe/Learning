class Solution:
    def isToeplitzMatrix(self, matrix):
        """Determines if every value within a matrix's diagonals is the same
        :type matrix: List[List[int]]
        :rtype: bool
        """
        xlen = len(matrix[0])
        ylen = len(matrix)
        # Convert the matrix into xy-locations and values dictionary
        xy_dict = self.toXYDict(matrix)
        # Get all starting locations for diagonals (i.e., first row and first column locs)
        diagonal_starts = self.getStarts(xlen, ylen)
        # Get the values in each diagonal
        all_diags = self.getDiags(xy_dict, diagonal_starts)
        # Check that all values in each diagonal are the same. Apply to all diags.
        return all([all(items[0] == item for item in items) for items in all_diags])

    def toXYDict(self, matrix):
        """Converts a 2D array into xy-coord dict
        :type matrix: List[List[int]]
        :rtype: Dictionary
        """

        xy_dict = {}
        for row_ix in range(len(matrix)):
            for col_ix in range(len(matrix[0])):
                xy_dict[(col_ix, row_ix)] = matrix[row_ix][col_ix]
        return xy_dict

    def getStarts(self, xlen, ylen):
        """Gets starting location for all diagonals
        :type dictionary: dictionary
        :type xlen: int
        :type ylen: int
        :rtype: List[tuple]
        """

        diag_starts = []
        for i in range(xlen):
            diag_starts.append((i, 0))
        for i in range(ylen):
            diag_starts.append((0, i))
        return diag_starts

    def getDiags(self, dictionary, starting_locs):
        """Given a dict of xy coords and vals, groups diagonal values together
        :type dictionary: dictionary
        :type starting_locs: List[tuple]
        :rtype: List[List[int]]
        """

        all_diags = []
        for loc in starting_locs:
            diag_vals = []
            diag_vals.append(dictionary[loc])
            nextVal = True
            new_loc = loc
            while nextVal:
                new_loc = (new_loc[0] + 1, new_loc[1] + 1)
                try:
                    diag_vals.append(dictionary[new_loc])
                except:
                    nextVal = False
            all_diags.append(diag_vals)
        return all_diags


if __name__ == '__main__':
    sol = Solution()
    print(sol.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))  # True
    print(sol.isToeplitzMatrix([[1,2,3,4],[5,2,3,3],[9,4,1,2]]))  # False
