import unittest
from point import Point
import rectangle


class TestPoints(unittest.TestCase):
    def setUp(self):
        self.point1 = Point(0,0)
        self.point2 = Point(3,4)
        self.point3 = Point(0,0)

    def test_repr(self):
        self.assertEqual(self.point1.__repr__(), '(0, 0)')

    def test_eq(self):
        self.assertEqual(self.point1 == self.point2, False)
        self.assertEqual(self.point1 == self.point3, True)

    def test_distance_to(self):
        self.assertEqual(self.point1.distance_to(self.point2), 5)
        self.assertEqual(self.point1.distance_to(self.point3), 0)

    def test_move(self):
        self.assertEqual(self.point1.move((1,1)), '(1, 1)')
        self.assertEqual(self.point3.move((-1,-1)), '(-1, -1)')

if __name__ == '__main__':
    unittest.main()