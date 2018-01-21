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

        # Convert 2D array to dict with x, y as keys
        self.makeLocationsDict(image, sr, sc)
        # Change pixel value of all four-directionally connected pixels
        self.floodConnected(sr, sc, newColor)
        # Convert the dictionary of modified pixel vals back to 2D array
        filled = self.toList(image)

        return filled

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

            # Base case, if connected
            if self.locationsDict[start_loc] == self.oldColor:
                self.locationsDict[start_loc] = newColor
                return (self.floodConnected(sr - 1, sc, newColor),
                        self.floodConnected(sr, sc + 1, newColor),
                        self.floodConnected(sr + 1, sc, newColor),
                        self.floodConnected(sr, sc - 1, newColor))
        except:
            return None

    def toList(self, image):
        """Converts locations dictionary back to a 2D array
        :type locationsDict: dictionary
        :rtype: List[List[int]]
        """

        locationList = []
        colVals = []
        y_pos = 1
        x_pos = 1

        while x_pos < (len(image) + 1):
            while y_pos < (len(image[0]) + 1):
                for key in self.locationsDict:
                    if key == (y_pos, x_pos):
                        colVals.append(self.locationsDict[key])
                        y_pos += 1
                        break
            locationList.append(colVals)
            colVals = []
            y_pos = 1
            x_pos += 1

        return locationList

if __name__ == '__main__':
    sol = Solution()
    print(sol.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2))
