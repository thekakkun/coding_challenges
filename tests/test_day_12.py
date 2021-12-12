import unittest

import day_12


class TestDay12(unittest.TestCase):
    test_input_1 = '''start-A
start-b
A-c
A-b
b-d
A-end
b-end'''

    test_input_2 = '''dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc'''

    test_input_3 = '''fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW'''

    def test_parse_input(self):
        test_caves_1 = day_12.parse_input(self.test_input_1)
        self.assertEqual(
            test_caves_1,
            {
                'start': {'A', 'b'},
                'A': {'start', 'b', 'c', 'end'},
                'b': {'start', 'A', 'd', 'end'},
                'c': {'A'},
                'd': {'b'},
                'end': {'A', 'b'}
            }
        )

    def test_get_paths_1(self):
        test_caves_1 = day_12.parse_input(self.test_input_1)
        self.assertEqual(
            day_12.get_paths(test_caves_1, day_12.successors_1),
            {
                ('start', 'A', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'b', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'end'),
                ('start', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'end'),
                ('start', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'b', 'A', 'end'),
                ('start', 'b', 'end')
            }
        )
        test_caves_2 = day_12.parse_input(self.test_input_2)
        self.assertEqual(
            day_12.get_paths(test_caves_2, day_12.successors_1),
            {
                ('start', 'HN', 'dc', 'HN', 'end'),
                ('start', 'HN', 'dc', 'HN', 'kj', 'HN', 'end'),
                ('start', 'HN', 'dc', 'end'),
                ('start', 'HN', 'dc', 'kj', 'HN', 'end'),
                ('start', 'HN', 'end'),
                ('start', 'HN', 'kj', 'HN', 'dc', 'HN', 'end'),
                ('start', 'HN', 'kj', 'HN', 'dc', 'end'),
                ('start', 'HN', 'kj', 'HN', 'end'),
                ('start', 'HN', 'kj', 'dc', 'HN', 'end'),
                ('start', 'HN', 'kj', 'dc', 'end'),
                ('start', 'dc', 'HN', 'end'),
                ('start', 'dc', 'HN', 'kj', 'HN', 'end'),
                ('start', 'dc', 'end'),
                ('start', 'dc', 'kj', 'HN', 'end'),
                ('start', 'kj', 'HN', 'dc', 'HN', 'end'),
                ('start', 'kj', 'HN', 'dc', 'end'),
                ('start', 'kj', 'HN', 'end'),
                ('start', 'kj', 'dc', 'HN', 'end'),
                ('start', 'kj', 'dc', 'end')}
        )
        test_caves_3 = day_12.parse_input(self.test_input_3)
        self.assertEqual(
            len(day_12.get_paths(test_caves_3, day_12.successors_1)), 226)

    def test_get_paths_2(self):
        test_caves_1 = day_12.parse_input(self.test_input_1)
        self.assertEqual(
            day_12.get_paths(test_caves_1, day_12.successors_2),
            {
                ('start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'b', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'b', 'A', 'b', 'end'),
                ('start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'b', 'A', 'c', 'A', 'b', 'end'),
                ('start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'b', 'd', 'b', 'A', 'end'),
                ('start', 'A', 'b', 'd', 'b', 'end'),
                ('start', 'A', 'b', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'A', 'b', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'd', 'b', 'end'),
                ('start', 'A', 'c', 'A', 'b', 'end'),
                ('start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'),
                ('start', 'A', 'c', 'A', 'c', 'A', 'b', 'end'),
                ('start', 'A', 'c', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'c', 'A', 'end'),
                ('start', 'A', 'end'),
                ('start', 'b', 'A', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'b', 'A', 'b', 'A', 'end'),
                ('start', 'b', 'A', 'b', 'end'),
                ('start', 'b', 'A', 'c', 'A', 'b', 'A', 'end'),
                ('start', 'b', 'A', 'c', 'A', 'b', 'end'),
                ('start', 'b', 'A', 'c', 'A', 'c', 'A', 'end'),
                ('start', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'b', 'A', 'end'),
                ('start', 'b', 'd', 'b', 'A', 'c', 'A', 'end'),
                ('start', 'b', 'd', 'b', 'A', 'end'),
                ('start', 'b', 'd', 'b', 'end'),
                ('start', 'b', 'end'),
            }
        )
        test_caves_2 = day_12.parse_input(self.test_input_2)
        self.assertEqual(
            len(day_12.get_paths(test_caves_2, day_12.successors_2)), 103)
        test_caves_3 = day_12.parse_input(self.test_input_3)
        self.assertEqual(
            len(day_12.get_paths(test_caves_3, day_12.successors_2)), 3509)


if __name__ == '__main__':
    unittest.main()
