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

    def __eq__(self, other):
        # Checks to see if x and y coordinate are the same
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __repr__(self):
        # Returns a string representation of __eq__ method
        return 'Coordinate(' + str(self.x) + ',' + str(self.y) + ')'

c1 = Coordinate(1,1)
c2 = Coordinate(1,1)
print(c1)
print(repr(c1))
print(c1 == c2)
