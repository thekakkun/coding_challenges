import day_05
import unittest


class TestDay05(unittest.TestCase):
    test_input = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

    def test_parse_input(self):
        self.assertEqual(
            day_05.parse_input(self.test_input),
            (
                ((0, 9), (5, 9)),
                ((8, 0), (0, 8)),
                ((9, 4), (3, 4)),
                ((2, 2), (2, 1)),
                ((7, 0), (7, 4)),
                ((6, 4), (2, 0)),
                ((0, 9), (2, 9)),
                ((3, 4), (1, 4)),
                ((0, 0), (8, 8)),
                ((5, 5), (8, 2))
            )
        )

    def test_map_vents(self):
        self.assertEqual(
            day_05.map_vents((((0, 9), (5, 9)),)),
            {
                (0, 9): 1,
                (1, 9): 1,
                (2, 9): 1,
                (3, 9): 1,
                (4, 9): 1,
                (5, 9): 1
            }
        )

        self.assertEqual(
            day_05.map_vents((((6, 4), (2, 0)),)),
            {
                (6, 4): 1,
                (5, 3): 1,
                (4, 2): 1,
                (3, 1): 1,
                (2, 0): 1
            }
        )

        self.assertEqual(
            day_05.map_vents((((9, 7), (7, 9)),)),
            {
                (9, 7): 1,
                (8, 8): 1,
                (7, 9): 1,
            }
        )

    def test_find_vents_1(self):
        self.assertEqual(
            day_05.find_vents_1(day_05.parse_input(self.test_input)),
            5)

    def test_find_vents_2(self):
        self.assertEqual(
            day_05.find_vents_2(day_05.parse_input(self.test_input)),
            12)


if __name__ == '__main__':
    unittest.main()
