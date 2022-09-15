import unittest

import day_02

test_commands = [
    'forward 5',
    'down 5',
    'forward 8',
    'up 3',
    'down 8',
    'forward 2'
]


class TestDay02(unittest.TestCase):
    def test_navigate_1(self):
        self.assertEqual(
            day_02.navigate_1(test_commands),
            150
        )

    def test_navigate_2(self):
        self.assertEqual(
            day_02.navigate_2(test_commands),
            900
        )


if __name__ == '__main__':
    unittest.main()
