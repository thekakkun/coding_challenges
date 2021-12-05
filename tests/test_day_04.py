import day_04
import unittest


class TestDay04(unittest.TestCase):
    test_input = '''
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
2  0 12  3  7
'''

    def test_parse_bingo(self):
        self.assertEqual(
            day_04.parse_bingo(self.test_input)[1],
            [
                [
                    22, 13, 17, 11, 0,
                    8, 2, 23, 4, 24,
                    21, 9, 14, 16, 7,
                    6, 10, 3, 18, 5,
                    1, 12, 20, 15, 19
                ],
                [
                    3, 15, 0, 2, 22,
                    9, 18, 13, 17, 5,
                    19, 8, 7, 25, 23,
                    20, 11, 10, 24, 4,
                    14, 21, 16, 12, 6
                ],
                [
                    14, 21, 17, 24, 4,
                    10, 16, 15, 9, 19,
                    18, 8, 23, 26, 20,
                    22, 11, 13, 6, 5,
                    2,  0, 12, 3, 7
                ]
            ]
        )

    def test_is_bingo(self):
        self.assertEqual(
            day_04.is_bingo(
                [22, 13, 17, 11, 0,
                 8, 2, 23, 4, 24,
                 21, 9, 14, 16, 7,
                 6, 10, 3, 18, 5,
                 1, 12, 20, 15, 19]
            ),
            False
        )
        self.assertEqual(
            day_04.is_bingo(
                [22, -1, 17, 11, 0,
                 8, -1, 23, 4, 24,
                 21, -1, 14, 16, 7,
                 6, -1, 3, 18, 5,
                 1, -1, 20, 15, 19]
            ),
            True
        )
        self.assertEqual(
            day_04.is_bingo(
                [22, 13, 17, 11, 0,
                 -1, -1, -1, -1, -1,
                 21, 9, 14, 16, 7,
                 6, 10, 3, 18, 5,
                 1, 12, 20, 15, 19]
            ),
            True
        )
        self.assertEqual(
            day_04.is_bingo(
                [-1, 13, -1, 11, 0,
                 8, 2, -1, 4, 24,
                 21, 9, 14, 16, 7,
                 6, -1, 3, 18, 5,
                 1, 12, 20, -1, 19]
            ),
            False
        )

    def test_play_bingo_1(self):
        self.assertEqual(
            day_04.play_bingo_1(day_04.parse_bingo(self.test_input)),
            4512
        )

    def test_play_bingo_2(self):
        self.assertEqual(
            day_04.play_bingo_2(day_04.parse_bingo(self.test_input)),
            1924
        )


if __name__ == '__main__':
    unittest.main()
