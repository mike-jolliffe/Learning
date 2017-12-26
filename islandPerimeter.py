class Solution:
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Key is location tuple, value is 1/0 for presence of land
        location_dict = {}

        # Convert grid to tuple-keyed dictionary
        for row_ix, row in enumerate(grid):
            for col_ix, value in enumerate(row):
                location_dict[(col_ix, row_ix)] = value
        print(location_dict)

        # Create perimeter placeholder
        perimeter = 0

        # For all locations
        for location in location_dict:
            # Get locations with land
            if location_dict[location] == 1:
                # Give max perimeter value
                cell_perimeter = 4
                # Break tuple back apart to x, y components
                x, y = location
                # if cell not at x upper bound
                if not x == len(grid[0]) - 1:
                    # Get value in position to right
                    right_val = location_dict[(x+1, y)]
                    if right_val == 1:
                        # If adjacent is land, subtract side from 4
                        cell_perimeter -= 1
                # if cell not at x lower bound
                if not x == 0:
                    # Get value in position to left
                    left_val = location_dict[(x-1, y)]
                    if left_val == 1:
                        cell_perimeter -= 1
                # if cell not upper y bound
                if not y == len(grid) - 1:
                    # Get value above
                    up_val = location_dict[(x, y+1)]
                    if up_val == 1:
                        cell_perimeter -= 1
                # if cell not y lower bound
                if not y == 0:
                    # Get value below
                    down_val = location_dict[(x, y-1)]
                    if down_val == 1:
                        cell_perimeter -= 1
                perimeter += cell_perimeter
                print("({}, {}): {}".format(y, x, cell_perimeter))
        return perimeter


if __name__ == '__main__':
    sol = Solution()
    print(sol.islandPerimeter([[1,1,0],[1,0,0]]))  # 8
    print(sol.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]))  # 16
