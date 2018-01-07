class Solution:

    def __init__(self):
        self.island_dict = None

    def maxAreaOfIsland(self, grid):
        """Returns the area of largest island in grid, counting connectivity
           in the four cardinal directions
        :type grid: List[List[int]]
        :rtype: int
        """

        # Convert grid to x,y dict
        self.island_dict = self.gridToDict(grid)
        # Create max_area holder
        max_area = 0
        area = 0
        # for each dict key
        for key in self.island_dict:
            # If key has value one
            if self.island_dict[key] == 1:
                # search in all four directions until no 1s found
                area = self.Search(self.island_dict, key)
                print("Area of islands: {}".format(area))
            else:
                # Check curr_area vs. max_area
                if area > max_area:
                    max_area = area
        return max([max_area, area])

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

    def Search(self, xymap, start, tot_area=0):
        """Returns total number of 1s connected four-directionally to given
           starting point (x,y coord)
        :type map: dictionary of x,y coord keys and 1/0 values
        :type start: tuple of x,y coords
        :rtype: int
        """
        try:
            #print("Location: {}, value: {}".format(start, xymap[start]))
            if xymap[start] == 0 or xymap[start] == 2:
                return tot_area
            elif xymap[start] == 1:
                tot_area += 1
                #print("Current total area: {}".format(tot_area))
                xymap[start] = 2

                up = self.Search(xymap, (start[0], start[1] - 1), tot_area)
                down = self.Search(xymap, (start[0], start[1] + 1), tot_area)
                left = self.Search(xymap, (start[0] - 1, start[1]), tot_area)
                right = self.Search(xymap, (start[0] + 1, start[1]), tot_area)

                #print(tot_area, up, down, left, right)
                #print(max([tot_area, up, down, left, right]))
                return max([up, down, left, right])

        except KeyError:
            #print("Location {} is out of bounds".format(start))
            return tot_area



if __name__ == '__main__':
    sol = Solution()
    #dictionary = sol.gridToDict([[0,0,1,0],[0,0,1,1]])
    #print(sol.maxAreaOfIsland([[0,0,1,0],[0,0,1,1]]))  # 3
    print(sol.maxAreaOfIsland([[1,0],[1,1]]))  # 3
    #print(sol.maxAreaOfIsland([[1]]))  # 1
