import unittest

import day_06


class TestDay06(unittest.TestCase):
    test_input = [3, 4, 3, 1, 2]
    test_rule = {
        0: (8, 6),
        1: (0,), 2: (1,), 3: (2,), 4: (3,), 5: (4,), 6: (5,), 7: (6,), 8: (7,)
    }


    def test_sim_fish(self):
        self.assertEqual(
            day_06.sim_fish(self.test_input, self.test_rule, 80),
            5934
        )
        self.assertEqual(
            day_06.sim_fish(self.test_input, self.test_rule, 256),
            26984457539
        )


if __name__ == '__main__':
    unittest.main()
