import unittest

from day_24 import alu

test_input_1 = '''inp x
mul x -1
'''

test_input_2 = '''inp z
inp x
mul z 3
eql z x
'''

test_input_3 = '''inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
'''


class TestDay24(unittest.TestCase):
    def test_alu(self):
        self.assertEqual(alu(test_input_1)([5])['x'], -5)
        self.assertEqual(alu(test_input_2)([5, 5])['z'], 0)
        self.assertEqual(alu(test_input_2)([5, 15])['z'], 1)
        self.assertEqual(alu(test_input_3)([7]),
                         {'w': 0, 'x': 1, 'y': 1, 'z': 1})
        self.assertEqual(alu(test_input_3)([8]),
                         {'w': 1, 'x': 0, 'y': 0, 'z': 0})


if __name__ == '__main__':
    unittest.main()
