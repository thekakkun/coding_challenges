import unittest

import day_07

test_input = (16, 1, 2, 0, 4, 2, 7, 1, 2, 14)


class TestDay07(unittest.TestCase):
    def test_total_fuel(self):
        self.assertEqual(
            day_07.total_fuel(test_input, 2, day_07.dist_1),
            37
        )
        self.assertEqual(
            day_07.total_fuel(test_input, 1, day_07.dist_1),
            41
        )
        self.assertEqual(
            day_07.total_fuel(test_input, 5, day_07.dist_2),
            168
        )
        self.assertEqual(
            day_07.total_fuel(test_input, 2, day_07.dist_2),
            206
        )

    def test_align_crabs(self):
        self.assertEqual(
            day_07.align_crabs(
                test_input,
                day_07.dist_1
            ),
            37
        )
        self.assertEqual(
            day_07.align_crabs(
                test_input,
                day_07.dist_2
            ),
            168
        )


if __name__ == '__main__':
    unittest.main()
