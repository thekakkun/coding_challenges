import unittest

import day_01

test_report = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]


class TestDay01(unittest.TestCase):
    def test_sweep_1(self):
        self.assertEqual(
            day_01.sweep_1(test_report),
            7
        )

    def test_sweep_2(self):
        self.assertEqual(
            day_01.sweep_2(test_report),
            5
        )


if __name__ == '__main__':
    unittest.main()
