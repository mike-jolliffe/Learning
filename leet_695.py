class Solution:
    def maxAreaOfIsland(self, grid):
        """Returns the area of largest island in grid, counting connectivity
           in the four cardinal directions
        :type grid: List[List[int]]
        :rtype: int
        """

        # Convert grid to x,y dict
        island_dict = self.gridToDict(grid)
        # Create max_area holder
        max_area = 0
        # for each dict key
        for key in island_dict:
            curr_area = 0
            # If key has value one
            if island_dict[key] == 1:
                # change its value to 2
                island_dict[key] = 2
                # Increment curr_area by 1
                curr_area += 1
                # repeat in all four directions until no 1s found
                addtl_area = self.Search(key)
            else:
                # Check curr_area vs. max_area
                if curr_area > max_area:
                    max_area = curr_area
                # Set curr_area to zero
                curr_area = 0

    def gridToDict(self, grid):
        """Returns dictionary representation of 2D array, with keys x-y coords
        :type grid: List[List[int]]
        :rtype: Dictionary
        """
        xyDict = {}

        for row_ix in range(len(grid)):
            for column_ix in range(len(grid[row_ix])):
                xyDict[(column_ix, row_ix)] = grid[row_ix][column_ix]

        return xyDict

    def Search(self, key):
        """Returns total number of 1s connected four-directionally to given
           starting point (x,y coord)
        :type key: tuple of x,y coords
        :rtype: int
        """

        

if __name__ == '__main__':
    sol = Solution()
    print(sol.gridToDict([[0,0,1,0],[0,0,1,1]]))
