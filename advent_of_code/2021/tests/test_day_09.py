import unittest

import day_09

test_heightmap = (
    (2, 1, 9, 9, 9, 4, 3, 2, 1, 0),
    (3, 9, 8, 7, 8, 9, 4, 9, 2, 1),
    (9, 8, 5, 6, 7, 8, 9, 8, 9, 2),
    (8, 7, 6, 7, 8, 9, 6, 7, 8, 9),
    (9, 8, 9, 9, 9, 6, 5, 6, 7, 8)
)


class TestDay09(unittest.TestCase):
    def test_measure_changes(self):
        self.assertEqual(day_09.get_risk_level(test_heightmap),
                         15
                         )

    def test_get_basin(self):
        self.assertEqual(
            day_09.get_basin(test_heightmap, (0, 1),
                             day_09.get_lower_than(test_heightmap)),
            set((
                (0, 0),
                (1, 0),
                (0, 1)
            ))
        )

    def test_find_basins(self):
        self.assertEqual(
            day_09.find_basins(test_heightmap), 1134)


if __name__ == '__main__':
    unittest.main()
