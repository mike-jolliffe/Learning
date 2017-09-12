import unittest
from road_trip import CityHopper


class TestHopper(unittest.TestCase):
    def setUp(self):
        self.hopper = CityHopper()
        self.start_city, self.num_hops = "Boston", 1
        self.can_hop = self.hopper.can_hop(self.start_city, self.num_hops)

    def test_get_input(self):
        self.assertIsInstance(self.start_city, str)
        self.assertIsInstance(self.num_hops, int)

    def test_can_hop(self):
        self.assertEqual(self.can_hop,
                         [(1, "Boston", "New York", 4),
                          (1, "Boston", "Albany", 6),
                          (1, "Boston", "Portland", 3)])
        print(self.can_hop)
        self.assertEqual(len(self.can_hop), 3)



    def test_min_time(self):
        self.assertEqual(self.hopper.min_time({'A': [2,3,4,5], 'B': [5,8,15]}),
                                              {'A': 2, 'B': 5})

    # def test_hand(self):
    #     self.assertEqual(self.player.score_hand(), 21)
    #
    # def test_hand_hit(self):
    #     self.assertEqual(len(self.player.hand), 2)


if __name__ == '__main__':
    unittest.main()