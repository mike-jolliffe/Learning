'''


Then create some top-level functions in those modules that know how to operate on instances of each class.

In the `rectangle` module:

* Know if a point is inside a rectangle

All functions, even magic methods, should have tests.

Create a bunch of Point instances and put them in a container.

Then, Given a single Point instance, return all of the point instances within a given radius.

Implement the Haversine formula to compute the distance between two given points on the earth.

[Haversine Formula Wiki](https://en.wikipedia.org/wiki/Haversine_formula)

[Haversine Formula Python Stack Overflow](http://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points)'''

import math
class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def distance_to(self, other):
        '''Returns the Euclidean distance between a pair of given points'''
        return math.sqrt((other.x - self.x)**2 + (other.y - self.y)**2)

    def move(self, distance):
        '''Moves a point by a given (x, y) tuple amount'''
        self.x += distance[0]
        self.y += distance[1]
        return self.__repr__()

if __name__ == '__main__':
    point1 = Point(0,0)
    point2 = Point(1,1)
    print(point1)
    print(point2)
    print(point1 == point2)
    print(point1.distance_to(point2))
    print(point1.move((1,1)))