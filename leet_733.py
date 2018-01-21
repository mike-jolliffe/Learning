class Solution:
    def __init__(self):
        self.locationsDict = {}
        self.oldColor = None

    def floodFill(self, image, sr, sc, newColor):
        """Change color of all four-direction connected same-color pixels
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        self.makeLocationsDict(image, sr, sc)
        self.floodConnected(sr, sc, newColor)

        print(self.locationsDict)

    def makeLocationsDict(self, image, sr, sc):
        """Create dictionary of all four-direction pixels from starting point
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: None
        """

        # Put all values in a dict keyed by x, y
        for row_ix in range(len(image)):
             for col_ix in range(len(image[row_ix])):
                 self.locationsDict[(col_ix + 1, row_ix + 1)] = image[row_ix][col_ix]
        # Get the color of the starting location
        self.oldColor = self.locationsDict[(sc, sr)]
        return None

    def floodConnected(self, sr, sc, newColor):
        """Change color in all four directions if pixel same value as start
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: None
        """

        # If start location in bounds
        try:
            start_loc = (sc, sr)
            print(start_loc)
            print(self.locationsDict)

            # Base case, if connected
            if self.locationsDict[start_loc] == self.oldColor:
                print("Same color")
                self.locationsDict[start_loc] = newColor
                return (self.floodConnected(sr - 1, sc, newColor),
                        self.floodConnected(sr, sc + 1, newColor),
                        self.floodConnected(sr + 1, sc, newColor),
                        self.floodConnected(sr, sc - 1, newColor))
        except:
            print("Outta bounds")
            return None
    # Modify the color of those pixels

    # Repack into 2D array
if __name__ == '__main__':
    sol = Solution()
    sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2)
