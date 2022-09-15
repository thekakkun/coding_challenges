import unittest

import day_13

test_input = '''6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5'''


class TestDay13(unittest.TestCase):
    def test_parse_input(self):
        self.assertEqual(
            day_13.parse_input(test_input),
            (
                {
                    (6, 10), (0, 14), (9, 10), (0, 3), (10, 4), (4, 11),
                    (6, 0), (6, 12), (4, 1), (0, 13), (10, 12), (3, 4),
                    (3, 0), (8, 4), (1, 10), (2, 14), (8, 10), (9, 0)
                },
                (('y', 7), ('x', 5))
            )
        )

    def test_make_fold(self):
        (dots, folds) = day_13.parse_input(test_input)
        self.assertEqual(
            day_13.make_fold(dots, folds[0]),
            {
                (0, 0), (2, 0), (3, 0), (6, 0), (9, 0),
                (0, 1), (4, 1),
                (6, 2), (10, 2),
                (0, 3), (4, 3),
                (1, 4), (3, 4), (6, 4), (8, 4), (9, 4), (10, 4)
            }
        )

    def test_get_code(self):
        (dots, folds) = day_13.parse_input(test_input)
        self.assertEqual(
            day_13.get_code(dots, folds),
            {
                (0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
                (0, 1), (4, 1),
                (0, 2), (4, 2),
                (0, 3), (4, 3),
                (0, 4), (1, 4), (2, 4), (3, 4), (4, 4),
            }
        )


if __name__ == '__main__':
    unittest.main()
