class Solution:
    def __init__(self):
        self.dims_list = []

    def constructRectangle(self, area):
        """Given an area, returns ideal webpage dimensions (i.e., height > width
           and height/width ratio as close to 1 as possible while achieving area)
        :type area: int
        :rtype: List[int]
        """

        start = area ** 0.5

        # TODO pull in makeRectangles
        

    def makeRectangles(self, height, width, area):
        """Recursively makes height, width pairs approaching the desired area
        :type height: int
        :type width: int
        :rtype: None
        """
        # Base case of width hitting floor, height hitting ceiling
        if width == 1 or height >= area:
            return None
        elif width * height == area:
            if not [height, width] in self.dims_list:
                self.dims_list.append([height, width])
            return (self.makeRectangles(height+1, width, area),
                    self.makeRectangles(height, width-1, area))
        else:
            return (self.makeRectangles(height+1, width, area),
                    self.makeRectangles(height, width-1, area))

if __name__ == '__main__':
    sol = Solution()
    sol.makeRectangles(5, 5, 32)
    print(sol.dims_list)

# Use sqrt as the ceiling for width and the floor for height, only save pairs
# that result in an area exactly equal to goal area
