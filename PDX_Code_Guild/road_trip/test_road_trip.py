import unittest
from road_trip import CityHopper


class TestHopper(unittest.TestCase):
    def setUp(self):
        # Set up a single hop from Boston for testing
        self.hopper1 = CityHopper()
        self.can_hop1 = self.hopper1.can_hop("Boston", 1)
        self.all_dests1, self.hop_times1 = self.hopper1.hop_times(self.can_hop1)
        self.all_times1 = self.hopper1.all_times(self.all_dests1, self.hop_times1)
        self.min_times1 = self.hopper1.min_time(self.all_times1)

        # Two hops from Boston for testing
        self.hopper2 = CityHopper()
        self.can_hop2 = self.hopper2.can_hop("Boston", 2)
        self.all_dests2, self.hop_times2 = self.hopper2.hop_times(self.can_hop2)
        self.all_times2 = self.hopper2.all_times(self.all_dests2, self.hop_times2)
        self.min_times2 = self.hopper2.min_time(self.all_times2)

        # Three hops from Boston for testing
        self.hopper3 = CityHopper()
        self.can_hop3 = self.hopper3.can_hop("Boston", 3)
        self.all_dests3, self.hop_times3 = self.hopper3.hop_times(self.can_hop3)

    def test_can_hop(self):
        self.assertEqual(self.can_hop1,
                         [(1, "Boston", "New York", 4),
                          (1, "Boston", "Albany", 6),
                          (1, "Boston", "Portland", 3)])
        self.assertEqual(len(self.can_hop1), 3)
        self.assertEqual(len(self.can_hop2), 11)
        self.assertEqual(len(self.can_hop3), 32)

    def test_hop_times(self):
        # Check that destination set is accurate
        self.assertEqual(self.all_dests1, {'New York', 'Albany', 'Portland'})
        self.assertEqual(self.all_dests2, {'New York', 'Albany', 'Portland', 'Boston', 'Philadelphia'})
        self.assertEqual(self.all_dests3, {'New York', 'Albany', 'Portland', 'Boston', 'Philadelphia'})

        # Check that distances dictionary populates correctly
        self.assertEqual(self.hop_times1, {1: [['New York', 4], ['Albany', 6], ['Portland', 3]]})
        self.assertEqual(self.hop_times2, {1: [['New York', 4], ['Albany', 6], ['Portland', 3]],
                                           2: [['Boston', 8], ['Albany', 9], ['Philadelphia', 13],
                                               ['Boston', 12], ['New York', 11], ['Portland', 13],
                                               ['Boston', 6], ['Albany', 10]]})

    def test_all_times(self):
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