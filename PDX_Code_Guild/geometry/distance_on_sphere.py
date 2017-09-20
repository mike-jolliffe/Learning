from math import radians, cos, sin, asin, sqrt
from point import Point

class Haversine(Point):

    def distance_to(self, other):
        '''Overrides the Euclidean distance calc in Point for distance on sphere specified in decimal degrees'''

        # convert decimal degrees to radians
        self.x, self.y, other.x, other.y = map(radians, [self.x, self.y, other.x, other.y])

        # haversine formula
        deg_lon = other.y - self.y
        deg_lat = other.x - self.x
        a = sin(deg_lat / 2) ** 2 + cos(self.y) * cos(other.y) * sin(deg_lon / 2) ** 2
        c = 2 * asin(sqrt(a))
        r = 3956  # Radius of earth in miles
        distance = c * r
        return f"{distance: 0.2f} miles"
world_dist = Haversine(45, 45)
print(world_dist.distance_to(Point(46, 46)))