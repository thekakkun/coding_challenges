import unittest
from functools import reduce

import day_18

test_input_1 = '''[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
[[[[0,7],4],[7,[[8,4],9]]],[1,1]]
[[[[0,7],4],[15,[0,13]]],[1,1]]
[[[[0,7],4],[[7,8],[0,13]]],[1,1]]
[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]
[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
'''

test_input_2 = '''[[[[4,3],4],4],[7,[[8,4],9]]]
[1,1]
'''

test_input_3 = '''[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]
'''

test_input_4 = '''
[[1,2],[[3,4],5]]
[[[[0,7],4],[[7,8],[6,0]]],[8,1]]
[[[[1,1],[2,2]],[3,3]],[4,4]]
[[[[3,0],[5,3]],[4,4]],[5,5]]
[[[[5,0],[7,4]],[5,5]],[6,6]]
[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]
'''


class TestDay18(unittest.TestCase):
    def test_is_explodable(self):
        test_assignment = day_18.parse_input(test_input_1)
        self.assertEqual(
            [day_18.is_explodable(num) for num in test_assignment],
            [
                (True, 5),
                (True, 17),
                (False, -1),
                (False, -1),
                (True, 23),
                (False, -1),
            ]
        )

    def test_explode(self):
        test_assignment = day_18.parse_input(test_input_1)
        self.assertEqual(
            day_18.explode(test_assignment[0]),
            test_assignment[1]
        )
        self.assertEqual(
            day_18.explode(test_assignment[1]),
            test_assignment[2]
        )
        self.assertEqual(
            day_18.explode(test_assignment[4]),
            test_assignment[5]
        )

    def test_is_splittable(self):
        test_assignment = day_18.parse_input(test_input_1)
        self.assertEqual(
            [day_18.is_splittable(num) for num in test_assignment],
            [
                (False, -1),
                (False, -1),
                (True, 13),
                (True, 22),
                (False, -1),
                (False, -1),
            ]
        )

    def test_split(self):
        test_assignment = day_18.parse_input(test_input_1)
        self.assertEqual(
            day_18.split(test_assignment[2]),
            test_assignment[3]
        )
        self.assertEqual(
            day_18.split(test_assignment[3]),
            test_assignment[4]
        )

    def test_add(self):
        test_assignment = day_18.parse_input(test_input_2)
        self.assertEqual(
            day_18.to_string((day_18.add(*test_assignment))),
            '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
        )

        test_assignment = day_18.parse_input(test_input_3)
        self.assertEqual(
            day_18.to_string(
                reduce(lambda x, y: day_18.add(x, y), test_assignment)
            ),
            '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
        )

    def test_get_magnitude(self):
        test_assignment = day_18.parse_input(test_input_4)
        self.assertEqual(
            [day_18.get_magnitude(line) for line in test_assignment],
            [143, 1384, 445, 791, 1137, 3488]
        )


if __name__ == '__main__':
    unittest.main()
