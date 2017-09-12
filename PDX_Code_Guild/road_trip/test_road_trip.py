import unittest
from road_trip import CityHopper


class TestHopper(unittest.TestCase):
    def setUp(self):
        self.hopper = CityHopper()
        self.start_city, self.num_hops = self.hopper.get_input()


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