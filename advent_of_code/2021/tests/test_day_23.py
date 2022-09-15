import unittest

from day_23 import Burrow, Room, organize

test_input = '''#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
'''


class TestDay23(unittest.TestCase):
    def test_Room(self):
        self.assertTrue(Room('A', ['A', 'B']).is_valid_origin())
        self.assertFalse(Room('A', ['A', 'A']).is_valid_origin())

        self.assertTrue(Room('A', ['A']).is_valid_dest('A'))
        self.assertFalse(Room('A', ['A', 'A']).is_valid_dest('A'))
        self.assertFalse(Room('A', ['B']).is_valid_dest('A'))

    def test_Burrow(self):
        b = Burrow(test_input)

        self.assertEqual(
            (b.state[2].designation, b.state[2].occupants),
            ('A', ['B', 'A'])
        )
        self.assertEqual(
            (b.state[4].designation, b.state[4].occupants),
            ('B', ['C', 'D'])
        )
        self.assertEqual(
            (b.state[6].designation, b.state[6].occupants),
            ('C', ['B', 'C'])
        )
        self.assertEqual(
            (b.state[8].designation, b.state[8].occupants),
            ('D', ['D', 'A'])
        )

    def test_organize(self):
        burrow = Burrow(test_input)
        self.assertEqual(organize(burrow), 12521)


if __name__ == '__main__':
    unittest.main()
