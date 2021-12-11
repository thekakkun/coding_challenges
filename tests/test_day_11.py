import unittest

import day_11


class TestDay11(unittest.TestCase):
    test_input_0 = '''5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526'''

    test_input_1 = '''6594254334
3856965822
6375667284
7252447257
7468496589
5278635756
3287952832
7993992245
5957959665
6394862637'''

    test_input_2 = '''8807476555
5089087054
8597889608
8485769600
8700908800
6600088989
6800005943
0000007456
9000000876
8700006848'''

    def test_run_step(self):
        self.assertEqual(
            day_11.run_step(day_11.parse_input(self.test_input_0)),
            (
                0,
                day_11.parse_input(self.test_input_1)
            )
        )
        self.assertEqual(
            day_11.run_step(day_11.parse_input(self.test_input_1)),
            (
                35,
                day_11.parse_input(self.test_input_2)
            )
        )

    def test_count_flashes(self):
        self.assertEqual(
            day_11.count_flashes(day_11.parse_input(self.test_input_0), 100), 1656)

    def test_find_simul(self):
        self.assertEqual(
            day_11.find_simul(day_11.parse_input(self.test_input_0)),
            195
        )


if __name__ == '__main__':
    unittest.main()
