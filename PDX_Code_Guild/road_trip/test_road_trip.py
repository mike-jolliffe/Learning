import unittest
from road_trip import CityHopper


class TestHopper(unittest.TestCase):
    def setUp(self):
        # Set up a single hop from Boston for testing
        self.hopper1 = CityHopper()
        self.hopper1.start_city = "Boston"
        self.hopper1.num_hops = 1
        self.can_hop1 = self.hopper1.can_hop("Boston", 1)
        self.all_dests1, self.hop_times1 = self.hopper1.hop_times(self.can_hop1)
        self.all_times1 = self.hopper1.all_times(self.all_dests1, self.hop_times1)
        self.min_times1 = self.hopper1.min_time(self.all_times1)

        # Two hops from Boston for testing
        self.hopper2 = CityHopper()
        self.hopper2.start_city = "Boston"
        self.hopper2.num_hops = 2
        self.can_hop2 = self.hopper2.can_hop("Boston", 2)
        self.all_dests2, self.hop_times2 = self.hopper2.hop_times(self.can_hop2)
        self.all_times2 = self.hopper2.all_times(self.all_dests2, self.hop_times2)
        self.min_times2 = self.hopper2.min_time(self.all_times2)

        # Three hops from Boston for testing
        self.hopper3 = CityHopper()
        self.hopper3.start_city = "Boston"
        self.hopper3.num_hops = 3
        self.can_hop3 = self.hopper3.can_hop("Boston", 3)
        self.all_dests3, self.hop_times3 = self.hopper3.hop_times(self.can_hop3)

    def test_can_hop(self):
        self.assertEqual(self.can_hop1,
                         [[1, "Boston", "New York", 4],
                          [1, "Boston", "Albany", 6],
                          [1, "Boston", "Portland", 3]])
        self.assertEqual(len(self.can_hop1), 3)
        self.assertEqual(len(self.can_hop2), 11)
        self.assertEqual(len(self.can_hop3), 32)

    def test_hop_times(self):
        # Check that destination set is accurate
        self.assertEqual(self.all_dests1, {'New York', 'Albany', 'Portland'})
        self.assertEqual(self.all_dests2, {'New York', 'Albany', 'Portland', 'Boston', 'Philadelphia'})
        self.assertEqual(self.all_dests3, {'New York', 'Albany', 'Portland', 'Boston', 'Philadelphia'})

        # Check that distances dictionary populates correctly
        self.assertEqual(self.hop_times1, [['Boston', 'New York', 4], ['Boston', 'Albany', 6], ['Boston', 'Portland', 3]])
        self.assertEqual(self.hop_times2, [['Boston', 'New York', 4], ['Boston', 'Albany', 6], ['Boston', 'Portland', 3],
                                           ['Boston','New York', 'Boston', 8], ['Boston', 'New York', 'Albany', 9],
                                           ['Boston', 'New York', 'Philadelphia', 13], ['Boston', 'Albany', 'Boston', 12],
                                           ['Boston', 'Albany', 'New York', 11], ['Boston', 'Albany', 'Portland', 13],
                                           ['Boston', 'Portland', 'Boston', 6], ['Boston', 'Portland', 'Albany', 10]])

        self.assertEqual(self.hop_times3, [['Boston', 'New York', 4], ['Boston', 'Albany', 6], ['Boston', 'Portland', 3],
                                           ['Boston','New York', 'Boston', 8], ['Boston', 'New York', 'Albany', 9],
                                           ['Boston', 'New York', 'Philadelphia', 13], ['Boston', 'Albany', 'Boston', 12],
                                           ['Boston', 'Albany', 'New York', 11], ['Boston', 'Albany', 'Portland', 13],
                                           ['Boston', 'Portland', 'Boston', 6], ['Boston', 'Portland', 'Albany', 10],
                                           ['Boston', 'New York', 'Boston', 'New York', 12],
                                           ['Boston', 'New York', 'Boston', 'Albany', 14],
                                           ['Boston','New York', 'Boston', 'Portland', 11],
                                           ['Boston', 'New York', 'Albany', 'Boston', 15],
                                           ['Boston', 'New York', 'Albany', 'New York', 14],
                                           ['Boston', 'New York', 'Albany', 'Portland', 16],
                                           ['Boston', 'New York', 'Philadelphia', 'New York', 22],
                                           ['Boston', 'Albany', 'Boston', 'New York', 16],
                                           ['Boston', 'Albany', 'Boston', 'Albany', 18],
                                           ['Boston', 'Albany', 'Boston', 'Portland', 15],
                                           ['Boston', 'Albany', 'New York', 'Boston', 15],
                                           ['Boston', 'Albany', 'New York', 'Albany', 16],
                                           ['Boston', 'Albany', 'New York', 'Philadelphia', 20],
                                           ['Boston', 'Albany', 'Portland', 'Boston', 16],
                                           ['Boston', 'Albany', 'Portland', 'Albany', 20],
                                           ['Boston', 'Portland', 'Boston', 'New York', 10],
                                           ['Boston', 'Portland', 'Boston', 'Albany', 12],
                                           ['Boston', 'Portland', 'Boston', 'Portland', 9],
                                           ['Boston', 'Portland', 'Albany', 'Boston', 16],
                                           ['Boston', 'Portland', 'Albany', 'New York', 15],
                                           ['Boston', 'Portland', 'Albany', 'Portland', 17]])

        # Check that cumulative times are aggregated by destination city across all possible hops
        self.assertEqual(self.all_times1, {'New York': [4], 'Albany': [6], 'Portland': [3]})
        self.assertEqual(self.all_times2, {'Boston': [8, 12, 6], 'New York': [4, 11], 'Albany': [6, 9, 10],
                                           'Portland': [3, 13], 'Philadelphia': [13]})

    def test_min_time(self):
        # Check that the minimum travel time for each destination city is returned
        self.assertEqual(self.min_times1, {'New York': 4, 'Albany': 6, 'Portland': 3})
        self.assertEqual(self.min_times2, {'Boston': 6, 'New York': 4, 'Albany': 6,
                                           'Portland': 3, 'Philadelphia': 13})


if __name__ == '__main__':
    unittest.main()
