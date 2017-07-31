class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'

    def __eq__(self):
        # Checks to see if x and y coordinate are the same
        if self.x == self.x and self.y == self.y:
            return True
        else:
            return False

    def __repr__(self):
        # Returns a string representation of __eq__ method
        return str(self.x == self.y)

c1 = Coordinate(1,1)
c2 = Coordinate(2,2)
print(c1)
