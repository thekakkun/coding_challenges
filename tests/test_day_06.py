import day_06
import unittest


class TestDay06(unittest.TestCase):
    test_input = [3, 4, 3, 1, 2]

    def test_count_fish(self):
        self.assertEqual(
            day_06.count_fish(self.test_input),
            {
                1: 1,
                2: 1,
                3: 2,
                4: 1
            }
        )

    def test_sim_fish(self):
        self.assertEqual(
            day_06.sim_fish(self.test_input, 80),
            5934
        )
        self.assertEqual(
            day_06.sim_fish(self.test_input, 256),
            26984457539
        )


if __name__ == '__main__':
    unittest.main()
