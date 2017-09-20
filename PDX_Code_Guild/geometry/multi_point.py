from point import Point

class MultiPoint(Point):
    def __init__(self, points):
        self.multipoints = points

    def in_radius(self, centroid, radius):
        '''Given an input Point object and radius, returns all Points within multipoints array that fall within the radius'''
        in_radius = []
        for point in self.multipoints:
            if point.distance_to(centroid) < radius:
                in_radius.append(point)
        return in_radius

if __name__ == '__main__':
    point_list = MultiPoint([Point(0,0), Point(1,1), Point(2,2), Point(3,3), Point(4,4)])
    print(point_list.in_radius(Point(0,0), 3))
