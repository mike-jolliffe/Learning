from point import Point

class Rectangle(Point):
    def __init__(self, x, y, width, height):
        super().__init__(x,y)
        self.width = width
        self.height = height
        self.corners = [(self.x, self.y),
                        (self.x, self.y - self.height),
                        (self.x + self.width, self.y),
                        (self.x + self.width, self.y - self.height)]

    def __repr__(self):
        return f"This rectangle starting at ({self.x}, {self.y}), with height {self.height} and width {self.width}"\
               f" is composed of the following points: {[corner for corner in self.corners]}"

    def __eq__(self, other):
        if self.corners == other.corners:
            return True
        else:
            return False

    def find_center(self):
        '''Finds the centroid of the rectangle'''
        # averages the x locations and the y locations
        return (((self.corners[0][0] + self.corners[2][0]) / 2, (self.corners[0][1] + self.corners[1][1]) / 2))

    def point_inside(self, point):
        '''Given a Point object, returns True if it falls within the rectangle '''
        max_x, min_x = max([points[0] for points in self.corners]), min([points[0] for points in self.corners])
        max_y, min_y = max([points[1] for points in self.corners]), min([points[1] for points in self.corners])

        if point.x in range(min_x, max_x + 1) and point.y in range(min_y, max_y + 1):
            return True
        else:
            return False

if __name__ == '__main__':
    new_rectangle = Rectangle(0,4,5,5)
    print(new_rectangle.point_inside(Point(100,3)))
    print(new_rectangle)