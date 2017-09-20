import unittest
from point import Point
from rectangle import Rectangle
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

class TestRects(unittest.TestCase):
    def setUp(self):
        self.rect1 = Rectangle(0, 5, 5, 5)
        self.rect2 = Rectangle(0, 5, 5, 5)
        self.rect3 = Rectangle(1, 6, 6, 6)

    def test_repr(self):
        self.assertEqual(self.rect1.__repr__(), f"This rectangle starting at (0, 5), with height 5 and width 5"\
               f" is composed of the following points: [(0, 5), (0, 0), (5, 5), (5, 0)]")

    def test_eq(self):
        self.assertEqual(self.rect1 == self.rect2, True)
        self.assertNotEqual(self.rect1 == self.rect3, True)

    def test_find_center(self):
        self.assertEqual(self.rect1.find_center(), (2.5, 2.5))

    def test_point_inside(self):
        self.assertTrue(self.rect1.point_inside(Point(2,2)))
        self.assertFalse(self.rect1.point_inside(Point(10,10)))



if __name__ == '__main__':
    unittest.main()